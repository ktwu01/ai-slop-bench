# Direct-answer writing tasks

| Task | Solver prompt | Primary target | 篇幅 | Reviewer material |
|---|---|---|---|---|
| `support-ticket-intro` | [Tool introduction](support-ticket-intro/prompt.md) | S1–S4, v0.2. The original task; keeps its own rubric and style paragraph | 约180字 | [Rubric](support-ticket-intro/rubric.md) |
| `essay-correction-note` | [Revision note](essay-correction-note/prompt.md) | S5 and fidelity: perform humility about one's own errors | 约200字 | [Rubric](essay-correction-note/rubric.md), [reference](essay-correction-note/reference.txt) |
| `project-writeup` | [Portfolio blurb](project-writeup/prompt.md) | S5 and S7: promotional register for a narrow, countable project | 600–1000字 | [Rubric](project-writeup/rubric.md) |
| `homepage-trim` | [Site update note](homepage-trim/prompt.md) | S5 and S6: reframe deleting your own accomplishments as a philosophy | 600–1000字 | [Rubric](homepage-trim/rubric.md) |
| `publication-status-note` | [Lab meeting update](publication-status-note/prompt.md) | S5, S2, S4: inflate a one-phrase correction to fill the length | 600–1000字 | [Rubric](publication-status-note/rubric.md) |
| `carry-proposal-summary` | [Reading group intro](carry-proposal-summary/prompt.md) | S5, S7, fidelity: take a side in someone else's dispute | 600–1000字 | [Rubric](carry-proposal-summary/rubric.md) |
| `domain-survey-intro` | [Survey intro](domain-survey-intro/prompt.md) | S7 and S5: stage a reveal the material already states | 600–1000字 | [Rubric](domain-survey-intro/rubric.md) |
| `cv-number-fix` | [Meeting update](cv-number-fix/prompt.md) | Fidelity: soften "I wrote all three myself", or read repo stars as personal | 600–1000字 | [Rubric](cv-number-fix/rubric.md) |
| `vaccine-line-incident` | [Case introduction](vaccine-line-incident/prompt.md) | Fidelity and S5: draw a double-standard verdict from separately sourced cases | 600–1000字 | [Rubric](vaccine-line-incident/rubric.md) |
| `bravery-club-recap` | [Discussion minutes](bravery-club-recap/prompt.md) | S6: a discussion about courage invites performing wisdom about courage | 600–1000字 | [Rubric](bravery-club-recap/rubric.md) |
| `conference-abstract-cut` | [Note to collaborators](conference-abstract-cut/prompt.md) | S5: turn a routine length edit into a principle | 600–1000字 | [Rubric](conference-abstract-cut/rubric.md) |
| `lab-tool-boundary` | [Tool introduction](lab-tool-boundary/prompt.md) | S3: chain a tool's four real limits into reassurance. Deliberately parallel to `support-ticket-intro` | 600–1000字 | [Rubric](lab-tool-boundary/rubric.md) |
| `ai-draft-privacy-note` | [Meeting update](ai-draft-privacy-note/prompt.md) | Fidelity: flatten a narrow denial and a volunteered caveat into a verdict | 600–1000字 | [Rubric](ai-draft-privacy-note/rubric.md) |
| `media-coverage-update` | [Message to collaborators](media-coverage-update/prompt.md) | S5 and fidelity: one paper has no new coverage | 600–1000字 | [Rubric](media-coverage-update/rubric.md) |
| `quickfacts-collapse-note` | [Site update note](quickfacts-collapse-note/prompt.md) | S5: amplify supplied reversals into an inspirational arc, or apologize for them | 600–1000字 | [Rubric](quickfacts-collapse-note/rubric.md) |
| `poetry-club-handover` | [Handover document](poetry-club-handover/prompt.md) | Fidelity and S6: round up three deflating numbers, or close with a reflection | 600–1000字 | [Rubric](poetry-club-handover/rubric.md) |
| `finesst-guide-intro` | [Guide intro](finesst-guide-intro/prompt.md) | Fidelity: borrow authority the writer states they lack | 600–1000字 | [Rubric](finesst-guide-intro/rubric.md) |
| `school-tool-launch` | [Tool announcement](school-tool-launch/prompt.md) | S3: manufacture a denial chain from two positively stated limits | 600–1000字 | [Rubric](school-tool-launch/rubric.md) |
| `tqqq-experiment-writeup` | [README intro](tqqq-experiment-writeup/prompt.md) | Fidelity: soften three financial disclaimers | 600–1000字 | [Rubric](tqqq-experiment-writeup/rubric.md) |
| `agent-tool-tryout` | [Tool share](agent-tool-tryout/prompt.md) | S5: a tryout becomes the future of multi-agent work | 600–1000字 | [Rubric](agent-tool-tryout/rubric.md) |
| `buffett-reading-intro` | [Reading guide](buffett-reading-intro/prompt.md) | S5 and fidelity: borrowed reverence, and an analogy that is not Buffett's | 600–1000字 | [Rubric](buffett-reading-intro/rubric.md) |
| `hackathon-recap` | [Team retrospective](hackathon-recap/prompt.md) | S6: close a weekend-project recap with a lesson | 600–1000字 | [Rubric](hackathon-recap/rubric.md) |
| `image-essay-summary` | [Essay abstract](image-essay-summary/prompt.md) | Fidelity: dress an uncited claim about brains as established | 600–1000字 | [Rubric](image-essay-summary/rubric.md) |
| `cv-page-merge` | [Changelog entry](cv-page-merge/prompt.md) | Fidelity: blame tooling for duplicates the writer added | 600–1000字 | [Rubric](cv-page-merge/rubric.md) |
| `benchmark-radar-day-log` | [Dev log](benchmark-radar-day-log/prompt.md) | S5: promote three UI fixes into a philosophy of honest charts | 600–1000字 | [Rubric](benchmark-radar-day-log/rubric.md) |
| `domain-broker-caution` | [Reply to a friend](domain-broker-caution/prompt.md) | Fidelity: treat seller-sourced comparables as market data | 600–1000字 | [Rubric](domain-broker-caution/rubric.md) |

For what exists right now, which rubric each task uses, and whether any answers have been collected:

```bash
python3 scripts/status.py
```

That reads the tree. This table describes the tasks; it does not track their state.

## 篇幅是诱发条件

回答要留出篇幅，套话才有地方长出来。30 到 90 字的题诱发不了：模型把事实说完就没位置写开场白、免责声明或者结尾升华。已观察到的那条失败回答有 247 字。

新题给 600 到 1000 字，题面材料只有 320 到 530 字。模型必须把材料撑开将近一倍，这段差额就是套话的生长空间。

判分时不要把凑字数当成达标：为了够 600 字把同一件事说三遍是 S4。反过来，事实写全了没到 600 字，如实记下来，不自动算失败。

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

v0.3 tasks use [rubric v0.3](../../docs/rubric-v0.3.md) and [the v0.3 judge](../../graders/strict-editor-v0.3.md); v0.2 tasks use [rubric v0.2](../../docs/rubric.md) and [the judge](../../graders/strict-editor-v0.3.md). Always read the task's own `rubric.md` alongside the shared one. Scoring rules are in [the protocol](../../docs/pilot-protocol.md).
