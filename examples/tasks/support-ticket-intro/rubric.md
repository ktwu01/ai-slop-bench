# Support-ticket introduction: evaluator notes

- Task ID: `support-ticket-intro`
- Rubric: `0.2` (S1–S4); grader policy: `strict-v1`
- Solver input: [prompt.md](prompt.md) only, plus the shared instruction and, in arm B, the v0.2 style paragraph
- Shared protocol: [docs/pilot-protocol.md](../../../docs/pilot-protocol.md)

This task predates S5–S7 and stays on [rubric v0.2](../../../docs/rubric.md) with the [v0.2 judge](../../../graders/strict-editor.md). Do not re-score it under v0.3 and do not pool its results with v0.3 tasks.

## Arm B style paragraph (v0.2)

This task keeps its own paragraph. Do not substitute the v0.3 one.

> 直接说明具体事实和作用。避免用“不是X，而是Y”“不只是X，更是Y”“这不关乎X，而关乎Y”这类固定对比句式给普通事实增加戏剧感。删去“需要特别说明的是”“值得注意的是”这类只宣布强调的引导语。避免把具体限制扩写成笼统的否定保证。不要为读者未提出的误解反复辩解，也不要重复交代同一个职责边界；删去没有新增信息的同义复述。

## Required facts

- Groups similar tickets together, each group carrying the original ticket links.
- Staff read the grouping first, then open the original ticket to handle it.
- Replies are written by staff. The tool does not send anything to customers automatically.
- The pilot starts next Monday with 8 colleagues in the after-sales group.
- Feedback is collected after two weeks, then a decision on whether to widen the scope.

Do not invent productivity percentages, guaranteed outcomes, automatic replies, or a confirmed rollout to everyone.

## Necessary boundaries are not defects

Humans write the replies, and the tool does not auto-send. Both are supplied facts and must survive. An answer can preserve them and still fail S3 by stacking them into a defensive chain. Judge the framing, not the presence of 不会.

## Observed calibration

The one collected answer is the [development observation](../../observations/support-ticket-user-001.md). It scores `reward=0` on S2, S3, and S4 with **zero** S1 hits, which is why the v0.1 contrast-only target was widened to S1–S4.

| Family | Span | Judgment |
|---|---|---|
| S1 | — | Zero hits. No declared contrast construction. |
| S2 | `需要特别说明的是` | Announces emphasis; removing it leaves the operational fact intact. |
| S3 | `工具只负责整理和分组，不会代替大家回复客户，也不会自动发送任何消息` | One passage: a role restriction plus two denials, reinforced by `回复仍由客服同事自行判断和撰写`. |
| S4 | `内容相近、属于同类问题` | Two phrasings of the single supplied grouping criterion. |

Fragment-level calibration for this task is in [graders/calibration.md](../../../graders/calibration.md).

That observation has thin provenance: model version, settings, and the exact prompt are unverified, and there is no matched B answer. It is calibration material, not a result.
