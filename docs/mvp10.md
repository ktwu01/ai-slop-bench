# MVP：10 道 Harbor 任务

日期：2026-09-19　状态：规则 v0.2.0，10 道任务已可运行，参照答案和 126 条对照样例全部按预期评分。

这是[提案](proposal.md)里 50 题计划的第一步：先把十个题组各做一道，验证任务格式、检查器和评分协议能跑通，再扩题。任务用 [Harbor](https://github.com/harbor-framework/harbor) 格式编写，可以直接交给 Harbor 支持的任何 agent 运行。

## 怎么跑

```bash
uv tool install harbor            # 或 pip install harbor

# 用参照答案自检，不需要 Docker
python3 scripts/selfcheck.py

# 用 oracle agent 跑一遍，确认十道题都可解（需要 Docker）
harbor run -p ./tasks -a oracle

# 用真实 agent 跑（需要对应厂商的 API key）
ANTHROPIC_API_KEY=... harbor run -p ./tasks -a claude-code -m anthropic/claude-opus-5

harbor view ./jobs                # 看每条规则的判定和证据

# 不经 Docker，直接用 codex CLI 当解题者量难度，每道题抽样 10 次
python3 dev/run_agent_codex.py --repeat 10
```

`selfcheck.py` 和 `harbor run -a oracle` 只能证明题目可解：oracle 是把仓库里的参照答案重放一遍，它必然通过，通过了也不说明题目有难度。难度只能由真实 agent 的通过率回答，这是 `dev/run_agent_codex.py` 存在的理由。

## 十道任务

每道任务对应提案里的一个题组。

| 任务目录 | 字数上限 | 主要考点 |
|---|---|---|
| `contrast-release-note` | 38 | 禁用「不是……而是……」，保住五项事实；草稿末句的导出功能下线属于别人的通知，必须丢掉 |
| `contrast-correction` | 48 | 只有日期写错了，会议室和设备检查都没变；改日期时不能顺手把它们也说成有变动 |
| `protected-quote` | 48 | 同一则通知的第一句必须逐字抄一次，紧邻的第二句必须转述、不得照抄 |
| `refund-no-new-promise` | 38 | 删套话时不得新增时限；草稿末句另一笔已退款订单不属于这条回复 |
| `handover-keep-list` | 无 | 用户明确要求清单，输出必须保留清单结构 |
| `rollback-plain-paragraph` | 30 | 保留术语「回滚」，不用比喻，不补英文；草稿末句的缓存清空属于运维手册 |
| `incident-uncertain-cause` | 74 | 不把同时发生写成因果；12% 是昨天的、3% 是前天的，两个读数不能串 |
| `query-result-no-fluff` | 32 | 直接给结果；9 月 12 日属于在用记录，8 月 30 日属于已删除记录、同事没问 |
| `mentor-email-keep-thanks` | 40 | 保留一句点名「摘要」的致谢，不替导师做承诺；引言那次已当面谢过，不再提 |
| `status-update-multi-step` | 42 / 60 / 60 | 三轮：新增事实后旧约束仍有效，最后一轮只改一个数字，相邻数字不许跟着动 |

题组与角色（`target` 测「能不能遵守」，`control` 测「会不会改坏」）：

| 任务目录 | 题组 | 角色 |
|---|---|---|
| `contrast-release-note` | 对比套式 | target |
| `contrast-correction` | 对比套式 | control |
| `protected-quote` | 受保护内容 | target |
| `refund-no-new-promise` | 事实与承诺 | target |
| `handover-keep-list` | 未要求的格式 | control |
| `rollback-plain-paragraph` | 自造词和比喻 | target |
| `incident-uncertain-cause` | 原因和不确定性 | target |
| `query-result-no-fluff` | 开场和结尾套话 | target |
| `mentor-email-keep-thanks` | 读者与语域 | control |
| `status-update-multi-step` | 多轮修订 | target |

提案里的「组合与迁移」题组暂未单独成题。它要求的两条风格约束加完整性，已经分散在上面多道题里（例如禁式加字数、去套话加保真）；等扩到 50 题时再补独立题组。

## 难度从哪里来

单靠一条禁式规则很容易通过，把句式换掉就行。这十道题的难度来自互相拉扯的要求：

- **禁式加保真**：为了避开禁式最省事的改法是删掉半句，而被删的那半句往往正是必须保留的信息。
- **字数上限**：上限刚好够装下必需事实，装不下客套话或比喻（`rollback-plain-paragraph` 30 字，`query-result-no-fluff` 32 字）。上限只是过滤器，不是主要难度来源：靠削字数把题目做难，量到的其实是数数能力。
- **豁免边界**：受保护引文里就有被禁的句式，模型必须逐字抄一次、且只抄一次，自己加引号不产生豁免（`protected-quote`）。同一则通知的第二句反过来只能转述，照抄即失败，于是相邻两句要求相反的处理。
- **反向陷阱**：`control` 题里该留的清单、该留的致谢，如果按「去 AI 味」的惯性删掉，就直接失败。
- **约束延续**：多轮任务第二轮只说「此前要求继续有效」，不重述具体禁式（`status-update-multi-step`）。
- **局部更新**：改一件事、同时原样保住紧挨着它的另几件事。`contrast-correction` 只有日期错了，房间号没错；`status-update-multi-step` 第三轮只改一个百分比，前后两个数字都不能动。这一类要求既不能靠整体重写蒙混，也不能靠原样照抄通过。
- **必须丢弃的材料**：有四道题在草稿或材料末尾放了一条属于别人的信息（导出功能下线、另一笔已退款订单、引言那次的当面致谢、缓存清空）。题面其他每一条要求都在奖励「保留原文内容」，只有这一条要求删，所以尽职尽责地全文转述反而失败。

## 检查器的范围

`shared/tests/slopcheck.py` 只判题目明确声明过的东西。它不判断一段话「像不像 AI」，也不会因为出现某个句式就认定文字有问题；只有题目禁用了那个句式，命中才算失败。

规则版本 `v0.2.0`。每条失败都返回规则 ID、原文字符位置和命中片段。

三个视图：

- **原文视图**（`raw`）：NFC 归一化、换行统一。用于受保护引文的逐字比对。
- **格式视图**（`fmt`）：原文视图去掉不可见的格式字符（Cf 类和软连字符一类），空白保留。用于 Markdown 和段落结构检查，所以在 `**` 中间插一个零宽字符不能把加粗藏过去。
- **检测视图**（`detect`）：再去掉所有空白和控制字符，逐字符做 NFKC 折叠（只在折叠结果仍是一个字符时折），并转小写。用于禁用句式和事实匹配，所以「不 是……而是」「ｒｏｌｌｂａｃｋ」「RoLlBaCk」都躲不过规则。

三个视图之间有双向偏移映射，失败信息里给的是原文坐标。

检测视图的 NFKC 折叠有一个后果值得单独写出来：全角标点会被折成半角，`；` 变成 `;`、`，` 变成 `,`、`：` 变成 `:`，而 `。`、`、`、`…` 原样保留。题目 spec 里的正则不会跟着折叠，所以手写一个 `[^。；，]` 字符类，实际上拦不住已经变成 `;` 和 `,` 的那些边界，「同一分句内」的绑定会悄悄跨句匹配成功。`slopcheck` 因此导出两个字符类，spec 一律用它们，不要自己拼：

- `NOT_CLAUSE`：分句内。边界是 `。；;！!？?` 和换行，不含半角句点，这样 `0.3%` 不会被当成两个分句。
- `NOT_SEGMENT`：更小的短语内。在分句边界上再加 `，,、：:…`。「9 月 12 日属于在用记录」这类绑定必须用它，否则一个逗号就能把日期挂到别的名词上。

字数统一定义为「去掉所有空白后的字符数」，题面里也是这么说的。

## 评分

`tests/grade.py` 写 `/logs/verifier/reward.json`，按类别给分：

| 键 | 含义 |
|---|---|
| `validity` | 交付文件存在、非空、没有复述题目要求 |
| `hard_rules` | 所有确定性风格规则通过 |
| `fidelity` | 必须保留的信息、受保护引文、必需语义标记都在 |
| `format` | 格式和字数要求通过 |
| `reward` | 以上全部通过才为 1.0 |
| `verifier_ok` | 检查器本身跑完了，没有崩溃。它为 0 表示这一条结果不可用，而不是 agent 答错 |

只有题目实际启用了某个类别，才会输出那个键。没有启用就不输出，避免白送一分。多轮任务用 `multi_step_reward_strategy = "final"`，最后一轮计主成绩，前两轮用于诊断。

这些分项不加权合成单一「人话总分」。风格规则通过率不能替代任务通过率。

## 仓库结构

```
shared/           检查器与环境的唯一来源
  environment/Dockerfile
  tests/          slopcheck.py, grade.py, test_output.py, test.sh
tasks/<name>/     10 道任务，每道自带一份 shared 的副本
  instruction.md  给 agent 看的题面
  task.toml       Harbor 任务配置与题组元数据
  tests/spec.py   本题启用哪些检查（唯一的题目专属检查代码）
  solution/       参照答案
dev/fixtures.py   对照样例：FAILING 是必须失败的答案加上该由哪条规则判失败，
                  PASSING 是必须得 1.0 的自然写法
dev/run_agent_codex.py  用 codex CLI 当解题者量通过率，--repeat N 做多次抽样
scripts/
  sync_shared.py  把 shared/ 同步进每道任务；--check 用于 CI
  selfcheck.py    不用 Docker 给参照答案和反例评分
dataset.toml      Harbor 数据集清单
```

Harbor 任务应当自包含，所以每道任务都带一份检查器副本，而不是从仓库根目录 import。`shared/` 是唯一的写入源，`scripts/sync_shared.py --check` 负责发现副本漂移。

## 已知局限

- 只有确定性检查。提案要求的人工保真核对和成对盲评还没做，所以现在通过一道题只说明它满足了声明过的规则。
- 事实匹配靠列举可接受的说法和正则。写法在列表之外但意思正确的答案会被误判，这是已知的假阴性来源。`dev/fixtures.py` 里的 `PASSING` 就是为此存在的：只看反例，一个过严的检查器会一直显示全绿，因为它照样能判掉每一条反例，只是顺带把题目变得无解。
- 事实匹配是「出现过没有」，它认不出否定和关系。所以需要断言的事实另外挂 `no_negated_facts` 锚点，需要绑定的事实写成 `re:` 正则，把一件事的两半锁在同一个分句或短语里。
- 反例由出题人手写，不是模型产出，覆盖的是设计时预期的失败方式。
- 10 道题适合诊断，不足以支撑模型排名。单次全绿也不能说明题目已经饱和：一个真实通过率 90% 的模型，连过 10 次独立抽样的概率约 35%。引用通过率要用 `--repeat`，评估某一条设计改动是否有效则需要更多次抽样。
