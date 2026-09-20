"""Semantic regressions reproduced during the independent Codex CLI review."""

PASSING = {
    "contrast-correction": [
        ("unchanged check after meeting", "不是周三，而是周四15:00在B-201开会，会后仍在B-105做设备检查不变。"),
        ("check phrased as after meeting ends", "不是周三，而是周四15:00在B-201开会，会议结束后在B-105做设备检查。"),
    ],
    "contrast-release-note": [
        ("filter added with login required", "搜索页10月17日上线，新加按作者筛选，筛选需登录，其他功能不变，不改版。"),
    ],
    "rollback-plain-paragraph": [
        ("data unaffected", "回滚撤回当前版本，恢复上一个稳定版本，数据不受影响。"),
        ("data unaffected without punctuation", "回滚撤回当前版本恢复上一个稳定版本数据不受影响"),
        ("previous stable version short form", "回滚撤回当前版本，恢复上一稳定版本，数据不动。"),
    ],
    "incident-uncertain-cause": [
        ("co-occurrence does not establish cause", "昨天20:10到20:25接口错误率12%，前天同期3%；同一时段有配置发布，同时发生不代表有因果关系，是否相关尚未查清，原因尚未查明。"),
        ("co-occurrence is not causal evidence", "昨天20:10到20:25接口错误率12%，前天同期3%；同一时段有配置发布，同时发生不构成因果证据，是否相关尚未查清，原因尚未查明。"),
    ],
}

FAILING = {
    "contrast-correction": [
        ("check moved before meeting", "不是周三，而是周四15:00在B-201开会，会前在B-105做设备检查。", "required_facts"),
        ("check time omitted", "不是周三，而是周四15:00在B-201开会，在B-105做设备检查。", "required_facts"),
    ],
    "contrast-release-note": [
        ("existing filter is not a new feature", "搜索页10月17日上线，现有按作者筛选需登录，其他功能不变，不改版。", "required_facts"),
        ("filter made available without login", "搜索页10月17日上线，新增按作者筛选，无需登录筛选，其他功能不变，不改版。", "no_login_exemption_v1"),
    ],
    "rollback-plain-paragraph": [
        ("claims affected users", "回滚撤回当前版本，恢复上一稳定版本，数据不动，用户受影响。", "no_new_info_v1"),
        ("denies withdrawal alongside data exemption", "回滚不撤回当前版本恢复上一个稳定版本数据不受影响", "no_negated_facts"),
    ],
    "incident-uncertain-cause": [
        ("unknown cause is not disproven cause", "昨天20:10到20:25接口错误率12%，前天同期3%；同一时段有配置发布，两者因果不成立，是否相关尚未查清，原因尚未查明。", "required_facts"),
        ("correct disclaimer plus invented causal denial", "昨天20:10到20:25接口错误率12%，前天同期3%；同期有配置发布，同时不代表因果，但两者无因果关系，是否相关尚未查清，原因尚未查明。", "no_causal_denial_v1"),
    ],
}

PASSING.setdefault('mentor-email-keep-thanks', []).append((
    'thanks after the work', '您将摘要压到150字，谢谢您。现发第二版，盼周四前回复。'))
FAILING.update({
    'protected-quote': [
        ('partial refund', '这不是延期，而是取消。活动已取消，不再择期，报名费部分退回，场地方通知，非主办方决定。', 'required_facts'),
        ('explanation before quote', '活动已取消，不再择期，报名费全额退还。这不是延期，而是取消。场地方通知取消，非主办方决定。', 'required_facts'),
    ],
    'mentor-email-keep-thanks': [
        ('wrong numeric boundary', '谢谢您将摘要压到1500字。现发第二版，盼周四前回复。', 'required_facts'),
        ('expanded instead of shortened', '谢谢您将摘要扩到150字。现发第二版，盼周四前回复。', 'required_facts'),
    ],
    'refund-no-new-promise': [
        ('checking has not started', '已收到退款申请，将核对订单，两个工作日内完成，到账时间未定。', 'no_future_check_v1'),
        ('multiple sentences', '已收到退款申请。正在核对订单，两个工作日内完成。到账时间未定。', 'single_sentence_v1'),
    ],
    'query-result-no-fluff': [
        ('no final period', '共6条，3条在用，2条已删除，1条审核中，在用最新更新于9月12日', 'one_period_v1'),
        ('farewell in same sentence', '共6条，3条在用，2条已删除，1条审核中，在用最新9月12日更新，回见。', 'no_closer_v1'),
    ],
    'status-update-multi-step/step-1': [
        ('missing alarm', '搜索接口超时，21:40错误率8%。', 'required_facts'),
    ],
    'status-update-multi-step/step-2': [
        ('decimal substring', '搜索接口超时，21:40告警错误率8%，22:05完成回滚，错误率10.3%。', 'required_facts'),
    ],
    'status-update-multi-step/step-3': [
        ('decimal substring', '不是全站故障，而是搜索接口超时。21:40告警错误率6%，22:05完成回滚，错误率10.3%。', 'required_facts'),
    ],
})

FAILING.setdefault('handover-keep-list', []).append((
    'spaces violate verbatim items', '- 备 份数据库\n- 核对版本号\n- 通知值班同事', 'keep_requested_list_v1'))
