# School tool launch: evaluator notes

- Task ID: `school-tool-launch`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` post `2025-07-08-school-evaluator-zh.md`: the three scoring dimensions, the ranking critique, and the within-school variance argument. Failing fragments are **authored**.

## Target

Primary: **S3 defensive overframing**. The tool has real limits: the user sets the weights, and the user supplies the data. The prompt now states both plainly **without** denials, so any chain of 不提供 / 不会给出 / 不联网 in an answer is the model's own addition, produced without being shown one.

Secondary: **S5**, converting a scoring widget into a critique of the ranking industry.

## Required facts

- Scores schools on: academic fit (does the program teach what you need), career outcomes (where graduates in your specific direction end up), cost versus aid (net cost after scholarships, not sticker price).
- Motivation: US News, QS, ARWU compress a school into a position on a list. Adequate as a first filter, but differences between students at one school are often larger than differences between schools.
- Web-based, open source, with a live demo.
- The user sets the weights. The user supplies the data.

Do not invent a user count, a school database, an accuracy claim, a recommendation engine, or a comparison against another tool.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `工具不提供推荐权重，不会替你做决定，也不会联网抓取任何数据，你的信息完全掌握在自己手里。` | S3 | Four denials plus a reassurance, none of them supplied in that form. The prompt states two facts positively; this is the model manufacturing a defensive chain. |
| `排名不是坏东西，而是被用错了地方。` | S1 | A manufactured contrast. The supplied point (fine as a first filter, fails as a decision tool) needs no frame. |
| `这个工具让每个人都能找到真正适合自己的学校。` | S5; also fidelity | 每个人 and 真正适合 exceed a weighting widget that holds no school data. |
| `请放心，所有数据都在你本地。` | S3 | 请放心 answers a worry nobody raised, and local storage is not a supplied fact. |
| `权重由你设定，怎么打分你说了算，工具只是帮你算个总分。` | S4 | Three phrasings of one supplied fact. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `打分的权重和数据都由你自己填。` | S3 pass | Both supplied limits, stated once, positively. |
| `同一所学校内不同学生之间的差异，往往比学校之间的差异更大。` | S5 pass | The supplied argument for why rankings fall short. |
| `学术契合度、职业出路、成本与助学金。` | S4 pass | Three distinct dimensions. |

## Task fitness and length

A message introducing the tool to a group, 600 to 1000 characters.
