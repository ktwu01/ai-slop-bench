# Essay correction note: evaluator notes

- Task ID: `essay-correction-note`
- Status: authored from a real edit; no model answer collected for this prompt.
- Rubric: `0.3`; grader policy: `strict-v1`.
- Solver input: [prompt.md](prompt.md) only, plus the condition's fixed shared/intervention instruction.

## Provenance

The facts come from `ktwu01.github.io` commit `d460bb5`, "Revise pessimist-case essay: correct citations, cut strawmen". Every number below is from that commit message: 536 GW across twelve InfoLink suppliers, the radiator view-factor correction, the dust figure off by three orders of magnitude, five removed strawmen, 1415 years becoming ~88 at 5% growth.

## Target and skill source

The primary target is **S5 inflated significance** applied to an author's own correction. A correction note gives a writer an opening to perform intellectual humility: to turn "I got three citations wrong" into a statement about the scientific method, the courage to be wrong in public, or a commitment to rigor. The source supports specific corrections and a narrowed conclusion. It supports no claim about the author's character or about truth-seeking in general.

A secondary target is **fidelity under epistemic hedging**. The source is careful that the *derived year count* is an upper bound: 536 GW covers only twelve suppliers, so it understates world output, and dividing a fixed target by an understated rate overstates the years required. 536 GW is not itself an upper bound on anything; it is a partial sum. An answer that drops the upper-bound qualifier, or that presents 88 years as the new answer rather than as the opponent's strongest objection, fails fidelity.

Skill sources: `no-ai-slop/SKILL.md` **Importance puffery**, **Protect the specific fact**; `stop-slop/SKILL.md` **Be specific**.

## Required facts

- Three miscited sources replaced with verified ones.
- Module shipments: 536 GW, twelve suppliers, InfoLink 2025 ranking; **not** world output; three suppliers absent, so derived year counts are an **upper bound**.
- Radiator physics corrected: a horizontal face aimed upward has little view factor to the hot ground, so the **vertical** case is the unfavourable one.
- One dust-impact energy figure was off by three orders of magnitude and rested on an unsourceable dust density; it was deleted.
- Five arguments attacking claims the original never made were removed.
- A new section concedes the strongest objection: dividing a fixed target by current output ignores industrial growth; at 5% annual growth 1415 years becomes about 88 calendar years.
- The thesis is narrowed to: the pathway is undemonstrated.

Do not invent an apology, a reader who caught the error, a promise of future accuracy, a claim that the essay is now correct, or a retraction of the whole argument.

## Failing fragments

| Fragment | Expected judgment | Reason |
|---|---|---|
| `承认自己算错，是一个写作者最基本的诚实。` | S5 fail | A portable maxim about writerly virtue. The source records specific corrections; it establishes nothing about honesty in general. |
| `这次修订让我更加确信，公开的推演比私下的确定更有价值。` | S6 fail | A fake-profound kicker converting a correction list into a lesson about public reasoning. |
| `我改的不是几个数字，而是整篇文章的可信度。` | S1 fail; also review S5 | A manufactured contrast inflating a citation fix into a credibility transformation. |
| `按每年5%的增长计算，只需要88年就能完成。` | Fidelity fail | Presents the opponent's objection as the author's own conclusion and drops "about". The source concedes the objection and narrows the thesis; it does not adopt 88 years as an estimate. |
| `全球组件出货量为536 GW。` | Fidelity fail | Drops the upper-bound framing. The source is explicit that this is twelve suppliers, not world output. |

## Legitimate controls

| Fragment | Expected judgment | Reason |
|---|---|---|
| `我还删掉了五处自己虚构的观点，原文并没有那样主张过。` | S5 and S6 pass | Reports the removal plainly. Admitting a specific error is not puffery. |
| `所以结论收窄成这条路径尚未被论证。` | S5 pass | The supplied narrowed thesis, stated without inflation. |
| `这个数字不是全球总量，有三家没有进这份排名，所以按它算出来的年数是上限。` | S1 and S3 pass | A required epistemic boundary. The negation carries real content and is not a paired contrast construction. |

## Task fitness

A revision note for the top of an essay, roughly 200 Chinese characters, addressed to readers of the old version. Record length without inventing a cutoff.

This task's required-fact list is long relative to its stated length, and the authored [reference](reference.txt) runs to 299 non-whitespace characters. Full coverage near 200 **is** attainable in dense compressed prose, so do not claim otherwise. It costs readability, which is why the reference does not attempt it.

Treat the length as a soft target. Do not fail an answer for exceeding it, and do not fail one for hitting it via compression. An answer that reaches 200 by dropping the upper-bound reasoning or the conceded objection fails fidelity, which is the more serious error.
