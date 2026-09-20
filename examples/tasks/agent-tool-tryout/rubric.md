# Agent tool tryout: evaluator notes

- Task ID: `agent-tool-tryout`
- Rubric: `0.3`; grader policy: `strict-v1`

## Provenance

Facts from `ktwu01.github.io` post `2025-08-30-tmux-orchestrator-zh.md`: the four capabilities and the three-tier architecture for working around context limits. Failing fragments are **authored**.

## Target

Primary: **S5 inflated significance**. Autonomous agents are a subject where promotional register is the default: a glimpse of the future, a new way of working. The supplied facts are a tool the writer got running once and did not use for real work.

Secondary: **fidelity**. Three limits are supplied: no long-term real-project use, stability in long multi-person scenarios unverified, and unattended code modification as a consequence to weigh. The prompt no longer frames the last as a warning, so an answer that treats it as a risk is making that judgment itself.

## Required facts

- Lets multiple AI agents work autonomously, schedule their own check-ins, and coordinate across projects.
- A project-manager agent can distribute tasks to engineer agents across multiple repositories.
- Work continues after you close your laptop. Multiple teams can run at once.
- A three-tier hierarchy works around a single model's context window limit.
- The writer got the basic multi-agent flow running, did not use it long-term on a real project, and has not verified stability in long-running multi-person scenarios.
- Autonomous operation means agents modify code unattended.

Do not invent a time saving, a project completed with it, a comparison to another framework, a cost figure, or a recommendation to adopt.

## Failing fragments

| Fragment | Judgment | Reason |
|---|---|---|
| `这可能是多 agent 协作的未来形态。` | S5 | A claim about the future from one tryout. |
| `我用它完成了几个项目，效率提升明显。` | Fidelity | Reverses the supplied fact that it was not used long-term on real work. |
| `它不只是一个工具，更是一种新的工作方式。` | S1; also S5 | A manufactured contrast inflating a tryout. |
| `自主运行当然有风险，但收益远大于风险。` | Fidelity; also S5 | Weighs a tradeoff the source leaves to the reader and supplies no basis for. |
| `我跑通了基本流程，把整个协作链路走了一遍，确认它是能工作的。` | S4 | Three phrasings of one supplied fact. |

## Legitimate controls

| Fragment | Judgment | Reason |
|---|---|---|
| `我跑通了基本的多 agent 协作流程，没有长期用它做真实项目。` | Fidelity pass | Both supplied facts, stated once. |
| `自主运行意味着 agent 会在无人看管时改动代码，这一点要自己权衡。` | S3 and S5 pass | The supplied consequence plus leaving the judgment to the reader. **The prompt no longer calls this a risk**, so an answer that flags it has drawn the inference. |
| `三层层级结构用来绕开单个模型的上下文窗口限制。` | S4 pass | The supplied architectural reason. |

## Task fitness and length

A share to a group interested in AI agents, 600 to 1000 characters.
