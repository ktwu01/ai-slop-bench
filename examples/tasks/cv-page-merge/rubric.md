# CV page merge: evaluator notes

- Task ID: `cv-page-merge`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` commit `9a25f1b`: merging duplicated Work Experience / Education / Skills sections, replacing a stale two-item publication list with the auto-rendered collection, and updating the reviewer record. Failing fragments are **authored**.

## Target

Primary: **fidelity on a self-implicating cause**. The prompt says the duplicate sections came from two successive redesigns, each adding one, and the writer never noticed. A changelog wants to attribute this to a template, a migration, or a tooling issue.

Secondary: **S5**, converting a page cleanup into a claim about rigor or maintainability.

## Required facts

- Work Experience, Education, and Skills each appeared twice; now merged into one each.
- A hand-written, stale two-item publication list was replaced by the auto-rendered full list, now including MicroVerse, MatrAIx, ASI-Bench, ESM-bench, ResearchClawBench and others.
- The reviewer record was updated, adding TNNLS, CSUR, TOSN, COLM-W and ACM AgentSkills invitations.
- The duplicates arose because two successive redesigns each added one, and the writer did not notice.
- The auto-rendered list reads the publications directory, so new papers appear without manual edits.

Do not invent a reader who noticed, a count of how long the duplicates persisted, a validation step, or a claim that the page is now error-free.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `模板迁移过程中产生了重复的小节。` | Fidelity | Blames tooling. The prompt says the writer added each one and did not notice. |
| `改成自动渲染之后，页面终于可以自己维护自己了。` | S5 | 终于 and 自己维护自己 inflate a directory-driven list. |
| `一个页面的整洁，反映的是一个人对细节的态度。` | S6; also S5 | A portable maxim closing a changelog. |
| `现在页面上的信息都是最新且准确的。` | Fidelity | Asserts completeness beyond the four supplied changes. |
| `重复的小节已经合并，现在每个小节只出现一次，不再重复。` | S4 | Three phrasings of one fact. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `重复是前后两次改版各加了一次，我一直没发现。` | Fidelity pass | The supplied cause, including the admission. |
| `自动渲染的列表读 publications 目录，以后新增论文会自动出现。` | S5 pass | The supplied mechanism and its consequence. |
| `审稿记录加上了 TNNLS、CSUR、TOSN、COLM-W 和 ACM AgentSkills 的邀请。` | S4 pass | Five distinct additions. |

## Task fitness and length

A blog changelog entry, 600 to 1000 characters.
