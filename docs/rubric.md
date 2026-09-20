# Rubric v0.2: slop patterns, factual fidelity, and task usefulness

Status: unfrozen development rubric for the approved [support-ticket introduction](../examples/tasks/support-ticket-intro/prompt.md), using grader policy **strict-v1**. The current protocol evaluates direct text answers; no Harbor, Docker, command execution, or output file is required from the model. Human reviewers and the [strict editorial judge](../graders/strict-editor-v0.3.md) use the same policy. The [score gate](../scripts/score_review.py) validates their judgments and calculates the result; it does not judge prose itself.

This v0.2 rubric continues to govern the original pilot. The [three new tasks](../examples/tasks/index.md) use [v0.3](rubric-v0.3.md), which adds S5–S7 while retaining strict-v1 and the S1–S4 definitions. Do not apply the support-ticket factual checklist to those tasks.

The benchmark asks whether ordinary writing requests elicit skill-described habits, and what changes when the same model receives a de-slop prompt. The task itself does not disclose the rubric. A pattern violation measures the declared editorial preference; it is not evidence of authorship or a universal judgment about a phrase.

## Version and evidence boundary

The approved v0.1 example focused on binary contrasts. The first user-supplied development answer contains no declared binary contrast. It exposes metadiscourse and defensive framing instead. Version v0.2 adds those families and broadens the B intervention accordingly. This is an explicit development revision after seeing an example, not a preregistered success on unseen data. The confirmed S3 passage is the full `工具只负责…不会代替…也不会自动…` chain.

The [observed answer and annotation](../examples/observations/support-ticket-user-001.md) are a calibration example. The stricter development policy also confirms its redundant grouping description under S4. Freeze v0.2 task, intervention, matching rules, and strict-v1 grader policy before collecting fresh paired outputs. Record both versions on every result. Do not reinterpret older scores as results collected under this policy.

## Strict grading policy: strict-v1

- **One confirmed defect fails the answer.** Any S1–S4 failure gives an overall reward of zero. Good facts, fluency, usefulness, and clean sentences elsewhere cannot offset it. No partial credit or averaging across families.
- **Inspect every family.** Finish S1, S2, S3, S4, factual fidelity, validity, and task fitness even after finding a failure. A contrast-free answer has not earned a style pass.
- **Evaluate the construction and its function.** Paraphrasing a disclaimer or splitting it across sentences does not remove S3. Keep literal S1 counts separate from contextual judgments about equivalent rhetorical contrasts.
- **Require evidence for exceptions.** Cite the source fact or task requirement that makes a flagged form necessary. General claims such as “sounds natural,” “could reassure readers,” “is common in announcements,” or “is otherwise helpful” do not justify an exception. A supplied fact justifies conveying its content; it does not automatically justify surrounding emphasis or defensive disclaimers.
- **Require a complete clean review to pass.** Quote exact defective spans and explain the violated rule. Give a reason for every family pass. Use `unresolved` only for a concrete ambiguity that prevents a decision, and explain what evidence would resolve it. Do not downgrade a defined calibration failure to unresolved merely by imagining a charitable reading.
- **Keep uncertainty visible.** An unresolved review never receives a passing reward. A confirmed failure still receives zero when other judgments are unresolved. Grader errors and missing reviews are not model successes or model failures.

Each task's own `rubric.md` carries the calibration cases defining failures and legitimate uses under this policy. They calibrate judges; keep them out of the solver context.

## Review procedure

1. Save the exact task, answer, prompt condition, model identifier, available settings, and rubric version. Use `unknown` when details are unavailable. Reviewers see the task and answer but not A/B labels.
2. Mark candidate spans. Report occurrence counts separately from confirmed style defects.
3. Explain each confirmed defect against the task and source facts. Check exceptions and preserve meaning-bearing negation.
4. Check required facts, additions, and usability independently. A clean style does not compensate for altered facts.
5. Retain the raw answer and per-rule evidence. Resolve uncertain cases before publishing a binary pass rate; do not silently count uncertainty as a failure.

## Style families enabled for this example

| ID | Family | Candidate evidence | Confirmation and exceptions |
|---|---|---|---|
| S1 | Formulaic binary contrast | `不是…而是…`, `不只是/不仅是…更是/而是…`, `不关乎…而关乎…` | Confirm gratuitous rhetorical reframing when it introduces an unstated opposing view or inflated identity. A requested correction, needed factual distinction, or protected quotation may be justified. Record a justified occurrence without declaring a slop failure. |
| S2 | Interpretive metadiscourse | A preface such as `需要特别说明的是`, `值得注意的是`, `重要的是` that tells readers how much attention to give the next fact | Confirm when removing the preface preserves the information and requested function. For this short introduction, `需要特别说明的是` is a failure even when the next fact matters operationally. Retain substantive warning content; exempt a preface only with a specific task-grounded purpose or protected quotation. |
| S3 | Defensive overframing | A role-limitation and denial chain such as `工具只负责…不会代替…也不会自动…`, or broad negative reassurance | Confirm when a passage defensively presents the tool's role through stacked limits and denials, rebuts an unraised concern, or gives sweeping reassurance. The full chain is confirmed S3 in this sample. The clauses need not repeat the same fact, and the judgment does not depend on the words `任何消息`. Preserve required facts while assessing how they are presented; factual coverage does not exempt the framing from style review. |
| S4 | Redundant elaboration | Adjacent paraphrases or a recap that adds no distinct proposition | Identify the repeated proposition and confirm if removing one expression preserves the supported information. In this task, `内容相近、属于同类问题` is confirmed S4: it restates the single grouping criterion without a supplied distinction. Do not invent a nuance to excuse repetition. Distinct workflow steps, different facts, and a requested summary remain legitimate. |

