"""English, stepwise file workflow integrated with the normal resolver inputs."""

import json
import os

import streamlit as st

import resolver_files as files


def image_api_key():
    """Images always use OpenAI, independently of the text provider."""
    for name in ("STUDY_BUDDY_IMAGE_API_KEY", "OPENAI_API_KEY"):
        value = os.getenv(name, "")
        if not value:
            try:
                value = st.secrets.get(name, "")
            except (FileNotFoundError, st.errors.StreamlitSecretNotFoundError):
                value = ""
        if value:
            return str(value).strip()
    return ""


def _show_checks(checks):
    automatic = [c for c in checks if c["status"] != "manual"]
    st.dataframe(
        automatic,
        hide_index=True,
        width="stretch",
        column_config={"status": "Status", "check": "Check", "detail": "Result"},
    )
    st.markdown("**Before you submit**")
    for check in checks:
        if check["status"] == "manual":
            st.markdown(f"- **{check['check']}:** {check['detail']}")


def render_file_workflow(brief, datasets, documents, client, model, base_key):
    with st.expander("Create Excel, illustrations and PowerPoint", expanded=False):
        st.markdown("#### 1. Review the brief and data")
        st.write(
            "Create editable files from the question and attachments above. Review the English plan, build the Excel charts, generate illustrations if needed, then download the checked files for your own submission."
        )
        st.caption(
            "No assignment is submitted by Study Buddy. Files and image keys stay in this browser session; download your work before leaving or reloading the app."
        )
        if not brief.strip() or not datasets:
            st.info(
                "Enter the task above and attach at least one CSV or Excel dataset to start. Supporting documents can provide requirements and source references."
            )
            return
        signature = files.digest_inputs(brief, datasets, documents)
        state_key = f"{base_key}_file_workflow"
        state = st.session_state.get(state_key)
        if not state or state["input_signature"] != signature:
            state = {
                "input_signature": signature,
                "images": {},
                "compiled": None,
                "output": None,
            }
            st.session_state[state_key] = state
        st.caption(
            " · ".join(
                f"input{i}: {label} ({len(df):,} rows)"
                for i, (label, df) in enumerate(datasets, 1)
            )
        )
        st.markdown("#### 2. Create and review the English plan")
        st.write(
            "The AI proposes a plan from the brief, column names and a short preview. Calculations later use every supplied row. Unsupported or unclear requirements remain visible for your review."
        )
        editor_key = f"{base_key}_file_plan_{signature[:12]}"
        ai_col, manual_col = st.columns(2)
        with ai_col:
            propose = st.button(
                "Create analysis plan",
                key=f"{base_key}_file_propose",
                disabled=client is None,
            )
        with manual_col:
            starter = st.button(
                "Start from dataset template", key=f"{base_key}_file_starter"
            )
        if client is None:
            st.info(
                "Configure a text AI provider to draft the plan, or start with a dataset template and edit it yourself."
            )
        if propose or starter:
            try:
                with st.spinner("Preparing the plan…"):
                    plan = (
                        files.propose_plan(client, model, brief, datasets, documents)
                        if propose
                        else files.starter_plan(datasets)
                    )
                    st.session_state[editor_key] = json.dumps(
                        plan, ensure_ascii=False, indent=2
                    )
            except files.PlanError as exc:
                st.error(str(exc))
            except Exception:
                st.error(
                    "The planning service could not complete the request. Check the configured text model and provider, or use the dataset template."
                )
        with st.expander("Advanced: edit the generation plan", expanded=False):
            raw = st.text_area(
                "Analysis plan (JSON)",
                key=editor_key,
                height=260,
                help="Edit titles, table expressions, chart types, assumptions and image prompts. Changing the plan invalidates older file downloads.",
            )
        if not raw.strip():
            return
        try:
            plan = files.parse_plan(raw)
            files.validate_sources(plan, brief, documents, datasets)
            plan_signature = files.digest_plan(plan)
        except (files.PlanError, KeyError, TypeError, ValueError) as exc:
            st.error(f"Plan needs correction: {exc}")
            return
        if state.get("plan_signature") != plan_signature:
            # Retain successful image calls only when the complete image request
            # is unchanged. Never silently reuse pixels for a different prompt.
            state["images"] = {
                i["id"]: state["images"][i["id"]]
                for i in plan.get("images", [])
                if i["id"] in state["images"]
                and state["images"][i["id"]].get("request") == files.digest_plan(i)
            }
            state.update(plan_signature=plan_signature, compiled=None, output=None)
        for i, step in enumerate(plan.get("steps", []), 1):
            st.markdown(f"**Step {i}.** {step}")
        for assumption in plan.get("assumptions", []):
            st.info(f"Assumption to review: {assumption}")
        for issue in plan.get("unresolved", []):
            st.warning(f"Unresolved requirement: {issue}")
        st.dataframe(
            [
                {
                    "Chart": c.get("title", c["id"]),
                    "Type": c["type"],
                    "Data": c["table"],
                    "Series": ", ".join(
                        s.get("name", s["column"]) for s in c["series"]
                    ),
                }
                for c in plan["charts"]
            ],
            hide_index=True,
            width="stretch",
        )
        with st.expander("Supported plan operations and limits"):
            st.code(
                files.PLAN_INSTRUCTIONS[files.PLAN_INSTRUCTIONS.index("Schema:") :],
                language="text",
            )
        st.markdown("#### 3. Build Excel and inspect the charts")
        if st.button("Build Excel and chart previews", key=f"{base_key}_file_excel"):
            state["compiled"] = None
            state["output"] = None
            try:
                with st.spinner(
                    "Calculating all rows and checking the saved workbook…"
                ):
                    tables, calculation_checks = files.execute_plan(plan, datasets)
                    workbook = files.build_excel(plan, tables)
                    checks = calculation_checks + files.validate_files(
                        plan, tables, workbook
                    )
                    previews = {
                        c["id"]: files.chart_preview(c, tables[c["table"]])
                        for c in plan["charts"]
                    }
                    state["compiled"] = {
                        "tables": tables,
                        "checks": checks,
                        "calculation_checks": calculation_checks,
                        "workbook": workbook,
                        "previews": previews,
                    }
            except files.PlanError as exc:
                st.error(str(exc))
            except Exception as exc:
                st.error(
                    f"Could not build the workbook ({type(exc).__name__}). Review the table and chart definitions; no checked output was created."
                )
        compiled = state.get("compiled")
        if not compiled:
            return
        st.download_button(
            "Download Excel with editable charts",
            compiled["workbook"],
            "Analysis.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key=f"{base_key}_file_xlsx",
            on_click="ignore",
        )
        for spec in plan["charts"]:
            with st.expander(spec.get("title", spec["id"])):
                st.image(
                    compiled["previews"][spec["id"]],
                    caption="Generated chart preview — not a screenshot from Microsoft Excel.",
                )
                for line in files.chart_findings(
                    spec, compiled["tables"][spec["table"]]
                ):
                    st.write(line)
                st.write(spec.get("explanation", ""))
        st.markdown("#### 4. Generate and review illustrations")
        if plan.get("images"):
            key = image_api_key()
            if not key:
                st.info(
                    "Illustrations need an OpenAI image API key, even when the text provider is Claude, Kimi or Ollama. Add STUDY_BUDDY_IMAGE_API_KEY to Streamlit Secrets, or enter a key for this session."
                )
                key = st.text_input(
                    "OpenAI image API key for this session",
                    type="password",
                    key=f"{base_key}_file_image_key",
                )
            image_model = os.getenv("STUDY_BUDDY_IMAGE_MODEL", "gpt-image-1.5")
            quality = st.selectbox(
                "Image quality",
                ["low", "medium", "high"],
                index=1,
                key=f"{base_key}_file_quality",
            )
            st.caption(
                f"OpenAI model: {image_model}. Each Generate button makes one paid image API request. No automatic retries. Only the displayed image prompt is sent, not the datasets. [OpenAI pricing](https://developers.openai.com/api/docs/pricing)"
            )
            for image in plan["images"]:
                with st.expander(image.get("title", image["id"]), expanded=True):
                    st.write(image["prompt"])
                    record = state["images"].get(image["id"])
                    if st.button(
                        f"{'Regenerate' if record else 'Generate'} illustration: {image['id']}",
                        key=f"{base_key}_file_image_{image['id']}",
                        disabled=not key,
                    ):
                        try:
                            from openai import OpenAI

                            with st.spinner("Generating the illustration…"):
                                # A separate official endpoint; never pass an
                                # OpenAI key to the configured text provider.
                                record = files.generate_illustration(
                                    OpenAI(
                                        api_key=key,
                                        base_url="https://api.openai.com/v1",
                                        max_retries=0,
                                        timeout=240,
                                    ),
                                    image,
                                    image_model,
                                    quality,
                                )
                                state["images"][image["id"]] = record
                                state["output"] = None
                        except Exception:
                            st.error(
                                "Image generation did not return a confirmed image. Check OpenAI image access, billing and the model setting. No automatic retry was made; review usage before trying again."
                            )
                    if record:
                        st.image(
                            record["original"],
                            caption="Original AI-generated illustration. Original bytes are retained.",
                        )
                        x = st.slider(
                            "Horizontal crop position",
                            0.0,
                            1.0,
                            0.5,
                            key=f"{base_key}_file_crop_x_{image['id']}",
                        )
                        y = st.slider(
                            "Vertical crop position",
                            0.0,
                            1.0,
                            0.5,
                            key=f"{base_key}_file_crop_y_{image['id']}",
                        )
                        edited = files.prepare_illustration(record, x, y)
                        if record.get("crop") != edited["crop"]:
                            state["output"] = None
                        state["images"][image["id"]] = edited
                        st.image(edited["edited"], caption=edited["edit"])
                        st.caption(
                            "Both versions, the crop description and a visible image source credit are included in the presentation. Confirm whether this edit meets your task requirements."
                        )
        else:
            st.caption(
                "No illustrations are requested in the current plan. Add image entries if your brief requires them."
            )
        missing = [
            i["id"] for i in plan.get("images", []) if i["id"] not in state["images"]
        ]
        st.markdown("#### 5. Build PowerPoint and the review pack")
        st.caption(
            "The presentation embeds the analysis workbook, including source sheets. Review the data you will share, and rebuild after changing it."
        )
        if missing:
            st.warning(
                "Illustrations still needed: "
                + ", ".join(missing)
                + ". Generate them or update the plan before building the presentation."
            )
        if st.button(
            "Build PowerPoint and review pack",
            key=f"{base_key}_file_deck",
            disabled=bool(missing),
        ):
            state["output"] = None
            try:
                with st.spinner(
                    "Creating native PowerPoint charts and checking the exported files…"
                ):
                    deck = files.build_powerpoint(
                        plan, compiled["tables"], compiled["workbook"], state["images"]
                    )
                    checks = compiled["calculation_checks"] + files.validate_files(
                        plan, compiled["tables"], compiled["workbook"], deck
                    )
                    guide = files.instructions(plan, compiled["tables"], checks)
                    report = {
                        "input_signature": signature,
                        "plan_signature": plan_signature,
                        "checks": checks,
                    }
                    pack = files.review_pack(
                        compiled["workbook"],
                        deck,
                        compiled["previews"],
                        state["images"],
                        guide,
                        report,
                    )
                    state["output"] = {
                        "deck": deck,
                        "checks": checks,
                        "guide": guide,
                        "pack": pack,
                        "report": report,
                    }
            except files.PlanError as exc:
                st.error(str(exc))
            except Exception as exc:
                st.error(
                    f"Could not complete the presentation ({type(exc).__name__}). No checked presentation download was created."
                )
        output = state.get("output")
        checks = output["checks"] if output else compiled["checks"]
        st.markdown("#### 6. Review checks and download")
        with st.expander("Automatic checks and remaining manual review", expanded=True):
            _show_checks(checks)
        if output:
            st.success(
                "File structure and data checks completed. Review the files and all manual items before submitting them yourself."
            )
            st.download_button(
                "Download PowerPoint with editable charts",
                output["deck"],
                "Presentation.pptx",
                "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                key=f"{base_key}_file_pptx",
                on_click="ignore",
            )
            st.download_button(
                "Download complete review pack",
                output["pack"],
                "Study Buddy review pack.zip",
                "application/zip",
                key=f"{base_key}_file_zip",
                on_click="ignore",
            )
            st.download_button(
                "Download English step-by-step guide",
                output["guide"],
                "Step-by-step guide.md",
                "text/markdown",
                key=f"{base_key}_file_guide",
                on_click="ignore",
            )
            st.download_button(
                "Download file check report",
                json.dumps(output["report"], indent=2),
                "File checks.json",
                "application/json",
                key=f"{base_key}_file_checks",
                on_click="ignore",
            )
