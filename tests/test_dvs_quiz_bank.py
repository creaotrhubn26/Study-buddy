"""Reviewed quiz coverage, corrected traps, practice feedback and resolver handoff."""
from pathlib import Path
import os, sys, tempfile, unittest, json
from collections import Counter
from types import SimpleNamespace
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
import dvs_quiz_bank as bank

class QuizBankTest(unittest.TestCase):
    def setUp(self):
        self.old=Path.cwd(); self.temp=tempfile.TemporaryDirectory(); os.chdir(self.temp.name)
    def tearDown(self):
        os.chdir(self.old); self.temp.cleanup()
    def run_app(self,app):
        app.run(timeout=90)
        self.assertFalse(app.exception,[e.message for e in app.exception]); return app
    def app(self,page='Learn & Practice'):
        app=AppTest.from_file(str(ROOT/'app.py'))
        for k,v in {'nav_section':'Assessment' if page=='Exam Simulator' else 'Learning','nav_page':page,'last_selected_course':'Data Visualisation','lp_selected_course':'FI1BBDV75 - Data Visualisation'}.items():app.session_state[k]=v
        return self.run_app(app)
    def test_coverage_and_official_corrections(self):
        qs=bank.get_questions()
        self.assertEqual(Counter(q['module'] for q in qs),{1:10,2:9,3:10,4:10})
        self.assertEqual(sum(len(q['source_positions']) for q in qs),40)
        self.assertEqual(len({q['id'] for q in qs}),39)
        byid={q['id']:q for q in qs}
        self.assertEqual(byid['dvs-m2-q04']['source_positions'],[4,9])
        for uid,correct in [('dvs-m1-q01','False'),('dvs-m1-q04','False'),('dvs-m3-q09','True'),('dvs-m3-q10','True'),('dvs-m4-q03','True')]:
            self.assertEqual(byid[uid]['options'][byid[uid]['correct']],correct)
        self.assertIn('not weak fidelity',byid['dvs-m1-q04']['explanation'])
        self.assertIn('unequal-width',byid['dvs-m3-q10']['explanation'])
        self.assertIn('also tell a good linear story',byid['dvs-m4-q03']['example'])
        for q in qs:
            self.assertTrue((bank.ASSETS/q['illustration']).is_file())
            self.assertTrue(q['explanation'] and q['example'])
            self.assertNotIn('attempt=',json.dumps(q))
        self.assertEqual(len(bank.get_curated_questions()),39)
    def test_practice_feedback_and_module_switching(self):
        app=self.app()
        self.assertIn('Module Quiz Bank',[t.label for t in app.tabs])
        app.button(key='dvs_bank_dvs-m1-q01_check').click(); self.run_app(app)
        self.assertIn('Choose an answer before checking.',[w.value for w in app.warning])
        app.radio(key='dvs_bank_dvs-m1-q01_answer').set_value('True'); self.run_app(app)
        app.button(key='dvs_bank_dvs-m1-q01_check').click(); self.run_app(app)
        self.assertTrue(any('Your checked answer was True' in w.value for w in app.warning))
        self.assertTrue(any('Colour should not' in m.value for m in app.markdown))
        app.radio(key='dvs_bank_dvs-m1-q01_answer').set_value('False'); self.run_app(app)
        app.button(key='dvs_bank_dvs-m1-q01_check').click(); self.run_app(app)
        self.assertTrue(any(s.value.startswith('Correct —') for s in app.success))
        for m in [2,3,4]:
            app.selectbox(key='dvs_bank_module').set_value(m); self.run_app(app)
            self.assertEqual(len(app.selectbox(key=f'dvs_bank_question_{m}').options),9 if m==2 else 10)
        app.selectbox(key='dvs_bank_module').set_value(None); self.run_app(app)
        self.assertEqual(app.session_state['dvs_bank_dvs-m1-q01_checked'],'False')
        self.assertEqual(app.radio(key='dvs_bank_dvs-m1-q01_answer').value,'False')
        self.assertIn('Download quiz revision notes with answers (English)',[d.label for d in app.get('download_button')])
    def test_handoff_and_stale_reference(self):
        app=self.app(); app.selectbox(key='dvs_bank_module').set_value(3); self.run_app(app)
        app.selectbox(key='dvs_bank_question_3').set_value('dvs-m3-q09'); self.run_app(app)
        app.button(key='dvs_bank_dvs-m3-q09_resolver').click(); self.run_app(app)
        prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt')
        self.assertIn('[DVS Module 3 / dvs-m3-q09]',prompt.value)
        self.assertIn('Quiz reference: answer, reasoning and illustration',[e.label for e in app.expander])
        self.assertFalse([e for e in app.expander if e.label.startswith('Resolver task')])
        prompt.set_value('Task 2.4: Plan three image designs.'); self.run_app(app)
        self.assertNotIn('Quiz reference: answer, reasoning and illustration',[e.label for e in app.expander])
        self.assertNotIn('resolver_answer_history',app.session_state)
    def test_curated_exam_without_ai(self):
        app=self.app('Exam Simulator')
        next(s for s in app.selectbox if s.label=='Select Course:').set_value('FI1BBDV75'); self.run_app(app)
        next(s for s in app.selectbox if s.label=='Curated Bank').set_value('DVS Module 2 quiz review'); self.run_app(app)
        next(b for b in app.button if b.label=='🚀 Start Exam').click(); self.run_app(app)
        qs=app.session_state['exam_questions']
        self.assertEqual(len(qs),9)
        self.assertEqual(len({q['question'] for q in qs}),9)
        self.assertTrue(all(any(q['question'].startswith(source['question']) for source in bank.get_curated_questions() if source['module']==2) for q in qs))
        self.assertTrue(all('ANSWER:' in q['question'] for q in qs))
    def test_english_verified_context_normal_and_strict(self):
        requests=[]
        def complete(**kwargs):
            requests.append(kwargs)
            return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English quiz explanation.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-test','AI_PROVIDER':'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app(); app.selectbox(key='dvs_bank_question_None').set_value('dvs-m1-q04'); self.run_app(app)
            app.button(key='dvs_bank_dvs-m1-q04_resolver').click(); self.run_app(app)
            self.assertEqual(len(requests),0)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click(); self.run_app(app)
            next(c for c in app.checkbox if c.label=='📚 Strict curriculum mode (use ONLY the syllabus)').set_value(True); self.run_app(app)
            next(b for b in app.button if b.label=='🔁 Re-generate answer').click(); self.run_app(app)
            self.assertEqual(len(requests),2)
            for r in requests:
                self.assertIn('LOW fidelity, not weak fidelity',r['messages'][1]['content'])
                self.assertIn('Correct answer: False',r['messages'][1]['content'])
                self.assertIn('ANSWER LANGUAGE: Write in English',r['messages'][0]['content'])
            self.assertIn('also supplied course material',requests[1]['messages'][0]['content'])

if __name__=='__main__':unittest.main()
