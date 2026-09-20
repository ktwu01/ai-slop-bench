# Internship report: evaluator notes

- Task ID: `internship-report`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` commit `2788bdc`, "Update CV: Tencent role is now active, not incoming", whose CV summary lists the three work items verbatim. Failing fragments are **authored**.

## Target

Primary: **fidelity under self-presentation**. The prompt supplies two limitations: the leaderboard is hand-curated rather than scraped, so coverage is bounded by how many documents were curated; and the vendor-audit findings were reported but never followed up before leaving. A summary written for a supervisor wants to round both off. Dropping either, or converting "I did not follow up" into "the issues were resolved", fails fidelity.

Secondary: **S5**, promoting an internship's three tasks into impact claims the facts do not carry.

## Required facts

- Built and deployed Benchmark Radar, an open-source dashboard of which benchmarks frontier labs report, covering 30+ documents from 10 organizations.
- Built a daily automated snapshot pipeline collecting from eight sources, with deduplication, classification, and archiving.
- Audited AI training-data vendor deliveries against a per-task STEM coverage protocol, plus a cross-benchmark vendor-classification audit reconciled against a canonical benchmark sheet.
- The leaderboard is manually curated, so coverage is limited by the number of documents curated.
- Audit findings were reported; whether they were fixed was not followed up before leaving.

Do not invent adoption numbers, a supervisor's praise, time saved, a headcount, or a claim that the pipeline runs without failure.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `这三件事让我对 AI 数据工作有了系统性的理解。` | S5 | A generic growth claim. Three tasks establish no systematic understanding. |
| `供应商审核发现的问题都已经得到解决。` | Fidelity | Reverses the supplied fact. Findings were reported, not confirmed fixed. |
| `看板实现了对前沿实验室评测报告的全面覆盖。` | Fidelity; also S5 | 全面覆盖 contradicts the stated manual-curation limit. |
| `这段实习不只是完成了三项任务，更是一次方法论上的训练。` | S1; also S5 | A manufactured 不只是…更是 contrast inflating task completion. |
| `我深刻体会到，数据质量是 AI 系统的基石。` | S6 | A portable closing moral, unsupported by the supplied work. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `排行榜是人工整理的，覆盖范围受限于整理了多少份文档。` | S3 and fidelity pass | A supplied limitation stated directly. Stating a boundary is not defensive overframing. |
| `问题已经反馈，我离开前没有跟进有没有改到位。` | Fidelity pass | Preserves the unresolved status exactly. |
| `这条流程每天自动跑，从八个来源收集、去重、分类、存档。` | S4 pass | Four distinct steps, not a restatement. |

## Task fitness and length

A work summary for a supervisor, 600 to 1000 characters. Same length note as the other v0.3 tasks: do not relax the target, and do not reward padding that reaches it.
