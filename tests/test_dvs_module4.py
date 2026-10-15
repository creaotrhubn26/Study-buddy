"""Verify Module 4 source rules, resources and English resolver handoffs."""
from pathlib import Path
import os,sys,tempfile,unittest,json,hashlib,csv,zipfile,collections,posixpath
import xml.etree.ElementTree as ET
from fractions import Fraction
from types import SimpleNamespace
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from streamlit.testing.v1 import AppTest
import dvs_module4 as module
from dvs_curriculum import get_dvs_course_lessons,get_dvs_training_modules,DVS_TASK_GUIDES,TEMPLATE_ROOT,get_dvs_primary_task_prompt

class Module4Test(unittest.TestCase):
    def setUp(self):
        self.old=Path.cwd();self.temp=tempfile.TemporaryDirectory();os.chdir(self.temp.name)
    def tearDown(self):os.chdir(self.old);self.temp.cleanup()
    def run_app(self,app):
        app.run(timeout=90);self.assertFalse(app.exception,[e.message for e in app.exception]);return app
    def app(self,page='Learn & Practice'):
        app=AppTest.from_file(str(ROOT/'app.py'))
        for k,v in {'nav_section':'Learning','nav_page':page,'last_selected_course':'Data Visualisation','lp_selected_course':'FI1BBDV75 - Data Visualisation','tc_course_filter':'FI1BBDV75 - Data Visualisation','dvs_lesson_module':4}.items():app.session_state[k]=v
        return self.run_app(app)
    def test_source_files_task_rules_and_scaffolds(self):
        self.assertEqual(get_dvs_primary_task_prompt('DVS Task 4.3: continue Task 4.2'), 'DVS Task 4.3:')
        self.assertEqual(get_dvs_primary_task_prompt('DVS Activity 4.4.1: compare Task 4.4'), 'DVS Activity 4.4.1:')
        self.assertEqual(get_dvs_primary_task_prompt('Compare Task 4.2 and Task 4.3'), 'Compare Task 4.2 and Task 4.3')
        self.assertEqual(len(get_dvs_course_lessons()),17);self.assertEqual(len(DVS_TASK_GUIDES),43)
        lessons=[l for l in get_dvs_course_lessons() if l['module_number']==4]
        self.assertEqual([l['lesson_number'] for l in lessons],['4.1','4.2','4.3','4.4'])
        self.assertEqual(len(module.GUIDES),5)
        for l in lessons:self.assertTrue((module.ROOT/l['dvs_illustrations'][0]['file']).is_file())
        for g in module.GUIDES:
            self.assertEqual((TEMPLATE_ROOT/f"DVS-{g['id']}-working-template.md").read_text(),module.get_template(g))
            self.assertIn(g['title'],g['markdown'])
            if g['id'].endswith('-task'):self.assertEqual(len(g['step_details']),7)
        for source in module.DATASETS:
            data=(module.DATA_ROOT/source['file']).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(),source['sha256'])
            self.assertEqual(len(list(csv.DictReader(data.decode('utf-8-sig').splitlines()))),source['rows'])
        with (module.DATA_ROOT/module.DATASETS[0]['file']).open() as f:rows=list(csv.DictReader(f))
        for col,limit,inclusive,expected in [('Company (Manufacturer)','3.5',False,42),('Country of Bean Origin','3.25',False,13),('Cocoa Percent','3',True,30)]:
            groups=collections.defaultdict(list)
            for row in rows:groups[row[col]].append(Fraction(row['Rating']))
            means=[sum(v)/len(v) for v in groups.values()]
            count=sum((m>=Fraction(limit) if inclusive else m>Fraction(limit)) for m in means)
            self.assertEqual(count,expected)
        self.assertEqual(sum(collections.Counter(r['Review Date'] for r in rows).values()),2588)
        for n,name in module.PRESENTATION_TEMPLATES.items():
            with zipfile.ZipFile(TEMPLATE_ROOT/name) as z:
                slides=[f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
                self.assertEqual(len(slides),9 if n=='4.4-task' else 5)
                self.assertTrue(any(f.startswith('ppt/notesSlides/notesSlide') for f in z.namelist()))
                text=''.join(z.read(f).decode() for f in slides)
                self.assertIn('[',text)
                self.assertFalse(any('3d' in f.lower() for f in z.namelist()))
                if n!='4.4-task':self.assertIn('<a:tbl',z.read('ppt/slides/slide5.xml').decode())
                self.assertGreaterEqual(len([f for f in z.namelist() if f.startswith('ppt/media/')]),1 if n=='4.4-task' else 4)
                self.assertEqual(len([f for f in z.namelist() if '/charts/chart' in f and f.endswith('.xml')]),8 if n=='4.4-task' else 1)
                self.assertEqual(len([f for f in z.namelist() if f.startswith('ppt/embeddings/') and f.endswith('.xlsx')]),8 if n=='4.4-task' else 1)
        lesson=module.LESSON_TEXT['4.4']
        for expected in ['200,000','2,000','Review Transition','Value Field Settings','group averages','989','2,588','Distinct Count']:
            self.assertIn(expected,lesson)
    def test_native_chart_values_match_independent_csv_aggregates(self):
        with (module.DATA_ROOT/module.DATASETS[0]['file']).open() as f:rows=list(csv.DictReader(f))
        ns={'c':'http://schemas.openxmlformats.org/drawingml/2006/chart'}
        with zipfile.ZipFile(TEMPLATE_ROOT/module.PRESENTATION_TEMPLATES['4.4-task']) as z:
            for col,owners,limit,inclusive in [('Company (Manufacturer)',[2,7,8],Fraction('3.5'),False),('Country of Bean Origin',[3],Fraction('3.25'),False),('Cocoa Percent',[4,9],Fraction('3'),True),('Review Date',[5],None,True),('Review Date',[6],None,True)]:
                groups=collections.defaultdict(list)
                for row in rows:groups[row[col]].append(Fraction(row['Rating']))
                expected={k:(len(v) if owners==[6] else float(sum(v)/len(v))) for k,v in groups.items() if limit is None or (sum(v)/len(v)>=limit if inclusive else sum(v)/len(v)>limit)}
                actual={}
                for owner in owners:
                    rels=ET.fromstring(z.read(f'ppt/slides/_rels/slide{owner}.xml.rels'))
                    target=next(r.attrib['Target'] for r in rels if r.attrib['Type'].endswith('/chart'))
                    part=target.lstrip('/') if target.startswith('/') else posixpath.normpath('ppt/slides/'+target)
                    xml=ET.fromstring(z.read(part))
                    labels=[e.text for e in xml.findall('.//c:ser/c:cat//c:pt/c:v',ns)]
                    values=[float(e.text) for e in xml.findall('.//c:ser/c:val//c:pt/c:v',ns)]
                    for k,v in zip(labels,values):self.assertNotIn(k,actual);actual[k]=v
                self.assertEqual(set(actual),set(expected))
                for k,v in expected.items():self.assertAlmostEqual(actual[k],v,places=12)
    def test_module_filter_and_all_five_independent_handoffs(self):
        app=self.app()
        self.assertEqual(len([e for e in app.expander if e.label.startswith('📚 Lesson')]),4)
        self.assertEqual(next(s for s in app.selectbox if s.label=='Show lessons from').value,4)
        for g in module.GUIDES:
            number=g['lesson_number'];kind='Task '+number if g['id'].endswith('-task') else 'Activity '+g['id']
            next(s for s in app.selectbox if s.label==f'Choose a DVS Lesson {number} activity or task').set_value(g['uid']);self.run_app(app)
            draft=f'{kind}: this is my draft. The real output has not been reopened.'
            next(t for t in app.text_area if t.label==f'Your {kind} draft and evidence').set_value(draft)
            next(s for s in app.selectbox if s.label==f'Choose a {kind} step' and not s.key.startswith('course_exam_connector')).set_value(1);self.run_app(app)
            next(b for b in app.button if b.label==f'Prepare {kind} in Exam Resolver').click();self.run_app(app)
            prompt=next(t for t in app.text_area if t.label=='Paste the exam question, case, or task prompt').value
            self.assertIn('DVS '+kind+':',prompt);self.assertIn(draft,prompt);self.assertNotIn('Current selected step:',prompt)
            self.assertEqual([e.label for e in app.expander if e.label.startswith('Resolver task')],[f"Resolver task {g['id']}: {g['title']}"])
            self.assertEqual(next(s for s in app.selectbox if s.label==f'Choose a {kind} step' and s.key.startswith('course_exam_connector')).value,1)
            labels=[d.label for d in app.get('download_button')]
            self.assertIn(f'Download {kind} working template (Markdown)',labels)
            if g['task_dataset']:self.assertIn(f"Download {g['task_dataset']} (original source data)",labels)
            if g['template_file']:self.assertIn(f'Download {kind} presentation scaffold (PowerPoint)',labels)
        self.assertNotIn('resolver_answer_history',app.session_state)
    def test_english_normal_strict_and_current_step(self):
        requests=[]
        def complete(**kw):
            requests.append(kw);return iter([SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English presentation review.'))])])
        fake=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env={'OPENAI_API_KEY':'offline-test','AI_PROVIDER':'openai'};env['_STUDY_BUDDY_INITIAL_ENV_KEYS']=json.dumps(list(os.environ)+list(env))
        with patch.dict(os.environ,env),patch('openai.OpenAI',return_value=fake):
            app=self.app()
            next(t for t in app.text_area if t.label=='Your Task 4.4 draft and evidence').set_value('I have not confirmed Review Transition yet.');self.run_app(app)
            next(b for b in app.button if b.label=='Prepare Task 4.4 in Exam Resolver').click();self.run_app(app)
            self.assertEqual(len(requests),0)
            next(s for s in app.selectbox if s.label=='Choose a Task 4.4 step' and s.key.startswith('course_exam_connector')).set_value(5);self.run_app(app)
            next(b for b in app.button if b.label=='💡 Generate answer with reasoning').click();self.run_app(app)
            next(c for c in app.checkbox if c.label=='📚 Strict curriculum mode (use ONLY the syllabus)').set_value(True);self.run_app(app)
            next(b for b in app.button if b.label=='🔁 Re-generate answer').click();self.run_app(app)
            self.assertEqual(len(requests),2)
            for r in requests:
                ctx=r['messages'][1]['content']
                for term in ['Current selected step: 6. Define the three custom shows','I have not confirmed Review Transition yet','### DVS Task 4.4:','group averages','>3.5','>3.25','>=3.0','Wisp','Float In','Review Transition','1–6','5–6']:self.assertIn(term,ctx)
                self.assertNotIn('Current selected step: 1.',ctx);self.assertNotIn('### DVS Activity 4.4.1:',ctx)
                self.assertIn('ANSWER LANGUAGE: Write in English',r['messages'][0]['content'])
            self.assertIn('STRICT CURRICULUM MODE',requests[1]['messages'][1]['content'])
            next(s for s in app.selectbox if s.label=='Choose a Task 4.4 step' and s.key.startswith('course_exam_connector')).set_value(0);self.run_app(app)
            self.assertTrue(any('earlier question or dataset' in i.value for i in app.info))
            self.assertEqual(len(requests),2)
    def test_training_and_existing_quiz_registration(self):
        data=get_dvs_training_modules()['DVS Module 4: Presentation Tools']
        self.assertEqual(len(data['lessons']),4);self.assertEqual(len(data['exercises']),5);self.assertEqual(len(data['quiz']),10)
        app=self.app('Training Center')
        next(s for s in app.selectbox if s.label=='🎯 Select Topic:').set_value('DVS Module 4: Presentation Tools');self.run_app(app)
        self.assertIn('Prepare Task 4.3 in Exam Resolver',[b.label for b in app.button])
        self.assertIn('Download Task 4.4 presentation scaffold (PowerPoint)',[d.label for d in app.get('download_button')])

if __name__=='__main__':unittest.main()
