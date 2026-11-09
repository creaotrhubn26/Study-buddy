"""Check the dataset-choice workflow, blank layered guide and real Resolver integration."""

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from zipfile import ZipFile, ZIP_STORED
from xml.etree import ElementTree as ET
from io import BytesIO
import csv
import json
import os
import sys
import unittest
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import arp_curriculum as curriculum
import arp_lesson22
import arp_lesson23 as lesson
import arp_ui
import test_arp_lesson11 as helpers


class ARPLesson23Tests(unittest.TestCase):
    setUp = helpers.ARPLesson11Tests.setUp
    tearDown = helpers.ARPLesson11Tests.tearDown
    run_app = helpers.ARPLesson11Tests.run_app
    app = helpers.ARPLesson11Tests.app

    def test_brief_blank_templates_and_layered_guide(self):
        self.assertEqual(
            [g["lesson_number"] for g in curriculum.all_task_guides()],
            ["1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4"],
        )
        self.assertEqual(len(lesson.STEPS), 7)
        self.assertTrue(lesson.LESSON_URL.endswith("id=22937&chapterid=81728"))
        self.assertTrue(lesson.TASK_URL.endswith("id=22937&chapterid=81735"))
        for t in [
            "Kaggle",
            "MS Excel",
            "GIMP",
            ".xcf",
            ".jpg",
            "not a fixed requirement",
            "not a requirement to include all three",
            "No dataset",
            "not native editable GIMP text",
            "not tested on this machine",
            "no word count",
        ]:
            self.assertIn(t, lesson.BOUNDARY)
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / lesson.GUIDE["template_file"]).read_text(),
            lesson.QUESTION_TEMPLATE,
        )
        self.assertEqual(
            (
                lesson.TEMPLATE_ROOT / "ARP Task 2.3 Infographic Storyboard.md"
            ).read_text(),
            lesson.STORYBOARD_TEMPLATE,
        )
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / "ARP Task 2.3 Seven Step Guide.md").read_text(),
            lesson.guide_markdown(),
        )
        with (lesson.TEMPLATE_ROOT / "ARP Task 2.3 EDA Evidence Log.csv").open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 4)
        self.assertTrue(
            all(
                r["Status"] == "Not checked"
                and not r["Observed finding"]
                and not r["Actual formula or summary method"]
                and not r["Population or sample"]
                for r in rows
            )
        )
        with (lesson.TEMPLATE_ROOT / "ARP Task 2.3 Source Register.csv").open() as f:
            rows = list(csv.DictReader(f))
        self.assertTrue(
            all(
                r["Status"] == "Not checked"
                and not r["URL or original source"]
                and not r["My access date"]
                for r in rows
            )
        )
        with ZipFile(lesson.TEMPLATE_ROOT / "ARP Task 2.3 Infographic Layout.ora") as z:
            self.assertEqual(z.infolist()[0].filename, "mimetype")
            self.assertEqual(z.infolist()[0].compress_type, ZIP_STORED)
            self.assertEqual(z.read("mimetype"), b"image/openraster")
            root = ET.fromstring(z.read("stack.xml"))
            self.assertEqual((root.get("w"), root.get("h")), ("800", "1200"))
            layers = root.findall("stack/layer")
            self.assertEqual(len(layers), 6)
            composite = Image.new("RGBA", (800, 1200), (0, 0, 0, 0))
            for layer in reversed(layers):
                self.assertIn(layer.get("src"), z.namelist())
                image = Image.open(BytesIO(z.read(layer.get("src")))).convert("RGBA")
                self.assertEqual(image.size, (800, 1200))
                composite = Image.alpha_composite(composite, image)
            merged = Image.open(BytesIO(z.read("mergedimage.png"))).convert("RGBA")
            self.assertLessEqual(
                max(
                    x[1] for x in ImageChops.difference(composite, merged).getextrema()
                ),
                2,
            )
            thumb = Image.open(BytesIO(z.read("Thumbnails/thumbnail.png")))
            self.assertLessEqual(max(thumb.size), 256)
            self.assertEqual(
                (lesson.ASSET_ROOT / "task-2-3-layout-preview.png").read_bytes(),
                z.read("mergedimage.png"),
            )
        for visual in lesson.ILLUSTRATIONS:
            self.assertTrue(
                (lesson.ASSET_ROOT / visual["file"]).read_bytes().startswith(b"\x89PNG")
            )
        modules = curriculum.get_training_modules()
        self.assertEqual(
            [
                l["lesson_number"]
                for l in modules["ARP Module 1: Report Writing"]["lessons"]
            ],
            ["1.1", "1.2", "1.3", "1.4"],
        )
        self.assertEqual(
            [
                l["lesson_number"]
                for l in modules["ARP Module 2: Report-Generating Tools"]["lessons"]
            ],
            ["2.1", "2.2", "2.3", "2.4"],
        )
        self.assertEqual(
            [
                e["title"]
                for e in modules["ARP Module 2: Report-Generating Tools"]["exercises"]
            ],
            [
                "Task 2.1 Source reliability",
                "Task 2.2 Nice Ride report",
                "Task 2.3 EDA infographic",
                "Task 2.4 Team communication",
            ],
        )
        g = curriculum.get_task_guides("2.3")[0]
        g["steps"].clear()
        self.assertEqual(len(curriculum.get_task_guides("2.3")[0]["steps"]), 7)

    def test_handoff_regular_strict_ai_and_independent_draft_step(self):
        requests = []

        def complete(**kw):
            requests.append(kw)
            return iter(
                [
                    SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(
                                    content="Choose and document your dataset, then verify the Excel evidence before creating the GIMP infographic."
                                )
                            )
                        ]
                    )
                ]
            )

        fake = SimpleNamespace(
            chat=SimpleNamespace(completions=SimpleNamespace(create=complete))
        )
        env = {"OPENAI_API_KEY": "offline-test", "AI_PROVIDER": "openai"}
        env["_STUDY_BUDDY_INITIAL_ENV_KEYS"] = json.dumps(list(os.environ) + list(env))
        with patch.dict(os.environ, env), patch("openai.OpenAI", return_value=fake):
            app = self.app()
            self.assertIn(
                "📚 Lesson 2.3: Generating Infographics",
                [e.label for e in app.expander],
            )
            note = "I have not selected a Kaggle dataset or performed EDA yet. My plan is to record the licence, import into Excel and create GIMP text layers after checking the layout."
            next(
                t
                for t in app.text_area
                if t.label == "Your infographic plan, EDA evidence and file checks"
            ).set_value(note)
            next(
                s for s in app.selectbox if s.label == "Choose a Task 2.3 step"
            ).set_value(4)
            self.run_app(app)
            self.assertEqual(
                arp_ui.draft(app.session_state, arp_lesson22.GUIDE),
                arp_lesson22.QUESTION_TEMPLATE,
            )
            next(
                b for b in app.button if b.label == "Prepare Task 2.3 in Exam Resolver"
            ).click()
            self.run_app(app)
            self.assertEqual(requests, [])
            self.assertTrue(
                any(
                    "Auto-detected question style:** EDA infographic design and GIMP export"
                    in m.value
                    for m in app.markdown
                )
            )
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            ).value
            self.assertIn("ARP Task 2.3:", prompt)
            self.assertIn(note, prompt)
            controls = [
                s
                for s in app.selectbox
                if (s.key or "").startswith(arp_ui.RESOLVER_BASE)
                and s.label.startswith("Choose a Task")
            ]
            self.assertEqual(
                [(s.label, s.value) for s in controls], [("Choose a Task 2.3 step", 4)]
            )
            next(
                b for b in app.button if b.label == "💡 Generate answer with reasoning"
            ).click()
            self.run_app(app)
            next(
                c
                for c in app.checkbox
                if c.label == "📚 Strict curriculum mode (use ONLY the syllabus)"
            ).set_value(True)
            self.run_app(app)
            next(b for b in app.button if b.label == "🔁 Re-generate answer").click()
            self.run_app(app)
            self.assertEqual(len(requests), 2)
            for req in requests:
                system, user = [m["content"] for m in req["messages"][:2]]
                self.assertIn("ANSWER LANGUAGE: Write in English", system)
                for t in [
                    "Kaggle",
                    "MS Excel",
                    "GIMP",
                    ".xcf",
                    ".jpg",
                    "not a fixed requirement",
                    "No dataset",
                    "not native editable GIMP text",
                    "no word count",
                ]:
                    self.assertIn(t, system)
                    self.assertIn(t, user)
                self.assertIn(
                    "current selected step: 5. Build the infographic with GIMP layers",
                    user,
                )
                self.assertIn("Save documentation: https://docs.gimp.org", user)
                self.assertIn(note, user)
                self.assertNotIn("Mercedes", user)
                self.assertNotIn("NaturalNews", user)
                self.assertNotIn("45892", user)
            signature = arp_ui.workflow_signature(app.session_state)
            next(
                s
                for s in app.selectbox
                if (s.key or "").startswith(arp_ui.RESOLVER_BASE)
                and s.label == "Choose a Task 2.3 step"
            ).set_value(6)
            self.run_app(app)
            self.assertNotEqual(signature, arp_ui.workflow_signature(app.session_state))
            self.assertIn("Previous AI answer", [e.label for e in app.expander])
            self.assertEqual(len(requests), 2)
            saved = json.loads(Path(".study_buddy_state.json").read_text())
            self.assertEqual(saved["arp_task_drafts"][lesson.GUIDE["uid"]], note)
            self.assertEqual(saved["arp_task_steps"][lesson.GUIDE["uid"]], 6)
            self.assertTrue(
                all(
                    s.value == 0
                    for s in app.selectbox
                    if s.label in ["Choose a Task 2.2 step", "Choose a Task 2.1 step"]
                )
            )

    def test_training_downloads_and_previous_tasks(self):
        app = self.app("Training Center")
        next(s for s in app.selectbox if s.label == "🎯 Select Topic:").set_value(
            "ARP Module 2: Report-Generating Tools"
        )
        self.run_app(app)
        for n in ["2.1", "2.2", "2.3", "2.4"]:
            self.assertIn(
                f"Prepare Task {n} in Exam Resolver", [b.label for b in app.button]
            )
        for _, label, _ in lesson.DOWNLOADS:
            self.assertIn(label, [d.label for d in app.get("download_button")])
        self.assertIn(
            "GIMP layout guide and the two output files",
            [e.label for e in app.expander],
        )
        self.assertNotIn(
            "Prepare Task 1.4 in Exam Resolver", [b.label for b in app.button]
        )


if __name__ == "__main__":
    unittest.main()
