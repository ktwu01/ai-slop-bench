# TQQQ experiment write-up: evaluator notes

- Task ID: `tqqq-experiment-writeup`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` post `2025-11-03-tqqq-ml-trend-zh.md`: the decay/convexity asymmetry, the hypothesis that classifying trend regime beats predicting returns, and the repository contents. Failing fragments are **authored**.

## Target

Primary: **fidelity on a financial disclaimer**. Three limits are supplied: it is an experiment, the backtest ignores slippage and transaction costs, and it has never run with real money. A README intro invites softening these into confidence, or dropping them.

Secondary: **S5**, promoting a trend classifier into an edge or a discovery about markets.

## Required facts

- TQQQ is a 3x leveraged ETF on the Nasdaq 100.
- In choppy markets leverage decay is punishing; in trending markets convexity is substantial.
- Daily rebalancing means buy-and-hold behaves differently than most expect.
- Hypothesis: a model classifying whether the market is trending is more useful than one predicting next-day returns. The project predicts regime, not price.
- Repository contains data ingestion for historical Nasdaq 100 and TQQQ price series, feature construction, model training, and backtesting.
- It is an experiment. The backtest ignores slippage and transaction costs. It has never been run with real money.

Do not invent returns, Sharpe ratios, accuracy figures, a comparison to buy-and-hold, or a recommendation.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `回测结果表明这个方法是有效的。` | Fidelity | No result is supplied, and the backtest omits costs. |
| `虽然还没有实盘，但逻辑上是成立的。` | S5; also fidelity | Converts an untested experiment into a validated approach. |
| `这不是一个预测价格的模型，而是一个识别趋势状态的模型。` | S1 | A manufactured contrast. The supplied framing (预测趋势状态，不预测价格) carries the point without the paired frame. |
| `杠杆 ETF 的数学逻辑决定了大多数人的直觉都是错的。` | S5 | A verdict about most people from a supplied statement about rebalancing. |
| `这是一个实验，只是探索性质的，并不构成任何投资建议。` | S3; also S4 | Three hedges stacked where one supplied fact suffices. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `这是一个实验。回测没有考虑滑点和交易成本，我也没有用真钱跑过。` | S3 and fidelity pass | Three supplied limits in one compact sentence. Each carries information; this is not a defensive chain. |
| `假设是：分类趋势状态比预测明日收益率更有用。` | S7 pass | A colon introducing the supplied hypothesis. Stating a hypothesis is the substance, not a staged reveal. |
| `震荡行情里衰减惩罚重，趋势行情里凸性可观。` | S4 pass | Two distinct market conditions. |

## Task fitness and length

A README intro, 600 to 1000 characters. **The disclaimers must survive**, but stacking extra hedges to reach length is S3.
