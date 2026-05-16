from streamlit.testing.v1 import AppTest


APP_PATH = "app.py"


def markdown_values(app_test):
    return [element.value for element in app_test.markdown]


def expander_labels(app_test):
    return [element.label for element in app_test.expander]


def set_exam_prompt(app_test, prompt):
    for text_area in app_test.text_area:
        if text_area.label == "Paste the exam question, case, or task prompt":
            text_area.set_value(prompt)
            return
    raise AssertionError("Exam prompt text area was not found.")


def set_selectbox_value(app_test, label, value):
    for selectbox in app_test.selectbox:
        if selectbox.label == label:
            selectbox.set_value(value)
            return
    raise AssertionError(f"Selectbox with label {label!r} was not found.")


def number_input_value(app_test, label):
    for widget in app_test.number_input:
        if widget.label == label:
            return widget.value
    raise AssertionError(f"Number input with label {label!r} was not found.")


def stats_summary_value(app_test):
    for text_area in app_test.text_area:
        if text_area.label == "Verified stats / hypothesis summary to use in your answer":
            return text_area.value
    raise AssertionError("Verified stats summary text area was not rendered.")


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
    set_exam_prompt(app_test, prompt)
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
    set_exam_prompt(app_test, prompt)
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


def run_chart_smoke():
    prompt = (
        "In descriptive data analysis, create a histogram, bar chart, scatter plot, and box plot. "
        "Use these values for the histogram and box plot: 12, 14, 15, 18, 21, 24. "
        "Use these category values for the bar chart: North 12, South 18, East 15. "
        "Use these pairs for the scatter plot:\n"
        "1,2\n"
        "2,3\n"
        "3,5\n"
        "4,7\n"
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Chart prompt run has exceptions: {app_test.exception}"

    labels = expander_labels(app_test)
    for required_label in [
        "Suggested Histogram",
        "Suggested Bar Chart",
        "Suggested Scatter Plot",
        "Suggested Box Plot",
    ]:
        assert required_label in labels, f"Missing expected chart expander: {required_label}"

    joined_markdown = "\n".join(markdown_values(app_test))
    assert "Suggested data visuals" in joined_markdown


def run_descriptive_stats_smoke():
    prompt = "Calculate the mean and median for these values: 12, 14, 15, 18, 21, 24."
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Descriptive stats prompt run has exceptions: {app_test.exception}"

    calc_type_value = None
    for selectbox in app_test.selectbox:
        if selectbox.label == "Calculation type":
            calc_type_value = selectbox.value
            break
    assert calc_type_value == "Descriptive statistics (raw values)", f"Expected descriptive statistics calculator, got {calc_type_value!r}"

    stats_summary = None
    for text_area in app_test.text_area:
        if text_area.label == "Verified stats / hypothesis summary to use in your answer":
            stats_summary = text_area.value
            break
    assert stats_summary is not None, "Verified descriptive stats summary text area was not rendered."
    assert "mean = 17.333" in stats_summary, stats_summary
    assert "median = 16.500" in stats_summary, stats_summary


def run_kpi_resolver_smoke():
    prompt = (
        "A small software house copied Facebook's KPI of mean time spent on page. "
        "The company sells mainly through direct calls to potential buyers, and the website is only used "
        "to show some previous solutions. Explain why this KPI is weak, what pitfall it shows, and which "
        "KPIs would fit the company better."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_selectbox_value(app_test, "Select a course to study:", "FI1BBDD75 - Data Driven Decision-Making")
    app_test.run(timeout=90)
    set_selectbox_value(app_test, "Question style", "Evaluation or KPI question")
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"KPI resolver prompt run has exceptions: {app_test.exception}"

    joined_markdown = "\n".join(markdown_values(app_test)).lower()
    assert "copied" in joined_markdown, joined_markdown
    assert "strategy" in joined_markdown, joined_markdown


def run_kpi_incentive_resolver_smoke():
    prompt = (
        "A global bank wants to introduce a KPI based on how many incidents each engineer handles and "
        "link it to an annual incentive. Junior engineers solve many simple incidents, while senior "
        "engineers solve only a few mission-critical incidents with very high business impact. Explain "
        "whether this KPI would be fair and what KPI approach would be better."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_selectbox_value(app_test, "Select a course to study:", "FI1BBDD75 - Data Driven Decision-Making")
    app_test.run(timeout=90)
    set_selectbox_value(app_test, "Question style", "Evaluation or KPI question")
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"KPI incentive prompt run has exceptions: {app_test.exception}"

    joined_markdown = "\n".join(markdown_values(app_test)).lower()
    assert "fair" in joined_markdown, joined_markdown
    assert "incentive" in joined_markdown, joined_markdown
    assert "complexity" in joined_markdown or "critical" in joined_markdown, joined_markdown


def run_kpi_telecom_resolver_smoke():
    prompt = (
        "Come up with a scenario and detail the steps required to determine the KPIs for a "
        "telecommunications company. Goal: increase overall sales and customer satisfaction."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_selectbox_value(app_test, "Select a course to study:", "FI1BBDD75 - Data Driven Decision-Making")
    app_test.run(timeout=90)
    set_selectbox_value(app_test, "Question style", "Evaluation or KPI question")
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Telecom KPI prompt run has exceptions: {app_test.exception}"

    joined_markdown = "\n".join(markdown_values(app_test)).lower()
    assert "telecommunications" in joined_markdown or "telecom" in joined_markdown, joined_markdown
    assert "customer satisfaction" in joined_markdown, joined_markdown
    assert "sales" in joined_markdown, joined_markdown


def run_auto_detect_and_lesson_evidence_smoke():
    prompt = (
        "Come up with a scenario and detail the steps required to determine the KPIs for a "
        "telecommunications company. Goal: increase overall sales and customer satisfaction."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_selectbox_value(app_test, "Select a course to study:", "FI1BBDD75 - Data Driven Decision-Making")
    app_test.run(timeout=90)
    set_selectbox_value(app_test, "Question style", "Unsure - auto detect")
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Auto-detect lesson-evidence run has exceptions: {app_test.exception}"

    joined_markdown = "\n".join(markdown_values(app_test))
    assert "Auto-detected question style" in joined_markdown, joined_markdown
    assert "Lesson evidence the resolver is pulling from" in joined_markdown, joined_markdown
    assert "How this exam prompt connects to the selected course" in joined_markdown, joined_markdown


def run_reordered_independent_t_test_smoke():
    """Bug 2 regression guard: autofill must use labels, not positional order."""
    prompt = (
        "An independent t-test compares two groups. "
        "Group A: n=35, mean=72, standard deviation=10. "
        "Group B: n=37, mean=78, standard deviation=11. "
        "Use alpha 0.05."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Reordered Indep t-test run has exceptions: {app_test.exception}"
    assert number_input_value(app_test, "Group A mean") == 72.0
    assert number_input_value(app_test, "Group A standard deviation") == 10.0
    assert number_input_value(app_test, "Group A sample size") == 35
    assert number_input_value(app_test, "Group B mean") == 78.0
    assert number_input_value(app_test, "Group B standard deviation") == 11.0
    assert number_input_value(app_test, "Group B sample size") == 37


def run_paired_t_test_sign_smoke():
    """Bug 3 regression guard: a paired prompt that signals an increase must
    produce a positive mean_diff and a positive t-value."""
    prompt = (
        "Run a paired t-test. Before: mean = 68. After: mean = 74. "
        "SD of differences = 8. Number of pairs = 30. "
        "Did the mean increase at alpha 0.05?"
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Paired t-test sign run has exceptions: {app_test.exception}"
    assert number_input_value(app_test, "Mean before") == 68.0
    assert number_input_value(app_test, "Mean after") == 74.0
    summary = stats_summary_value(app_test)
    assert "mean difference = 6.000" in summary, summary
    # 6 / (8/sqrt(30)) = 4.108. Asserting the positive sign also verifies
    # the after-minus-before convention.
    assert "t = 4.108" in summary, summary


def run_anova_before_paired_routing_smoke():
    """Routing fix: 'three paired groups' must route to ANOVA, not paired t-test."""
    prompt = (
        "Compare three paired groups of measurements using repeated measures ANOVA. "
        "Group 1: mean 100, sd 12, n 30. Group 2: mean 105, sd 14, n 28. "
        "Group 3: mean 110, sd 13, n 32."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"ANOVA routing run has exceptions: {app_test.exception}"
    calc_type_value = None
    for selectbox in app_test.selectbox:
        if selectbox.label == "Calculation type":
            calc_type_value = selectbox.value
            break
    assert calc_type_value == "One-way ANOVA (3 groups)", (
        f"Expected ANOVA route, got {calc_type_value!r}"
    )


def run_two_proportion_tail_smoke():
    """Routing + UI fix: prompt about conversion-rate increase routes to two-proportion z-test
    and exposes a tail-type selector that defaults to right-tailed."""
    prompt = (
        "Run a two-proportion z-test. Group A had 520 conversions out of 10000 visitors. "
        "Group B had 570 conversions out of 10050 visitors. "
        "Did the conversion rate increase? Use alpha 0.05."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Two-proportion run has exceptions: {app_test.exception}"
    calc_type_value = None
    for selectbox in app_test.selectbox:
        if selectbox.label == "Calculation type":
            calc_type_value = selectbox.value
            break
    assert calc_type_value == "Two-proportion z-test", calc_type_value
    summary = stats_summary_value(app_test)
    assert "tail = Right-tailed" in summary, summary


def run_norwegian_routing_smoke():
    """Norwegian alias: 'paret t-test' must route to Paired t-test."""
    prompt = (
        "Vi vil kjøre en paret t-test for å sammenligne målinger før og etter behandling. "
        "Gjennomsnittet før var 68, gjennomsnittet etter var 74, standardavviket til "
        "differansene var 8, og antall par var 30."
    )
    app_test = AppTest.from_file(APP_PATH)
    app_test.run(timeout=90)
    set_exam_prompt(app_test, prompt)
    app_test.run(timeout=90)

    assert len(app_test.exception) == 0, f"Norwegian routing run has exceptions: {app_test.exception}"
    calc_type_value = None
    for selectbox in app_test.selectbox:
        if selectbox.label == "Calculation type":
            calc_type_value = selectbox.value
            break
    assert calc_type_value == "Paired t-test", calc_type_value


def main():
    run_initial_smoke()
    run_stats_smoke()
    run_data_model_smoke()
    run_chart_smoke()
    run_descriptive_stats_smoke()
    run_kpi_resolver_smoke()
    run_kpi_incentive_resolver_smoke()
    run_kpi_telecom_resolver_smoke()
    run_auto_detect_and_lesson_evidence_smoke()
    run_reordered_independent_t_test_smoke()
    run_paired_t_test_sign_smoke()
    run_anova_before_paired_routing_smoke()
    run_two_proportion_tail_smoke()
    run_norwegian_routing_smoke()
    print("exam_resolver_smoke_test: PASS")


if __name__ == "__main__":
    main()
