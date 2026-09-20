# What makes a task usable

正常的 prompt，然后生成了 ai slop。而不是在 task prompt 里面就包含 slop 或者说到 slop。那是 hint。

## 2026-09-20

五个 task 里有四个犯了这条，删掉了：

- `devlog-plain-language`：prompt 里写了「遇到绕不开的专业词就在原地用大白话解释一句」，直接教了写法。
- `ci-rule-announcement`：要宣布一条禁止 slop 句式的检查规则，prompt 只能把那些句式列出来。
- `translation-fix-note`：讲的就是把别扭的翻译腔改顺。
- `media-caption-cut`：讲的就是删掉一句没用的话，prompt 还给了删的理由。

留下 `essay-correction-note`。它是一篇长文修订后要写的说明，讲的是引用、物理和结论，跟文风无关。

同一天另外删掉了三个更早写的题：`library-evening-return`、`repair-diary`、`waitlist-cancellation`。它们的 prompt 本身没有 hint，但都是凭假设出题，没有真实出处，也没有模型跑过。

说清读者是谁没问题，教怎么写就不行。

## tasks/ 里的十道旧题

同样的毛病：题面直接给出要避开的写法。有的列出禁用词（「好的」「当然」「尽快」「由于」），有的给一份带套话的草稿让模型改，有的干脆把「不是……而是……」印在题面上要求照写。模型不必自己判断，照着删或照着抄就行。

改法是把这些限制从题面移进检查器。检查器该查的照查，模型不再被告知。八道题按这个改了，`scripts/selfcheck.py` 的 183 个样例仍然全过，说明检查器本来就不读题面，之前那些话只是在泄题。

两道没改：`contrast-correction` 和 `status-update-multi-step` 第三轮要求必须写出「不是……而是……」。那是有意的指令遵循检验，看模型会不会反射式回避而不读题。它们保留原样，但 `task.toml` 里写明不是套话诱发题。
