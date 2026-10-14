"""Task 1.4 three-concept workflow, activity templates and AI-context checks."""
from pathlib import Path
import os,sys,tempfile,unittest,json,zipfile
from types import SimpleNamespace
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
from dvs_lesson14 import GUIDE,GUIDES,CONCEPTS,TASK_STEPS,ILLUSTRATIONS
from dvs_curriculum import TEMPLATE_ROOT,ASSET_ROOT
from evo_tasks import resolver_task_number_boost
class DvsLesson14Test(unittest.TestCase):
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
    def test_templates_three_concepts_and_two_reflection_tasks_together(self):
        app=self.app()
        self.assertIn('Download three-concept template (Word)',[d.label for d in app.get('download_button')])
        for image in ILLUSTRATIONS:self.assertTrue((ASSET_ROOT/image['file']).is_file())
        with zipfile.ZipFile(TEMPLATE_ROOT/GUIDE['template_file']) as z:xml=z.read('word/document.xml').decode()
        for name,*_ in CONCEPTS:self.assertIn(name,xml)
        self.assertIn('Reading Level SC 3.1.5 is Level AAA',xml)
        self.assertNotIn('<w:pBdr',xml)
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 1.4: review my three applied reflections.')
        self.run_app(app)
        self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],['Resolver task 1.4-task: Inclusive design usability and accessibility reflections'])
        self.assertIn('**Auto-detected question style:** Inclusion usability accessibility reflection',[m.value for m in app.markdown])
        chooser=next(s for s in app.selectbox if s.label=='Choose a Task 1.4 concept' and s.key.startswith('course_exam_connector'))
        self.assertEqual(len(chooser.options),3)
        for i,step in enumerate(TASK_STEPS):
            app.selectbox(key=chooser.key).set_value(i);self.run_app(app)
            self.assertIn('Check: '+step[2],[c.value for c in app.caption])
        self.assertEqual(resolver_task_number_boost(GUIDE,'Activity 1.4.1'),0)
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 1.3 and Task 1.4: help me plan both reflection assignments.')
        self.run_app(app)
        self.assertIn('Download seven-principle template (Word)',[d.label for d in app.get('download_button')])
        self.assertIn('Download three-concept template (Word)',[d.label for d in app.get('download_button')])
    def test_draft_concept_handoff_and_retention(self):
        app=self.app();draft='Usability proposal: clear Apply and Reset controls. Planned task: filter the chart and recover from an empty result. No completed test yet.'
        next(t for t in app.text_area if t.label=='Your Task 1.4 reflections and research notes').set_value(draft);self.run_app(app)
        next(s for s in app.selectbox if s.label=='Choose a Task 1.4 concept').set_value(2);self.run_app(app)
        next(b for b in app.button if b.label=='Prepare Task 1.4 in Exam Resolver').click();self.run_app(app)
        prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
        self.assertIn(draft,prompt);self.assertIn('DVS Task 1.4:',prompt);self.assertIn('three task headings',prompt)
        self.assertEqual(next(s for s in app.selectbox if s.label=='Choose a Task 1.4 concept' and s.key.startswith('course_exam_connector')).value,2)
        self.assertNotIn('resolver_answer_history',app.session_state)
        next(s for s in app.selectbox if s.label=='Choose a DVS Lesson 1.4 activity or task').set_value(GUIDES[1]['uid']);self.run_app(app)
        next(s for s in app.selectbox if s.label=='Choose a DVS Lesson 1.4 activity or task').set_value(GUIDE['uid']);self.run_app(app)
        self.assertEqual(next(t for t in app.text_area if t.label=='Your Task 1.4 reflections and research notes').value,draft)
    def test_activity_handoffs_and_activity_specific_templates(self):
        app=self.app()
        for guide,label in zip(GUIDES[1:],['Download contrast check log (Markdown)','Download language selector plan (Markdown)']):
            next(s for s in app.selectbox if s.label=='Choose a DVS Lesson 1.4 activity or task').set_value(guide['uid']);self.run_app(app)
            self.assertIn(label,[d.label for d in app.get('download_button')])
            next(b for b in app.button if b.label==f"Prepare Activity {guide['id']} in Exam Resolver").click();self.run_app(app)
            prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
            self.assertIn(f"DVS Activity {guide['id']}:",prompt)
            self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],[f"Resolver task {guide['id']}: {guide['title']}"])
        self.assertTrue(all(name in prompt for name in ['English','Norwegian','German','French']))
    def test_normal_and_strict_ai_context_have_three_concepts_and_sources(self):
        requests=[]
        def complete(**kwargs):
            requests.append(kwargs);return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English concept reflection review.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-ui-test-key','AI_PROVIDER':'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app()
            next(t for t in app.text_area if t.label=='Your Task 1.4 reflections and research notes').set_value('My proposal: keyboard controls and a text/data alternative. No observed results yet.');self.run_app(app)
            next(b for b in app.button if b.label=='Prepare Task 1.4 in Exam Resolver').click();self.run_app(app)
            self.assertEqual(len(requests),0)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click();self.run_app(app)
            next(c for c in app.checkbox if c.label=='📚 Strict curriculum mode (use ONLY the syllabus)').set_value(True);self.run_app(app)
            next(b for b in app.button if b.label=='🔁 Re-generate answer').click();self.run_app(app)
            for request in requests:
                context=request['messages'][1]['content']
                self.assertIn('My proposal: keyboard controls',context)
                self.assertIn('### DVS Task 1.4: Three applied reflections',context)
                for name,*_ in CONCEPTS:self.assertIn(name,context)
                self.assertIn('four principles support the accessibility paragraph',context)
                self.assertIn('w3.org/WAI/fundamentals/accessibility-usability-inclusion/',context)
                self.assertNotIn('### DVS Task 1.3:',context)
                self.assertIn('ANSWER LANGUAGE: Write in English',request['messages'][0]['content'])
            self.assertIn('STRICT CURRICULUM MODE',requests[1]['messages'][1]['content'])
