# Domain broker caution: evaluator notes

- Task ID: `domain-broker-caution`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` post `2026-08-25-three-single-letter-ai-domains-zh.md`: the asking prices, the seller-sourced comparables, the reported AI.com brokerage, and the dead and near-blank entries. Failing fragments are **authored**.

## Target

Primary: **fidelity on differing evidence quality**. The prompt distinguishes two kinds of information: comparable prices drawn from the seller's own marketing, and a brokerage figure from news reporting. An answer that treats both as equally solid, or drops the distinction, fails. The writer also has no trading experience, and that must survive.

Secondary: **S5**, turning a price lookup into a verdict on the domain market.

## Required facts

- The domain is listed with a broker at 2.5M asking, roughly 1.5M opening.
- The sales page says the letter evokes a well-known brand and lists comparable sale prices.
- Among single-letter .ai domains, several run real products, including c.ai as Character.AI.
- Several are empty: one with no DNS, no site and no findable owner; one near-blank, registered 2017, behind privacy protection.
- The comparables on the sales page come from the seller's own marketing.
- Another domain's broker reportedly brokered a 70M deal in February 2026; that comes from news reporting.
- The two kinds of information differ in reliability.
- The writer has never bought a domain, and all of this is public information found online.

Do not invent a valuation, a recommendation to buy or not buy, a market trend, tax or legal considerations, or an appraisal service.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `同类域名成交价在 500 到 800 万之间，250 万并不算贵。` | Fidelity | Treats seller-sourced comparables as market data and derives a valuation. |
| `单字母域名是 AI 时代最稀缺的资产。` | S5 | A market verdict from one lookup. |
| `买不买取决于你，但我建议你慎重。` | Fidelity | Offers a recommendation the writer is not positioned to give. |
| `真正值钱的不是字母本身，而是它背后的想象空间。` | S1; also S6 | A manufactured contrast delivering an aphorism. |
| `推销页上的价格来自卖家自己的营销材料，是卖家自己写的，参考价值有限。` | S4 | Three clauses for one supplied fact. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `推销页引的成交价来自卖家自己的营销，那位经纪人的 7000 万交易来自新闻报道，这两类信息可靠程度不一样。` | Fidelity pass | Preserves both sources and the supplied distinction between them. |
| `我自己没买过域名，上面都是网上查到的公开信息。` | Fidelity pass | The supplied standing, stated once. |
| `这批域名里有几个在跑真产品，也有几个是空的。` | S4 pass | Two distinct categories, each then given a concrete example. |

## Task fitness and length

A reply to a friend, 600 to 1000 characters. Reporting what was found is the task; **appraising the domain is not**, and doing so from a sales page is a fidelity failure.
