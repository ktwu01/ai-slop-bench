# Benchmark Radar day log: evaluator notes

- Task ID: `benchmark-radar-day-log`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` post `2026-08-21-benchmark-radar-day26-zh.md`, describing PR #302: the leaderboard reorder, the history-navigation fix with its eight-versus-six split, and the decision to draw a stepwise best-score line rather than invent a cost axis. Failing fragments are **authored**.

## Target

Primary: **S5 inflated significance**. A daily dev log covering three UI fixes invites promoting them into a philosophy of honest visualization or user respect. The material already contains the reasoning, stated plainly: there is no cost in the data, so inventing an axis would be lying.

Secondary: **S4**, since three changes described at length is the shape that invites restating each one in general terms after describing it concretely.

## Required facts

- The leaderboard previously sat sixth on the page, behind method notes, an evidence bar, a findings panel, a search box, and a 480px-tall chart. Now it leads: five summary rows, then the full 80-row table.
- Filtering, expand-all, and default-collapsed are retained; old links still work.
- Address changes previously overwrote history rather than adding to it, so search, open an item, then back would leave the site. Now eight navigation kinds add history (switching views, clicking an item); six still overwrite (typing in a filter). A listener re-renders, so back and forward both behave.
- Someone wanted a cost-versus-accuracy frontier, but no score in the data has a cost, and inventing an axis for it would be lying.
- Replaced with a stepwise best-score line: flat segments and vertical jumps, jumping only when a later model actually breaks the record, with no diagonals implying intermediate values.
- For scraped third-party scores the line is omitted, because those rows lack a comparable metric.

Do not invent load times, user feedback, a bug count, or a next-day plan beyond what is supplied.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `我们宁愿少画一条线，也不愿意撒一个谎。` | S6; also S1 | A portable principle with a manufactured contrast. The supplied reasoning is specific: there is no cost in the data. |
| `这次改动让用户体验有了质的提升。` | S5 | 质的提升 from three UI fixes, with nothing supplied to support it. |
| `排名从第六位提到了第一位，用户现在一眼就能看到最重要的信息。` | Fidelity; also S5 | 最重要的信息 is an assertion the source does not make. |
| `图表不是用来好看的，而是用来说真话的。` | S1; also S6 | A manufactured contrast delivering an aphorism. |
| `返回导航修好了，现在按返回不会离开网站，历史记录正常了，前进后退都对。` | S4 | Four clauses for one fixed behavior. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `这份数据里任何分数都没有成本，为它编一个轴就是撒谎。` | S5 and S6 pass | The supplied reasoning. Blunt, specific, and tied to this dataset rather than to visualization in general. |
| `八类导航会新增历史，六类仍然覆盖。` | S4 pass | The supplied split, stated once with both numbers. |
| `跳只发生在后面的模型真的破了纪录时，不画斜线暗示中间有值。` | S3 pass | A design constraint with its reason. The negation carries real information. |

## Task fitness and length

A daily dev log entry for followers of the project, 600 to 1000 characters.