For S1's literal occurrence detector, ignore whitespace and match within a span delimited by `。！？；!?;` or a newline. Also allow exactly one such boundary if the next span begins with the corresponding second marker (`而是`, `更是`, or `而关乎`). Do not bridge intervening sentences. Keep raw character offsets for evidence. This declared list does not claim to detect every possible contrast.

S2–S4 require context. A literal detector may nominate a span, but cannot certify that its function is empty, defensive, or repetitive. If one passage matches several families, keep the labels but count one passage when reporting the number of defective passages. Do not inflate severity by counting each negative word separately.

### Preserve facts while grading their framing

Source facts: the support staff write replies; the tool does not automatically send them to customers.

A concise statement such as `回复由客服撰写，工具不会自动向客户发送。` satisfies these boundaries. The negation is required information and is not a defensive-framing failure by itself.

The observed cluster is:

> 需要特别说明的是，工具只负责整理和分组，不会代替大家回复客户，也不会自动发送任何消息，回复仍由客服同事自行判断和撰写。

S2 applies to `需要特别说明的是`. S3 applies to the full sequence **`工具只负责整理和分组，不会代替大家回复客户，也不会自动发送任何消息`**. The sequence stacks a restrictive role statement and two denials into a defensive explanation of what the tool will not do. All three clauses contribute to this confirmed S3 passage. Neither repeated facts nor the intensifier `任何消息` is required for that judgment.

The following `回复仍由客服同事自行判断和撰写` further reinforces the responsibility disclaimer. Count this as one S3 passage, with its constituent spans retained as evidence. Preserve the source's human-reply and customer-sending facts in direct wording. Fidelity and defensive presentation are separate judgments.

## Factual fidelity and additions

For this task, verify these propositions:

- Similar tickets are grouped, and each group includes original-ticket links.
- Staff can consult a group, then open and handle original tickets.
- Staff write the replies; the tool does not automatically send to customers.
- The pilot starts next Monday with eight after-sales colleagues.
- Feedback is collected after two weeks; expansion is decided afterward, not promised in advance.

Report `coverage` (preserved/missing/changed) separately from `additions`:

- **Unsupported factual claim or commitment:** an invented result, capability, guarantee, or rollout decision. This can fail fidelity when the unsupported assertion is unambiguous.
- **Unsupported advice or procedure:** new suggested actions not present in the source. Label them separately from false factual claims. They fail fidelity if they are presented as an established obligation, policy, or authorization that changes the task; otherwise assess whether they are useful or unnecessary additions.
- **Ambiguous scope:** wording such as `不会自动发送任何消息` could broaden a ban on customer sending to all messages, or could inherit the customer context. This factual-scope question remains open independently of its confirmed S3 defensive-overframing judgment. Do not require a proven contradiction to assign S3, or infer a factual contradiction from the style failure alone.

Required facts can use any equivalent wording. A reference answer is illustrative, never the only acceptable answer.

## Task fitness and overall result

Review whether the answer is relevant, readable, and usable as the requested spoken introduction. The phrase `约180字` gives an approximate target. Report the counting convention and observed length; do not invent an exact cutoff after seeing an answer. Similarly, distinguish a short introduction from an expressly specified physical-line format. Two paragraphs alone do not establish a slop failure.

For each answer report:

- `validity`: usable answer exists and addresses the task.
- `pattern_occurrences`: family, raw span, and literal count where defined.
- `style_verdicts`: confirmed defect / justified use / uncertain, with reasons.
- `fidelity`: pass / fail / uncertain, including coverage and additions.
- `task_fitness`: pass / fail / uncertain, with any length or format observations.
- `overall`: pass / fail / unresolved.

Overall passes only when validity, fidelity, task fitness, and all four style families explicitly pass. Any confirmed failure sets `overall=fail` and `reward=0`, even when every other check passes. If no failure exists and any judgment remains unresolved, set `overall=unresolved` and `reward=null`. Only a fully passing review receives `reward=1`. Missing fields or fabricated evidence invalidate the review. Publish unresolved counts; adjudicate them before computing a definitive overall pass rate.

Always report per-family rates and fidelity alongside the overall result. A contrast-free answer can fail other families. Do not describe those failures as binary-contrast hits. For the observed development sample, strict-v1 confirms S2, S3, and S4; no pass-rate or A/B effect follows from one supplied answer.

## Source mapping and limits

- `no-ai-slop/SKILL.md`: **Binary contrasts**, **Interpretive metadiscourse**, **Negative listing**, **Make every sentence earn its place**, and **Keep the user's meaning**.
- `stop-slop/SKILL.md`: **Cut filler phrases**, **Break formulaic structures**, **Be specific** (including avoiding vague extremes), and **Trust readers**; `references/structures.md` describes binary contrasts and negative listing.
- Defensive overframing is this benchmark's contextual application of those principles and the user's requested target. The skills do not establish that every responsibility limit or negative sentence is slop.

These are specified editorial preferences with examples and exceptions. Skill authority alone does not establish a phrase's failure rate, a model's training history, or the quality of an unseen output. New families require a versioned development change and fresh evaluation; they must not be added silently to a held-out score.
