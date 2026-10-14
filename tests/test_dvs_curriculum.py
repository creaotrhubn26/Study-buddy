"""Offline checks of the DVS lesson, persona handoff and resolver context."""

from pathlib import Path
import os
import sys
import tempfile
import unittest
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from streamlit.testing.v1 import AppTest
from dvs_curriculum import (COURSE_CODE, ASSET_ROOT, TEMPLATE_ROOT, TASK_STEPS,
    get_dvs_course_lessons, get_dvs_task_guides, get_dvs_task_guide_markdown)
from evo_tasks import resolver_task_number_boost


class DvsWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.previous_directory = Path.cwd()
        self.scratch = tempfile.TemporaryDirectory()
        os.chdir(self.scratch.name)

    def tearDown(self):
        os.chdir(self.previous_directory)
        self.scratch.cleanup()

    def app(self, page='Learn & Practice'):
        app = AppTest.from_file(str(ROOT / 'app.py'))
        app.session_state['nav_section'] = 'Learning'
        app.session_state['nav_page'] = page
        app.session_state['last_selected_course'] = 'Data Visualisation'
        app.session_state['lp_selected_course'] = f'{COURSE_CODE} - Data Visualisation'
        app.session_state['tc_course_filter'] = f'{COURSE_CODE} - Data Visualisation'
        app.run(timeout=90)
        self.assertFalse(app.exception, [e.message for e in app.exception])
        return app

    def select(self, app, label, value):
        next(s for s in app.selectbox if s.label == label).set_value(value)
        app.run(timeout=90)
        self.assertFalse(app.exception, [e.message for e in app.exception])

    def test_lesson_and_persona_assets_are_real_english_downloads(self):
        lesson = get_dvs_course_lessons()[0]
        self.assertIn('chapterid=81501', lesson['source_url'])
        self.assertIn('Says', lesson['content'])
        self.assertIn('Step 7', lesson['content'])
        for visual in lesson['dvs_illustrations']:
            self.assertTrue((ASSET_ROOT / visual['file']).is_file())
        app = self.app()
        lessons = [e.label for e in app.expander if e.label.startswith('📚 Lesson')]
        self.assertEqual(lessons, ['📚 Lesson 1.1: Design Thinking — Part 1'])
        self.assertIn('Visual study guide — Empathise and Define', [e.label for e in app.expander])
        self.assertIn('Visual study guide — Hypothetical CEO persona', [e.label for e in app.expander])
        downloads = [d.label for d in app.get('download_button')]
        self.assertIn('Download persona template (Word)', downloads)
        self.assertIn('Download persona template (Markdown)', downloads)
        self.assertEqual(downloads.count('Download DVS illustration (PNG)'), 2)
        guide = next(g for g in get_dvs_task_guides('1.1') if g['id'] == '1.1-task')
        with zipfile.ZipFile(TEMPLATE_ROOT / guide['template_file']) as archive:
            doc = archive.read('word/document.xml').decode()
            styles = archive.read('word/styles.xml').decode()
        self.assertIn('Enjoys BASE jumping', doc)
        self.assertIn('Hypothetical goals', doc)
        self.assertIn('Question to validate', doc)
        self.assertNotIn('<w:pBdr', doc)
        self.assertNotIn('<w:pBdr', styles)

    def test_resolver_matches_dvs_task_steps_and_keeps_course_context_separate(self):
        guides = get_dvs_task_guides('1.1')
        task = next(g for g in guides if g['id'] == '1.1-task')
        activity = next(g for g in guides if g['id'] == '1.1.1')
        self.assertEqual(resolver_task_number_boost(task, 'DVS Task 1.1'), 500)
        self.assertEqual(resolver_task_number_boost(task, 'Task 1.1.1'), 0)
        self.assertEqual(resolver_task_number_boost(activity, 'Activity 1.1.1'), 500)
        app = self.app()
        prompt = next(t for t in app.text_area if t.label == 'Paste the exam question, case, or task prompt')
        prompt.set_value('Task 1.1: help me create the hypothetical CEO persona.')
        app.run(timeout=90)
        labels = [e.label for e in app.expander if e.label.startswith('Resolver task')]
        self.assertEqual(labels, ['Resolver task 1.1-task: Hypothetical CEO persona'])
        chooser = next(s for s in app.selectbox if s.key.startswith('course_exam_connector') and s.label == 'Choose a Task 1.1 step')
        self.assertEqual(len(chooser.options), 4)
        for i, step in enumerate(TASK_STEPS):
            app.selectbox(key=chooser.key).set_value(i)
            app.run(timeout=90)
            self.assertFalse(app.exception)
            self.assertIn(f'Check: {step[2]}', [c.value for c in app.caption])
        self.assertNotIn('Download matched workbook: EVO Module 7 Tasks.xlsx', [d.label for d in app.get('download_button')])
        self.select(app, 'Select a course to study:', 'FI1BBEO10 - Evaluation of Outcomes')
        self.assertFalse(any(s.label == 'Choose a Task 1.1 step' for s in app.selectbox))
        self.assertTrue(any(e.label.startswith('📚 Lesson 7.4:') for e in app.expander))

    def test_persona_draft_and_selected_step_transfer_from_lesson_without_generation(self):
        app = self.app()
        draft = 'Hypothetical goal: compare adoption opportunities. Validation question: what decision must this presentation support?'
        next(t for t in app.text_area if t.label == 'Your Task 1.1 persona draft').set_value(draft)
        app.run(timeout=90)
        next(s for s in app.selectbox if s.label == 'Choose a Task 1.1 step').set_value(2)
        app.run(timeout=90)
        next(b for b in app.button if b.label == 'Prepare Task 1.1 in Exam Resolver').click()
        app.run(timeout=90)
        self.assertFalse(app.exception, [e.message for e in app.exception])
        prompt = next(t for t in app.text_area if t.label == 'Paste the exam question, case, or task prompt').value
        self.assertIn(draft, prompt)
        self.assertIn('DVS Task 1.1:', prompt)
        self.assertIn('hypothetical assumptions', prompt)
        self.assertIn('**Auto-detected question style:** Persona design task', [m.value for m in app.markdown])
        chooser = next(s for s in app.selectbox if s.key.startswith('course_exam_connector') and s.label == 'Choose a Task 1.1 step')
        self.assertEqual(chooser.value, 2)
        self.assertNotIn('resolver_answer_history', app.session_state)
        self.select(app, 'Choose a DVS Lesson 1.1 activity or task', 'dvs-1.1.1-81506')
        self.select(app, 'Choose a DVS Lesson 1.1 activity or task', 'dvs-1.1-task-81509')
        self.assertEqual(next(t for t in app.text_area if t.label == 'Your Task 1.1 persona draft').value, draft)

    def test_ai_uses_same_english_guide_and_persona_draft_then_honours_activity_selection(self):
        import json
        from types import SimpleNamespace
        from unittest.mock import patch
        requests = []
        def complete(**kwargs):
            requests.append(kwargs)
            return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English review of a hypothetical persona.'))])])
        fake = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env = {'OPENAI_API_KEY': 'offline-ui-test-key', 'AI_PROVIDER': 'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS'] = json.dumps(list(os.environ) + list(env))
        with patch.dict(os.environ, env), patch('openai.OpenAI', return_value=fake):
            app = self.app()
            draft = 'Hypothetical goal: compare market adoption opportunities.'
            next(t for t in app.text_area if t.label == 'Your Task 1.1 persona draft').set_value(draft)
            app.run(timeout=90)
            next(b for b in app.button if b.label == 'Prepare Task 1.1 in Exam Resolver').click()
            app.run(timeout=90)
            self.assertEqual(len(requests), 0)
            next(b for b in app.button if b.label == '💡 Generate answer with reasoning').click()
            app.run(timeout=90)
            self.assertFalse(app.exception)
            context = requests[0]['messages'][1]['content']
            self.assertIn(draft, context)
            self.assertIn('### DVS Task 1.1: Hypothetical CEO persona', context)
            self.assertIn('**Problem statement:**', context)
            self.assertIn('Additional characteristics are hypothetical assumptions', context)
            self.assertIn('ANSWER LANGUAGE: Write in English', requests[0]['messages'][0]['content'])
            self.assertNotIn('Task 7.3:', context)
            self.select(app, 'Source pool', 'Task guides only')
            self.select(app, 'Resolver scope', 'Specific lesson or outcome')
            choices = next(s for s in app.selectbox if s.label == 'Choose the task guide to focus on')
            self.assertEqual(len(choices.options), 2)
            self.select(app, choices.label, next(o for o in choices.options if o.startswith('Task guide 1.1.1:')))
            self.assertTrue(any('earlier question or dataset' in i.value for i in app.info))
            next(b for b in app.button if b.label == '🔁 Re-generate answer').click()
            app.run(timeout=90)
            self.assertFalse(app.exception)
            context = requests[1]['messages'][1]['content']
            self.assertIn('### Activity 1.1.1: Funky Monkey athlete persona', context)
            self.assertNotIn('### DVS Task 1.1: Hypothetical CEO persona', context)

    def test_training_center_uses_official_code_and_preserves_existing_topics(self):
        app = self.app('Training Center')
        chooser = next(s for s in app.selectbox if s.label == '🎯 Select Topic:')
        self.assertIn('DVS Module 1: Design Thinking', chooser.options)
        self.assertIn('Data Visualization Fundamentals', chooser.options)
        self.select(app, chooser.label, 'DVS Module 1: Design Thinking')
        self.assertTrue(any(e.label == 'Lesson 1: Design Thinking — Part 1' for e in app.expander))
        self.assertTrue(any(b.label == 'Prepare Task 1.1 in Exam Resolver' for b in app.button))


if __name__ == '__main__':
    unittest.main()
