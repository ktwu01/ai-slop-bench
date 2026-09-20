# Poetry club handover: evaluator notes

- Task ID: `poetry-club-handover`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

The club and the 1,300+ figure come from `ktwu01.github.io` (`9a25f1b` syncs that number as the source of truth). The handover scenario is authored around it, as are the failing fragments.

## Target

Primary: **fidelity on deflating numbers**. The prompt supplies three facts that undercut a flattering reading: 1,300+ counts followers rather than active participants, actual attendance at each online reading is usually twenty or thirty, and post readership varies with no stable pattern. A handover note written by a founder leaving invites rounding these up.

Secondary: **S6**, closing a farewell document with a reflection on what the club meant.

## Required facts

- Grown from zero to 1,300+ members.
- Regular work: weekly submission calls plus layout and posting, a monthly online reading, running the public account.
- To hand over: public-account backend, submission mailbox, archived event documents, member roster.
- 1,300+ is the follower count, not active participants.
- Each online reading usually draws twenty or thirty people.
- Post readership varies widely with no stable pattern.
- No budget; events have always been run at zero cost; not affiliated with any organization.
- After leaving, the writer stops day-to-day involvement; credentials and archives transfer in full, and the successor decides format and direction.

Do not invent growth targets, a successor's name, advice about what to keep, a promise to stay available, or a claim about the club's impact.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `诗社现在有 1,300 多位活跃成员。` | Fidelity | Converts followers into active members, the exact distinction the prompt draws. |
| `每次读诗会都有不少人参加。` | Fidelity | Replaces a supplied number (twenty or thirty) with a vague favorable phrase. |
| `愿这份热爱继续传递下去。` | S6 | A closing sentiment in place of the handover content. |
| `从零到 1,300 人，这四年教会我的比我付出的更多。` | S6; also S5 | A personal moral appended to an operational document. |
| `推送的阅读量有高有低，起伏比较大，没有固定规律。` | S4 | Three phrasings of one supplied fact. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `1,300 多是公众号关注人数，线上读诗会通常到场二三十人。` | Fidelity pass | Both supplied numbers with their correct scopes. The prompt no longer says 不是活跃参与人数, so an answer that makes the follower/participant distinction explicit has inferred it from the two numbers. |
| `诗社没有经费，活动一直零成本办，也没有挂靠任何机构。` | S3 pass | Three distinct operational facts a successor needs. Not a defensive chain: each carries information, none preempts a worry. |
| `我离开后不再参与日常运营，怎么改版、怎么调整活动形式，都由你们定。` | S6 pass | A clean statement of the handover boundary. Ending without a reflection is correct here. |

## Task fitness and length

A handover document for a successor, 600 to 1000 characters. Practical completeness is the goal; an operational document needs no closing sentiment, and adding one to fill length is S6.
