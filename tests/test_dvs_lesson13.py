"""Workflow checks for seven reflections, activity isolation and resolver context."""
from pathlib import Path
import os,sys,tempfile,unittest,json,zipfile
from types import SimpleNamespace
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
from dvs_lesson13 import GUIDE,GUIDES,PRINCIPLES,TASK_STEPS,ILLUSTRATIONS
from dvs_curriculum import TEMPLATE_ROOT,ASSET_ROOT
from evo_tasks import resolver_task_number_boost
class DvsLesson13Test(unittest.TestCase):
    def setUp(self):
        self.old=Path.cwd();self.temp=tempfile.TemporaryDirectory();os.chdir(self.temp.name)
    def tearDown(self):
        os.chdir(self.old);self.temp.cleanup()
    def app(self):
        app=AppTest.from_file(str(ROOT/'app.py'))
        for key,value in {'nav_section':'Learning','nav_page':'Learn & Practice','last_selected_course':'Data Visualisation','lp_selected_course':'FI1BBDV75 - Data Visualisation'}.items():app.session_state[key]=value
        return self.run_app(app)
    def run_app(self,app):
        app.run(timeout=90);self.assertFalse(app.exception,[e.message for e in app.exception]);return app
    def test_word_assets_and_all_seven_resolver_principles(self):
        app=self.app()
        self.assertIn('Download seven-principle template (Word)',[d.label for d in app.get('download_button')])
        for image in ILLUSTRATIONS:self.assertTrue((ASSET_ROOT/image['file']).is_file())
        with zipfile.ZipFile(TEMPLATE_ROOT/GUIDE['template_file']) as z:xml=z.read('word/document.xml').decode()
        for name,*_ in PRINCIPLES:self.assertIn(name,xml)
        self.assertNotIn('<w:pBdr',xml)
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 1.3: review my seven universal design reflections.')
        self.run_app(app)
        self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],['Resolver task 1.3-task: Seven universal design reflections'])
        self.assertIn('**Auto-detected question style:** Universal design reflection',[m.value for m in app.markdown])
        chooser=next(s for s in app.selectbox if s.label=='Choose a Task 1.3 principle' and s.key.startswith('course_exam_connector'))
        self.assertEqual(len(chooser.options),7)
        for i,step in enumerate(TASK_STEPS):
            app.selectbox(key=chooser.key).set_value(i);self.run_app(app)
            self.assertIn('Check: '+step[2],[c.value for c in app.caption])
        self.assertEqual(resolver_task_number_boost(GUIDE,'Activity 1.3.1'),0)
    def test_reflection_draft_principle_transfer_and_retention(self):
        app=self.app();draft='Equitable Use: I would provide equivalent text and data access. Proposed check: compare the message across views. Source: W3C WAI.'
        next(t for t in app.text_area if t.label=='Your Task 1.3 reflections and research notes').set_value(draft);self.run_app(app)
        next(s for s in app.selectbox if s.label=='Choose a Task 1.3 principle').set_value(6);self.run_app(app)
        next(b for b in app.button if b.label=='Prepare Task 1.3 in Exam Resolver').click();self.run_app(app)
        prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
        self.assertIn(draft,prompt);self.assertIn('DVS Task 1.3:',prompt)
        self.assertEqual(next(s for s in app.selectbox if s.label=='Choose a Task 1.3 principle' and s.key.startswith('course_exam_connector')).value,6)
        self.assertNotIn('resolver_answer_history',app.session_state)
        chooser=next(s for s in app.selectbox if s.label=='Choose a DVS Lesson 1.3 activity or task')
        chooser.set_value(GUIDES[1]['uid']);self.run_app(app)
        next(s for s in app.selectbox if s.label==chooser.label).set_value(GUIDE['uid']);self.run_app(app)
        self.assertEqual(next(t for t in app.text_area if t.label=='Your Task 1.3 reflections and research notes').value,draft)
    def test_each_activity_prepares_its_own_brief(self):
        app=self.app()
        for guide in GUIDES[1:]:
            next(s for s in app.selectbox if s.label=='Choose a DVS Lesson 1.3 activity or task').set_value(guide['uid']);self.run_app(app)
            next(b for b in app.button if b.label==f"Prepare Activity {guide['id']} in Exam Resolver").click();self.run_app(app)
            prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
            self.assertIn(f"DVS Activity {guide['id']}:",prompt)
            self.assertNotIn('Funky Monkey',prompt)
            self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],[f"Resolver task {guide['id']}: {guide['title']}"])
    def test_ai_receives_full_seven_principle_guide_and_english_draft(self):
        requests=[]
        def complete(**kwargs):
            requests.append(kwargs);return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English reflection review.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-ui-test-key','AI_PROVIDER':'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app()
            next(t for t in app.text_area if t.label=='Your Task 1.3 reflections and research notes').set_value('My proposal: labelled patterns and a data table. I have not performed the check.');self.run_app(app)
            next(b for b in app.button if b.label=='Prepare Task 1.3 in Exam Resolver').click();self.run_app(app)
            self.assertEqual(len(requests),0)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click();self.run_app(app)
            context=requests[0]['messages'][1]['content']
            self.assertIn('My proposal: labelled patterns',context)
            self.assertIn('### DVS Task 1.3: Seven universal design reflections',context)
            for name,*_ in PRINCIPLES:self.assertIn(name,context)
            self.assertIn('NC State numbers Tolerance for Error fifth',context)
            self.assertIn('w3.org/WAI/tutorials/images/complex/',context)
            self.assertNotIn('### DVS Task 1.2:',context)
            self.assertNotIn('### DVS Activity 1.3.1:',context)
            self.assertIn('ANSWER LANGUAGE: Write in English',requests[0]['messages'][0]['content'])

            next(c for c in app.checkbox if c.label == '📚 Strict curriculum mode (use ONLY the syllabus)').set_value(True);self.run_app(app)
            next(b for b in app.button if b.label == '🔁 Re-generate answer').click();self.run_app(app)
            strict_context = requests[1]['messages'][1]['content']
            for name,*_ in PRINCIPLES:self.assertIn(name,strict_context)
            self.assertIn('w3.org/WAI/tutorials/images/complex/',strict_context)
            self.assertIn('STRICT CURRICULUM MODE',strict_context)
