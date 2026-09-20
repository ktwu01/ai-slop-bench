# Direct-answer writing tasks

| Task | Solver prompt | Primary target | Reviewer material |
|---|---|---|---|
| `support-ticket-intro` | [Tool introduction](support-ticket-intro/prompt.md) | S1–S4, v0.2. The original task; keeps its own rubric and style paragraph | [Rubric](support-ticket-intro/rubric.md) |
| `essay-correction-note` | [Revision note](essay-correction-note/prompt.md) | S5 and fidelity: perform humility about one's own errors, or drop the upper-bound reasoning and the conceded objection | [Rubric](essay-correction-note/rubric.md), [reference](essay-correction-note/reference.txt) |

For what exists right now, which rubric each task uses, and whether any answers have been collected:

```bash
python3 scripts/status.py
```

That reads the tree. This table describes the tasks; it does not track their state.

## What makes a task usable

正常的 prompt，然后生成了 ai slop。不能在 prompt 里就说到 slop。见 [task-design-rules.md](../../docs/task-design-rules.md)。

这个 task 要的是一篇长文修订后的说明，内容是引用、物理和结论，跟文风无关。压力来自处境：公开承认自己出错，容易写成一种姿态，而事实并不支持。

The scenario and every fact come from `ktwu01.github.io` commit `d460bb5`, "Revise pessimist-case essay: correct citations, cut strawmen". The rubric's failing fragments are **authored**, not observed; the commit supplies the situation, not a recorded model failure.

## Matched A/B instructions

The shared instruction, the A/B construction, and the sampling steps are in [docs/pilot-protocol.md](../../docs/pilot-protocol.md). Each rubric version supplies its own style paragraph.

The **v0.3** paragraph, used by v0.3 tasks:

> 直接说明具体事实和作用。避免用固定对比句式给普通事实增加戏剧感。删去只宣布强调或解释重要性的引导语。不要用一连串职责限制和否定句来回应读者未提出的担心，也不要重复表达同一信息。不要把普通安排拔高成宏大转变，或附加没有依据的价值宣言。结尾保留具体观察、已有感受或下一步安排，删去装饰性比喻和泛泛的人生道理。直接解释原因和做法。不要自问自答、故作悬念，也不要假设读者忽略了某个关键。保留有事实依据的区别、感受、致谢和真正需要的问题。

`support-ticket-intro` keeps its v0.2 paragraph, recorded in its own [rubric](support-ticket-intro/rubric.md). Results are not pooled across versions.

## Grading

v0.3 tasks use [rubric v0.3](../../docs/rubric-v0.3.md) and [the v0.3 judge](../../graders/strict-editor-v0.3.md); v0.2 tasks use [rubric v0.2](../../docs/rubric.md) and [its judge](../../graders/strict-editor.md). Always read the task's own `rubric.md` alongside the shared one. Scoring rules are in [the protocol](../../docs/pilot-protocol.md).
