from streamlit.testing.v1 import AppTest


APP_PATH = "app.py"


def markdown_values(app_test):
    return [element.value for element in app_test.markdown]


def expander_labels(app_test):
    return [element.label for element in app_test.expander]


def run_initial_smoke():
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    assert len(app_test.exception) == 0, f"Initial app run has exceptions: {app_test.exception}"
    assert any(
        selectbox.label == "Select a course to study:" for selectbox in app_test.selectbox
    ), "Course selector was not rendered on the initial app run."


def run_stats_smoke():
    prompt = (
        "An independent t-test compares two groups. Group A has mean 72, standard deviation 10, "
        "and sample size 35. Group B has mean 78, standard deviation 11, and sample size 37. "
        "Use alpha 0.05."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    app_test.text_area[0].set_value(prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Stats prompt run has exceptions: {app_test.exception}"

    calc_type_value = None
    for selectbox in app_test.selectbox:
        if selectbox.label == "Calculation type":
            calc_type_value = selectbox.value
            break
    assert calc_type_value == "Independent t-test", f"Expected Independent t-test, got {calc_type_value!r}"

    stats_summary = None
    for text_area in app_test.text_area:
        if text_area.label == "Verified stats / hypothesis summary to use in your answer":
            stats_summary = text_area.value
            break
    assert stats_summary is not None, "Verified stats summary text area was not rendered."
    assert "mean A = 72.000" in stats_summary, stats_summary
    assert "mean B = 78.000" in stats_summary, stats_summary
    assert "nA = 35" in stats_summary, stats_summary
    assert "nB = 37" in stats_summary, stats_summary

    joined_markdown = "\n".join(markdown_values(app_test))
    assert "Downloadable Google Sheets template for this statistical method" in joined_markdown


def run_data_model_smoke():
    prompt = (
        "Using the examples of a School Management System, a banking institution and an online "
        "craft shop, create diagrams depicting ER, hierarchical, relational, and network modelling. "
        "Also show how to build them in Google Sheets."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    app_test.text_area[0].set_value(prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Data-model prompt run has exceptions: {app_test.exception}"

    labels = expander_labels(app_test)
    for required_label in [
        "Suggested ER Diagram",
        "Suggested Hierarchical Diagram",
        "Suggested Relational Diagram",
        "Suggested Network Diagram",
        "Google Sheets setup - ER case",
        "Google Sheets setup - Hierarchical case",
        "Google Sheets setup - Relational case",
        "Google Sheets setup - Network case",
    ]:
        assert required_label in labels, f"Missing expected expander: {required_label}"

    joined_markdown = "\n".join(markdown_values(app_test))
    assert "Suggested visual diagrams" in joined_markdown
    assert "How to build the same case in Google Sheets" in joined_markdown
    assert "Downloadable Google Sheets templates" in joined_markdown


def main():
    run_initial_smoke()
    run_stats_smoke()
    run_data_model_smoke()
    print("exam_resolver_smoke_test: PASS")


if __name__ == "__main__":
    main()
