# AI Slop Bench

**给模型普通写作任务，比较加与不加去套话提示时，它会怎么写。**

模型读题后直接回答。聊天界面、API 或 CLI 都能采样，无须 Harbor、Docker、写文件或调用工具。题目见[题目目录](examples/tasks/index.md)。当前有哪些题、跑没跑过，用 `python3 scripts/status.py` 查。

## 当前题集

| 题目 | 主要观察的表达 | 字数 |
|---|---|---|
| 客服工具介绍 | S2 元话语、S3 过度防御、S4 冗余（已观察到） | 约 180 字 |
| 长文修订说明 | S5：把承认自己出错写成一种姿态 | 约 200 字 |

题面只是普通写作请求，不提文风、不列禁用词、不给带套话的草稿。出题前提见[出题规则](docs/task-design-rules.md)。

回答要留出篇幅，套话才有地方长出来。30 到 90 字的题诱发不了：模型把事实说完就没位置了。已观察到的那条失败回答有 247 字。

## 比较与判分

A 组不额外添加去套话提示，B 组加固定提示。两组的题目、模型、设置和事实保留要求相同，每次从新会话开始。v0.3 的题共用 [v0.3 B 提示](examples/tasks/index.md)，v0.2 的题用自己的；不同版本的结果须分别标明，不能混算成一次干预。

所有题都采用 **strict-v1**：任意一项确认一处问题，整份回答即失败，`reward = 0`。原题查 S1–S4，新题查全 S1–S7，不能只查该题的主要目标。事实保真、任务完成和可用性也必须合格。不取平均、不给部分分，未裁定项不能算通过。

用户提供的原题 GPT 回答已标注为 S2、S3、S4 失败，无 S1 命中。“工具只负责整理和分组，不会代替大家回复客户，也不会自动发送任何消息”整体是一处 S3。完整证据见[样本标注](examples/observations/support-ticket-user-001.md)。这是一条开发观察，没有配对 B 回答，不能据此报告通过率或干预效果。

## 运行材料

- [题目目录与 A/B 指令](examples/tasks/index.md)、[rubric v0.3](docs/rubric-v0.3.md)、[v0.3 严格评审提示](graders/strict-editor-v0.3.md)。
- [试验流程](docs/pilot-protocol.md)、[出题前提](docs/task-design-rules.md)。
- 客服工具介绍题：[题面](examples/tasks/support-ticket-intro/prompt.md)、[rubric v0.2](docs/rubric.md)、[严格评审提示](graders/strict-editor-v0.3.md)。
- [评分校验脚本](scripts/score_review.py)：支持 v0.2 与 v0.3，校验评审 JSON 并汇总结果，不代替语义评审。
- [评测设计](docs/proposal.md)、[采样安排](docs/mvp10.md)。

采样前先冻结题面、提示、rubric、校准材料和评审指令。每题每组独立采五次，交错运行并保留全部首次输出。详见[试验流程](docs/pilot-protocol.md)。

平台系统提示不可见时，A 组只能标为“未额外添加去套话提示”。CLI 默认指令也可能包含风格要求，使用前须核对实际上下文。无额外提示不能证明模型没有接受过去套话训练。

## 旧任务与工具

`tasks/`、`shared/`、`dataset.toml` 和现有自检脚本保留此前的十道 Harbor 格式任务，主要用于明确约束下的指令遵循诊断。它们的旧结果不等于当前自然写作题的结果，也不是运行新评测的前提。

Skills 提供选题线索，实际难度由后续实验决定。题目、反例和严格规则本身不能证明通过率低，更不能保证 0% pass@1。
