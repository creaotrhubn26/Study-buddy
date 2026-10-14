"""Meaningful checks of Task 1.2 rendering, isolation, handoff and AI context."""
from pathlib import Path
import os
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch
import json
import zipfile
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
from dvs_lesson12 import GUIDE,TASK_STEPS,ILLUSTRATIONS,get_task_guide_markdown
from dvs_curriculum import TEMPLATE_ROOT,ASSET_ROOT
from evo_tasks import resolver_task_number_boost

class DvsLesson12Test(unittest.TestCase):
    def setUp(self):
        self.old=Path.cwd();self.temp=tempfile.TemporaryDirectory();os.chdir(self.temp.name)
    def tearDown(self):
        os.chdir(self.old);self.temp.cleanup()
    def app(self):
        app=AppTest.from_file(str(ROOT/'app.py'))
        for key,value in {'nav_section':'Learning','nav_page':'Learn & Practice','last_selected_course':'Data Visualisation','lp_selected_course':'FI1BBDV75 - Data Visualisation'}.items():
            app.session_state[key]=value
        return self.run_app(app)
    def run_app(self,app):
        app.run(timeout=90);self.assertFalse(app.exception,[e.message for e in app.exception]);return app
    def test_required_resources_and_all_six_resolver_steps(self):
        app=self.app()
        self.assertIn('Download wireframe and test plan (Word)',[d.label for d in app.get('download_button')])
        for v in ILLUSTRATIONS:self.assertTrue((ASSET_ROOT/v['file']).is_file())
        with zipfile.ZipFile(TEMPLATE_ROOT/GUIDE['template_file']) as z:
            xml=z.read('word/document.xml').decode()
        self.assertIn('Plan the results screen',xml);self.assertIn('Observation record',xml)
        self.assertNotIn('<w:pBdr',xml)
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 1.2: help me plan a mobile BMI wireframe.')
        self.run_app(app)
        self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],['Resolver task 1.2-task: Mobile BMI low-fidelity wireframe'])
        self.assertIn('**Auto-detected question style:** Wireframe design task',[m.value for m in app.markdown])
        chooser=next(s for s in app.selectbox if s.label=='Choose a Task 1.2 step' and s.key.startswith('course_exam_connector'))
        self.assertEqual(len(chooser.options),6)
        for i,step in enumerate(TASK_STEPS):
            app.selectbox(key=chooser.key).set_value(i);self.run_app(app)
            self.assertIn('Check: '+step[2],[c.value for c in app.caption])
        self.assertEqual(resolver_task_number_boost(GUIDE,'Task 1.1'),0)
    def test_wireframe_plan_step_transfer_and_session_retention(self):
        app=self.app();draft='Input screen: Height (cm), Weight (kg), Age (years), Calculate BMI. Results: labelled You marker, chart selector and age filter. Proposed test: find your marker.'
        next(t for t in app.text_area if t.label=='Your Task 1.2 wireframe and test plan').set_value(draft);self.run_app(app)
        next(s for s in app.selectbox if s.label=='Choose a Task 1.2 step').set_value(4);self.run_app(app)
        next(b for b in app.button if b.label=='Prepare Task 1.2 in Exam Resolver').click();self.run_app(app)
        prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
        self.assertIn(draft,prompt);self.assertIn('DVS Task 1.2:',prompt)
        chooser=next(s for s in app.selectbox if s.label=='Choose a Task 1.2 step' and s.key.startswith('course_exam_connector'))
        self.assertEqual(chooser.value,4);self.assertNotIn('resolver_answer_history',app.session_state)
        course=next(s for s in app.selectbox if s.label=='Select a course to study:')
        course.set_value('FI1BBEO10 - Evaluation of Outcomes');self.run_app(app)
        self.assertFalse(any(s.label=='Choose a Task 1.2 step' for s in app.selectbox))
        next(s for s in app.selectbox if s.label=='Select a course to study:').set_value('FI1BBDV75 - Data Visualisation');self.run_app(app)
        self.assertEqual(next(t for t in app.text_area if t.label=='Your Task 1.2 wireframe and test plan').value,draft)
    def test_ai_receives_wireframe_guide_and_plan_in_english(self):
        requests=[]
        def complete(**kwargs):
            requests.append(kwargs)
            return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English wireframe review.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-ui-test-key','AI_PROVIDER':'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app()
            next(t for t in app.text_area if t.label=='Your Task 1.2 wireframe and test plan').set_value('My sketch plan: two screens, labelled units and a diamond You marker.');self.run_app(app)
            next(b for b in app.button if b.label=='Prepare Task 1.2 in Exam Resolver').click();self.run_app(app)
            self.assertEqual(len(requests),0)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click();self.run_app(app)
            context=requests[0]['messages'][1]['content']
            self.assertIn('My sketch plan: two screens',context)
            self.assertIn('### DVS Task 1.2: Mobile BMI low-fidelity wireframe',context)
            self.assertTrue(any('reviews your written plan' in c.value for c in app.caption))
            self.assertIn('6. Review and explain the design',context)
            self.assertIn('Age supports comparison filtering',context)
            self.assertNotIn('### DVS Task 1.1: Hypothetical CEO persona',context)
            self.assertIn('ANSWER LANGUAGE: Write in English',requests[0]['messages'][0]['content'])
