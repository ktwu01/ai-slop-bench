# Archived difficulty candidates

Historical exploration of explicit-constraint tasks. These candidates are separate from [the approved direct-answer example](../examples/tasks/support-ticket-intro/prompt.md) and [the three new natural-writing tasks](../examples/tasks/index.md). Follow those files' versioned rubrics for current work. The draft text below is retained for interpreting earlier local pilot artifacts.

These were proposals, not measured improvements. Freeze each prompt and its proposition rubric before running pilots. Do not infer that an unfamiliar paraphrase is wrong from a regex miss. Grade style scope separately from factual fidelity, and inspect every claimed model failure. The budgets below are ceilings with ample room, not targets.

Sources: `stop-slop/references/structures.md` (binary contrasts), especially its instruction to drop the negated half; `no-ai-slop/SKILL.md`, “Binary contrasts,” “Keep the user's meaning,” and preservation of real uncertainty; `haohao-shuohua/SKILL.md`, factual fidelity, predicate direction, modality, and local protected spans. These candidates test the conflict between mechanical contrast removal and meaning preservation. A historical independent Codex review (since removed), section 8, recommended matched policies, moving quote exceptions, and an additional turn after a policy reversal.

## Candidate A: one attribution contains two independently governed voices

Single turn. The protected quotation is deliberately surrounded by an attribution, a paraphrase of someone else's speech, and another quoted draft sentence. Quotation marks alone do not create an exception.

### Prompt

```text
把下面的记录整理成发给报名者的通知。事实都要保留，不要添承诺。先交代活动安排，再交代退款；不用标题、列表或结尾客套话，正文不超过300字。

记录：
场地方确认：“这不是延期，而是取消。”
主办方转述财务组的意思：不是退款取消，而是到账日期尚未确定。
编辑拟了一句说明：“这不是自动退款，而是要由报名者提交申请。”
已经申请的人不用再申请；尚未申请的人需要在10月20日前提交。全额退还报名费，不退报名者自行预订的车票费。取消活动由场地方决定，退款办法由主办方决定。

写法有一个例外：场地方说的那句原话必须完整引用一次，连句号也保留；其他地方都不用“不是……而是……”句式。这里按句号、问号、叹号、分号或换行划分，单个分句里先有“不是”、后有“而是”就算这个句式。转述和编辑拟稿都要改写，自己加上引号也不能变成例外。所有事实可换说法，只有场地方那句原话需要逐字保留。

把最终通知写入 /app/output.txt，只放通知正文。
```

### Reference answer

```text
场地方确认：“这不是延期，而是取消。”取消活动由场地方决定。主办方决定退款办法：退款照常办理，到账日期尚未确定。报名者需提交申请，已经申请的不用重复提交，尚未申请的请在10月20日前提交。报名费全额退还，自行预订的车票费不退。
```

### Frozen rubric and anticipated failure

- One protected literal quote; no contrast pattern outside its actual span. A duplicated or self-created quotation is not exempt.
- Cancellation, not postponement; venue owns cancellation, organizer owns refund policy.
- Refund still exists; arrival date unknown; application required; existing applicants exempt from reapplication; new applicants have the specified deadline.
- Registration fee fully refunded; independently booked train fare excluded.
- No new promise. No requirement to mirror reference sentence order beyond arrangements preceding refunds.

The trap is not simply copying one quote. Broad “preserve quotations” behavior protects the editor's unapproved sentence too; broad anti-contrast behavior deletes the refund-still-happening proposition. Similar actors and refund negations make these two mistakes plausible. Compared with the existing protected-quote task, the exception must follow provenance rather than typography.

Negative minimal pairs: replace “退款照常办理，到账日期尚未确定” with only “到账日期尚未确定” (missing continuation of refunds); change the applicant exemption into “报名者都需重新申请” (scope reversal); preserve the editor's contrast inside new quotes (exception leakage).

## Candidate B: meaningful negation with different quantifier and evidence scopes

Single turn. No exact answer string is required. This is a semantic-fidelity challenge; a blacklist cannot be its complete grader.

### Prompt

```text
给同事改写下面这段试验结论，去掉“不是……而是……”那种转折架子和凑气势的短句。可以合并句子，但每个判断的范围、确定程度和相互关系都得保留；不要替作者下更强或更弱的结论。允许保留有实际意思的否定词。正文不超过350字，不用标题、列表或总结口号。

草稿：
这次不是证明所有用户都会变快，而是只确认已登录用户的搜索中位耗时下降。不是所有未登录用户都没变快；其中有人变快了，但他们整体的中位耗时没有下降。
不是已经排除了缓存的影响，而是现有记录不足以判断缓存有没有影响。缓存开启的请求更快，这个观察本身不能证明开启缓存会让请求变快。
不是无需登录就能筛选，而是只有“按作者筛选”需要登录，搜索本身不用登录。不是用户都拒绝授权，而是我们还没询问是否授权。

正文中不出现“不是……而是……”：同一分句内先出现“不是”、后出现“而是”算违规，分句以句号、问号、叹号、分号或换行分开。不要把草稿包在引号里绕过要求。数字、术语和事实可按原意组织，不要求沿用原句。

把正文写入 /app/output.txt，只放正文。
```

### Reference answer

```text
试验只确认了已登录用户的搜索中位耗时下降，没有证明所有用户都会变快。部分未登录用户变快了，但未登录用户整体的中位耗时没有下降。现有记录不足以判断缓存是否有影响，缓存的影响仍未排除。缓存开启的请求更快，这一观察不能证明开启缓存会让请求变快。搜索无需登录，按作者筛选才需要登录。我们尚未询问用户是否授权，不能把这说成用户都拒绝了授权。
```

