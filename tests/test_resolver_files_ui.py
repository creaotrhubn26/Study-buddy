from io import BytesIO
import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from PIL import Image
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import resolver_files as files

HARNESS = f"""
import sys
sys.path.insert(0,{str(ROOT)!r})
import pandas as pd
import streamlit as st
from resolver_files_ui import render_file_workflow
brief=st.text_area('Test brief',value='Compare annual demand. Create a line chart and a presentation.')
last=st.number_input('Last observed value',value=150)
data=[('synthetic.csv',pd.DataFrame({{'Year':[2021,2022,2023],'Demand':[100,120,last]}}))]
render_file_workflow(brief,data,[],None,None,'test')
"""


class WorkflowUITests(unittest.TestCase):
    def run_app(self, app):
        app.run(timeout=30)
        self.assertFalse(app.exception, [e.message for e in app.exception])
        return app

    def button(self, app, label):
        return next(b for b in app.button if b.label == label)

    def editor(self, app):
        return next(t for t in app.text_area if t.label == "Analysis plan (JSON)")

    def downloads(self, app):
        return [b.label for b in app.get("download_button")]

    def test_download_workflow_and_stale_state(self):
        app = self.run_app(AppTest.from_string(HARNESS))
        self.button(app, "Start from dataset template").click()
        self.run_app(app)
        self.button(app, "Build Excel and chart previews").click()
        self.run_app(app)
        self.assertIn("Download Excel with editable charts", self.downloads(app))
        self.button(app, "Build PowerPoint and review pack").click()
        self.run_app(app)
        self.assertIn("Download complete review pack", self.downloads(app))
        self.assertEqual(
            len(
                app.session_state["test_file_workflow"]["compiled"]["tables"][
                    "input1"
                ].frame
            ),
            3,
        )
        next(n for n in app.number_input if n.label == "Last observed value").set_value(
            999
        )
        self.run_app(app)
        self.assertNotIn("Download complete review pack", self.downloads(app))
        self.assertNotIn("Download Excel with editable charts", self.downloads(app))

    def test_invalid_plan_blocks_exports_and_model_is_not_called_on_rerun(self):
        app = self.run_app(AppTest.from_string(HARNESS))
        self.button(app, "Start from dataset template").click()
        self.run_app(app)
        self.editor(app).set_value("{bad")
        self.run_app(app)
        self.assertTrue(app.error)
        self.assertEqual(self.downloads(app), [])

    def test_failed_image_request_is_not_retried_on_rerun(self):
        with (
            patch.dict(os.environ, {"STUDY_BUDDY_IMAGE_API_KEY": "offline-image-test"}),
            patch.object(
                files,
                "generate_illustration",
                side_effect=RuntimeError("service unavailable"),
            ) as request,
        ):
            app = self.run_app(AppTest.from_string(HARNESS))
            self.button(app, "Start from dataset template").click()
            self.run_app(app)
            plan = json.loads(self.editor(app).value)
            plan["images"] = [
                {
                    "id": "concept",
                    "title": "Concept",
                    "prompt": "An educational demand illustration",
                }
            ]
            self.editor(app).set_value(json.dumps(plan))
            self.run_app(app)
            self.button(app, "Build Excel and chart previews").click()
            self.run_app(app)
            self.button(app, "Generate illustration: concept").click()
            self.run_app(app)
            self.assertEqual(request.call_count, 1)
            self.assertTrue(app.error)
            self.run_app(app)
            self.assertEqual(request.call_count, 1)
            self.assertTrue(
                self.button(app, "Build PowerPoint and review pack").disabled
            )

    def test_images_explicit_resumable_and_crop_invalidates_presentation(self):
        image = BytesIO()
        Image.new("RGB", (120, 100), "green").save(image, "PNG")
        calls = []

        def generate(client, spec, model, quality):
            calls.append(spec["id"])
            return {
                "original": image.getvalue(),
                "created": "2026-01-01T12:00:00+00:00",
                "model": model,
                "request": files.digest_plan(spec),
            }

        with (
            patch.dict(os.environ, {"STUDY_BUDDY_IMAGE_API_KEY": "offline-image-test"}),
            patch.object(files, "generate_illustration", side_effect=generate),
        ):
            app = self.run_app(AppTest.from_string(HARNESS))
            self.button(app, "Start from dataset template").click()
            self.run_app(app)
            plan = json.loads(self.editor(app).value)
            plan["images"] = [
                {
                    "id": "concept",
                    "title": "Concept",
                    "prompt": "An educational demand illustration",
                    "caption": "Illustration only.",
                }
            ]
            self.editor(app).set_value(json.dumps(plan))
            self.run_app(app)
            self.button(app, "Build Excel and chart previews").click()
            self.run_app(app)
            self.assertTrue(
                self.button(app, "Build PowerPoint and review pack").disabled
            )
            self.button(app, "Generate illustration: concept").click()
            self.run_app(app)
            self.assertEqual(calls, ["concept"])
            self.run_app(app)
            self.assertEqual(calls, ["concept"])
            self.button(app, "Build PowerPoint and review pack").click()
            self.run_app(app)
            self.assertIn(
                "Download PowerPoint with editable charts", self.downloads(app)
            )
            next(
                s for s in app.slider if s.label == "Vertical crop position"
            ).set_value(0.8)
            self.run_app(app)
            self.assertNotIn(
                "Download PowerPoint with editable charts", self.downloads(app)
            )
            self.assertEqual(calls, ["concept"])


if __name__ == "__main__":
    unittest.main()
