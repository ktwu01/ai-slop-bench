#!/usr/bin/env node

import { createHash } from "node:crypto";
import {
  copyFileSync,
  existsSync,
  mkdirSync,
  readFileSync,
  writeFileSync,
} from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const reviewDirectory = path.resolve(scriptDirectory, "..");

const defaultSourcePath = path.join(
  reviewDirectory,
  "review-FINAL.md",
);
const defaultOutputPath = path.join(
  reviewDirectory,
  "output",
  "pdf",
  "NeurIPS-ANA-2026-17_review_report.tex",
);

const args = process.argv.slice(2);
const compilePdf = !args.includes("--no-compile");
const positionalArgs = args.filter((argument) => argument !== "--no-compile");

if (positionalArgs.length > 2) {
  fail(
    "Usage: node scripts/build-review-report.mjs [SOURCE.md] [OUTPUT.tex] [--no-compile]",
  );
}

const sourcePath = path.resolve(positionalArgs[0] ?? defaultSourcePath);
const outputPath = path.resolve(positionalArgs[1] ?? defaultOutputPath);

if (!existsSync(sourcePath)) {
  fail(`Source file not found: ${sourcePath}`);
}

const source = readFileSync(sourcePath, "utf8");
const sourceLines = source.split(/\r?\n/);
const excerptLines = extractReviewExcerpt(sourceLines);
const excerpt = excerptLines.join("\n");
const excerptHash = createHash("sha256").update(excerpt).digest("hex");
const logicalLines = unwrapSoftLineBreaks(excerptLines);
const latexBody = markdownLinesToLatex(logicalLines);
const latexDocument = renderLatexDocument(excerptHash, latexBody);

mkdirSync(path.dirname(outputPath), { recursive: true });
writeFileSync(outputPath, latexDocument, "utf8");

if (compilePdf) {
  compileLatex(outputPath);
}

const outputRelativeToReview = path.relative(reviewDirectory, outputPath);
console.log(`Generated ${outputRelativeToReview}`);
console.log(`Source excerpt SHA-256: ${excerptHash}`);

