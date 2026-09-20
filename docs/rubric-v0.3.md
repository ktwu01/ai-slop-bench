# Rubric v0.3: additional writing tasks

Status: development. Applies to the [v0.3 tasks](../examples/tasks/index.md), using **strict-v1**. The original support-ticket example retains [rubric v0.2](rubric.md), its original task, and its existing review. There are no model results for the new tasks.

This version preserves S1–S4 definitions and strict-v1 grading from v0.2 and adds S5–S7 from the writing skills. The support-ticket facts and calibration examples in v0.2 belong only to that task. For each task, use its own `rubric.md` factual checklist, exceptions, reference, and calibration fragments. A prompt that qualifies as a task at all is defined in [task-design-rules.md](task-design-rules.md). Review all seven style families even when one family is the primary elicitation target.

## Added style families

| ID | Pattern and skill source | Confirmed defect | Legitimate use |
|---|---|---|---|
| S5 | Inflated significance; `no-ai-slop` **Importance puffery** and **Superficial analysis** | Attaching an unsupported grand identity, cultural turning point, or generic dedication claim to a modest change. Examples include asserting that an extra service window redefines public service or proves a deep institutional commitment. Cite the inflated clause and the missing support. | A specific benefit established by the facts, a supported comparison, or an actual documented milestone. Positive language alone is not a failure. |
| S6 | Fake-profound ending; `no-ai-slop` **Fake-profound kickers**, `stop-slop` **Cut quotables**, and `haohao-shuohua` **比喻红线** | Ending with an invented universal life lesson, decorative metaphor, or portable sentimental maxim that substitutes grandeur for the supplied events. A paraphrase of the same ornamental ending still fails. | A supplied personal feeling, concrete observation, ordinary gratitude, attributed quotation, or task-relevant explanatory analogy. The diary asks for a feeling, so deleting its supported emotion is not an improvement. |
| S7 | Staged insight; `no-ai-slop` **Faux-insight setups**, **Rhetorical setups**, **Colon reveals**, and **Dramatic fragmentation**; `stop-slop/references/structures.md` **Rhetorical Setups** | Manufacturing an overlooked truth, self-answered suspense question, or dramatic reveal before a straightforward explanation. Identify the setup and show what concrete explanation it delays or replaces. | Genuine questions that seek missing information, supplied quotations, ordinary labels, or Q&A structure requested by the task. A colon or a question mark alone is not a failure. |

S5 concerns asserted significance; S6 concerns an ornamental closing; S7 concerns staged presentation of insight. A passage may receive multiple family labels when each definition applies. Preserve that evidence without counting the passage several times. S1–S4 still apply to false contrasts, metadiscourse, defensive framing, and repetition in these tasks.

## Strict decision rule

One confirmed style defect, fidelity failure, invalid answer, or task-fitness failure gives `overall=fail` and `reward=0`. No averages, partial credit, or compensating strengths. Finish every judgment even after finding a failure. An exception needs task or source support; an imagined audience preference is insufficient. Required facts, appropriate warmth, and real causal explanations must survive.

Unresolved judgments remain visible. When no failure exists and any required judgment is unresolved, `reward=null`. All seven style families plus validity, fidelity, and task fitness must pass for `reward=1`. Grader errors invalidate the review and are not model outcomes.

## Reviewer output and execution

Use [strict-editor-v0.3.md](../graders/strict-editor-v0.3.md). A review contains `rubric_version: "0.3"`, `policy_version: "strict-v1"`, `task_id`, the verbatim `answer`, all S1–S7 judgments in `style`, and validity/fidelity/task-fitness judgments. Each judgment has a verdict and reason; every style failure also has exact quoted evidence. Include the declared S1 literal count separately from contextual equivalent constructions. Only the literal occurrence count uses the v0.2 matching rule; it does not constrain contextual evaluation.

```bash
python3 scripts/score_review.py review.json
```

The score gate validates the review and combines its judgments. It does not classify prose. Version 0.3 requires S1–S7; version 0.2 continues to require S1–S4. Task identity is recorded for provenance and must be checked by the reviewer against the supplied task; the gate does not verify the task's semantics.

Freeze task texts, B guidance, rubric, calibration, and judge instructions before collecting fresh A/B answers. Author-written references and defective fragments establish the intended grading boundaries, not an empirical failure rate. Keep them out of solver context.
