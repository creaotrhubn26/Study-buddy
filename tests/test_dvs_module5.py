"""Verify preparation provenance and the real lesson → resolver workflow."""
from pathlib import Path
import os,sys,tempfile,unittest,json
from types import SimpleNamespace
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
import dvs_module5 as module
from dvs_curriculum import get_dvs_course_lessons,get_dvs_training_modules,DVS_TASK_GUIDES,TEMPLATE_ROOT

class Module5Test(unittest.TestCase):
    def setUp(self):
        self.old=Path.cwd();self.temp=tempfile.TemporaryDirectory();os.chdir(self.temp.name)
    def tearDown(self):os.chdir(self.old);self.temp.cleanup()
    def run_app(self,app):
        app.run(timeout=90);self.assertFalse(app.exception,[e.message for e in app.exception]);return app
    def app(self,page='Learn & Practice'):
        app=AppTest.from_file(str(ROOT/'app.py'))
        for k,v in {'nav_section':'Learning','nav_page':page,'last_selected_course':'Data Visualisation','lp_selected_course':'FI1BBDV75 - Data Visualisation','tc_course_filter':'FI1BBDV75 - Data Visualisation','dvs_lesson_module':5}.items():app.session_state[k]=v
        return self.run_app(app)
    def test_reviewed_requirements_and_no_assessment_question_bank(self):
        lessons=[l for l in get_dvs_course_lessons() if l['module_number']==5]
        self.assertEqual(len(lessons),1);self.assertEqual(len(module.STEPS),7)
        for fact in ['48 hours','80 marks','32 marks','18 October 2026','Section A','Section B','internal to this app']:
            self.assertIn(fact,lessons[0]['content'])
        self.assertTrue((ROOT/'assets/dvs'/module.ILLUSTRATIONS[0]['file']).is_file())
        self.assertEqual((TEMPLATE_ROOT/'DVS Course Assessment Preparation.md').read_text(),module.get_template())
        self.assertEqual(len(DVS_TASK_GUIDES),43)
        training=get_dvs_training_modules()['DVS Module 5: Course Assessment Preparation']
        self.assertEqual(len(training['lessons']),1)
        self.assertEqual(len(training['exercises']),1)
        self.assertEqual(len(training['quiz']),3)
        self.assertTrue(all('original Study Buddy question' in q['question'] for q in training['quiz']))
        from dvs_quiz_bank import get_curated_questions
        self.assertEqual(len(get_curated_questions()),39)
    def test_prepare_notes_download_and_current_step_in_normal_and_strict_ai(self):
        requests=[]
        def complete(**kw):
            requests.append(kw);return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English preparation review.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-test','AI_PROVIDER':'openai'};env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app()
            self.assertEqual(len([e for e in app.expander if e.label.startswith('📚 Lesson')]),1)
            next(t for t in app.text_area if t.label=='Your assessment preparation notes').set_value('I still need to reopen my practice image export.')
            next(s for s in app.selectbox if s.label=='Choose a preparation step').set_value(2);self.run_app(app)
            next(b for b in app.button if b.label=='Prepare assessment study plan in Exam Resolver').click();self.run_app(app)
            prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
            self.assertIn('DVS Activity 5.1:',prompt)
            self.assertIn('I still need to reopen my practice image export.',prompt)
            self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],['Resolver task 5.1: '+module.GUIDE['title']])
            step=next(s for s in app.selectbox if s.label=='Choose a preparation step' and s.key.startswith('course_exam_connector'))
            self.assertEqual(step.value,2)
            self.assertEqual(len(requests),0)
            labels=[d.label for d in app.get('download_button')]
            self.assertIn('Download assessment preparation template (Markdown)',labels)
            self.assertIn('Download my preparation notes (Markdown)',labels)
            step.set_value(5);self.run_app(app)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click();self.run_app(app)
            next(c for c in app.checkbox if c.label=='📚 Strict curriculum mode (use ONLY the syllabus)').set_value(True);self.run_app(app)
            next(b for b in app.button if b.label=='🔁 Re-generate answer').click();self.run_app(app)
            self.assertEqual(len(requests),2)
            for request in requests:
                text=request['messages'][1]['content']
                for term in ['Current selected step: 6. Diagnose gaps','I still need to reopen my practice image export.','Preparation only','48 hours','18 October 2026']:
                    self.assertIn(term,text)
                self.assertNotIn('### DVS Task 4.4:',text)
                self.assertIn('ANSWER LANGUAGE: Write in English',request['messages'][0]['content'])
            self.assertIn('STRICT CURRICULUM MODE',requests[1]['messages'][1]['content'])
            next(s for s in app.selectbox if s.label=='Choose a preparation step' and s.key.startswith('course_exam_connector')).set_value(6);self.run_app(app)
            self.assertTrue(any('earlier question or dataset' in i.value for i in app.info))
            self.assertEqual(len(requests),2)
    def test_training_preparation_is_available(self):
        app=self.app('Training Center')
        next(s for s in app.selectbox if s.label=='🎯 Select Topic:').set_value('DVS Module 5: Course Assessment Preparation');self.run_app(app)
        self.assertIn('Prepare assessment study plan in Exam Resolver',[b.label for b in app.button])
        self.assertIn('Download assessment preparation template (Markdown)',[d.label for d in app.get('download_button')])

if __name__=='__main__':unittest.main()
