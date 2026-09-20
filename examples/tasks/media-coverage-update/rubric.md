# Media coverage update: evaluator notes

- Task ID: `media-coverage-update`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` commit `29d08cd`, "Complete Forbes and Synced research coverage", which added the two outlets and split coauthored-research coverage into its own paragraph. Failing fragments are **authored**.

## Target

Primary: **S5 inflated significance**. Announcing press coverage to collaborators is where a writer reaches for momentum, impact, or recognition. The supplied facts are two new outlets for one paper and one for another.

Secondary: **fidelity**. MicroVerse has no new coverage and must not be swept into the good news. The separation of "coverage of me" from "coverage of research I coauthored" is a supplied distinction.

## Required facts

- MatrAIx: population-scale simulated-user infrastructure, 8.3 billion persona agents. Prior coverage: NZZ am Sonntag, Numerama, WIRED Czech, plus Hugging Face Daily Papers. New: Forbes (US) and 机器之心 (Synced).
- ASI-Bench: 60 research-grade tasks across 11 scientific domains. New: 机器之心.
- MicroVerse: identity drift in long-horizon multi-agent simulations. **No new coverage.**
- Both new items were added to the homepage and media page.
- The homepage previously organized coverage around the writer being featured; these two are coverage of coauthored research, so they were put in a separate paragraph rather than merged into the existing one.

Do not invent readership numbers, citation counts, an editor's interest, follow-up coverage, or a claim about the papers' reception.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `Forbes 的报道标志着我们的工作进入了主流视野。` | S5 | One article becomes a milestone in visibility. |
| `三篇论文都获得了媒体关注。` | Fidelity | MicroVerse has none. |
| `这不只是几篇报道，更是对我们研究价值的认可。` | S1; also S5 | A manufactured contrast converting coverage into validation. |
| `媒体的关注还在持续扩大。` | Fidelity; also S5 | Asserts a trend from two additions. |
| `新增了 Forbes 和机器之心两家媒体的报道，这两家都报道了 MatrAIx，报道已经上线。` | S4 | Three clauses for one fact. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `MicroVerse 目前还没有新的报道。` | Fidelity pass | States the absence plainly, as supplied. |
| `之前主页是按我本人被报道来组织的，这两条属于合作研究被报道，所以单独分了一段。` | S5 pass | The supplied editorial reason, stated once. |
| `MatrAIx 新增 Forbes 和机器之心，ASI-Bench 新增机器之心。` | S4 pass | Two distinct facts about two papers. |

## Task fitness and length

A message to collaborators, 600 to 1000 characters. Naming each paper and its coverage is the substance.
