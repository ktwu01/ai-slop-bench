#!/usr/bin/env python3
"""Pilot frozen draft prompts. Outputs require independent semantic review.

This is adaptive task development, not a benchmark score. References never go
into solver prompts. Run after reading dev/difficulty_candidates.md.
"""
import hashlib
import json
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from run_agent_codex import run_codex, session_metadata

ROOT = Path(__file__).resolve().parent.parent
source = ROOT / 'dev/difficulty_candidates.md'
text = source.read_text()
out = ROOT / 'dev/agent_runs' / ('candidates-' + datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S'))
out.mkdir(parents=True)
summary = {'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
           'model': 'gpt-6-astra', 'reasoning_effort': 'low',
           'measurement': 'adaptive pilot; semantic review required', 'turns': []}
for candidate, body in re.findall(r'## Candidate ([ABC]):(.*?)(?=\n## Candidate|\n## Pilot)', text, re.S):
    blocks = re.findall(r'```text\n(.*?)\n```', body, re.S)
    prompts = blocks[::2]
    assert len(prompts) == (4 if candidate == 'C' else 1)
    with tempfile.TemporaryDirectory(prefix=f'slop-candidate-{candidate}-') as tmp:
        session = None
        for i, prompt in enumerate(prompts, 1):
            key = f'{candidate}-{i}'
            prompt = prompt.replace('/app/output.txt', 'output.txt')
            prompt += '\n只凭本次对话作答，不读取工作目录以外的文件。'
            (out / f'{key}.prompt.txt').write_text(prompt)
            session, raw = run_codex(Path(tmp), prompt, session, 'gpt-6-astra', 'low')
            (out / f'{key}.codex.jsonl').write_text(raw)
            answer_path = Path(tmp) / 'output.txt'
            answer = answer_path.read_text() if answer_path.exists() else None
            if answer is not None:
                (out / f'{key}.output.txt').write_text(answer)
            summary['turns'].append({'unit': key, 'session': session,
                                     'output': answer, 'model_evidence': session_metadata(session)})
            (out / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))
            print(key, repr(answer), flush=True)
print(out)
