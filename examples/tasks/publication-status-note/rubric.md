# Publication status note: evaluator notes

- Task ID: `publication-status-note`
- Rubric: `0.3`; grader policy: `strict-v1`
- Solver input: [prompt.md](prompt.md) only, plus the shared instruction and, in arm B, the v0.3 style paragraph

## Provenance

Facts from `ktwu01.github.io` commit `c8926d9`, "Update portfolio: add Benchmark Radar, fix stale facts, dedupe meteor entry". The venue line changed from `Submitted to JGR: Space Physics` to `Published in JGR: Space Physics (2024)`, and a duplicate meteor entry was merged. Failing fragments below are **authored**, not observed.

## Target

Primary: **S5 inflated significance**, driven by the length gap. The actual change is one phrase and one merged duplicate. The prompt asks for 600 to 1000 characters. A writer with 400 characters of material and 1000 characters to fill reaches for significance: a lesson about data hygiene, a claim that the portfolio is now trustworthy, a process improvement nobody instituted.

Secondary: **S2 metadiscourse** and **S4 redundant elaboration**, the other two ways to fill space without adding information.

## Required facts

- Paper: Diurnal and Seasonal Variations of Meteor Velocity Observed at Middle Latitude by the Mengcheng Meteor Radar, Wu et al.
- The page said `Submitted to JGR: Space Physics`; the paper was in fact published there in 2024.
- The oral presentation at the 20th National Symposium on Solar-Terrestrial Space Physics is correct and unchanged.
- A duplicate meteor-radar entry was merged into one.
- Other entries were checked; no further stale information was found.

Do not invent a reader who noticed, a review process, a recurring audit, a count of how long the page was wrong, or a claim that all pages are now current.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `这件事提醒我们，学术履历的每一个字都值得被认真对待。` | S5 | A portable maxim. One stale venue line establishes nothing about 每一个字. |
| `我已经建立了定期核查机制，确保类似问题不再发生。` | Fidelity | No mechanism is supplied. The source describes one pass over one page. |
| `虽然只是一处措辞，但它关系到整个作品集的可信度。` | S5 | Inflates a status field into page-wide credibility. |
| `需要特别说明的是，口头报告那一条是准确的。` | S2 | The preface announces emphasis; deleting it leaves the fact intact. |
| `这一条信息已经过期了，页面上写的状态和实际情况不一致，没有及时更新。` | S4 | Three clauses for one proposition. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `页面上写的是投稿中，实际这篇 2024 年就已经在 JGR: Space Physics 发表了。` | S5 pass | The supplied correction, stated once. |
| `其他条目我对照检查过，没发现别的过期信息。` | S5 and fidelity pass | Exactly what the source supports, including its limited scope. |

## Task fitness and length

A spoken update for a lab meeting, 600 to 1000 characters. **The length is the trap, so do not relax it**, but do not treat padding as compliance either: an answer that reaches 600 by repeating the correction in three forms fails S4. An answer that covers every required fact concisely and stops short of 600 is a legitimate outcome worth recording, not an automatic failure. Record the length and the counting convention.
