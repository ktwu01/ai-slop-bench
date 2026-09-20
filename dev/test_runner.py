"""Reliability checks for the local Codex measurement runner (no API calls)."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import run_agent_codex as runner


EVENTS = '{"type":"thread.started","thread_id":"session"}\n{"type":"turn.completed"}\n'


class RunnerTests(unittest.TestCase):
    def test_completed_session(self):
        with patch.object(runner.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, EVENTS, '')) as run:
            self.assertEqual(runner.run_codex(Path('/tmp'), 'prompt', 'session', 'model', 'high'), ('session', EVENTS))
            command = run.call_args.args[0]
            self.assertIn('resume', command)
            self.assertIn('model', command)
            self.assertIn('model_reasoning_effort="high"', command)

    def test_failures_never_accepted_as_completed(self):
        cases = [(1, EVENTS), (0, EVENTS.splitlines()[0]),
                 (0, '{"type":"turn.completed"}'),
                 (0, EVENTS + '{"type":"turn.failed"}\n')]
        for code, stdout in cases:
            with self.subTest(code=code, stdout=stdout), patch.object(
                runner.subprocess, 'run', return_value=subprocess.CompletedProcess([], code, stdout, '')
            ), self.assertRaises(runner.TurnError):
                runner.run_codex(Path('/tmp'), 'prompt', None)

    def test_resume_rejects_different_session(self):
        with patch.object(runner.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, EVENTS, '')):
            with self.assertRaisesRegex(runner.TurnError, 'resume_session_mismatch'):
                runner.run_codex(Path('/tmp'), 'prompt', 'different')

    def test_timeout_preserves_partial_log(self):
        error = subprocess.TimeoutExpired('codex', 1, output=b'partial', stderr=b'error')
        with patch.object(runner.subprocess, 'run', side_effect=error):
            with self.assertRaises(runner.TurnError) as ctx:
                runner.run_codex(Path('/tmp'), 'prompt', None)
            self.assertEqual(ctx.exception.raw, 'partialerror')

    def test_timeout_does_not_grade_stale_output_or_restart_session(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            step_dirs = [root / 'tasks' / 'sample' / 'steps' / str(i) for i in range(3)]
            for step in step_dirs:
                (step / 'tests').mkdir(parents=True)
                (step / 'instruction.md').write_text('Update output.txt')
            unit_list = [(f'sample/{i}', step / 'tests', step / 'solution') for i, step in enumerate(step_dirs)]
            calls = []

            def codex(workdir, prompt, session, *args):
                calls.append(session)
                summaries = list((root / 'dev' / 'agent_runs').glob('*/summary.json'))
                previous = json.loads(summaries[0].read_text())
                self.assertEqual(len(previous['units']), len(calls) - 1)
                if session is None:
                    (workdir / 'output.txt').write_text('first turn answer')
                    return 'session', EVENTS
                self.assertEqual((workdir / 'output.txt').read_text(), 'first turn answer')
                raise runner.TurnError('timeout', 'partial log')

            with patch.object(runner, 'ROOT', root), patch.object(runner, 'units', return_value=unit_list), \
                 patch.object(runner.shutil, 'which', return_value='/bin/codex'), \
                 patch.object(runner.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, 'codex test', '')), \
                 patch.object(runner, 'run_codex', side_effect=codex), \
                 patch.object(runner, 'session_metadata', return_value={}), \
                 patch.object(runner, 'grade_file', return_value=(1.0, set(), 'pass', {'reward': 1.0, 'verifier_ok': 1.0})) as grade, \
                 patch('sys.argv', ['runner']):
                self.assertEqual(runner.main(), 0)
            self.assertEqual(calls, [None, 'session'])
            grade.assert_called_once()
            summary = json.loads(next((root / 'dev' / 'agent_runs').glob('*/summary.json')).read_text())
            self.assertEqual([r['status'] for r in summary['units']], ['graded', 'timeout', 'skipped'])
            self.assertEqual(summary['draws'], {'sample': [0.0]})
            self.assertEqual(summary['pass_rate'], {'sample': 0.0})

    def test_effective_model_evidence_is_session_scoped(self):
        with tempfile.TemporaryDirectory() as tmp:
            sessions = Path(tmp) / 'sessions'
            sessions.mkdir()
            (sessions / 'rollout-session.jsonl').write_text(
                json.dumps({'type': 'turn_context', 'payload': {
                    'model': 'effective-model', 'effort': 'high', 'unrelated_secret': 'never copy'}}) + '\n')
            with patch.dict(runner.os.environ, {'CODEX_HOME': tmp}):
                evidence = runner.session_metadata('session')
                self.assertTrue(evidence['effective_model_verified'])
                self.assertEqual(evidence['contexts'], [{'model': 'effective-model', 'effort': 'high'}])
                self.assertFalse(runner.session_metadata('missing')['effective_model_verified'])

    def test_grader_payload_and_exit_validation(self):
        cases = [({'reward': 0.0, 'verifier_ok': 0.0}, 1, False),
                 ({'reward': 0.0}, 1, False),
                 ({'reward': '0', 'verifier_ok': 1.0}, 1, False),
                 ({'reward': True, 'verifier_ok': 1.0}, 0, False),
                 ({'reward': 0.5, 'verifier_ok': 1.0}, 1, False),
                 ([], 0, False), ('invalid JSON', 1, False), (None, 1, False),
                 ({'reward': 1.0, 'verifier_ok': 1.0}, 1, False),
                 ({'reward': 0.0, 'verifier_ok': 1.0}, 0, False),
                 ({'reward': 0.0, 'verifier_ok': 1.0}, 2, False),
                 ({'reward': 0.0, 'verifier_ok': 1.0}, 1, True),
                 ({'reward': 1.0, 'verifier_ok': 1.0}, 0, True)]
        for payload, code, valid in cases:
            def verifier(*args, **kwargs):
                if payload is not None:
                    body = payload if isinstance(payload, str) else json.dumps(payload)
                    (Path(kwargs['env']['SLOPCHECK_REWARD_DIR']) / 'reward.json').write_text(body)
                return subprocess.CompletedProcess([], code, '  FAIL  rule: reason', 'evidence')
            with self.subTest(payload=payload, code=code), patch.object(runner.subprocess, 'run', side_effect=verifier):
                if valid:
                    self.assertEqual(runner.grade(Path('/tmp'), 'answer')[0], payload['reward'])
                else:
                    with self.assertRaisesRegex(ValueError, 'grader infrastructure error'):
                        runner.grade(Path('/tmp'), 'answer')

    def test_grader_crash_and_midrun_mutation_are_excluded(self):
        for scenario in ('grader_crash', 'task_mutation'):
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                task = root / 'tasks' / 'sample'
                (task / 'tests').mkdir(parents=True)
                (task / 'instruction.md').write_text('Write output')
                def codex(workdir, *args):
                    (workdir / 'output.txt').write_text('answer')
                    if scenario == 'task_mutation':
                        (task / 'instruction.md').write_text('Changed requirements')
                    return 'session', EVENTS
                with patch.object(runner, 'ROOT', root), \
                     patch.object(runner, 'units', return_value=[('sample', task / 'tests', task / 'solution')]), \
                     patch.object(runner.shutil, 'which', return_value='/bin/codex'), \
                     patch.object(runner.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, 'codex test', '')), \
                     patch.object(runner, 'run_codex', side_effect=codex), \
                     patch.object(runner, 'session_metadata', return_value={}), \
                     patch.object(runner, 'grade_file', side_effect=ValueError('grader infrastructure error')) as grade, \
                     patch('sys.argv', ['runner']):
                    self.assertEqual(runner.main(), 2)
                summary = json.loads(next((root / 'dev' / 'agent_runs').glob('*/summary.json')).read_text())
                self.assertEqual(summary['pass_rate'], {})
                self.assertEqual(summary['units'][0]['status'], 'infrastructure_error')
                if scenario == 'task_mutation':
                    grade.assert_not_called()
                    self.assertIn('task_content_changed', summary['units'][0]['error'])

    def test_timeout_with_explicit_service_error_is_infrastructure(self):
        error = subprocess.TimeoutExpired('codex', 1, output=b'{"type":"error","message":"service unavailable"}\n')
        with patch.object(runner.subprocess, 'run', side_effect=error):
            with self.assertRaisesRegex(runner.TurnError, 'failed_event_before_timeout'):
                runner.run_codex(Path('/tmp'), 'prompt', None)

    def test_artifact_reader_matches_harbor(self):
        tests = runner.ROOT / 'tasks' / 'protected-quote' / 'tests'
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'output.txt'
            target = Path(tmp) / 'target.txt'
            target.write_text('answer')
            path.symlink_to(target)
            reward, failed, _, scores = runner.grade_file(tests, path)
            self.assertEqual(reward, 0.0)
            self.assertIn('output_exists', failed)
            self.assertEqual(scores['verifier_ok'], 1.0)
            captured = Path(tmp) / 'capture.txt'
            self.assertEqual(runner.archive_delivery(path, captured)['kind'], 'symlink')
            self.assertFalse(captured.exists())
            path.unlink()
            path.write_bytes(b'x' * (64 * 1024 + 2))
            reward, failed, _, scores = runner.grade_file(tests, path)
            self.assertEqual(reward, 0.0)
            self.assertIn('output_exists', failed)
            self.assertEqual(scores['verifier_ok'], 1.0)
            capture = runner.archive_delivery(path, captured)
            self.assertEqual(capture['captured_bytes'], 64 * 1024 + 1)
            self.assertTrue(capture['truncated'])
            path.write_bytes(b'\xff\xfe')
            reward, failed, _, scores = runner.grade_file(tests, path)
            self.assertEqual(reward, 0.0)
            self.assertNotIn('output_exists', failed)
            self.assertEqual(scores['verifier_ok'], 1.0)
            runner.archive_delivery(path, captured)
            self.assertEqual(captured.read_bytes(), b'\xff\xfe')
            path.unlink()
            path.mkdir()
            self.assertIn('output_exists', runner.grade_file(tests, path)[1])

    def test_broken_spec_import_emits_verifier_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            tests = Path(tmp)
            (tests / 'grade.py').write_bytes((runner.ROOT / 'shared' / 'tests' / 'grade.py').read_bytes())
            (tests / 'spec.py').write_text('raise RuntimeError("broken spec import")')
            with self.assertRaisesRegex(ValueError, 'verifier_ok=0.0'):
                runner.grade_file(tests, tests / 'output.txt')

    def test_invalid_arguments(self):
        for args in [['--repeat', '0'], ['--repeat', '-1'], ['sample', 'unknown']]:
            with self.subTest(args=args), patch('sys.argv', ['runner'] + args), \
                 patch.object(runner, 'units', return_value=[('sample', Path('/tmp'), Path('/tmp'))]):
                with self.assertRaises(SystemExit) as ctx:
                    runner.main()
                self.assertEqual(ctx.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