// The author-facing review runs from "## Summary" to the end, but the
// confidential editor note is dropped: it is an editor-only channel and does
// not belong in the shared PDF. The title/metadata block (lines above
// "## Summary") is also dropped, since the venue portal already carries the
// manuscript ID and recommendation.
function extractReviewExcerpt(lines) {
  const startHeading = "## Summary";
  const editorNotePrefix = "## Confidential note to the editor";

  const start = lines.indexOf(startHeading);
  if (start === -1) {
    fail(`Missing start heading: ${startHeading}`);
  }

  const kept = [];
  let skippingEditorNote = false;

  for (let index = start; index < lines.length; index += 1) {
    const line = lines[index];

    if (line.startsWith(editorNotePrefix)) {
      skippingEditorNote = true;
      continue;
    }
    // A new top-level "## " heading ends the editor-note skip region.
    if (skippingEditorNote) {
      if (/^## (?!Confidential note to the editor)/.test(line)) {
        skippingEditorNote = false;
      } else {
        continue;
      }
    }

    kept.push(line);
  }

  while (
    kept.length > 0 &&
    (kept.at(-1) === "" || kept.at(-1) === "---")
  ) {
    kept.pop();
  }

  const hasMajor = kept.some((line) => line.startsWith("## Major scientific concerns"));
  const hasRecommendation = kept.some((line) =>
    line.startsWith("## Recommendation rationale"),
  );
  const majorCount = kept.filter((line) => /^### M\d+\./.test(line)).length;

  if (!hasMajor || !hasRecommendation) {
    fail(
      "Expected the review to contain the major-concerns section and the recommendation rationale.",
    );
  }
  if (majorCount < 1) {
    fail("Expected at least one major concern (### M1., ...).");
  }

  return kept;
}

// Legacy Markdown may contain soft wrapping. Per Markdown semantics a
// single newline inside a paragraph or list item is a SOFT break and must be
// joined into flowing text; only a blank line separates blocks. This pass
// collapses each block to one logical line so the downstream converter (and
// LaTeX) break lines by measure, not at the author's wrap column.
function unwrapSoftLineBreaks(lines) {
  const logical = [];
  let buffer = null; // accumulating a paragraph or list item

  const isBlank = (line) => line.trim() === "";
  const isRule = (line) => line.trim() === "---";
  const isHeading = (line) => /^#{1,6}\s/.test(line);
  const isBullet = (line) => /^-\s+/.test(line);
  const isNumbered = (line) => /^\d+\.\s+/.test(line);

  function flush() {
    if (buffer !== null) {
      logical.push(buffer);
      buffer = null;
    }
  }

  for (const rawLine of lines) {
    if (isBlank(rawLine)) {
      flush();
      logical.push("");
      continue;
    }
    if (isRule(rawLine)) {
      flush();
      logical.push("---");
      continue;
    }
    if (isHeading(rawLine)) {
      flush();
      logical.push(rawLine.trim());
      continue;
    }
    if (isBullet(rawLine) || isNumbered(rawLine)) {
      // A new list item starts its own block.
      flush();
      buffer = rawLine.replace(/\s+$/, "");
      continue;
    }
    // A plain, possibly indented continuation line: join to the current block
    // (paragraph or the open list item) with a single space.
    const continuation = rawLine.trim();
    if (buffer === null) {
      buffer = continuation;
    } else {
      buffer += " " + continuation;
    }
  }
  flush();

  return logical;
}

function markdownLinesToLatex(lines) {
  const body = [];
  let listType = null; // "itemize" | "enumerate" | null

  function closeList() {
    if (listType) {
      body.push(`\\end{${listType}}`, "");
      listType = null;
    }
  }

  function openList(type) {
    if (listType && listType !== type) {
      closeList();
    }
    if (!listType) {
      body.push(`\\begin{${type}}`);
      listType = type;
    }
  }

  for (const rawLine of lines) {
    const line = rawLine;

    // Horizontal rules become vertical space, not a page rule.
    if (line.trim() === "---") {
      closeList();
      body.push("\\medskip", "");
      continue;
    }

    const sectionMatch = line.match(/^##\s+(.+)$/);
    const subsectionMatch = line.match(/^###\s+(.+)$/);
    const bulletMatch = line.match(/^-\s+(.+)$/);
    const numberedMatch = line.match(/^\d+\.\s+(.+)$/);

    if (sectionMatch) {
      closeList();
      body.push(`\\section*{${convertInlineMarkdown(sectionMatch[1])}}`, "");
    } else if (subsectionMatch) {
      closeList();
      body.push(
        `\\subsection*{${convertInlineMarkdown(subsectionMatch[1])}}`,
        "",
      );
    } else if (bulletMatch) {
      openList("itemize");
      body.push(`  \\item ${convertInlineMarkdown(bulletMatch[1])}`);
    } else if (numberedMatch) {
      openList("enumerate");
      body.push(`  \\item ${convertInlineMarkdown(numberedMatch[1])}`);
    } else if (line === "") {
      closeList();
    } else {
      closeList();
      body.push(convertInlineMarkdown(line), "");
    }
  }

  closeList();
  return body.join("\n");
}

// Handles **bold**, *italic*, and `code` spans, escaping everything else.
function convertInlineMarkdown(text) {
  let result = "";
  let cursor = 0;

  while (cursor < text.length) {
    if (text.startsWith("**", cursor)) {
      const close = text.indexOf("**", cursor + 2);
      if (close !== -1) {
        result += `\\textbf{${convertInlineMarkdown(text.slice(cursor + 2, close))}}`;
        cursor = close + 2;
        continue;
      }
    }

    if (text[cursor] === "`") {
      const close = text.indexOf("`", cursor + 1);
      if (close !== -1) {
        result += `\\texttt{${escapeLatex(text.slice(cursor + 1, close))}}`;
        cursor = close + 1;
        continue;
      }
    }

    if (text[cursor] === "*") {
      const close = text.indexOf("*", cursor + 1);
      if (close !== -1) {
        result += `\\emph{${convertInlineMarkdown(text.slice(cursor + 1, close))}}`;
        cursor = close + 1;
        continue;
      }
    }

    // Advance to the next markup marker.
    let stop = text.length;
    for (const marker of ["**", "`", "*"]) {
      const at = text.indexOf(marker, cursor);
      if (at !== -1 && at < stop) {
        stop = at;
      }
    }
    if (stop === cursor) {
      stop = cursor + 1;
    }
    result += escapeLatex(text.slice(cursor, stop));
    cursor = stop;
  }

  return result;
}

function escapeLatex(text) {
  return text
    .replace(/\\/g, "\\textbackslash{}")
    .replace(/([#$%&_{}])/g, "\\$1")
    .replace(/~/g, "\\textasciitilde{}")
    .replace(/\^/g, "\\textasciicircum{}")
    .replace(/—/g, "---")
    .replace(/–/g, "--")
    // Straight quotes to LaTeX curly quotes (no csquotes, no active chars).
    .replace(/"([^"]*)"/g, "``$1''")
    .replace(/(^|[\s(])'/g, "$1`")
    .replace(/'/g, "'");
}

function renderLatexDocument(sourceHash, body) {
  return String.raw`% Generated by 17_Metag/scripts/build-review-report.mjs
% Do not edit this file directly; edit review-FINAL.md and rebuild.
% Extracted source excerpt SHA-256: ${sourceHash}
\documentclass[11pt,letterpaper]{article}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{tgtermes}
\usepackage[scale=0.92]{tgheros}
\usepackage{microtype}
\usepackage[margin=1in]{geometry}
\usepackage[dvipsnames]{xcolor}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{hyperref}

\definecolor{reviewblue}{HTML}{17365D}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 0},
}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.62em plus 0.12em minus 0.08em}
% Lists reset \parskip to 0 internally so that wrapped lines inside a long
% item keep the item's hanging indentation instead of flushing to the margin.
\setlist[itemize]{
  leftmargin=1.55em,
  itemsep=0.5em,
  topsep=0.35em,
  parsep=0pt,
  before=\setlength{\parskip}{0pt},
}
\setlist[enumerate]{
  leftmargin=1.9em,
  itemsep=0.5em,
  topsep=0.35em,
  parsep=0pt,
  before=\setlength{\parskip}{0pt},
}
\titleformat{\section}
  {\Large\bfseries\color{reviewblue}}
  {}{0pt}{}
\titleformat{\subsection}
  {\large\bfseries\color{reviewblue}}
  {}{0pt}{}
\titlespacing*{\section}{0pt}{1.7em}{0.55em}
\titlespacing*{\subsection}{0pt}{1.25em}{0.4em}

% Clean page: no header, no footer, no page numbers, no rules.
\pagestyle{empty}

\begin{document}

${body}

\end{document}
`;
}

function compileLatex(texPath) {
  const reproducibleEnvironment = {
    ...process.env,
    FORCE_SOURCE_DATE: "1",
    SOURCE_DATE_EPOCH: "946684800",
  };
  const compileResult = spawnSync(
    "latexmk",
    ["-cd", "-pdf", "-interaction=nonstopmode", "-halt-on-error", texPath],
    {
      cwd: path.dirname(texPath),
      env: reproducibleEnvironment,
      stdio: "inherit",
    },
  );

  if (compileResult.error) {
    fail(`Could not run latexmk: ${compileResult.error.message}`);
  }
  if (compileResult.status !== 0) {
    fail(`latexmk failed with exit code ${compileResult.status}.`);
  }

  const logPath = texPath.replace(/\.tex$/i, ".log");
  const savedLogPath = texPath.replace(/\.tex$/i, "_compile.log");
  const pdfPath = texPath.replace(/\.tex$/i, ".pdf");

  if (!existsSync(logPath) || !existsSync(pdfPath)) {
    fail("latexmk completed without producing the expected PDF and log.");
  }

  copyFileSync(logPath, savedLogPath);
  const compileLog = readFileSync(savedLogPath, "utf8");
  const warningPattern =
    /(^!|LaTeX Warning|Package .* Warning|Overfull|Underfull|undefined|Citation)/m;

  const cleanupResult = spawnSync("latexmk", ["-cd", "-c", texPath], {
    cwd: path.dirname(texPath),
    env: reproducibleEnvironment,
    stdio: "inherit",
  });

  if (cleanupResult.error || cleanupResult.status !== 0) {
    fail("latexmk compiled the PDF but failed to clean auxiliary files.");
  }
  if (warningPattern.test(compileLog)) {
    fail(`Compilation warnings remain; inspect ${savedLogPath}.`);
  }
}

function fail(message) {
  console.error(message);
  process.exit(1);
}
