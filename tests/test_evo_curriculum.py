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
        self.assertIn('Matched EVO task guides and exam resources', markdown)
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


if __name__ == "__main__":
    unittest.main()
