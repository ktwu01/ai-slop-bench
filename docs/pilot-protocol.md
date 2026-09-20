# Pilot protocol

How to collect answers for any task in this benchmark. Task-specific facts live in each task's `rubric.md`; nothing here is about one task.

## Delivery

The model answers the writing request directly. No Harbor, Docker, coding agent, tool use, or output file is required. Save the returned text externally for scoring. A fresh chat, an API call, or a CLI that exposes its configuration can supply the answer. Do not mix interfaces inside a matched comparison.

## Conditions: one controlled difference

Both arms receive this shared instruction, followed by the task's `prompt.md`:

> You are an assistant completing the user's writing task. Preserve the supplied facts, negations, conditions, and uncertainty. Do not invent claims or commitments. Return the requested text directly.

| Condition | Prompt construction |
|---|---|
| A: no added de-slop guidance | Shared instruction + task |
| B: de-slop guidance | Shared instruction + the task's style paragraph + task |

Factual guidance is shared; only the style paragraph differs. Each rubric version ships its own paragraph, so a task's version determines which one it gets. The comparison estimates the effect of the whole paragraph and cannot attribute the effect of any single sentence without a further ablation.

**A task prompt may not carry style guidance of its own.** Anything inside the task text reaches both arms and destroys the single controlled difference. See [task-design-rules.md](task-design-rules.md).

## Steps

1. Freeze the task, shared instruction, style paragraph, rubric, and versions before collecting any output.
2. Collect five independent answers per condition per task, interleaving A and B. Use a new conversation or independent request for each answer. Never ask one conversation to de-slop its own previous answer.
3. Hold model, product/API/CLI, settings, and context constant. Record the visible instruction stack. If the interface hides system instructions, record that limitation and label A as **no added guidance**, not as verified absence of every style instruction or training effect.
4. Save exact prompts and raw answers. Keep references, rubrics, prior answers, and grader feedback out of solver context.
5. Review blinded to A/B and to model identity. Inspect every reported defect and fidelity failure. Report all outputs, counts, unresolved cases, and the rubric version.

## Scoring

Under **strict-v1**, one confirmed style defect, fidelity failure, invalid answer, or task-fitness failure gives `overall=fail` and `reward=0`. No averages, partial credit, or compensating strengths. Finish every judgment even after finding a failure. An exception needs task or source support.

Unresolved judgments stay visible. With no failure and any required judgment unresolved, `reward=null`. Publish per-family and fidelity results beside the overall count.

The [score gate](../scripts/score_review.py) validates a review and aggregates its judgments. It does not classify prose.

## Versions

Tasks on different rubric versions are not pooled. A v0.2 task keeps its v0.2 rubric, judge, and style paragraph; a v0.3 task uses v0.3. Report versioned results separately and identify the difference before any comparison.

Authored references and deliberately defective fragments are calibration material. They set grading boundaries and are never empirical success or failure counts.
