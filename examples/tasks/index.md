# Direct-answer writing tasks

One authored task, alongside the [approved support-ticket pilot](../one-task-ablation.md). It has not been tested on models.

| Task | Solver prompt | Primary target | Reviewer material |
|---|---|---|---|
| `essay-correction-note` | [Revision note](essay-correction-note/prompt.md) | S5 and fidelity: perform humility about one's own errors, or drop the upper-bound reasoning and the conceded objection | [Rubric](essay-correction-note/rubric.md), [reference](essay-correction-note/reference.txt) |

## What makes a task usable

正常的 prompt，然后生成了 ai slop。不能在 prompt 里就说到 slop。见 [task-design-rules.md](../../docs/task-design-rules.md)。

这个 task 要的是一篇长文修订后的说明，内容是引用、物理和结论，跟文风无关。压力来自处境：公开承认自己出错，容易写成一种姿态，而事实并不支持。

The scenario and every fact come from `ktwu01.github.io` commit `d460bb5`, "Revise pessimist-case essay: correct citations, cut strawmen". The rubric's failing fragments are **authored**, not observed; the commit supplies the situation, not a recorded model failure.

## Matched A/B instructions

Both arms receive this shared instruction followed by the exact same `prompt.md`:

> You are an assistant completing the user's writing task. Preserve the supplied facts, negations, conditions, and uncertainty. Do not invent claims or commitments. Return the requested text directly.

A adds no style guidance. B inserts the following fixed **v0.3** style paragraph between the shared instruction and task:

> 直接说明具体事实和作用。避免用固定对比句式给普通事实增加戏剧感。删去只宣布强调或解释重要性的引导语。不要用一连串职责限制和否定句来回应读者未提出的担心，也不要重复表达同一信息。不要把普通安排拔高成宏大转变，或附加没有依据的价值宣言。结尾保留具体观察、已有感受或下一步安排，删去装饰性比喻和泛泛的人生道理。直接解释原因和做法。不要自问自答、故作悬念，也不要假设读者忽略了某个关键。保留有事实依据的区别、感受、致谢和真正需要的问题。

The original pilot retains its v0.2 B paragraph and scoring. Do not pool results across these intervention/rubric versions without identifying the difference.

## Grading and sampling

Use [rubric v0.3](../../docs/rubric-v0.3.md), [the v0.3 judge](../../graders/strict-editor-v0.3.md), and the task-specific rubric. All S1–S7 apply. Under strict-v1, any confirmed defect gives zero; no partial credit. Keep unresolved judgments separate from passes. The score gate accepts v0.3 reviews with exactly S1–S7 and preserves v0.2 support.

For a future pilot, freeze these materials first. Collect five fresh independent first answers per arm, interleaving A/B with the same model, interface, and settings. Save exact prompts, visible instructions, model/settings, raw answers, task ID, and all versions. Blind graders to condition and model identity. Report every answer, per-family outcomes, fidelity, and unresolved cases. If platform instructions are hidden, label A as "no added guidance."

Harbor is unnecessary. Models answer directly; operators save the returned text and grader review externally. Authored bad fragments and the reference answer are calibration material, never empirical success or failure counts.
