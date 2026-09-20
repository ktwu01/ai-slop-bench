# Hackathon recap: evaluator notes

- Task ID: `hackathon-recap`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` post `2025-10-10-alphaearthhack-zh.md`: the hackathon's scope and the team's choice of a problem small enough to ship and big enough to matter. Failing fragments are **authored**.

## Target

Primary: **S6 fake-profound ending**. A weekend-project retrospective invites a closing reflection on what the team learned, what a deadline teaches, or what collaboration means. The material is a project plus three technical limits.

Secondary: **fidelity**. The three limits (hardcoded paths, single region, precomputed demo) are the part a recap wants to omit or soften. The prompt states them without hedging, and says they do not affect its standing as a hackathon project.

## Required facts

- A UT Austin geosciences hackathon bringing together Jackson School and university-wide students and researchers to build something concrete on real geoscience problems over a weekend.
- The team chose a problem small enough to deliver within the deadline and big enough to be worth doing: how far AI could be pushed on Earth-system data.
- There is a live demo; the code is open source.
- Hardcoded paths in the data-processing step mean a different dataset will not run.
- The model was only tried on the one region the team chose.
- The live demo serves precomputed results.
- These do not affect its standing as a hackathon project, but anyone building on it needs to know.

Do not invent a placement, judges' comments, team size, hours worked, or a plan to continue.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `48 小时教会我们的，比一个学期还多。` | S6 | A portable lesson closing an operational recap. |
| `代码还有待完善，但方向是对的。` | Fidelity | Softens three specific limits into a vague caveat and adds an endorsement. |
| `我们做的不只是一个项目，更是一次对协作极限的探索。` | S1; also S5 | A manufactured contrast inflating a weekend build. |
| `在线演示可以实时体验模型效果。` | Fidelity | Contradicts the supplied fact that the demo serves precomputed results. |
| `时间紧、任务重，很多东西是赶出来的，完成度上有取舍。` | S4 | Four phrasings of one supplied fact. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `数据处理那部分有硬编码路径，换一份数据就跑不通。` | Fidelity pass | A supplied limit with its concrete consequence. |
| `模型只在我们挑的那个区域上试过。` | Fidelity pass | Scope stated exactly. |
| `这些不影响它作为黑客松项目的完成度，但接着做的人需要先知道。` | S3 pass | The supplied framing. It sets scope rather than defending against a criticism. |

## Task fitness and length

A retrospective for the team's shared document, 600 to 1000 characters. **An operational recap needs no closing reflection**, and adding one to reach 600 characters is S6.