### Frozen rubric and anticipated failure

- Confirmed improvement is the logged-in cohort's **median search latency**, not every individual's speed and not all users.
- Some logged-out users improved; their cohort median did not decline. Both must survive.
- Cache influence is neither established nor ruled out; observed association does not establish an intervention effect. Do not accept “缓存没有影响” or “缓存会加速”.
- Login required for author filtering, unnecessary for search itself.
- Authorization has not been requested. Do not replace that process state with refusal, agreement, or uncertainty about an already-requested response.
- No contrast pattern; ordinary meaningful negations are permitted. Multiple paragraphs are allowed.

The draft contains negations of universal statements, negations of evidence, a genuine negative result, and a local access condition. A generic “state Y directly” rewrite loses distinct propositions. The rubric judges the preserved meaning, not a chosen set of Chinese synonyms. This candidate should expose overcorrection more directly than a smaller character budget.

Negative minimal pairs: “未登录用户都没变快”; “缓存没有影响”; “缓存已被证实能加速”; “用户还没同意授权”; “搜索需要登录”. Each changes a different declared proposition.

## Candidate C: move an exception, then revise a neighboring fact without restating policy

Four turns in one persistent agent session. Deliver and grade each turn; final success means all four turns pass. The first two turns establish an edited document, the third moves the quote exception, and the fourth tests whether that new scope persists. Do not show future turns up front.

### Turn 1

```text
整理成给参会者的通知。下面两句是内部草稿，暂时都不用原句，事实要保留：
甲：这不是延期，而是取消。
乙：这不是取消，而是改到线上。
甲说的是周三的设备演示，乙说的是周四的答疑。设备演示的费用全退；答疑原来的报名继续有效，不必重新报名。答疑时间为15:00，入口在报名邮件里。

正文不用“不是……而是……”句式，不用标题、列表或客套话，不超过250字。这里同一个分句内先出现“不是”、后出现“而是”就算这个句式，分句以句号、问号、叹号、分号或换行分开。保持两项活动各自的安排，不能混在一起。此后的修改沿用这些要求，除非我明确改动。把完整正文写入 /app/output.txt。
```

Reference:

```text
周三的设备演示取消，不再延期举行，费用全退。周四的答疑照常举行，改为线上，15:00开始，入口在报名邮件里。原报名继续有效，不必重新报名。
```

### Turn 2

```text
主办方要求引用甲的原话。请把甲那句完整引用一次，放在设备演示的说明中。这是句式禁令唯一的例外，其他文字仍照原来的要求。另补充：答疑结束后会发录像。更新完整正文。
```

Reference:

```text
周三的设备演示，主办方说明：“这不是延期，而是取消。”演示费用全退。周四的答疑照常举行，改为线上，15:00开始，入口在报名邮件里。原报名继续有效，不必重新报名，答疑结束后会发录像。
```

### Turn 3

```text
引用要求换一下：甲不再保留原话，改用乙的原话，并放在答疑的说明中。唯一的句式例外随这次替换转到乙，其他要求不变。两项活动的安排都没有变。更新完整正文。
```

Reference:

```text
周三的设备演示取消，不再延期举行，费用全退。周四的答疑，主办方说明：“这不是取消，而是改到线上。”答疑15:00开始，入口在报名邮件里。原报名继续有效，不必重新报名，答疑结束后会发录像。
```

### Turn 4

```text
再更正一处：邮件里写的答疑开始时间有误，正确时间为15:30。原来的15:00实际是入口开放时间，入口还是报名邮件里的那个。请让读者看清开放和开始是两件事，不要讲修改经过。更新完整正文。
```

Reference:

```text
周三的设备演示取消，不再延期举行，费用全退。周四的答疑，主办方说明：“这不是取消，而是改到线上。”入口15:00开放，仍在报名邮件里，答疑15:30开始。原报名继续有效，不必重新报名，答疑结束后会发录像。
```

### Frozen rubric and anticipated failure

All prior facts persist unless explicitly replaced. Turn 1 bans both contrasts; turn 2 protects only 甲; turns 3 and 4 protect only 乙. At each quoted turn the specified source string appears exactly once in the appropriate activity's explanation. Paraphrase elsewhere is unrestricted apart from the stated literal pattern ban. A quote does not substitute for missing activity identity.

Turn 4 must keep 15:00 as opening time, assign 15:30 to the start, retain the recording commitment from turn 2, and retain the moved quote policy from turn 3. It must not add “不是15:00，而是15:30,” revive甲's exception, remove the still-valid opening time, or make the canceled demonstration an online event. These are separate error categories, not one broad regex failure.

The final turn makes the tempting contrast useful for a real correction, but does not authorize a new exception. Unlike simply restating the reversal in the final prompt, it requires preserving a policy from a previous turn while applying a semantic update to a nearby number. Both numbers remain legitimate, so banning the old number would create an unfair verifier.

## Pilot and wording checks

Run each frozen candidate once before making edits based on failures. Keep failures that reflect the rubric; reject failures produced only by a restrictive grader. Record candidate selection as adaptive challenge mining, not as an unbiased pass-rate estimate. Use a fresh unseen draw for any headline rate.

Chinese wording was reread for factual relations, scope, and natural phrasing. Contrast forms in prompt material and protected quotations are intentional test data and are exempt from editorial removal. The reference answers retain meaning-bearing negation. All three designs use comfortable budgets and accept alternate phrasings outside explicit quotes.

Mechanical punctuation scan: 0 findings inside Chinese prompt and reference blocks. Four mixed-language documentation matches were reviewed; quotation punctuation was corrected, and the remaining two are English rubric sentences naming 甲 and 乙.
