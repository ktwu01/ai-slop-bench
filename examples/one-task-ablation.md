# Approved ablation task: introduce a support-ticket pilot

Status: approved by the user on 2026-09-19. Use this single task for the first paired pilot. Expansion to ten tasks follows evaluation of the pilot.

## What this example tests

Does an agent spontaneously reach for the binary-contrast patterns documented in `stop-slop` and `no-ai-slop`, and does adding a focused de-slop prompt suppress those patterns without changing the facts?

The ordinary writing task is identical in both conditions. It contains no banned-phrase list, reference answer, instruction to avoid AI style, or prewritten slop to copy. The scenario invites a product-value explanation, where an agent may introduce an unnecessary rhetorical contrast. A low pass rate is a hypothesis, not a grading requirement.

## The task shown to both agents

> 我们准备在客服组试用一个工单整理工具。它会把同类问题归到一起，每组都附上原工单链接。客服可以先看分组，再打开原工单处理；回复仍由客服自己写，工具不会自动发给客户。
>
> 下周一开始试用，先给售后组的8位同事使用。两周后收集他们的反馈，再决定是否扩大范围。
>
> 请为内部周会写一段介绍，讲清这个工具能帮同事做什么、怎样使用，以及试用安排。读者是客服同事，写成可以直接念出来的发言，约180字。

The Harbor delivery suffix is identical in both conditions: `把最终发言写入 /app/output.txt。`

## The only experimental difference

| Condition | Agent instructions |
|---|---|
| A: neutral | `You are an assistant completing the user's task. Use available tools when needed. Preserve the supplied facts, negations, conditions, and uncertainty. Do not invent claims or commitments.` |
| B: de-slop | The identical neutral instructions, followed by the fixed paragraph below. |

De-slop paragraph:

> 避免用“不是X，而是Y”“不只是X，更是Y”或“这不关乎X，而关乎Y”这类固定对比句式给普通事实增加戏剧感。直接说明具体事实和作用。

The factual-fidelity instruction is shared by both conditions. Only the style paragraph differs. This is a focused intervention derived from the skills' binary-contrast rule, not a claim to evaluate either complete skill. Freeze this exact paragraph before testing.

## Scoring fixed before outputs are collected

Report three results separately:

1. **Target-pattern occurrence:** detect the declared `不是…而是…`, `不只是/不仅是…更是/而是…`, and `不关乎…而关乎…` structures. Match within a span delimited by `。！？；!?;` or a newline, or across exactly one such boundary when the next span begins with the corresponding second marker (`而是`, `更是`, or `而关乎`). Ignore whitespace; permit no intervening sentence or additional boundary. Return the exact text span. Do not expand the pattern list after seeing an answer. Ordinary comparisons and meaningful standalone negation do not count.
2. **Factual fidelity:** preserve grouping similar tickets, original-ticket links, the suggested workflow, human-written replies/no automatic sending, Monday start, eight after-sales colleagues, and collecting feedback after two weeks before deciding on expansion. Invented productivity percentages, guaranteed outcomes, automatic replies, or confirmed rollout to everyone fail fidelity.
3. **Usefulness:** blind review whether the output is a usable spoken introduction. Label each pattern hit as a useful factual distinction or gratuitous rhetorical framing. This prevents a useful contrast from automatically becoming evidence of bad writing.

For the narrow binary score, `pattern-free and faithful = 1` only when a usable answer preserves the required facts and contains no declared target pattern. Label this a **style-preference score**, not proof that every contrast is bad or that a text was AI-written. Also publish the context-aware judgments; do not conflate the two measures.

The approximate length is a normal writing request, not a character-count trap. No hidden exact-wording requirements. Reviewers accept equivalent paraphrases.

## Pilot protocol

Use independent fresh Harbor containers and fresh Codex sessions. Fix model, CLI version, reasoning effort, task text, tool access, and grading across A and B. Replace Codex's shipped base prompt in both conditions: its default already contains anti-slop instructions. Verify the actual recorded base instructions against the expected hash and inspect developer messages for extra writing guidance. Do not expose skills, graders, references, or prior attempts to the solver.

Start with five independent attempts per condition on this single task. Inspect every reported hit and every factual failure. Report individual outputs and counts, not a claimed population rate from a tiny sample. Only curate additional tasks once this example measures the intended behavior.

“Neutral” means no de-slop instruction in the visible agent prompt/configuration. It cannot establish that the underlying model received no such training.

## Sources

- Local `stop-slop/references/structures.md`: Binary Contrasts.
- Local `no-ai-slop/SKILL.md`: Binary contrasts; Keep the user's meaning.
- The base override was verified in the neutral Harbor smoke trial at `jobs/slop-neutral-smoke-20260919`; that trial used an older explicit-ban task and is not a result for this proposed example.
