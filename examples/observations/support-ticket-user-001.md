# Development observation: support-ticket introduction

This is a user-supplied answer used to develop rubric v0.2 and grader policy strict-v1. It is not a controlled A/B trial or a held-out result. The current strict policy confirms S4 in addition to S2 and S3; this is a recorded development revision.

## Provenance

| Field | Recorded value |
|---|---|
| Source | User pasted the answer in this conversation |
| Model | GPT, as reported by the user |
| Exact version and generation settings | Unknown |
| Harness | User reports no Harbor |
| De-slop condition | User reports no de-slop guidance |
| Exact full prompt / shared instruction | Not supplied; not verified identical to the approved prompt |
| System instructions / previous context | Unknown |
| Matched B answer | None |
| Raw answer | [support-ticket-user-001.txt](support-ticket-user-001.txt) |
| Use | Development/calibration, excluded from fresh paired evaluation |
| Grading policy | Rubric 0.2 / strict-v1 |
| Structured review | [support-ticket-user-001.review.json](support-ticket-user-001.review.json), authored from the annotation below |

## Annotation

The relevant source is the [approved task](../tasks/support-ticket-intro/prompt.md), and the current definitions are [rubric v0.2](../../docs/rubric.md).

| Rule or dimension | Evidence | Judgment |
|---|---|---|
| S1 binary contrast | No declared `不是…而是…`, `不只是…更是…`, or `不关乎…而关乎…` construction | Zero hits. Negative words alone do not make a contrast. |
| S2 metadiscourse | `需要特别说明的是` | Confirmed under this rubric's preference for direct factual explanation. The preface announces emphasis; removing it leaves the operational information intact. |
| S3 defensive overframing | `工具只负责整理和分组，不会代替大家回复客户，也不会自动发送任何消息` | Confirmed as one defensive passage: a restrictive role statement followed by two denials. All three clauses contribute. The judgment does not require repeated facts, the words `任何消息`, or a proven factual contradiction. The following `回复仍由客服同事自行判断和撰写` reinforces the same disclaimer. Preserve the underlying source facts when revising the expression. |
| S4 redundant elaboration | `内容相近、属于同类问题` | Confirmed under strict-v1. Both descriptions express the single supplied grouping criterion. Removing either preserves that information; the task supplies no distinction to justify the repetition. |
| Core fact coverage | Grouping, links, workflow, human replies, customer autosending limit, Monday, eight colleagues, two-week feedback, conditional expansion | All core propositions appear. Coverage alone does not certify all added wording. |
| Scope | `不会自动发送任何消息` | Separate fidelity review flag: literally broader than customer sending, but the surrounding customer context may limit its meaning. This uncertainty does not weaken its confirmed S3 style judgment. No definite factual contradiction assigned. |
| Added procedure | `大家按日常方式处理工单即可` | Unsupported workflow assurance; review whether it introduces a material authorization. |
| Added advice | `留意分组是否准确、查找工单是否方便，以及实际使用中的问题` | Additional feedback suggestions, not invented measured results. Judge separately from false facts. |
| Length / layout | 247 non-whitespace characters including punctuation; 227 Han/numeric characters; two paragraphs | Descriptive observations. No retroactive exact threshold for `约180字`, and no automatic failure for two paragraphs. |

The answer fails **rubric v0.2 / strict-v1** on S2, S3, and S4 and receives `reward=0`. Each confirmed family failure is sufficient. The full `工具只负责…不会代替…也不会自动…` sequence is one confirmed S3 passage. Fidelity questions about additions remain explicitly flagged and cannot offset the confirmed failures. The original contrast-only detector would record zero S1 hits. Do not relabel this as a successful “not X, but Y” trap or as a preregistered result.

This sample shows why a contrast-only rubric misses other intended patterns. It does not establish that de-slop prompting improves an answer, or that a model's pass rate is below any percentage. Those questions require fresh paired samples under the frozen protocol.
