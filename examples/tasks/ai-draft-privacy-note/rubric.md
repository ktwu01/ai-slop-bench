# AI draft privacy note: evaluator notes

- Task ID: `ai-draft-privacy-note`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` post `2026-09-08-your-data-never-left-your-computer-zh.md`, which quotes Buckmaster's statement, his own disclaimer, OpenAI's response, its volunteered caveat, and Mark Chen's remark. Failing fragments are **authored**.

## Target

Primary: **fidelity on carefully worded statements**. Every quoted party was precise, and the precision is the content. Buckmaster asked and did not get an answer on training; he explicitly accuses nobody. OpenAI's denial is narrow (no specific user data accessed for this problem) and it volunteers that de-identified data cannot be ruled out. An answer that flattens any of this into "OpenAI denied it" or "they used his data" fails.

Secondary: **S5 and S7**, drawing a verdict about AI companies, or staging the episode as a revelation about privacy.

## Required facts

- 2026-09-07, Tristan Buckmaster's statement; work with an Anthropic researcher on finite-time blowup for fluid equations, on the path to the Navier-Stokes problem; drafts lived in Codex sessions throughout.
- He asked whether the model was trained on or accessed their sessions; was told the model did not look up user data; asked again about training and got no answer.
- His own disclaimer: he has not seen OpenAI's proof, does not know what their model did or how, does not know whether their data was used, and is not accusing anyone.
- OpenAI: researchers and agents saw none of their work by any means before public release; in particular no specific user data was accessed to solve this problem.
- OpenAI also: while unlikely, they cannot rule out that de-identified data from the pair's product usage helped improve their models.
- Mark Chen: the company uses user feedback and de-identified data to improve products, and by his account every large-model company does.
- On the public evidence there is no proof of wrongdoing regarding data.

Do not invent an investigation, a policy change, a resolution, other researchers' cases, or a recommendation the source does not make.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `OpenAI 否认了使用他的数据。` | Fidelity | Broadens a narrow denial. OpenAI denied accessing specific user data for this problem and explicitly could not rule out de-identified data. |
| `这件事说明，把数据交给云端 AI 就是在赌运气。` | S5 | A general verdict. The source states no wrongdoing was proven. |
| `他追问训练问题时的沉默，或许才是最响亮的回答。` | S7; also fidelity | Stages silence as a reveal and converts an absence of evidence into an implied answer. |
| `这不是一起数据泄露事件，而是一次信任的崩塌。` | S1; also S5 | A manufactured contrast delivering a verdict the material does not support. |
| `Buckmaster 没有指控任何人，他只是提出了问题，他也表示自己并不掌握证据。` | S4 | Three clauses for one supplied fact. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `他说他没看过对方的证明，也不知道自己的数据是否被使用过，没有在指控任何人。` | S3 and fidelity pass | Reports his supplied disclaimer. Several negations here carry real content; this is not a defensive chain. |
| `OpenAI 说为解决这个问题没有访问过任何特定的用户数据，同时说无法排除去标识化数据曾帮助改进模型。` | Fidelity pass | Preserves both the narrow denial and the volunteered caveat. |
| `就公开证据而言，数据这件事上没有不当行为的证明。` | S5 pass | The supplied conclusion, scoped to public evidence. |

## Task fitness and length

A spoken update for a group meeting, 600 to 1000 characters, aimed at letting listeners judge for themselves. **Presenting both sides precisely is the task**; refusing to state what each party said is not neutrality.
