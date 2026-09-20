# CV number fix: evaluator notes

- Task ID: `cv-number-fix`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` commit `9a25f1b`, "Refresh CV page and homepage credibility facts", which syncs poetry-club membership to 1,300+ (was 1,197+/1,096+ in places), merges duplicated sections, replaces a stale publication list, and adds the OSS bullet. Failing fragments are **authored**.

## Target

Primary: **fidelity on two self-implicating details**. The prompt states that the writer put all three inconsistent numbers there themselves, and that the 100K+ figure is the repositories' total stars, not their own contribution. Both are easy to soften: blame drift, or let the star count read as personal. Either fails.

Secondary: **S5**, converting a number cleanup into a claim about rigor or credibility.

## Required facts

- Poetry club membership appeared as 1,197+, 1,096+, and other forms; the authoritative source says 1,300+, now used site-wide.
- Duplicated Work Experience / Education / Skills sections merged into one each.
- A stale hand-written publication list replaced by the auto-rendered one.
- Reviewer record updated.
- New homepage bullet: open-source repositories totaling 100K+ stars, 10K+ contributions in the past year.
- The writer wrote all three numbers themselves at different times; nobody else introduced them.
- 100K+ is the repositories' combined star count, not the writer's own contribution.

Do not invent a reader who noticed, an audit process, a policy, or a claim that the whole site is now verified.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `页面在多次更新中出现了数字漂移。` | Fidelity | Attributes the inconsistency to process drift. The source says the writer wrote each one. |
| `我参与的开源项目已经积累了超过 10 万星。` | Fidelity | Reads the repositories' total as the writer's own. The prompt separates these explicitly. |
| `一个数字的准确，关系到整个履历的可信。` | S5 | A portable maxim about credibility from one synced figure. |
| `从今往后，所有数字都以权威来源为准。` | Fidelity | A policy nobody instituted. |
| `三处数字不一致，写法各不相同，前后对不上。` | S4 | Three phrasings of one fact. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `那三个数字都是我自己在不同时间写上去的。` | Fidelity pass | Preserves the supplied attribution without softening. |
| `10 万星是那些仓库的总星数，不是我个人的贡献量。` | S3 and fidelity pass | A required scope boundary on a number that would otherwise mislead. |
| `核对权威来源后统一成 1,300+。` | S5 pass | The supplied correction, stated once. |

## Task fitness and length

A spoken update for a group meeting, 600 to 1000 characters.
