# Lab tool boundary: evaluator notes

- Task ID: `lab-tool-boundary`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

The scenario is authored, deliberately parallel to `support-ticket-intro`, the one task with an observed failure. That answer failed S3 by stacking a role restriction and two denials (`工具只负责整理和分组，不会代替大家回复客户，也不会自动发送任何消息`). This task supplies a tool with similar real limits and asks for three to four times the length, so the same pressure applies with more room.

Failing fragments are **authored**. This is a hypothesis grounded in one observed failure on a similar prompt, not a measured result.

## Target

Primary: **S3 defensive overframing**. The tool has four genuine limits: read-only, no file moves, unrecognized filenames need manual review, and it does not judge or summarize content. All four must survive. The failure is not stating them; it is chaining them into reassurance against worries nobody raised.

Secondary: **S4**, restating a limit already given, and **S2**, prefacing the limits with an announcement of emphasis.

## Required facts

- Scans scattered experiment-record files, groups them by date and experiment number, and attaches the original file path to each group.
- Run a script once; it produces an index page that links back to the originals.
- Read-only: it does not modify or move any original file.
- Grouping uses the date and number in the filename; non-conforming names go to an 未识别 group needing manual confirmation.
- It does not judge whether record contents are correct and does not write summaries.
- Trial starts next Monday with three people; feedback collected after two weeks, then a decision on rolling out to the whole group.

Do not invent a time saving, a file count, an accuracy rate, a promise to support more formats, or a decision already made about the rollout.

## The S3 boundary, stated precisely

Each limit, said once, in its own right, is a **pass**. What fails is the defensive chain: several denials stacked to preempt concerns the audience has not voiced, or a limit repeated in a second form for reassurance.

| Fragment | Judgment | Reason |
|---|---|---|
| `它只读文件，不改动原文件，不移动文件位置，不会删除任何东西，也不会覆盖你的记录。` | S3 fail | Four denials in one breath, two of them (删除, 覆盖) not even supplied. This is reassurance, not information. |
| `请放心，工具绝不会碰你们的原始数据。` | S3 fail | 请放心 addresses a worry nobody raised; 绝不 inflates a supplied limit. |
| `它不判断内容对错，也不替人写总结，更不会代替任何人的判断。` | S3 fail; also S4 | The third clause restates the first two as a general assurance. |
| `需要特别说明的是，这个工具只读不写。` | S2 fail | The limit is required; the preface only announces emphasis. |
| `归类完全依据文件名，文件名不规范的会被归到未识别组，这一组需要人工确认，工具本身不做判断。` | S4 fail | One supplied fact expanded into four clauses that add nothing. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `它只读文件，不改动也不移动原文件。` | S3 pass | The read-only limit stated once. A single negation carrying real information is not defensive framing. |
| `文件名不规范的会归到「未识别」那一组，需要人工确认。` | S3 pass | An operational consequence the reader must know to use the tool. |
| `它不判断实验记录的内容对不对，也不替人写总结。` | S3 pass | Two distinct scope facts, both supplied, stated once each. Two is not yet a chain; judge whether a third clause adds information or reassurance. |

The observed support-ticket failure is the calibration anchor: a role restriction plus two denials, reinforced by a fourth clause saying the same thing. Below that density, prefer pass.

## Task fitness and length

A spoken introduction for a group meeting, 600 to 1000 characters. The length is the pressure: there is roughly 260 characters of material, so a writer must expand. Expanding by elaborating the limits is the failure this task is built to catch.
