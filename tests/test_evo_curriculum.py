"""Exercise the EVO learning, resolver and Training Center workflows offline."""

import os
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evo_curriculum import ASSET_ROOT, COURSE_CODE, EVO_LESSONS, get_evo_training_modules
from evo_tasks import TASK_GUIDES, TEMPLATE_FILES, TEMPLATE_ROOT, get_evo_task_guides, resolver_task_number_boost, get_evo_resolver_ai_units
from streamlit.testing.v1 import AppTest


def select(app, label, value):
    widget = next(widget for widget in app.selectbox if widget.label == label)
    widget.set_value(value)
    app.run(timeout=90)
    if app.exception:
        raise AssertionError([error.message for error in app.exception])


class EvoWorkflowTest(unittest.TestCase):
    def setUp(self):
        # App persistence must never overwrite a user's saved study progress.
        self.previous_directory = Path.cwd()
        self.scratch = tempfile.TemporaryDirectory()
        os.chdir(self.scratch.name)

    def tearDown(self):
        os.chdir(self.previous_directory)
        self.scratch.cleanup()

    def app(self, page):
        app = AppTest.from_file(str(ROOT / "app.py"))
        app.session_state["nav_section"] = "Learning"
        app.session_state["nav_page"] = page
        app.session_state["last_selected_course"] = "Evaluation of Outcomes"
        app.session_state["lp_selected_course"] = f"{COURSE_CODE} - Evaluation of Outcomes"
        app.session_state["tc_course_filter"] = f"{COURSE_CODE} - Evaluation of Outcomes"
        app.run(timeout=90)
        self.assertFalse(app.exception, [error.message for error in app.exception])
        return app

    def test_default_dashboard_starts_without_saved_progress(self):
        app = AppTest.from_file(str(ROOT / "app.py")).run(timeout=90)
        self.assertFalse(app.exception, [error.message for error in app.exception])
        self.assertTrue(any(item.value == "📌 Today" for item in app.subheader))

    def test_learn_and_practice_renders_all_official_lesson_numbers(self):
        app = self.app("Learn & Practice")
        labels = [item.label for item in app.expander if item.label.startswith("📚 Lesson")]
        expected = [f"{module}.{lesson}" for module in range(1, 8) for lesson in range(1, 5)]
        actual = [label.split("Lesson ")[1].split(":")[0] for label in labels]
        self.assertEqual(actual, expected)
        markdown = "\n".join(item.value for item in app.markdown)
        self.assertIn("Splendor Hotel Groups", markdown)
        self.assertIn("Superstore", markdown)
        self.assertIn("Privacy", markdown)
        self.assertTrue(all(f"chapterid={lesson['source_url'].split('chapterid=')[1]}" in markdown for lesson in EVO_LESSONS))

    def test_resolver_can_focus_on_every_evo_lesson(self):
        app = self.app("Learn & Practice")
        select(app, "Source pool", "Lessons only")
        select(app, "Resolver scope", "Specific lesson or outcome")
        chooser = next(item for item in app.selectbox if item.label == "Choose the lesson or outcome to focus on")
        self.assertEqual(len(chooser.options), 28)
        final_lesson = next(option for option in chooser.options if option.startswith("Lesson 7.4:"))
        select(app, chooser.label, final_lesson)
        markdown = "\n".join(item.value for item in app.markdown)
        self.assertIn("Avg Daily Rate", markdown)
        self.assertFalse(app.exception)

    def test_seven_training_modules_preserve_legacy_topics_and_progress(self):
        app = self.app("Training Center")
        chooser = next(item for item in app.selectbox if item.label == "🎯 Select Topic:")
        canonical = [option for option in chooser.options if option.startswith("EVO Module ")]
        self.assertEqual(len(canonical), 7)
        self.assertIn("Statistical Result Analysis", chooser.options)
        self.assertIn("ETL & Version Control", chooser.options)
        for name, module in get_evo_training_modules().items():
            with self.subTest(module=name):
                select(app, "🎯 Select Topic:", name)
                self.assertEqual(len([item for item in app.expander if item.label.startswith("Lesson ")]), 4)
                self.assertEqual(len([item for item in app.expander if item.label.startswith("Exercise ")]), 4)
                self.assertEqual(len([item for item in app.radio if item.label == "Select your answer:"]), 4)
        final_name = canonical[-1]
        select(app, "🎯 Select Topic:", final_name)
        final_module = get_evo_training_modules()[final_name]
        for index, question in enumerate(final_module["quiz"]):
            app.radio(key=f"quiz_{final_name}_{index}").set_value(question["options"][question["correct"]])
        next(button for button in app.button if button.label == "Submit Quiz").click()
        app.run(timeout=90)
        self.assertFalse(app.exception)
        self.assertEqual(app.session_state["training_progress"][final_name]["quiz_score"], 4)

    def test_illustrations_are_bundled_and_downloadable(self):
        illustrated = [lesson for lesson in EVO_LESSONS if lesson["illustration"]]
        self.assertEqual(len(illustrated), 7)
        for lesson in illustrated:
            self.assertTrue((ASSET_ROOT / lesson["illustration"]).is_file(), lesson["illustration"])
        app = self.app("Learn & Practice")
        downloads = [item for item in app.get("download_button") if item.label == "Download illustration (PNG)"]
        self.assertEqual(len(downloads), 7)
        self.assertFalse(app.exception)

    def test_every_activity_has_a_lesson_guide_and_duplicate_ids_are_distinct(self):
        self.assertEqual(len(TASK_GUIDES), 98)
        self.assertEqual(len({g['uid'] for g in TASK_GUIDES}), 98)
        duplicate = [g for g in TASK_GUIDES if g['id'] == '5.3.2']
        self.assertEqual(len(duplicate), 2)
        self.assertEqual({g['method'] for g in duplicate}, {'version', 'powerbi'})
        for lesson in EVO_LESSONS:
            guides = get_evo_task_guides(lesson['lesson_number'])
            self.assertTrue(guides)
            self.assertTrue(any(g['id'].endswith('-task') for g in guides))
            for guide in guides:
                self.assertEqual(len(guide['steps']), 3)
                self.assertIn('Fyll-inn-mal', guide['markdown'])
                self.assertIn('chapterid=', guide['source_url'])

    def test_task_picker_loads_correct_dataset_and_downloads(self):
        app = self.app('Learn & Practice')
        selects = [s for s in app.selectbox if s.label.startswith('Velg aktivitet eller task')]
        self.assertEqual(len(selects), 28)
        select(app, 'Velg aktivitet eller task i 7.2', '7.2-task-81485')
        markdown = '\n'.join(item.value for item in app.markdown)
        self.assertIn('Z_Revenue er konstant', markdown)
        self.assertIn('Korrelasjonen er udefinert', markdown)
        self.assertIn('Excel CORREL gir #DIV/0!', markdown)
        self.assertIn('valutaenheter dersom metadata', markdown)
        self.assertIn('Task-datasettet er online kundesalg', markdown)
        self.assertEqual(len([d for d in app.get('download_button') if d.label == 'Last ned tilhørende Excel-mal']), 28)
        for filename in TEMPLATE_FILES.values():
            self.assertTrue((TEMPLATE_ROOT / filename).is_file())

    def test_task_workbooks_keep_raw_prepared_and_objective_sheets(self):
        import zipfile
        import xml.etree.ElementTree as ET
        ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        for module, count in [('6', 17), ('7', 21)]:
            with zipfile.ZipFile(TEMPLATE_ROOT / TEMPLATE_FILES[module]) as z:
                root = ET.fromstring(z.read('xl/workbook.xml'))
                names = [e.attrib['name'] for e in root.findall('x:sheets/x:sheet', ns)]
                self.assertEqual(len(names), count)
                self.assertTrue({'Raw', 'Prepared', 'Cleaning log', 'Checks', 'Conclusion 4'} <= set(names))
                self.assertTrue(any(p.startswith('xl/tables/') for p in z.namelist()))
                for p in z.namelist():
                    if p.startswith('xl/worksheets/sheet') and p.endswith('.xml'):
                        xml = ET.fromstring(z.read(p))
                        self.assertFalse(xml.findall('.//x:c[@t="e"]', ns), p)

    def test_resolver_selects_exact_task_with_its_guide_and_workbook(self):
        app = self.app('Learn & Practice')
        select(app, 'Source pool', 'Task guides only')
        select(app, 'Resolver scope', 'Specific lesson or outcome')
        chooser = next(s for s in app.selectbox if s.label == 'Choose the task guide to focus on')
        self.assertEqual(len(chooser.options), 98)
        target = next(o for o in chooser.options if o.startswith('Task guide 7.2-task:'))
        select(app, chooser.label, target)
        markdown = '\n'.join(item.value for item in app.markdown)
        self.assertIn('2. Task guide and workbook', markdown)
        self.assertIn('Z_Revenue er konstant', markdown)
        downloads = [d.label for d in app.get('download_button')]
        self.assertIn('Download matched workbook: EVO Module 7 Tasks.xlsx', downloads)
        self.assertNotIn('Download matched workbook: EVO Module 6 Tasks.xlsx', downloads)
        self.assertEqual(len([d for d in downloads if d == 'Download matched module illustration']), 1)

    def test_resolver_auto_matching_and_task_number_boundaries(self):
        target = next(g for g in TASK_GUIDES if g['id'] == '7.2-task')
        self.assertEqual(resolver_task_number_boost(target, 'Task 7.2'), 500)
        self.assertEqual(resolver_task_number_boost(target, '7.2-task: spending'), 500)
        self.assertEqual(resolver_task_number_boost(target, 'Task 7.2.1 Airbnb'), 0)
        self.assertEqual(resolver_task_number_boost(target, 'Task 17.2'), 0)
        app = self.app('Learn & Practice')
        prompt = next(t for t in app.text_area if t.label == 'Paste the exam question, case, or task prompt')
        prompt.set_value('Task 7.2: analyse MntGoldProds and Z_Revenue in marketing_campaign_fixed.csv, explain profitability limitations.')
        app.run(timeout=90)
        self.assertFalse(app.exception)
        labels = [e.label for e in app.expander if e.label.startswith('Resolver task')]
        self.assertTrue(labels)
        self.assertTrue(labels[0].startswith('Resolver task 7.2-task:'), labels)
        self.assertEqual(len(labels), 1)
        downloads = [d.label for d in app.get('download_button')]
        self.assertNotIn('Download matched workbook: EVO Module 6 Tasks.xlsx', downloads)
        self.assertNotIn('Download matched workbook: EVO Calculation Templates.xlsx', downloads)
        draft = next(t for t in app.text_area if t.label == 'Use this as a starting answer, then adapt it to the exact wording of the question')
        self.assertNotIn('SHG', draft.value)

    def test_ai_context_respects_selected_task_and_includes_parent_lesson(self):
        guide = next(g for g in TASK_GUIDES if g['id'] == '7.2-task')
        units = [
            {'id': 'lesson::7.2', 'label': 'Lesson 7.2', 'kind': 'Lesson'},
            {'id': 'lesson::6.2', 'label': 'Lesson 6.2', 'kind': 'Lesson'},
            {'id': 'task::7.2', 'label': 'Marketing task', 'kind': 'Task', 'task_guide': guide},
            {'id': 'skill::1', 'label': 'Skill 1', 'kind': 'Skill'},
        ]
        context = get_evo_resolver_ai_units(units, 'Task guides only', 'Specific lesson or outcome', 'Marketing task')
        self.assertEqual([u['id'] for u in context], ['task::7.2', 'lesson::7.2'])

        context = get_evo_resolver_ai_units(units, 'Lessons + task guides', 'Whole course (auto-select best matches)', prompt='Task 7.2')
        self.assertEqual([u['id'] for u in context], ['task::7.2', 'lesson::7.2'])
        self.assertEqual(guide['task_dataset'], 'marketing_campaign_fixed.csv')
        context = get_evo_resolver_ai_units(units, 'Lessons only', 'Whole course (auto-select best matches)')
        self.assertEqual([u['id'] for u in context], ['lesson::7.2', 'lesson::6.2'])
        context = get_evo_resolver_ai_units(units, 'Lessons + task guides', 'Manual selection', manual=['Marketing task'])
        self.assertEqual([u['id'] for u in context], ['task::7.2', 'lesson::7.2'])

    def test_task_72_objectives_show_the_actual_workbook_and_preserve_the_prompt(self):
        app = self.app('Learn & Practice')
        prompt = next(t for t in app.text_area if t.label == 'Paste the exam question, case, or task prompt')
        prompt.set_value('Task 7.2: help me analyse the marketing dataset.')
        app.run(timeout=90)
        chooser = next(s for s in app.selectbox if s.label == 'Choose a Task 7.2 objective')
        from exam_resolver_ui import TASK_72_OBJECTIVES
        self.assertEqual(chooser.options, [v[0] for v in TASK_72_OBJECTIVES.values()])
        for sheet, objective in TASK_72_OBJECTIVES.items():
            select(app, chooser.label, sheet)
            markdown = '\n'.join(item.value for item in app.markdown)
            self.assertIn(f'Excel worksheet `{sheet}`', markdown)
            self.assertIn(objective[2], markdown)
            self.assertIn(objective[4], '\n'.join(item.value for item in app.info))
            self.assertEqual(next(t for t in app.text_area if t.label == prompt.label).value, prompt.value)

    def test_empty_question_does_not_show_irrelevant_drafts_and_changed_question_refreshes_scaffold(self):
        app = self.app('Learn & Practice')
        self.assertFalse(any(t.label == 'Adapt this guide into your own exam wording' for t in app.text_area))
        prompt = next(t for t in app.text_area if t.label == 'Paste the exam question, case, or task prompt')
        prompt.set_value('Task 6.2: online shop customer sales.')
        app.run(timeout=90)
        prompt = next(t for t in app.text_area if t.label == prompt.label)
        prompt.set_value('Task 7.2: marketing product spend and Z_Revenue.')
        app.run(timeout=90)
        draft = next(t for t in app.text_area if t.label == 'Adapt this guide into your own exam wording')
        self.assertIn('Task guide 7.2-task:', draft.value)
        self.assertNotIn('Task guide 6.2-task:', draft.value)
        draft.set_value('My edited answer for this question')
        app.run(timeout=90)
        select(app, 'Choose a Task 7.2 objective', 'Retention')
        self.assertEqual(next(t for t in app.text_area if t.label == draft.label).value, 'My edited answer for this question')

    def test_task_73_objectives_keep_the_right_workbook_and_independent_selections(self):
        from exam_resolver_ui import TASK_72_OBJECTIVES, TASK_73_OBJECTIVES
        app = self.app('Learn & Practice')
        prompt_label = 'Paste the exam question, case, or task prompt'
        next(t for t in app.text_area if t.label == prompt_label).set_value('Task 7.2: analyse the marketing dataset.')
        app.run(timeout=90)
        select(app, 'Choose a Task 7.2 objective', 'Retention')
        next(t for t in app.text_area if t.label == prompt_label).set_value('Task 7.3: guide me through the seven marketing objectives.')
        app.run(timeout=90)
        self.assertFalse(app.exception)
        chooser = next(s for s in app.selectbox if s.label == 'Choose a Task 7.3 objective')
        self.assertEqual(chooser.options, [v[0] for v in TASK_73_OBJECTIVES.values()])
        self.assertEqual(len(chooser.options), 7)
        for sheet, objective in TASK_73_OBJECTIVES.items():
            with self.subTest(sheet=sheet):
                select(app, chooser.label, sheet)
                markdown = '\n'.join(item.value for item in app.markdown)
                self.assertIn(f'Excel worksheet `{sheet}`', markdown)
                self.assertIn(objective[2], markdown)
                self.assertIn(objective[4], '\n'.join(item.value for item in app.info))
                self.assertIn('Dataset: marketing_campaign_fixed.csv', '\n'.join(c.value for c in app.caption))
                downloads = [d.label for d in app.get('download_button')]
                self.assertIn('Download matched workbook: EVO Module 7 Tasks.xlsx', downloads)
                self.assertNotIn('Download matched workbook: EVO Module 6 Tasks.xlsx', downloads)
                self.assertEqual(next(t for t in app.text_area if t.label == prompt_label).value, 'Task 7.3: guide me through the seven marketing objectives.')
        next(t for t in app.text_area if t.label == prompt_label).set_value('Task 7.2: analyse the marketing dataset.')
        app.run(timeout=90)
        chooser72 = next(s for s in app.selectbox if s.label == 'Choose a Task 7.2 objective')
        self.assertIn(chooser72.value, TASK_72_OBJECTIVES)
        self.assertEqual(chooser72.options, [v[0] for v in TASK_72_OBJECTIVES.values()])
        select(app, chooser72.label, 'Retention')
        self.assertIn('Excel worksheet `Retention`', '\n'.join(m.value for m in app.markdown))

    def test_task_73_english_download_covers_all_real_workbook_sheets(self):
        import zipfile
        import xml.etree.ElementTree as ET
        from exam_resolver_ui import TASK_73_OBJECTIVES, get_resolver_task_guide_markdown
        guide = next(g for g in TASK_GUIDES if g['id'] == '7.3-task')
        text = get_resolver_task_guide_markdown(guide)
        self.assertIn('### Task 7.3: Customer insight, segmentation and campaign response', text)
        self.assertIn('chapterid=81490', text)
        self.assertIn('marketing_campaign_fixed.csv', text)
        self.assertIn('not solved data', text)
        self.assertEqual(text.count('\n#### '), 7)
        with zipfile.ZipFile(TEMPLATE_ROOT / guide['template_file']) as archive:
            root = ET.fromstring(archive.read('xl/workbook.xml'))
            ns = {'x': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            names = {e.attrib['name'] for e in root.findall('x:sheets/x:sheet', ns)}
        for sheet, objective in TASK_73_OBJECTIVES.items():
            self.assertIn(sheet, names)
            self.assertIn(objective[1], text)
            self.assertIn(objective[4], text)
        other = next(g for g in TASK_GUIDES if g['id'] == '6.2-task')
        self.assertEqual(get_resolver_task_guide_markdown(other), other['markdown'])

    def test_task_73_ai_request_uses_the_same_english_worksheet_guide(self):
        import json
        from types import SimpleNamespace
        from unittest.mock import patch
        requests = []

        def complete(**kwargs):
            requests.append(kwargs)
            chunk = SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content='English answer from an offline test.'))])
            return iter([chunk])

        fake_client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=complete)))
        env = {'OPENAI_API_KEY': 'offline-ui-test-key', 'AI_PROVIDER': 'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS'] = json.dumps(list(os.environ) + list(env))
        with patch.dict(os.environ, env), patch('openai.OpenAI', return_value=fake_client):
            app = self.app('Learn & Practice')
            next(t for t in app.text_area if t.label == 'Paste the exam question, case, or task prompt').set_value('Task 7.3: Explain the complaints objective.')
            app.run(timeout=90)
            next(b for b in app.button if b.label == '💡 Generate answer with reasoning').click()
            app.run(timeout=90)
            self.assertFalse(app.exception)
            self.assertEqual(len(requests), 1)
            messages = requests[0]['messages']
            self.assertIn('ANSWER LANGUAGE: Write in English', messages[0]['content'])
            self.assertIn('### Task 7.3: Customer insight, segmentation and campaign response', messages[1]['content'])
            self.assertIn('**Worksheets:** Complaints, Personas, Response spending, Detailed segments, Household channels, Web engagement, Response prediction', messages[1]['content'])
            self.assertIn('Customer satisfaction and complaints', messages[1]['content'])
            self.assertNotIn('### Task 7.2:', messages[1]['content'])

    def test_cloud_update_refreshes_a_cached_helper_missing_the_new_guide_api(self):
        import importlib
        import exam_resolver_ui
        # Reproduce a long-running Streamlit worker still holding the old
        # helper while the updated app starts importing its new guide API.
        del exam_resolver_ui.get_resolver_task_guide_markdown
        try:
            app = self.app('Learn & Practice')
            self.assertTrue(callable(exam_resolver_ui.get_resolver_task_guide_markdown))
            next(t for t in app.text_area if t.label == 'Paste the exam question, case, or task prompt').set_value('Task 7.3: explain complaints.')
            app.run(timeout=90)
            self.assertFalse(app.exception)
            chooser = next(s for s in app.selectbox if s.label == 'Choose a Task 7.3 objective')
            self.assertEqual(len(chooser.options), 7)
        finally:
            importlib.reload(exam_resolver_ui)

    def test_stale_ai_answer_is_separated_from_current_question(self):
        from unittest.mock import patch
        import json
        env = {'OPENAI_API_KEY': 'offline-ui-test-key', 'AI_PROVIDER': 'openai'}
        env['_STUDY_BUDDY_INITIAL_ENV_KEYS'] = json.dumps(list(os.environ) + list(env))
        with patch.dict(os.environ, env):
            app = self.app('Learn & Practice')
            base = 'course_exam_connector_fi1bbeo10_learn_practice'
            app.session_state[f'{base}_prompt'] = 'Task 7.2: explain Z_Revenue.'
            app.session_state[f'{base}_ai_answer'] = 'A cached answer to Task 6.2.'
            app.session_state[f'{base}_ai_answer_signature'] = 'older-question'
            app.run(timeout=90)
            self.assertFalse(app.exception)
            self.assertTrue(any('earlier question or dataset' in item.value for item in app.info))
            previous = next(e for e in app.expander if e.label == 'Previous AI answer')
            self.assertFalse(previous.proto.expanded)
            headings = [m.value for m in app.markdown if m.value in {'### 1. Question and data', '### 2. Task guide and workbook', '### 3. Answer and reasoning'}]
            self.assertEqual(headings[:3], ['### 1. Question and data', '### 2. Task guide and workbook', '### 3. Answer and reasoning'])

    def test_general_statistics_resolver_keeps_verified_calculations_available(self):
        app = self.app('Learn & Practice')
        select(app, 'Select a course to study:', 'FI1BBST05 - Statistical Tools')
        prompt = next(t for t in app.text_area if t.label == 'Paste the exam question, case, or task prompt')
        prompt.set_value('An independent t-test compares two groups. Group A has mean 72, standard deviation 10, and sample size 35. Group B has mean 78, standard deviation 11, and sample size 37. Use alpha 0.05.')
        app.run(timeout=90)
        self.assertFalse(app.exception)
        summary = next(t for t in app.text_area if t.label == 'Verified stats / hypothesis summary to use in your answer')
        self.assertIn('mean A = 72.000', summary.value)
        self.assertIn('mean B = 78.000', summary.value)
        markdown = '\n'.join(item.value for item in app.markdown)
        self.assertIn('2. Sources for this question', markdown)



if __name__ == "__main__":
    unittest.main()
