# AI Slop Bench

**说人话 Bench：少点套话，保住原意。**

A proposed benchmark for Chinese LLM writing and rewriting, combining verifiable style constraints with meaning preservation and human evaluation.

目前处于提案阶段。首版计划编写 50 道任务，题集、评测程序和模型结果尚未发布。

## 测什么

用户明确要求不用某个句式，模型能否遵守？去掉套话之后，数字、条件、术语和承诺是否仍然准确？写出的内容是否适合给定的读者和场景？

首版拟从写作 skills 中提取可检验的要求，整理成 40 道主要测试题和 10 道边界对照。确定性检查负责明确的句式与格式要求，人工核对语义保真，并盲评自然度和直接采用偏好。

例如，题目要求通知同事搜索页周五上线、新增按作者筛选，并明确禁用“不是……而是……”：

> 搜索页周五上线，新增按作者筛选。

这份答案可以通过句式检查。如果省掉上线时间，或擅自补充其他功能，即使没有命中禁式，任务仍然失败。

## 提案与计划

- [完整提案](docs/proposal.md)：任务分配、例题、评分、对照与复现协议。
- [后续实验计划](https://github.com/ktwu01/ai-slop-bench/issues/1)：题集整理、改写基线和专用改写模型的训练条件。
- [研究背景](docs/proposal.md#研究背景)：测量目标、裁判可靠性和公开指标的局限。
- [出题参考](docs/proposal.md#参考来源提供候选规则)：写作 skills 中的候选规则与适用边界。

## 相关项目

[Language Defensive Bench](https://github.com/ktwu01/language-defensive-bench)研究多轮纠正后仍进入最终交付的无关历史，以及局部纠正被扩大成长期禁令的现象。[提案 issue](https://github.com/ktwu01/language-defensive-bench/issues/1)记录任务与评分设计。该仓库目前为私有，需要访问权限。

两个项目分别维护题集和成绩，可以参考彼此的规则检查、人工标注和反例设计。

## 提供案例

欢迎通过 [Issues](https://github.com/ktwu01/ai-slop-bench/issues)提供原始任务、模型回复、需要保留的信息和具体失败片段。也欢迎提供应当保留对比句、列表、术语或正式语气的对照案例。

模型输出需注明版本和提示条件。提交的文本请使用有权公开的材料，并移除个人信息。
