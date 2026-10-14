"""Task 2.2 graph analysis, four-rule application and safe evidence handoff."""
from pathlib import Path
import os,sys,tempfile,unittest,json,zipfile
from types import SimpleNamespace
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
from dvs_lesson22 import GUIDE,TASK_STEPS,RULES,ILLUSTRATIONS
from dvs_curriculum import get_dvs_training_modules,TEMPLATE_ROOT,ASSET_ROOT
class DvsLesson22Test(unittest.TestCase):
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
    def test_resources_exact_matching_steps_and_two_module2_tasks(self):
        for visual in ILLUSTRATIONS:self.assertTrue((ASSET_ROOT/visual['file']).is_file())
        with zipfile.ZipFile(TEMPLATE_ROOT/GUIDE['template_file']) as z:
            xml=z.read('word/document.xml').decode();styles=z.read('word/styles.xml').decode()
        for name,*_ in RULES:self.assertIn(name,xml)
        self.assertIn('no page count or font requirement',xml)
        self.assertIn('Figure 7 - Unemployment',xml);self.assertIn('Figure 8 - Public health expenditure',xml)
        self.assertNotIn('<w:pBdr',xml+styles)
        app=self.app()
        for label in ['Download graph analysis template (Markdown)','Download four rules template (Markdown)','Download chart and peer review log (Markdown)','Download graph analysis and four rules template (Word)']:
            self.assertIn(label,[d.label for d in app.get('download_button')])
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 2.2: review my graph analysis and four rules.');self.run_app(app)
        self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],['Resolver task 2.2-task: Misleading graph analysis and four ethical rules'])
        self.assertIn('**Auto-detected question style:** Ethical graph analysis and rule application',[m.value for m in app.markdown])
        chooser=next(s for s in app.selectbox if s.label=='Choose a Task 2.2 step' and s.key.startswith('course_exam_connector'))
        self.assertEqual(len(chooser.options),7)
        for i,step in enumerate(TASK_STEPS):
            app.selectbox(key=chooser.key).set_value(i);self.run_app(app)
            self.assertIn('Check: '+step[2],[c.value for c in app.caption])
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 2.1 and Task 2.2: help me plan both tasks.');self.run_app(app)
        self.assertIn('Download website review and UX template (Word)',[d.label for d in app.get('download_button')])
        self.assertIn('Download graph analysis and four rules template (Word)',[d.label for d in app.get('download_button')])
    def test_draft_and_step_transfer_without_generation(self):
        app=self.app();draft='Figure 7 observation: November label and position disagree. Figure 8 proposed correction: zero-baseline bars and explicit future status. My peer review is planned, not completed.'
        next(t for t in app.text_area if t.label=='Your Task 2.2 graph analysis rules and review notes').set_value(draft);self.run_app(app)
        next(s for s in app.selectbox if s.label=='Choose a Task 2.2 step').set_value(5);self.run_app(app)
        next(b for b in app.button if b.label=='Prepare Task 2.2 in Exam Resolver').click();self.run_app(app)
        prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
        self.assertIn(draft,prompt);self.assertIn('DVS Task 2.2:',prompt);self.assertIn('no specified page count or font',prompt)
        self.assertEqual(next(s for s in app.selectbox if s.label=='Choose a Task 2.2 step' and s.key.startswith('course_exam_connector')).value,5)
        self.assertNotIn('resolver_answer_history',app.session_state)
        self.assertEqual(app.session_state['dvs_persona_drafts'][GUIDE['uid']],draft)
    def test_module2_training_preserves_lesson21_and_module1_order(self):
        modules=get_dvs_training_modules()
        self.assertEqual([l['lesson_number'] for l in modules['DVS Module 1: Design Thinking']['lessons']],['1.1','1.2','1.3','1.4'])
        self.assertEqual([l['lesson_number'] for l in modules['DVS Module 2: User Experience and User Experience Design']['lessons']],['2.1','2.2'])
        app=self.app('Training Center')
        next(s for s in app.selectbox if s.label=='🎯 Select Topic:').set_value('DVS Module 2: User Experience and User Experience Design');self.run_app(app)
        labels=[b.label for b in app.button]
        self.assertIn('Prepare Task 2.1 in Exam Resolver',labels);self.assertIn('Prepare Task 2.2 in Exam Resolver',labels)
        self.assertNotIn('Prepare Task 1.1 in Exam Resolver',labels)
    def test_complete_normal_and_strict_english_context(self):
        requests=[]
        def complete(**kwargs):
            requests.append(kwargs);return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English graph analysis and four-rule review.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-ui-test-key','AI_PROVIDER':'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app()
            next(t for t in app.text_area if t.label=='Your Task 2.2 graph analysis rules and review notes').set_value('My planned peer review has no actual feedback yet.');self.run_app(app)
            next(b for b in app.button if b.label=='Prepare Task 2.2 in Exam Resolver').click();self.run_app(app)
            self.assertEqual(len(requests),0)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click();self.run_app(app)
            next(c for c in app.checkbox if c.label=='📚 Strict curriculum mode (use ONLY the syllabus)').set_value(True);self.run_app(app)
            next(b for b in app.button if b.label=='🔁 Re-generate answer').click();self.run_app(app)
            self.assertEqual(len(requests),2)
            for request in requests:
                context=request['messages'][1]['content']
                for expected in ['My planned peer review','### DVS Task 2.2:','7. Review evidence and corrections','8.6%','4.0%','3.75','2023 and 2027','no page count or font','It does not inspect','ONS line-chart discussion','This guide is not Noroff’s completed solution.']:
                    self.assertIn(expected,context)
                for name,*_ in RULES:self.assertIn(name,context)
                self.assertNotIn('### DVS Task 2.1:',context)
                self.assertIn('ANSWER LANGUAGE: Write in English',request['messages'][0]['content'])
            self.assertIn('STRICT CURRICULUM MODE',requests[1]['messages'][1]['content'])
