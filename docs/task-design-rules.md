# What makes a task usable

正常的 prompt，然后生成了 ai slop。而不是在 task prompt 里面就包含 slop 或者说到 slop。那是 hint。

## 2026-09-20

五个 task 里有四个犯了这条，删掉了：

- `devlog-plain-language`：prompt 里写了「遇到绕不开的专业词就在原地用大白话解释一句」，直接教了写法。
- `ci-rule-announcement`：要宣布一条禁止 slop 句式的检查规则，prompt 只能把那些句式列出来。
- `translation-fix-note`：讲的就是把别扭的翻译腔改顺。
- `media-caption-cut`：讲的就是删掉一句没用的话，prompt 还给了删的理由。

留下 `essay-correction-note`。它是一篇长文修订后要写的说明，讲的是引用、物理和结论，跟文风无关。

说清读者是谁没问题，教怎么写就不行。
