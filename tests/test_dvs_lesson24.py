"""Three GIMP outputs, independent activities and honest resolver handoff."""
from pathlib import Path
import os,sys,tempfile,unittest,json,zipfile
from types import SimpleNamespace
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
from dvs_lesson24 import GUIDE,GUIDES,TASK_STEPS,ACTIVITY_STEPS,ILLUSTRATIONS
from dvs_curriculum import get_dvs_training_modules,TEMPLATE_ROOT,ASSET_ROOT
class DvsLesson24Test(unittest.TestCase):
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
    def test_three_output_resources_and_seven_steps(self):
        for visual in ILLUSTRATIONS:self.assertTrue((ASSET_ROOT/visual['file']).is_file())
        with zipfile.ZipFile(TEMPLATE_ROOT/GUIDE['template_file']) as z:
            xml=z.read('word/document.xml').decode();styles=z.read('word/styles.xml').decode()
        for expected in ['Question 1','Question 2','Question 3','80%','Stone','Data Analyst','tree.png','tree.jpg','does not inspect image pixels']:
            self.assertIn(expected,xml)
        self.assertNotIn('<w:pBdr',xml+styles)
        app=self.app()
        for label in ['Download three image design worksheet (Markdown)','Download editing and export log (Markdown)','Download GIMP image design worksheet (Word)']:
            self.assertIn(label,[d.label for d in app.get('download_button')])
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 2.4: review my three GIMP image designs.');self.run_app(app)
        self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],['Resolver task 2.4-task: Three image designs with GIMP'])
        self.assertIn('**Auto-detected question style:** GIMP image editing plan and evidence',[m.value for m in app.markdown])
        chooser=next(s for s in app.selectbox if s.label=='Choose a Task 2.4 step' and s.key.startswith('course_exam_connector'))
        self.assertEqual(len(chooser.options),7)
        for i,step in enumerate(TASK_STEPS):
            app.selectbox(key=chooser.key).set_value(i);self.run_app(app)
            self.assertIn('Check: '+step[2],[c.value for c in app.caption])
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 2.3 and Task 2.4: plan both tasks.');self.run_app(app)
        labels=[d.label for d in app.get('download_button')]
        self.assertIn('Download graphics and software comparison template (Word)',labels)
        self.assertIn('Download GIMP image design worksheet (Word)',labels)
    def test_main_draft_step_transfer_and_training_order(self):
        modules=get_dvs_training_modules()
        self.assertEqual([l['lesson_number'] for l in modules['DVS Module 1: Design Thinking']['lessons']],['1.1','1.2','1.3','1.4'])
        self.assertEqual([l['lesson_number'] for l in modules['DVS Module 2: User Experience and User Experience Design']['lessons']],['2.1','2.2','2.3','2.4'])
        app=self.app();draft='I plan to check the leaves opacity at 80%. Stone availability and export reopening are not checked yet.'
        next(t for t in app.text_area if t.label=='Your Task 2.4 editing plan and check notes').set_value(draft);self.run_app(app)
        next(s for s in app.selectbox if s.label=='Choose a Task 2.4 step').set_value(4);self.run_app(app)
        next(b for b in app.button if b.label=='Prepare Task 2.4 in Exam Resolver').click();self.run_app(app)
        prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
        for expected in [draft,'DVS Task 2.4:','leaves opacity 80%','Stone','strawberry','No font/page count']:self.assertIn(expected,prompt)
        self.assertEqual(next(s for s in app.selectbox if s.label=='Choose a Task 2.4 step' and s.key.startswith('course_exam_connector')).value,4)
        self.assertNotIn('resolver_answer_history',app.session_state)
        self.assertEqual(app.session_state['dvs_persona_drafts'][GUIDE['uid']],draft)
        app=self.app('Training Center')
        next(s for s in app.selectbox if s.label=='🎯 Select Topic:').set_value('DVS Module 2: User Experience and User Experience Design');self.run_app(app)
        self.assertIn('Prepare Task 2.4 in Exam Resolver',[b.label for b in app.button])
    def test_four_independent_activity_handoffs_and_retained_drafts(self):
        app=self.app()
        for guide in GUIDES[1:]:
            number=guide['id']
            next(s for s in app.selectbox if s.label=='Choose a DVS Lesson 2.4 activity or task').set_value(guide['uid']);self.run_app(app)
            self.assertIn(f'Download Activity {number} worksheet (Markdown)',[d.label for d in app.get('download_button')])
            draft=f'Activity {number} planned operation only; I have not performed the reopen check.'
            next(t for t in app.text_area if t.label==f'Your Activity {number} editing plan and check notes').set_value(draft);self.run_app(app)
            next(s for s in app.selectbox if s.label==f'Choose an Activity {number} step' and not s.key.startswith('course_exam_connector')).set_value(1);self.run_app(app)
            next(b for b in app.button if b.label==f'Prepare Activity {number} in Exam Resolver').click();self.run_app(app)
            prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
            self.assertIn(f'DVS Activity {number}:',prompt);self.assertIn(draft,prompt)
            self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],[f"Resolver task {number}: {guide['title']}"])
            self.assertEqual(next(s for s in app.selectbox if s.label==f'Choose an Activity {number} step' and s.key.startswith('course_exam_connector')).value,1)
            self.assertNotIn('resolver_answer_history',app.session_state)
        for guide in GUIDES[1:]:self.assertIn(f"Activity {guide['id']} planned",app.session_state['dvs_persona_drafts'][guide['uid']])
        self.assertIn('Data Analyst',prompt)
    def test_complete_normal_and_strict_english_context(self):
        requests=[]
        def complete(**kwargs):
            requests.append(kwargs);return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English editing plan review.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-ui-test-key','AI_PROVIDER':'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app()
            next(t for t in app.text_area if t.label=='Your Task 2.4 editing plan and check notes').set_value('Actual pixel and export checks are still planned.');self.run_app(app)
            next(b for b in app.button if b.label=='Prepare Task 2.4 in Exam Resolver').click();self.run_app(app)
            self.assertEqual(len(requests),0)
            next(s for s in app.selectbox if s.label=='Choose a Task 2.4 step' and s.key.startswith('course_exam_connector')).set_value(6);self.run_app(app)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click();self.run_app(app)
            next(c for c in app.checkbox if c.label=='📚 Strict curriculum mode (use ONLY the syllabus)').set_value(True);self.run_app(app)
            next(b for b in app.button if b.label=='🔁 Re-generate answer').click();self.run_app(app)
            self.assertEqual(len(requests),2)
            for request in requests:
                context=request['messages'][1]['content']
                for expected in ['Current selected step: 7. Save, export and review all three outputs','Actual pixel and export checks are still planned','### DVS Task 2.4:','7. Save, export and review all three outputs','LEAVES','80%','Stone','Q3 highest','no unit, year or exact data labels','tree.png','tree.jpg','Colors → Color to Alpha','Ctrl','https://docs.gimp.org/3.0/en/gimp-images-out.html','It does not inspect image pixels','not a completed official solution']:
                    self.assertIn(expected,context)
                self.assertNotIn('### DVS Task 2.3:',context)
                self.assertIn('ANSWER LANGUAGE: Write in English',request['messages'][0]['content'])
            self.assertIn('STRICT CURRICULUM MODE',requests[1]['messages'][1]['content'])
