# Quick facts collapse note: evaluator notes

- Task ID: `quickfacts-collapse-note`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` commit `427588a`, "Keep selected quick facts visible and collapse the rest", which keeps five items visible and moves three into a `<details>` block. Failing fragments are **authored**.

## Target

Primary: **S5 inflated significance**, with an unusual secondary hazard. The retained items are themselves written as reversals: ranked last then scholarship finalist, rejected then invited back to lecture. The prompt says this phrasing was a deliberate personal choice.

That creates the trap: a model describing these items may **amplify the reversals into an inspirational arc** about perseverance, or it may over-correct and apologize for them. Both fail. The task is to explain a layout change.

Secondary: **S4**, restating the one supplied reason (too many items, readers lose the thread).

## Required facts

- Kept visible: founded USTC Xingyun Poetry Club, grown from zero to 1,300+ members; Guo Moruo Scholarship finalist after entering ranked last in the college; returned to Tsinghua to lecture 40+ teachers as the only undergraduate among 40+ scholars, three years after being rejected there; Git contributor; a hamster named ASI.
- Collapsed: founded earth-space-ai.org; First Honor Graduate at Shenzhen X-Institute; published an SCI paper shortly after graduation.
- Reason: the list kept growing, and listing everything at once made it hard for readers to see what matters.
- Collapsed items are not deleted and remain viewable when expanded.
- The contrastive phrasing of some retained items was the writer's own choice, not a template.

Do not invent analytics, a reader complaint, a redesign, or a plan to remove the collapsed items.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `从垫底到决赛，从被拒到站上讲台，这些经历本身就是最好的自我介绍。` | S5; also S6 | Converts two supplied items into an inspirational arc with a closing flourish. |
| `保留的都是最能代表我的，折叠的相对次要。` | Fidelity | Asserts a judgment about relative importance the source does not supply. The reason given is readability, not ranking. |
| `这种对比写法可能显得刻意，但它们都是真实经历。` | S3 | Defends against a criticism nobody made. The prompt states the choice plainly; it does not ask for justification. |
| `条目越来越多，信息过载，读者很难快速抓住重点，页面也显得冗长。` | S4 | Four phrasings of one supplied reason. |
| `折叠不是隐藏，而是让重点更清楚。` | S1 | A manufactured contrast. The supplied facts (not deleted, still viewable) carry the point directly. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `折叠的那几条没有删，点开还能看到。` | S3 pass | A required factual boundary preventing a misreading. |
| `这一块条目越来越多，一口气全列出来，读者反而抓不住重点。` | S4 and S5 pass | The supplied reason, stated once. |
| `郭沫若奖学金决赛入围，而我高考入学时在学院排名垫底。` | S5 pass | A retained item quoted as it stands. **Reproducing a supplied contrastive item is not S1**: the contrast is in the source, not manufactured by the writer. |

## Task fitness and length

A site update note, 600 to 1000 characters. Listing which items moved and why is the substance.
