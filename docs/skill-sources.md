# 写作 skills 的远端来源

核验日期：2026-09-18。

提案参考的 `haohao-shuohua`、`stop-slop` 和 `no-ai-slop` 已确认公开上游；`shuorenhua` 目前仅确认私有镜像，尚未确认公开上游。

以下固定提交用于复现提案引用的版本，主文件 SHA-256 见本文的内容指纹。

## 公开上游

| Skill | 上游仓库 | 固定版本文件 | 核验文件 |
|---|---|---|---|
| `haohao-shuohua` | [Job-Yang/jobbyang-ai-skills](https://github.com/Job-Yang/jobbyang-ai-skills) | [SKILL.md @ dd94fe96](https://github.com/Job-Yang/jobbyang-ai-skills/blob/dd94fe96780332a981da1b692c2a0af7fd463ea4/skills/haohao-shuohua/SKILL.md) | `SKILL.md`，35,877 字节 |
| `stop-slop` | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | [SKILL.md @ 8da1f030](https://github.com/hardikpandya/stop-slop/blob/8da1f030185bdfe8471220585162991eaeb970e9/SKILL.md) | `SKILL.md` 及三个 references 文件 |
| `no-ai-slop` | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | [SKILL.md @ b53e2659](https://github.com/petergyang/no-ai-slop/blob/b53e2659b986093f7c681d8b4e998715e90da2a2/skills/no-ai-slop/SKILL.md) | `SKILL.md` 及同目录的 `eval.md` |

`stop-slop` 的仓库由 [Hardik Pandya 的发布说明](https://hvpandya.com/stop-slop)直接链接。`no-ai-slop` 的仓库也由 [Peter Yang 的发布说明](https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns)直接链接。

`no-ai-slop` 引用的版本为 `b53e2659`。核验时，上游 `main` 为 `000650b156983f5159695b441477f4e63b25dc85`，已调整一个工作流步骤和一项自检要求。复现时应使用表中的固定提交。

`stop-slop` 和 `no-ai-slop` 的固定版本均有 MIT 许可，分别见 [Hardik Pandya 的 LICENSE](https://github.com/hardikpandya/stop-slop/blob/8da1f030185bdfe8471220585162991eaeb970e9/LICENSE) 和 [Peter Yang 的 LICENSE](https://github.com/petergyang/no-ai-slop/blob/b53e2659b986093f7c681d8b4e998715e90da2a2/LICENSE)。本仓库当前只记录来源，没有复制这些 skill 包。

## 尚未确认公开上游的 skill

`shuorenhua` 的已核验远端副本是 [ktwu01/codex-settings 中的 SKILL.md](https://github.com/ktwu01/codex-settings/blob/f31ae30c5154f79eb3f62ba9aacdbe1452d5104d/skills/shuorenhua/SKILL.md)，文件署名为 [wzenus](https://x.com/wzenus)，共 4,174 字节。

该镜像仓库为私有，需要访问权限。当前没有核验到原作者公开发布这份 skill 的 GitHub 仓库，不能用其他同名项目代替其来源。它可以继续提供出题线索；若作为公开可复现的实验配置使用，还需提供获得授权的公开版本，或明确记录访问限制。

## 内容指纹

以下为上述固定提交中 `SKILL.md` 的 SHA-256：

```text
haohao-shuohua  919d95dc532e8fb63a52ce9a20f044d5bc3a22ace5de207fc2062950b895f772
shuorenhua     0012b8ecf22e33671d0176a0d689343f4c3d2a6f958efee957338a712c6e39a4
stop-slop      7432a1d9ebdd42b27666da8458af252edf549f723fb14bcd4791425103930310
no-ai-slop     16719efd6dc6fe5978be7f6db41a474ca246970e5014acc057e29d7bfbd63b0e
```

正式评测时还需保存实际加载的完整文件清单及哈希，特别是按需读取的 references。主文件哈希不能代替完整实验配置；benchmark 尚未运行。
