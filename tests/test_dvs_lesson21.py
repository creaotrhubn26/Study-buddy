"""Two-question UX task: module isolation, draft handoff and complete AI context."""
from pathlib import Path
import os,sys,tempfile,unittest,json,zipfile
from types import SimpleNamespace
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
from dvs_lesson21 import GUIDE,TASK_STEPS,ILLUSTRATIONS,REDIRECT_NOTE
from dvs_curriculum import get_dvs_training_modules,TEMPLATE_ROOT,ASSET_ROOT
class DvsLesson21Test(unittest.TestCase):
    def setUp(self):
        self.old=Path.cwd();self.temp=tempfile.TemporaryDirectory();os.chdir(self.temp.name)
    def tearDown(self):
        os.chdir(self.old);self.temp.cleanup()
    def run_app(self,app):
        app.run(timeout=90);self.assertFalse(app.exception,[e.message for e in app.exception]);return app
    def app(self,page='Learn & Practice'):
        app=AppTest.from_file(str(ROOT/'app.py'))
        for key,value in {'nav_section':'Learning','nav_page':page,'last_selected_course':'Data Visualisation','lp_selected_course':'FI1BBDV75 - Data Visualisation','tc_course_filter':'FI1BBDV75 - Data Visualisation'}.items():app.session_state[key]=value
        return self.run_app(app)
    def test_task_resources_and_module_isolation(self):
        modules=get_dvs_training_modules()
        self.assertEqual([l['lesson_number'] for l in modules['DVS Module 1: Design Thinking']['lessons']],['1.1','1.2','1.3','1.4'])
        self.assertEqual([l['lesson_number'] for l in modules['DVS Module 2: User Experience and User Experience Design']['lessons']],['2.1'])
        for item in ILLUSTRATIONS:self.assertTrue((ASSET_ROOT/item['file']).is_file())
        with zipfile.ZipFile(TEMPLATE_ROOT/GUIDE['template_file']) as z:
            xml=z.read('word/document.xml').decode();styles=z.read('word/styles.xml').decode()
        self.assertIn('Question 1: Website review',xml);self.assertIn('Question 2: UX design',xml)
        self.assertIn('at least half a page',xml);self.assertIn('Arial',styles);self.assertIn('w:sz w:val="22"',styles)
        self.assertNotIn('<w:pBdr',xml+styles)
        app=self.app()
        for name in ['Download website review template (Markdown)','Download UX application template (Markdown)','Download website evidence log (Markdown)','Download website review and UX template (Word)']:
            self.assertIn(name,[d.label for d in app.get('download_button')])
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 2.1: help me plan both answers.');self.run_app(app)
        self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],['Resolver task 2.1-task: Website UX review and visualisation application'])
        self.assertIn('**Auto-detected question style:** UX website review and application',[m.value for m in app.markdown])
        chooser=next(s for s in app.selectbox if s.label=='Choose a Task 2.1 step' and s.key.startswith('course_exam_connector'))
        self.assertEqual(len(chooser.options),7)
        for i,step in enumerate(TASK_STEPS):
            app.selectbox(key=chooser.key).set_value(i);self.run_app(app)
            self.assertIn('Check: '+step[2],[c.value for c in app.caption])
    def test_draft_and_step_handoff(self):
        app=self.app();draft='Question 1 evidence: Forum link redirects; historical evaluation pending tutor approval. Question 2 proposal: labelled bars with a data alternative for category comparison.'
        next(t for t in app.text_area if t.label=='Your Task 2.1 report UX application and evidence').set_value(draft);self.run_app(app)
        next(s for s in app.selectbox if s.label=='Choose a Task 2.1 step').set_value(5);self.run_app(app)
        next(b for b in app.button if b.label=='Prepare Task 2.1 in Exam Resolver').click();self.run_app(app)
        prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
        self.assertIn(draft,prompt);self.assertIn('DVS Task 2.1:',prompt);self.assertIn('Arial 11 pt',prompt)
        self.assertEqual(next(s for s in app.selectbox if s.label=='Choose a Task 2.1 step' and s.key.startswith('course_exam_connector')).value,5)
        self.assertNotIn('resolver_answer_history',app.session_state)
        self.assertEqual(app.session_state['dvs_persona_drafts'][GUIDE['uid']],draft)
    def test_training_center_has_separate_module2_topic(self):
        app=self.app('Training Center')
        next(s for s in app.selectbox if s.label=='🎯 Select Topic:').set_value('DVS Module 2: User Experience and User Experience Design');self.run_app(app)
        self.assertIn('Prepare Task 2.1 in Exam Resolver',[b.label for b in app.button])
        self.assertNotIn('Prepare Task 1.1 in Exam Resolver',[b.label for b in app.button])
    def test_normal_and_strict_ai_context_keep_both_questions_and_boundaries(self):
        requests=[]
        def complete(**kwargs):
            requests.append(kwargs);return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English UX draft review.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-ui-test-key','AI_PROVIDER':'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app()
            next(t for t in app.text_area if t.label=='Your Task 2.1 report UX application and evidence').set_value('My observation: current Forum link reaches About. No historical observations.');self.run_app(app)
            next(b for b in app.button if b.label=='Prepare Task 2.1 in Exam Resolver').click();self.run_app(app)
            self.assertEqual(len(requests),0)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click();self.run_app(app)
            next(c for c in app.checkbox if c.label=='📚 Strict curriculum mode (use ONLY the syllabus)').set_value(True);self.run_app(app)
            next(b for b in app.button if b.label=='🔁 Re-generate answer').click();self.run_app(app)
            self.assertEqual(len(requests),2)
            for request in requests:
                context=request['messages'][1]['content']
                for expected in ['My observation: current Forum','### DVS Task 2.1:','one-page report','at least half a page','Arial 11 pt','7. Review both outputs',REDIRECT_NOTE,'semanticstudios.com/user_experience_design/']:
                    self.assertIn(expected,context)
                self.assertNotIn('### DVS Task 1.4:',context)
                self.assertIn('ANSWER LANGUAGE: Write in English',request['messages'][0]['content'])
            self.assertIn('STRICT CURRICULUM MODE',requests[1]['messages'][1]['content'])
