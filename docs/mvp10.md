# MVP：10 道 Harbor 任务

日期：2026-09-19　状态：v0.1.0，10 道任务已可运行，参照答案全部通过。

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
```

## 十道任务

每道任务对应提案里的一个题组。`role` 为 `target` 的题测「能不能遵守」，`role` 为 `control` 的题测「会不会改坏」，也就是把不该删的东西删掉。

| 任务目录 | 题组 | 角色 | 主要考点 |
|---|---|---|---|
| `contrast-release-note` | 对比套式 | target | 禁用「不是……而是……」，同时保住三项事实和 60 字上限 |
| `contrast-correction` | 对比套式 | control | 换掉句式但必须保留明确的日期纠正，不能把否定半句整句删掉 |
| `protected-quote` | 受保护内容 | target | 受保护引文本身含禁式，须逐字保留且只出现一次，引文之外仍禁用 |
| `refund-no-new-promise` | 事实与承诺 | target | 删套话时不得新增时限、速度或结果承诺 |
| `handover-keep-list` | 未要求的格式 | control | 用户明确要求清单，输出必须保留清单结构 |
| `rollback-plain-paragraph` | 自造词和比喻 | target | 保留标准术语「回滚」，不用比喻，不补英文 |
| `incident-uncertain-cause` | 原因和不确定性 | target | 不把同时发生写成因果，同时保住时间、指标和发布事实 |
| `query-result-no-fluff` | 开场和结尾套话 | target | 直接给结果，30 字内装下两项数据 |
| `mentor-email-keep-thanks` | 读者与语域 | control | 保留一句必要致谢，同时不替导师做承诺 |
| `status-update-multi-step` | 多轮修订 | target | 第二轮新增事实后，第一轮的禁用要求仍然有效，旧事实不能丢 |

提案里的「组合与迁移」题组暂未单独成题。它要求的两条风格约束加完整性，已经分散在上面多道题里（例如禁式加字数、去套话加保真）；等扩到 50 题时再补独立题组。

## 难度从哪里来

单靠一条禁式规则很容易通过，把句式换掉就行。这十道题的难度来自互相拉扯的要求：

- **禁式加保真**：为了避开禁式最省事的改法是删掉半句，而被删的那半句往往正是必须保留的信息（`contrast-correction`）。
- **字数上限**：上限刚好够装下必需事实，装不下任何客套话或比喻（`query-result-no-fluff` 30 字，`rollback-plain-paragraph` 45 字）。
- **豁免边界**：受保护引文里就有被禁的句式，模型必须逐字抄一次、且只抄一次，自己加引号不产生豁免（`protected-quote`）。
- **反向陷阱**：`control` 题里该留的清单、该留的致谢，如果按「去 AI 味」的惯性删掉，就直接失败。
- **约束延续**：多轮任务第二轮只说「此前要求继续有效」，不重述具体禁式（`status-update-multi-step`）。

## 检查器的范围

`shared/tests/slopcheck.py` 只判题目明确声明过的东西。它不判断一段话「像不像 AI」，也不会因为出现某个句式就认定文字有问题；只有题目禁用了那个句式，命中才算失败。

规则版本 `v0.1.0`。每条失败都返回规则 ID、原文字符位置和命中片段。

两个视图：

- **原文视图**：NFC 归一化、换行统一。用于格式检查（Markdown、段落、行结构）和受保护引文的逐字比对。
- **检测视图**：在原文视图基础上去掉零宽字符和所有横向空白。用于禁用句式和事实匹配，所以「不 是……而是」和插入零宽字符的写法都躲不过规则。

检测视图的每个位置都能映射回原文位置，失败信息里给的是原文坐标。分句边界取 `。！？；!?;…` 和换行，不含半角句点，这样 `0.3%` 不会被误当成两个分句而让跨句的违规漏过去。

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

只有题目实际启用了某个类别，才会输出那个键。没有启用就不输出，避免白送一分。多轮任务用 `multi_step_reward_strategy = "final"`，最后一轮计主成绩，第一轮用于诊断。

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
dev/fixtures.py   反例：必须失败的答案，以及该由哪条规则判失败
scripts/
  sync_shared.py  把 shared/ 同步进每道任务；--check 用于 CI
  selfcheck.py    不用 Docker 给参照答案和反例评分
dataset.toml      Harbor 数据集清单
```

Harbor 任务应当自包含，所以每道任务都带一份检查器副本，而不是从仓库根目录 import。`shared/` 是唯一的写入源，`scripts/sync_shared.py --check` 负责发现副本漂移。

## 已知局限

- 只有确定性检查。提案要求的人工保真核对和成对盲评还没做，所以现在通过一道题只说明它满足了声明过的规则。
- 事实匹配靠列举可接受的说法。写法在列表之外但意思正确的答案会被误判，这是已知的假阴性来源；扩题时要靠人工核对把列表补齐。
- 反例由出题人手写，不是模型产出，覆盖的是设计时预期的失败方式。
- 10 道题适合诊断，不足以支撑模型排名。
