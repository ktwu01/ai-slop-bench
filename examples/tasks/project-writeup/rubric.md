# Project write-up: evaluator notes

- Task ID: `project-writeup`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` commit `c8926d9`, which added `_portfolio/benchmark-radar.md`. Every number below appears in that file. Failing fragments are **authored**.

## Target

Primary: **S5 inflated significance**. A portfolio blurb is the genre where promotional register is expected, and the prompt names a non-expert reader, which invites grand framing to convey importance. The supplied facts are narrow and countable: a hand-curated ranking answering one question, with published counting rules.

Secondary: **S7 staged insight**, opening with a rhetorical question or a withheld reveal instead of saying what the project is.

## Required facts

- Answers one narrow question: which benchmarks do frontier labs actually report when releasing a model.
- Method: manual curation of model cards, system cards, and technical reports.
- Each document counts at most once per benchmark; card count and organization count are published separately.
- 30+ documents, 10 organizations, 79+ benchmarks.
- Leaderboard shows card count, organization count, and scores over time.
- A daily pipeline collects from eight named sources, deduplicates, classifies by a published taxonomy, and exposes the ranking components.
- MIT licensed, v0.8.0, 117 stars.
- The star-history chart is self-generated and published to its own branch, so growth claims are checkable.

Do not invent users, citations, institutional adoption, comparisons to other projects, or a roadmap.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `在 AI 评测这个混乱的领域里，Benchmark Radar 带来了久违的秩序。` | S5 | Asserts a field-wide condition and a resolution. The source supports a ranking of 30+ documents. |
| `你真的知道实验室在用什么基准吗？大多数人并不知道。` | S7 | A self-answered setup staging an ordinary explanation. |
| `它不只是一个看板，更是一种对可复核性的坚持。` | S1; also S5 | A manufactured contrast converting a dashboard into a principle. |
| `它让每一个关于模型能力的说法都变得可以验证。` | Fidelity; also S5 | 每一个 far exceeds the supplied scope. Only the star-history claim is described as self-checkable. |
| `项目收录了大量文档，覆盖了众多机构和基准。` | S4; also fidelity | Replaces three exact numbers with vague quantifiers. The counts are the information. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `同一份文档对同一个基准最多只算一次，卡片数和机构数分开公布。` | S5 pass | A supplied counting rule. Methodological precision is not puffery. |
| `星数变化图由项目自己生成并发布到单独分支，所以增长的说法都能自己核对。` | S5 pass | The supplied verifiability claim, scoped to what it actually covers. |
| `它回答一个很窄的问题：前沿实验室发布模型时，实际报告了哪些基准？` | S7 pass | A colon introducing the supplied question. The task requires stating what the project does; this is not a staged reveal. |

## Task fitness and length

A portfolio blurb for a non-expert reader, 600 to 1000 characters. Explaining an unavoidable term in plain words is appropriate for the stated reader and is **not** a defect, but the prompt does not ask for it, so its absence is also not a defect. Judge only whether the writing is usable for the named reader.
