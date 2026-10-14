"""Seven-question graphics workflow and complete English resolver context."""
from pathlib import Path
import os,sys,tempfile,unittest,json,zipfile
from types import SimpleNamespace
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
from dvs_lesson23 import GUIDE,TASK_STEPS,ILLUSTRATIONS,PRODUCTS
from dvs_curriculum import get_dvs_training_modules,TEMPLATE_ROOT,ASSET_ROOT
class DvsLesson23Test(unittest.TestCase):
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
    def test_resources_matching_and_all_seven_questions(self):
        for visual in ILLUSTRATIONS:self.assertTrue((ASSET_ROOT/visual['file']).is_file())
        with zipfile.ZipFile(TEMPLATE_ROOT/GUIDE['template_file']) as z:
            xml=z.read('word/document.xml').decode();styles=z.read('word/styles.xml').decode()
        for expected in ['Question 1','Question 6','CorelDRAW','Procreate','Photopea','platform','price','functions']:
            self.assertIn(expected.lower(),xml.lower())
        self.assertNotIn('<w:pBdr',xml+styles)
        app=self.app()
        for label in ['Download graphics study worksheet (Markdown)','Download software comparison template (Markdown)','Download GIMP orientation log (Markdown)','Download graphics and software comparison template (Word)']:
            self.assertIn(label,[d.label for d in app.get('download_button')])
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 2.3: review my graphics answers and software comparison.');self.run_app(app)
        self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],['Resolver task 2.3-task: Graphics study questions and software comparison'])
        self.assertIn('**Auto-detected question style:** Graphics concepts and software comparison',[m.value for m in app.markdown])
        chooser=next(s for s in app.selectbox if s.label=='Choose a Task 2.3 question' and s.key.startswith('course_exam_connector'))
        self.assertEqual(len(chooser.options),7)
        for i,step in enumerate(TASK_STEPS):
            app.selectbox(key=chooser.key).set_value(i);self.run_app(app)
            self.assertIn('Check: '+step[2],[c.value for c in app.caption])
        next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').set_value('Task 2.2 and Task 2.3: plan both tasks.');self.run_app(app)
        self.assertIn('Download graph analysis and four rules template (Word)',[d.label for d in app.get('download_button')])
        self.assertIn('Download graphics and software comparison template (Word)',[d.label for d in app.get('download_button')])
    def test_custom_draft_and_question_transfer_without_generation(self):
        app=self.app();draft='My vector choices are Inkscape and Illustrator. Company devices are unknown; I will confirm them before recommending a product.'
        next(t for t in app.text_area if t.label=='Your Task 2.3 study answers and software comparison').set_value(draft);self.run_app(app)
        next(s for s in app.selectbox if s.label=='Choose a Task 2.3 question').set_value(6);self.run_app(app)
        next(b for b in app.button if b.label=='Prepare Task 2.3 in Exam Resolver').click();self.run_app(app)
        prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
        for expected in [draft,'DVS Task 2.3:','recommendation is optional','no page count or font']:self.assertIn(expected,prompt)
        self.assertEqual(next(s for s in app.selectbox if s.label=='Choose a Task 2.3 question' and s.key.startswith('course_exam_connector')).value,6)
        self.assertNotIn('resolver_answer_history',app.session_state)
        self.assertEqual(app.session_state['dvs_persona_drafts'][GUIDE['uid']],draft)
    def test_training_modules_keep_previous_lessons(self):
        modules=get_dvs_training_modules()
        self.assertEqual([l['lesson_number'] for l in modules['DVS Module 1: Design Thinking']['lessons']],['1.1','1.2','1.3','1.4'])
        self.assertEqual([l['lesson_number'] for l in modules['DVS Module 2: User Experience and User Experience Design']['lessons']],['2.1','2.2','2.3','2.4'])
        app=self.app('Training Center')
        next(s for s in app.selectbox if s.label=='🎯 Select Topic:').set_value('DVS Module 2: User Experience and User Experience Design');self.run_app(app)
        labels=[b.label for b in app.button]
        for number in ['2.1','2.2','2.3','2.4']:self.assertIn(f'Prepare Task {number} in Exam Resolver',labels)
        self.assertNotIn('Prepare Task 1.1 in Exam Resolver',labels)
    def test_complete_normal_and_strict_english_context(self):
        requests=[]
        def complete(**kwargs):
            requests.append(kwargs);return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English graphics comparison review.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-ui-test-key','AI_PROVIDER':'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app()
            next(t for t in app.text_area if t.label=='Your Task 2.3 study answers and software comparison').set_value('Company devices are unknown and product testing is planned.');self.run_app(app)
            next(b for b in app.button if b.label=='Prepare Task 2.3 in Exam Resolver').click();self.run_app(app)
            self.assertEqual(len(requests),0)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click();self.run_app(app)
            next(c for c in app.checkbox if c.label=='📚 Strict curriculum mode (use ONLY the syllabus)').set_value(True);self.run_app(app)
            next(b for b in app.button if b.label=='🔁 Re-generate answer').click();self.run_app(app)
            self.assertEqual(len(requests),2)
            for request in requests:
                context=request['messages'][1]['content']
                for expected in ['Company devices are unknown','### DVS Task 2.3:','7. Compare the three software candidates','14 October 2026','NOK 4,240','NOK 179','EUR 15','one-time payments','Inkscape','Adobe Illustrator','no page count or font','does not submit or grade H5P','official completed solution','https://docs.gimp.org/3.0/en/gimp-images-out.html']:
                    self.assertIn(expected,context)
                for p in PRODUCTS:self.assertIn(p['name'],context);self.assertIn(p['source'],context)
                self.assertNotIn('### DVS Task 2.2:',context)
                self.assertIn('ANSWER LANGUAGE: Write in English',request['messages'][0]['content'])
            self.assertIn('STRICT CURRICULUM MODE',requests[1]['messages'][1]['content'])