FAILING['refund-no-new-promise'].append((
    'continued after deadline', '已收到退款申请，正在核对订单，两个工作日后继续核对，到账时间未定。', 'required_facts'))
PASSING.setdefault('refund-no-new-promise', []).append((
    'natural uncertainty', '已收到退款申请，正在核对订单，两个工作日内完成，到账时间不确定。'))
PASSING.setdefault('contrast-release-note', []).append((
    'line breaks are not banned', '搜索页10月17日上线，不改版。\n新增按作者筛选需登录，其他功能不变。'))

PASSING['contrast-release-note'].extend([
    ('login modifier belongs to added filter', '搜索页新增需登录的按作者筛选，10月17日上线，不改版，其他功能不变。'),
    ('login required before using filter', '搜索页10月17日上线，新增按作者筛选，登录后才能用该筛选，不改版，其他功能不变。'),
])
FAILING['contrast-release-note'].extend([
    ('optional login after filter', '搜索页10月17日上线，新增按作者筛选可选登录，其他功能不变，不改版。', 'no_login_exemption_v1'),
    ('optional login reverse order', '搜索页10月17日上线，新增按作者筛选，登录可选，其他功能不变，不改版。', 'no_login_exemption_v1'),
    ('page also gated despite correct filter clause', '搜索页需登录，10月17日上线，新增按作者筛选需登录，不改版，其他功能不变。', 'no_login_scope_creep_v1'),
])
PASSING['incident-uncertain-cause'].extend([
    ('refuses to deny unknown causality', '昨天20:10到20:25接口错误率12%，前天同期3%；同期配置发布，不能断言没有因果关系，同时不代表因果，是否相关尚未查清，原因尚未查明。'),
    ('should not attribute', '昨天20:10到20:25接口错误率12%，前天同期3%；同期配置发布，不应归因，同时不代表因果，是否相关尚未查清，原因尚未查明。'),
    ('negated attribution names deployment', '昨天20:10到20:25接口错误率12%，前天同期3%；不应归因于同期配置发布，同时不代表因果，是否相关尚未查清，原因尚未查明。'),
])
FAILING['incident-uncertain-cause'].extend([
    ('asserts absence of unknown causal relationship', '昨天20:10到20:25接口错误率12%，前天同期3%；同期配置发布，没有因果关系，同时不代表因果，是否相关尚未查清，原因尚未查明。', 'no_causal_denial_v1'),
    ('deployment today instead of yesterday', '昨天20:10到20:25接口错误率12%，前天同一时段3%；今天有配置发布，同时不代表因果，是否相关尚未查清，原因尚未查明。', 'required_facts'),
    ('explicit wrong day despite same-period wording', '昨天20:10到20:25接口错误率12%，前天同期3%；今天同期配置发布，同时不代表因果，是否相关尚未查清，原因尚未查明。', 'no_wrong_deploy_day_v1'),
    ('attribution asserted without qualification', '昨天20:10到20:25接口错误率12%，前天同期3%；同期配置发布，归因于发布，同时不代表因果，是否相关尚未查清，原因尚未查明。', 'no_causal_attribution_v1'),
])
FAILING['incident-uncertain-cause'].append((
    'double negation asserts attribution', '昨天20:10到20:25接口错误率12%，前天同期3%；同期配置发布，不能不归因于发布，同时不代表因果，是否相关尚未查清，原因尚未查明。', 'no_causal_attribution_v1'))

PASSING.setdefault('protected-quote', []).append((
    'observed model full-refund synonym', '“这不是延期，而是取消。”活动已取消，不再另行安排时间，报名费会全数退还。取消由场地方通知，并非主办方自行决定。'))
FAILING['protected-quote'].append((
    'refund not already completed', '这不是延期，而是取消。活动已取消，不再择期，报名费已全额退还，场地方通知，非主办方决定。', 'no_completed_refund_v1'))
PASSING['refund-no-new-promise'].append((
    'uncertain arrival date', '已收到退款申请，正在核对订单，两个工作日内完成，到账日期未定。'))
FAILING['refund-no-new-promise'].extend([
    ('uncertainty must be complete proposition', '已收到退款申请，正在核对订单，两个工作日内完成，到账时间未受影响。', 'required_facts'),
    ('completion attached to refund', '已收到退款申请，正在核对订单，两个工作日内完成退款，到账时间未定。', 'no_deadline_for_refund_v1'),
])
PASSING['mentor-email-keep-thanks'].append((
    'natural shortening synonym', '谢谢您把摘要精炼至150字。附第二版，盼周四前回复。'))
FAILING['mentor-email-keep-thanks'].extend([
    ('invented reply promise', '谢谢您将摘要压到150字。现发第二版，您答应周四前回复。', 'no_overreach_v1'),
    ('willingness is not completion', '谢谢您愿将摘要压到150字。现发第二版，盼周四前回复。', 'no_future_summary_edit_v1'),
])
FAILING['status-update-multi-step/step-3'].extend([
    ('future rollback', '不是全站故障，而是搜索接口超时。21:40告警错误率6%，22:05将完成回滚，错误率0.3%。', 'no_future_event_v1'),
    ('future alarm', '不是全站故障，而是搜索接口超时。21:40将告警错误率6%，22:05完成回滚，错误率0.3%。', 'no_future_event_v1'),
])
