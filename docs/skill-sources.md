# 写作 skills 的远端来源

核验日期：2026-09-18。

提案参考的四个本地 skill 都能找到远端内容。其中三个有与本地文件完全一致的公开上游版本；`shuorenhua` 目前只核验到私有镜像，尚未确认公开上游。

核验从本地安装目录的实际位置、Git 来源和作者署名开始，再下载远端文件，比较原始字节及 SHA-256。目录名相同不足以确认来源。固定提交对应的是已验证的内容版本，不代表确定了当初的安装时间或安装方式。

## 公开上游

| Skill | 上游仓库 | 与本地一致的固定文件 | 核验范围 |
|---|---|---|---|
| `haohao-shuohua` | [Job-Yang/jobbyang-ai-skills](https://github.com/Job-Yang/jobbyang-ai-skills) | [SKILL.md @ dd94fe96](https://github.com/Job-Yang/jobbyang-ai-skills/blob/dd94fe96780332a981da1b692c2a0af7fd463ea4/skills/haohao-shuohua/SKILL.md) | 主文件完全一致，35,877 字节 |
| `stop-slop` | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | [SKILL.md @ 8da1f030](https://github.com/hardikpandya/stop-slop/blob/8da1f030185bdfe8471220585162991eaeb970e9/SKILL.md) | 本地目录内全部 7 个文件一致，包括三个 references 文件 |
| `no-ai-slop` | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | [SKILL.md @ b53e2659](https://github.com/petergyang/no-ai-slop/blob/b53e2659b986093f7c681d8b4e998715e90da2a2/skills/no-ai-slop/SKILL.md) | 本地主文件与同目录 `eval.md` 均完全一致 |

`stop-slop` 的本地署名与 [Hardik Pandya 的发布说明](https://hvpandya.com/stop-slop)一致，发布说明直接链接上述仓库。`no-ai-slop` 的仓库也由 [Peter Yang 的发布说明](https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns)直接链接。

`no-ai-slop` 的本地版本对应较早提交。核验时，上游 `main` 为 `000650b156983f5159695b441477f4e63b25dc85`，已调整一个工作流步骤和一项自检要求。因此复现提案所读版本时，应使用表中的 `b53e2659`，不能直接下载最新 `main`。

`stop-slop` 和 `no-ai-slop` 的固定版本均有 MIT 许可，分别见 [Hardik Pandya 的 LICENSE](https://github.com/hardikpandya/stop-slop/blob/8da1f030185bdfe8471220585162991eaeb970e9/LICENSE) 和 [Peter Yang 的 LICENSE](https://github.com/petergyang/no-ai-slop/blob/b53e2659b986093f7c681d8b4e998715e90da2a2/LICENSE)。本仓库当前只记录来源，没有复制这些 skill 包。

## 尚未确认公开上游的 skill

`shuorenhua` 的本地文件署名为 [wzenus](https://x.com/wzenus)。已验证的远端副本是 [ktwu01/codex-settings 中的 SKILL.md](https://github.com/ktwu01/codex-settings/blob/f31ae30c5154f79eb3f62ba9aacdbe1452d5104d/skills/shuorenhua/SKILL.md)，与本地文件完全一致，4,174 字节。

该镜像仓库为私有，需要访问权限。当前没有核验到原作者公开发布这份 skill 的 GitHub 仓库，不能用其他同名项目代替其来源。它可以继续提供出题线索；若作为公开可复现的实验配置使用，还需提供获得授权的公开版本，或明确记录访问限制。

## 内容指纹

以下为实际读取的主文件 SHA-256，与上面的固定远端文件逐项一致：

```text
haohao-shuohua  919d95dc532e8fb63a52ce9a20f044d5bc3a22ace5de207fc2062950b895f772
shuorenhua     0012b8ecf22e33671d0176a0d689343f4c3d2a6f958efee957338a712c6e39a4
stop-slop      7432a1d9ebdd42b27666da8458af252edf549f723fb14bcd4791425103930310
no-ai-slop     16719efd6dc6fe5978be7f6db41a474ca246970e5014acc057e29d7bfbd63b0e
```

正式评测时还需保存实际加载的完整文件清单及哈希，特别是按需读取的 references。主文件匹配不能代替完整实验配置，也不表示已经运行了 benchmark。
