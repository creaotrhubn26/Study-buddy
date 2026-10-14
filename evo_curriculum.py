"""EVO study notes aligned with the authenticated Noroff lesson books.

These are original revision explanations and practice activities, not a copy of
the course books or assessment. Lesson numbers and source links were checked
on 2026-10-13. Keep the existing supplemental Training Center topics intact.
"""

from copy import deepcopy
from pathlib import Path
from evo_lesson_walkthroughs import LESSON_ILLUSTRATIONS, LESSON_WALKTHROUGHS

CONTENT_REVISION = "2026-10-14-lessons-73-74"

COURSE_CODE = "FI1BBEO10"
COURSE_NAME = "Evaluation of Outcomes"
SOURCE_CHECKED_ON = "2026-10-13"
ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "evo"

MODULE_TITLES = [
    "Key Performance Indicators (KPIs) and Statistical Tools",
    "Ensembling Data, ETL and Tools",
    "Statistical Inferences, Iterative Error Elimination and Confidence Levels",
    "Implementing reliability checks and error detection",
    "Data-related Confidence, Collaboration and Communication",
    "The Complete Data Analysis Pipeline: A Step-by-Step Guide",
    "The Complete Data Analysis Pipeline: Guided vs. Independent Approaches",
]

ILLUSTRATIONS = [
    ("module-1-kpi-evidence.png", "KPI → investigate → evaluate → decide. A metric needs a target and context before it can guide action."),
    ("module-2-ensemble-etl.png", "ETL prepares the data; bagging, boosting and stacking combine model predictions in different ways."),
    ("module-3-confidence-models.png", "With the same data, higher confidence requires a wider interval. Precision and recall describe different classification errors."),
    ("module-4-quality-ethics.png", "Profile → validate → investigate → correct → recheck. Document the reason for a change and check for bias."),
    ("module-5-collaboration.png", "Versioned data and clear explanations let a team reproduce, review and act on an analysis."),
    ("module-6-superstore-pipeline.png", "The guided Superstore project links a business question to clean data, EDA, statistical interpretation and recommendations."),
    ("module-7-hotel-pipeline.png", "The independent SHG hotel project connects booking channels, lead time, cancellations and revenue to a defensible recommendation."),
]


def _lesson(number, title, chapter_id, content, key_points, question, hint, answer,
            quiz_question, options, correct, explanation):
    content = LESSON_WALKTHROUGHS.get(number, content)
    module_number = int(number.split(".")[0])
    book_id = 22832 + module_number
    source_url = f"https://learning.noroff.no/mod/book/view.php?id={book_id}&chapterid={chapter_id}"
    practice = {
        "title": f"{number} — Apply the lesson",
        "type": "case_study",
        "question": question,
        "hint": hint,
        "answer": answer,
    }
    return {
        "lesson_number": number,
        "title": title,
        "module_number": module_number,
        "module_title": MODULE_TITLES[module_number - 1],
        "course_code": COURSE_CODE,
        "source_url": source_url,
        "source_checked_on": "2026-10-14" if number in LESSON_WALKTHROUGHS else SOURCE_CHECKED_ON,
        "content": content.strip() + "\n\n#### Practice\n\n" + question
                   + f"\n\n[Open the original lesson and datasets on Noroff]({source_url}).\n",
        "key_points": key_points,
        "visual_elements": {"diagrams": False, "tables": "|" in content, "highlighted_sections": True},
        "illustration": LESSON_ILLUSTRATIONS[number][0] if number in LESSON_ILLUSTRATIONS else (ILLUSTRATIONS[module_number - 1][0] if number.endswith(".1") else None),
        "illustration_caption": LESSON_ILLUSTRATIONS[number][1] if number in LESSON_ILLUSTRATIONS else ILLUSTRATIONS[module_number - 1][1],
        "lesson_illustration": number in LESSON_ILLUSTRATIONS,
        "exercise": practice,
        "quiz": {
            "question": quiz_question,
            "options": options,
            "correct": correct,
            "explanation": explanation,
        },
    }


EVO_LESSONS = [
    _lesson("1.1", "Data Analysis, Key Performance Indicators (KPIs), and Version Control", 81121, """
### KPIs: choose evidence that changes a decision
A **KPI** measures progress toward a defined objective. Start with the business goal, specify the metric, identify a baseline and target, and decide who will act when performance changes. A high number has little meaning without a comparison period, denominator or benchmark.

| Distinction | Meaning | Example |
|---|---|---|
| Leading indicator | An early signal of a possible future outcome | Qualified enquiries |
| Lagging indicator | A measure of an outcome already achieved | Monthly revenue |
| Quantitative evidence | Numerical measurement | Resolution time |
| Qualitative evidence | Explanations and experiences | Reasons customers complain |

### Heuristics and dashboards
A **heuristic** is a shortcut for making a decision. Availability emphasises recent or memorable information; representativeness fits a new case into a familiar pattern; anchoring gives too much weight to the first benchmark. A KPI dashboard can focus attention, but these shortcuts can also hide context. Combine trends, targets and customer feedback rather than treating one metric as the whole story.

### Integrity and version control
Explain how each KPI is calculated, preserve the original data and track changes to definitions or filters. If the definition of a resolved ticket changes, the before-and-after figures may no longer be comparable. Record the change instead of quietly presenting an apparent improvement.

#### Exam answer pattern
Define the KPI → connect it to the objective → explain its calculation and benchmark → state its limitation → recommend a justified action.
""", ["Align KPIs with a business objective, baseline, target and action", "Distinguish leading/lagging indicators and numerical/contextual evidence", "Availability, representativeness and anchoring can distort KPI interpretation", "Version control preserves comparable definitions and traceable changes"],
        "A support team closes more tickets, but customers report unresolved problems. Propose two KPIs and explain how you would evaluate the change.",
        "Compare throughput with a quality outcome; preserve the definition of closed and resolved.",
        "Track closure rate together with reopen rate or customer satisfaction, using the same period and denominator. Read feedback to understand why cases are reopened. Check whether the closure definition changed and recommend improvements based on both speed and quality.",
        "A KPI rises immediately after its calculation changes. What should you do first?",
        ["Declare the strategy successful", "Check definition and comparability", "Remove the previous data", "Ignore qualitative feedback"], 1,
        "A change in measurement can create an apparent improvement without a change in business performance."),

    _lesson("1.2", "Statistical Inference, Result Table Analysis, and Critical Tools", 81137, """
### Read a result table as evidence
**Statistical inference** uses a sample to estimate or test something about a population. Check the sampling method and whether the sample represents the intended population before generalising. Random, stratified and systematic sampling answer different practical needs; convenience samples can introduce selection bias.

### Regression and residuals
In a simple regression, `Y = intercept + slope × X + error`. Explain the slope in the original units, the uncertainty around the estimate, and whether the relationship is useful for the business question. **R²** describes the proportion of observed variation explained in the fitted sample; adjusted R² also accounts for model complexity. A small p-value does not establish causation or guarantee useful predictions.

Inspect **residuals**, the differences between observed and predicted values. Curvature suggests an inadequate linear form; changing spread may violate constant-variance assumptions. Evaluate MAE or RMSE and performance on data not used for fitting, as appropriate.

### Summaries and tests
A five-number summary is minimum, Q1, median, Q3 and maximum. IQR is Q3 − Q1. Variance and standard deviation describe spread. In hypothesis testing, state H₀, H₁ and alpha before inspecting results. A z-test requires suitable assumptions, including the relevant population standard deviation being known for the usual mean z-test; use a t-test when estimating that uncertainty from the sample.

#### Exam answer pattern
Name the output → interpret it in context → check assumptions and sampling → explain what it supports and what remains uncertain.
""", ["Inference depends on the sampling design and representativeness", "Interpret regression coefficients, R², adjusted R² and residuals together", "Five-number summaries and IQR describe the distribution and spread", "Select a z-test or t-test according to assumptions; correlation does not establish causation"],
        "A regression has R² = 0.82, but its residual plot curves and its test-data error is high. Should it be used for forecasting? Explain.",
        "A good fitted-sample statistic does not settle model adequacy or generalisation.",
        "R² describes the fitted sample, but curvature suggests a misspecified linear relationship and high test error indicates weak generalisation. Investigate the model form and validation design before using its forecasts.",
        "Which quantities form a five-number summary?",
        ["Mean, variance, skewness, kurtosis and mode", "Intercept, slope, R², p and n", "Minimum, Q1, median, Q3 and maximum", "Five random observations"], 2,
        "The five-number summary describes the centre and spread of the observed distribution."),

    _lesson("1.3", "Variance Measurement, Confidence Levels, and Problem Solving", 81152, """
### Spread changes the interpretation of an average
Two branches can have the same average sales and very different variability. **Variance** averages squared deviations from the mean; standard deviation is its square root and uses the original measurement units. For a sample, use the `n − 1` denominator when estimating population variance.

| Excel function | Purpose |
|---|---|
| `=VAR.S(B2:B101)` | Sample variance |
| `=STDEV.S(B2:B101)` | Sample standard deviation |
| `=AVERAGE(B2:B101)` | Sample mean |

### Confidence intervals
A confidence interval for a population mean takes the form `estimate ± critical value × standard error`. With unknown population standard deviation, a common interval is `mean ± t* × s / SQRT(n)`, assuming the sampling and distribution conditions fit. Increasing confidence from 95% to 99% widens the interval when other inputs are fixed. More observations generally reduce sampling uncertainty, but do not fix biased collection.

The 95% refers to the long-run coverage of the interval-producing procedure. It does not mean that 95% of individual observations lie inside this mean interval. A prediction interval for a new observation answers a different question and usually includes more uncertainty.

### Solve the cause of a problem
Investigate unexpected results using root-cause analysis and the **5 Whys**. Check source data, process changes and alternative explanations. A high house price may be a valid luxury property rather than an entry error. Document the reason for any correction and rerun the analysis.
""", ["Variance uses squared units; standard deviation uses the original units", "A confidence interval estimates uncertainty around a population parameter", "Higher confidence gives a wider interval with the same data", "Use root-cause analysis before treating an unusual observation as an error"],
        "Two sales teams average 100 orders per week. Their standard deviations are 5 and 30. Explain the operational difference and what a 95% mean confidence interval would describe.",
        "Separate weekly variability from uncertainty in the estimated population mean.",
        "The second team has less predictable weekly demand, affecting staffing and inventory. A 95% mean confidence interval describes sampling uncertainty in the estimated average, not a band containing 95% of individual weeks.",
        "With all other inputs unchanged, raising confidence from 95% to 99% makes an interval:",
        ["Wider", "Narrower", "Identical", "A guarantee about every forecast"], 0,
        "A higher critical value is needed for higher coverage, increasing the margin of error."),

    _lesson("1.4", "Iterative Error Elimination techniques, Ethical Principles, and Solution Facilitation", 81168, """
### Classify errors before choosing a correction
| Error source | Example | Appropriate investigation |
|---|---|---|
| Human | Transposed digits or a typo | Cross-check the original record |
| Technical | Faulty parsing or a software calculation | Test the transformation or algorithm |
| Systemic | A process repeatedly drops one group | Audit and redesign the process |
| Sampling | The selected sample does not support the intended population claim | Review sample design and coverage |

### Detect → diagnose → correct → recheck
Preserve raw input, profile the data, identify a suspicious result, trace its cause, apply a justified correction and rerun both validation and analysis. Check whether the fix introduced another problem. Prevention can include validation rules, automated checks, staff training and periodic audits.

Do not equate sampling variability with systematic sampling bias: even a well-designed random sample has random estimation error. Biased coverage requires a different remedy from simply collecting a larger sample.

### Ethics and collaboration
Transparency means recording what changed and why. Integrity means avoiding changes just to obtain a desired finding. Fairness means checking whether cleaning or exclusion disproportionately affects particular groups. A data point should not be removed solely because it contradicts your hypothesis.

Communicate an error using a reproducible example: affected field and records, observed symptom, likely cause, impact, proposed remedy, owner and verification result. Discuss the process constructively so team members can report further issues.
""", ["Distinguish human, technical, systemic and sampling-related problems", "Preserve raw input and verify the result after each correction", "Do not remove data merely to obtain a preferred conclusion", "Communicate impact, proposed remedy and verification with the team"],
        "A survey contains only managers, but its report claims to represent all employees. Classify the problem and propose a correction and team communication.",
        "Consider who was excluded and whether correcting individual rows would solve the problem.",
        "The collection has selection/coverage bias. Obtain a representative sample across employee groups or restrict the claim to managers. Document the limitation and explain the effect on conclusions to the team; editing individual answers does not fix the design.",
        "Which correction is ethically justified?",
        ["Remove all values that weaken the hypothesis", "Replace every low score with the mean", "Hide excluded records", "Investigate and document an invalid entry using the source record"], 3,
        "Corrections should have an evidence-based reason and remain traceable."),

    _lesson("2.1", "Ensembling Data and Industry Techniques", 81184, """
### Why combine models?
**Ensembling** combines model predictions to obtain a result that can be more stable or accurate than an individual model. It does not automatically repair poor raw data, remove bias or guarantee better performance. Evaluate the combined model on appropriately held-out data.

| Method | How it works | Main distinction |
|---|---|---|
| Bagging | Train models on bootstrap samples and average/vote | Parallel models; often reduces variance |
| Boosting | Add models sequentially, targeting errors of the preceding ensemble | Successive error reduction |
| Stacking | Train a meta-model on the predictions of base models | Learns how to combine predictions |

A **bootstrap** sample is drawn with replacement, so a record can appear more than once. Random forests combine multiple decision trees. A stacking meta-model should learn from out-of-fold predictions rather than base-model predictions on the same rows used for fitting, to limit leakage.

### Fit the industry and decision
Financial data can have volatility, noise and changing patterns. Healthcare may prioritise interpretable, reliable decisions on rare events. E-commerce may prioritise predictive quality at scale. Explain the cost of errors, validation method, computational requirements and interpretability before recommending an ensemble.

#### Exam answer pattern
Define the method → explain its combination mechanism → justify its fit → compare a baseline → state validation evidence and limitations.
""", ["Bagging aggregates bootstrap models; boosting adds models sequentially; stacking uses a meta-model", "Bootstrapping samples with replacement", "Evaluate reliability on suitable held-out data and prevent leakage", "Industry-specific error costs and interpretability affect model choice"],
        "A demand forecast changes sharply whenever its training sample changes. Which ensemble would you investigate first, and how would you check whether it helps?",
        "Focus on prediction variance and use identical evaluation periods for comparisons.",
        "Investigate bagging, which averages predictions from models fitted to bootstrap samples. Compare its held-out forecast error and stability with the original baseline. For time-ordered data, validate on later periods and avoid future-information leakage.",
        "Which approach trains a model to combine predictions from other models?",
        ["A z-test", "Stacking", "Deduplication", "A five-number summary"], 1,
        "Stacking uses base-model predictions as inputs to a meta-model."),

    _lesson("2.2", "Quantitative and Qualitative methods in data analysis", 81201, """
### Numbers and explanations answer different questions
**Quantitative methods** analyse numerical measurements: how many customers cancel, how much revenue changes, or whether group means differ. **Qualitative methods** analyse experiences, descriptions and context through interviews, observations and text.

| Question | Suitable evidence | Example method |
|---|---|---|
| How large is the change? | Counts, amounts and rates | Descriptive statistics or a suitable test |
| Why are customers dissatisfied? | Comments and interviews | Coding and thematic analysis |
| Do both accounts agree? | Both sources | Triangulation and cross-verification |

### Reliability and validity
Reliability concerns consistency under comparable conditions. Validity concerns whether the method measures the intended concept. A repeatable survey can still ask the wrong question. Define the population, use an appropriate instrument and explain how collection choices affect interpretation.

For qualitative work, retain context, document a coding scheme and examine contradictory examples instead of collecting only supportive quotations. Numerical coding of a category does not necessarily make it a meaningful continuous measurement.

### Combine the methods
A retailer may observe a fall in repeat purchases, then use interviews to learn about confusing returns. Compare themes with transaction patterns. Agreement strengthens confidence; disagreement should prompt investigation rather than be concealed.

#### Exam answer pattern
Choose the evidence for each question, explain the method, connect the findings and disclose sampling or interpretation limitations.
""", ["Quantitative methods measure amounts and patterns; qualitative methods explore meaning and context", "Reliability and validity are different requirements", "Triangulation cross-checks evidence from complementary methods", "Qualitative coding and interpretation should be documented and contextual"],
        "A shop's customer satisfaction score improves, but interviewees describe worse service. How would you investigate?",
        "Check whether both sources cover the same customers and time period.",
        "Review the survey measure, sample, response rate and dates. Code interview themes systematically and compare customer segments. The disagreement may expose selection bias or a measure that misses an important aspect of service; report it openly.",
        "What does validity primarily ask?",
        ["Is the file compressed?", "Are all methods numerical?", "Does the method measure the intended concept?", "Are all results identical?"], 2,
        "Consistency is reliability; measuring the intended concept is validity."),

    _lesson("2.3", "ETL Systems, Data Analysis Lifecycle, and Ensuring Reliability", 81213, """
### Extract, Transform, Load
**ETL** moves data from source systems into an organised analytical destination. Extraction gathers relevant records; transformation cleans, standardises and reshapes them; loading stores the prepared result. Quality checks belong at every stage.

| Stage | Example | Evaluation check |
|---|---|---|
| Extract | Read regional sales files | Are expected files, dates and records present? |
| Transform | Standardise currency, dates and product names | Are mappings correct; have rows been lost or duplicated? |
| Load | Store an analytical table | Do totals, keys and refresh dates match expectations? |

### Reliability throughout the lifecycle
Retain raw files, record source and extraction time, reconcile counts and totals, document missing-value decisions, and monitor freshness. Security and privacy requirements affect what is extracted and retained. A fast pipeline that silently drops data can produce unreliable outcome evaluations.

Integration challenges include different schemas, stale data, scale, failed refreshes and inconsistent definitions. Use repeatable steps and error reports instead of unrecorded manual changes.

### Power BI orientation
The course introduces Power BI, its licensing and installation considerations, then uses it to acquire and transform data. Power Query prepares data; the model stores tables and relationships; reports present results. Follow the current vendor guidance for installation and licensing, particularly for a Mac setup. The original lesson links provide the course's setup material.

#### Exam answer pattern
Describe each ETL stage and a concrete quality check, then explain how a failure would affect the business conclusion.
""", ["Extract gathers, Transform prepares, Load stores analytical data", "Reconcile counts, keys and totals at each ETL stage", "Freshness, provenance and repeatable transformations support reliability", "Power Query prepares data before modelling and reporting in Power BI"],
        "A pipeline extracts 10,000 orders but loads 8,900. How would you determine whether the resulting KPI can be trusted?",
        "Reconcile row counts and investigate the transformation rules before treating the difference as valid filtering.",
        "Trace exclusions, joins, duplicates and failed parses. Reconcile order IDs and totals against the source. Document legitimate filters and correct unintended losses, then recalculate the KPI using its stated population and period.",
        "Which is a transformation operation?",
        ["Standardising date and currency formats", "Defining a business objective", "Interpreting a p-value", "Presenting a recommendation"], 0,
        "Transformation prepares and standardises extracted records for analysis."),

    _lesson("2.4", "Mastery of Tools, Ethical Decision-making, and Collaborative Frameworks", 81229, """
### Choose tools for the analytical job
Excel supports transparent calculations and PivotTables; Power Query supports repeatable preparation; Power BI combines data modelling, calculations and reporting. Larger or more automated workflows may use SQL, Python or R. Explain why the tool fits the data volume, collaboration requirements and user's skills.

### Acquire and transform data in Power BI
Follow the lesson's invoice and customer-information walkthrough. Inspect each table's columns, types and row counts. Transform data in Power Query, rename fields clearly and retain the steps so another analyst can reproduce the import. Avoid a join that multiplies invoice rows or hides unmatched customer IDs.

### Ethics and teamwork
Specify who owns the data, who may access it, which purpose the analysis serves and what information needs protection. Agree on metric definitions and validation responsibilities. A shared report is useful only when its inputs and methods are understandable.

### Version control
A version-control system records changes and allows review or recovery. Use meaningful commits, branches for separate work, review before integrating changes and resolve conflicts intentionally. Keep raw and processed datasets distinguishable. Git is well suited to code and text; large binary workbooks also need an agreed file-versioning and storage process.

#### Exam answer pattern
Tool choice → workflow and transformations → validation → ethical constraints → collaboration and change tracking.
""", ["Match analytical tools to workflow, scale and collaboration needs", "Inspect invoice/customer imports and retain transformation steps", "Agree ownership, access, responsibilities and common definitions", "Meaningful version history makes analysis reproducible and reviewable"],
        "Two analysts edit the same sales workbook and obtain different totals. Propose a collaborative workflow that prevents this.",
        "Include a common source version, reproducible transformations and review.",
        "Freeze a referenced raw-data version, agree calculation definitions, separate working changes and retain a documented transformation pipeline. Review differences before integrating them. Record which dataset and workbook version produced the final totals.",
        "What is the strongest reason to retain transformation steps?",
        ["To avoid checking results", "To make files larger", "To replace ethical review", "To reproduce and review how raw data became the analytical dataset"], 3,
        "Documented transformations let a colleague trace and repeat the analytical workflow."),

    _lesson("3.1", "Problem-solving Using Statistical Inferences", 81257, """
### Turn a business question into a testable claim
Define the population, outcome, comparison and practical decision. For a two-group mean comparison, H₀ commonly states equal population means; H₁ states a difference or a pre-specified direction. Choose alpha and the test before interpreting the result.

| Analytical question | Candidate method |
|---|---|
| Compare two independent means | Two-sample t-test, subject to assumptions |
| Compare matched observations | Paired t-test |
| Compare several group means | One-way ANOVA |
| Explore numerical associations | Regression or suitable correlation |
| Compare categorical frequencies | Chi-square test, subject to expected-count conditions |

### Evaluate rather than merely calculate
Check independence, sampling, distribution and the relevant variance assumptions. Multiple tests raise false-positive concerns. Report effect size and confidence intervals as well as the decision about H₀. A statistically detectable difference may be too small to change operations.

Create an outcome-evaluation plan: objective, data requirements, method, assumptions, quality checks, interpretation, decision criteria and reporting responsibilities. Advanced inference methods should solve a specific problem rather than be selected for complexity alone.

### Power BI data models
Inspect tables and keys before creating relationships. Check cardinality, matching data types and missing matches; automatically detected relationships still need review. A wrongly configured relationship can distort aggregations before a statistical test is even considered.
""", ["Translate the business problem into population, outcome and hypotheses", "Choose the test according to measurement types and study design", "Report practical magnitude and uncertainty alongside statistical significance", "Review Power BI table relationships and keys before using model outputs"],
        "The same 25 employees are measured before and after training. Which test design fits, and what should your conclusion contain?",
        "Each employee supplies a pair; explain practical improvement as well as significance.",
        "A paired design analyses each employee's before-after difference. Check assumptions on those differences, state H₀ and alpha, report the mean change and interval, and interpret the p-value and operational importance without claiming causation beyond the design.",
        "Which design calls for a paired analysis?",
        ["Two unrelated customer samples", "The same participants measured before and after", "Three unrelated warehouses", "Two categorical frequency tables"], 1,
        "Paired analysis accounts for the relationship between repeated observations on the same units."),

    _lesson("3.2", "Iterative Error Elimination in Practice", 81272, """
### Improve the analytical process in controlled cycles
Errors can enter through collection, processing, model selection or interpretation. A suspicious result is a reason to investigate, not permission to change the data until the result looks desirable.

1. Save the original input and reproduce the finding.
2. Profile the relevant fields and trace transformation steps.
3. Identify the root cause and a justified correction.
4. Change one documented part of the workflow.
5. Repeat validation and analysis; compare the outcome.
6. Introduce a prevention check and retain a change log.

### Power Query cleaning
The lesson applies removal of unnecessary columns, treatment of missing values, duplicate checks, filtering, renaming and type changes. Decide whether a blank means unknown, not applicable or not yet observed. Removing every blank row without checking its meaning can bias the remaining sample.

Deduplicate using the fields that define a real record. An ID can prevent identical business records from being detected if it is included without thought. On the other hand, two equal-valued transactions can be genuine distinct events.

### Judge the corrected result
Check row counts, ranges and totals after every step. Explain how the correction affects coefficients, uncertainty or a KPI. Compare error rates before and after, and verify that the new workflow behaves consistently on a fresh sample.

#### Exam answer pattern
Observed fault → cause and evidence → documented correction → recheck → prevention.
""", ["Use repeatable detect-diagnose-correct-recheck cycles", "Power Query cleaning includes types, missing values, duplicates, filters and naming", "The meaning of a record determines deduplication keys", "Compare validation and analytical results before and after the change"],
        "A text-to-date conversion removes one region's records. Explain an iterative fix and verification plan.",
        "Inspect locale and parse failures rather than deleting all failed dates.",
        "Reproduce the failure and inspect the source format and locale. Correct the conversion rule, retain failed rows for review, reconcile regional row counts and totals, rerun the KPI and add a parse-failure alert to prevent recurrence.",
        "After fixing a transformation, what should happen next?",
        ["Delete the raw data", "Assume the model is correct", "Repeat validation and compare the analytical result", "Hide the change log"], 2,
        "A correction must be checked for effectiveness and unintended consequences."),

    _lesson("3.3", "Scenario Building With Confidence Levels", 81285, """
### Make uncertainty explicit
Scenario analysis explores plausible outcomes under different assumptions. Define the decision, time horizon, uncertain drivers and measurable outcomes. For demand planning, drivers could include customer growth, average order size and fulfilment capacity.

Separate **scenarios** from **confidence intervals**: a pessimistic scenario describes assumed conditions; a confidence interval estimates uncertainty in a parameter. A prediction interval concerns a future observation. These are different objects even when presented together.

### Build and check scenarios
Create baseline, favourable and adverse cases using internally consistent assumptions. Calibrate inputs against historical evidence, review plausibility with subject experts and stress-test extreme conditions. Use sensitivity analysis to show which assumptions drive the decision.

**Monte Carlo simulation** repeatedly draws uncertain inputs from specified distributions and calculates resulting outcomes. **Bootstrapping** resamples observed data to study estimator variability. **Bayesian inference** combines a prior with evidence to update uncertainty. These methods depend on explicit assumptions and do not turn a weak dataset into certainty.

### Spreadsheet practice
Use separate cells for assumptions, calculations and outputs. In a simple illustration, `Revenue = Customers × AverageSpend`; vary both drivers and compare outcomes. Random simulations should record input distributions, iteration count and the approach used to reproduce the results.

#### Exam answer pattern
Decision and drivers → evidence and assumptions → plausible scenarios → uncertainty and stress test → recommendation and monitoring.
""", ["Define the decision, horizon, drivers and assumptions before building scenarios", "Scenario, confidence interval and prediction interval answer different questions", "Historical calibration, stress tests and expert review assess plausibility", "Monte Carlo, bootstrapping and Bayesian inference model uncertainty in different ways"],
        "Forecast revenue with 1,000 baseline customers spending 50 each. Compare an adverse case of 800 spending 45 and a favourable case of 1,100 spending 55. What else is needed before choosing a staffing level?",
        "Calculate each case, then ask about capacity, probabilities and assumption evidence.",
        "Baseline revenue is 50,000, adverse 36,000 and favourable 60,500. Staffing also requires service demand and capacity, plausible driver assumptions, uncertainty and costs of understaffing/overstaffing. These three figures are scenarios, not a 95% confidence interval.",
        "A pessimistic scenario is automatically the lower bound of a 95% confidence interval.",
        ["True: both mean a low value", "True: all scenarios have 95% probability", "True: confidence equals severity", "False: scenario assumptions and parameter intervals are different"], 3,
        "Scenario conditions are not equivalent to the sampling uncertainty quantified by a confidence interval."),

    _lesson("3.4", "Critical Assessment of Data Models", 81297, """
### Evaluate the errors that matter
For a classifier, define the positive class and inspect a **confusion matrix**: true positives (TP), false positives (FP), false negatives (FN) and true negatives (TN).

| Metric | Formula | Question |
|---|---|---|
| Accuracy | `(TP + TN) / total` | What fraction was classified correctly? |
| Precision | `TP / (TP + FP)` | How trustworthy are positive predictions? |
| Recall | `TP / (TP + FN)` | How many actual positives did we find? |
| F1 | `2 × precision × recall / (precision + recall)` | How do precision and recall balance? |

Accuracy can be misleading for rare events. Choosing a threshold trades false-positive and false-negative costs. A **ROC curve** compares true-positive rate with false-positive rate across thresholds; AUC summarises that ranking performance. The course also introduces partial AUC and decision-curve analysis, which focus attention on a relevant operating range or decision benefit.

### Validate and monitor
Separate training from evaluation, check leakage, compare a baseline and assess performance across relevant groups. Use suitable regression errors for numerical predictions. Track changing inputs, error rates and fairness after deployment; good past performance may deteriorate.

### Power BI practice
Conditional formatting and table/matrix summaries can highlight KPI deviations and error patterns. Define the measure and context before using colour to signal success or failure.
""", ["Use the confusion matrix to interpret accuracy, precision, recall and F1", "Rare-event accuracy can hide a model that finds no positive cases", "ROC/AUC and decision-focused assessment examine threshold trade-offs", "Validate independently and monitor drift, fairness and performance over time"],
        "A fraud model labels every case non-fraud and achieves 99% accuracy. Is that enough? Explain the metric you would inspect.",
        "Ask how many real fraud cases the model detected.",
        "No. If fraud is rare, predicting only the majority class can achieve high accuracy with zero recall. Inspect the confusion matrix, recall and precision, then choose a threshold using missed-fraud and false-alarm costs and validate on held-out data.",
        "Which metric directly measures the proportion of actual positives detected?",
        ["Recall", "Precision", "MAE", "Adjusted R²"], 0,
        "Recall is TP divided by TP + FN."),

    _lesson("4.1", "Implementing Reliability Checks and Error Detection", 81323, """
### Profile before trusting a result
Assess the dataset's row count, types, keys, missingness, ranges, distributions and refresh date. **Reliability** requires repeatable collection and consistent processing. Incorrect units or stale information can undermine an otherwise accurate calculation.

| Check | Example | Follow-up |
|---|---|---|
| Range | Negative age | Compare with the original record |
| Logical consistency | Completion before start time | Inspect parsing and timestamps |
| Completeness | Blank required outcome | Investigate its meaning and pattern |
| Uniqueness | Repeated business record | Review deduplication keys |
| Distribution | Sudden change in spread | Check process changes and real events |

### Use statistics and context together
Mean, median, mode, variance, standard deviation and plots can expose unusual patterns. A z-score indicates distance from the mean in standard-deviation units; `z = (x − mean) / sd`. A value beyond ±3 is a flag for investigation under an appropriate distribution, not an automatic proof of error.

Validation rules and statistical tests complement source verification. Compare subgroup coverage and the effect of exclusions. Imputation requires a defensible method and a record of what was imputed. A hypothesis test does not by itself certify the quality of the entire dataset.

#### Exam answer pattern
Identify the quality rule → show the failed check → investigate the cause → justify correction or retention → report the effect on the result.
""", ["Profile keys, types, counts, missingness, ranges and distribution", "Validation should include cross-field logical checks", "Outlier flags require contextual investigation", "Document imputation, exclusions and their impact on the analysis"],
        "An order is recorded as completed two days before it was placed. List checks and a defensible response.",
        "Check date format, time zone, column meaning and source records.",
        "Verify timestamps and their meanings, inspect locale/type conversion and cross-check the source. Correct a confirmed parsing error or flag the record if its true values cannot be established. Document the decision and its impact rather than silently changing dates.",
        "A z-score outside ±3 proves that an observation must be deleted.",
        ["True in every dataset", "False: investigate distribution and business context", "True only because it is numeric", "True if the result becomes significant"], 1,
        "An unusual observation may be valid; deletion needs a justified reason."),

    _lesson("4.2", "Evaluative Techniques for Data-driven Outcomes", 81336, """
### EDA creates questions; tests evaluate specific claims
**Exploratory Data Analysis** studies the distribution and structure of a dataset. Inspect central tendency, spread, missingness, groups, correlations, time trends and potential outliers. Histograms, box plots, scatter plots and PivotTables can make patterns easier to see.

### Move from pattern to a defensible result
Suppose one market has more total sales. That may reflect more transactions, larger quantities or higher prices. A t-test comparing unit prices tests only a difference in mean unit prices; it does not explain the whole difference in total sales. State the quantity each analysis actually addresses.

Use simple or multiple regression for suitable numerical outcomes. Interpret coefficients while holding the other included predictors constant, examine model performance and residuals, and validate on suitable data. Choose tests according to the question and assumptions rather than according to whichever output looks favourable.

### Practical workflow
Profile and clean data → use EDA to identify patterns → formulate a specific hypothesis → choose and perform the analysis → assess uncertainty → connect the result to a business action. Avoid presenting an exploratory correlation as causal evidence.

### Power BI tooltips
Tooltips add contextual details to a report without overcrowding its main visual. Use meaningful labels, relevant measures and consistent context so a user can understand the underlying population and comparison.
""", ["EDA explores distributions, groups, time patterns and quality issues", "A test answers its stated question, not every related business question", "Regression interpretation needs assumptions, residuals and validation", "Use contextual Power BI tooltips to clarify a report's measures"],
        "The UK contributes more total revenue than other markets. A t-test finds different mean unit prices. Does that test explain the revenue difference?",
        "Revenue also depends on quantities and transaction volume.",
        "No. The test addresses mean unit prices only. Investigate transaction counts, quantities, product mix and period coverage alongside prices before interpreting the total-revenue difference.",
        "What is the primary role of EDA?",
        ["Prove causality from every pattern", "Replace data cleaning", "Explore data structure, patterns and issues before focused analysis", "Guarantee a significant p-value"], 2,
        "EDA informs hypotheses and method choice; it does not automatically confirm them."),

    _lesson("4.3", "Ethical Principles in Data Analysis", 81352, """
### Responsible analysis has technical and ethical requirements
The course examines privacy, security, fairness, transparency and accountability. Define the legitimate purpose and affected stakeholders before gathering or analysing data. Restrict collection and access to what the purpose requires and document the governing rules.

### Recognise bias and assess fairness
Selection and sampling bias can exclude relevant populations. Observer bias can influence collection and interpretation. Algorithmic bias can reproduce historical inequalities. Compare data coverage and relevant performance measures across groups instead of assuming that a good overall score guarantees fair outcomes.

Individual fairness and group fairness are distinct perspectives. Different fairness criteria may conflict; explain the chosen criterion and its relevance to the decision. Removing a demographic column alone does not eliminate all bias because other fields can act as proxies.

### Make the work understandable
Record data sources, transformations, model choice, assumptions, limitations and decisions. Explain what the model can and cannot support. Protect identifiers and follow the applicable data-use requirements; the original course covers GDPR and related regulatory concepts.

#### Exam answer pattern
Purpose and stakeholders → privacy and access → possible bias → concrete mitigation → transparent reporting and accountability.
""", ["Privacy, security, fairness, transparency and accountability guide responsible analysis", "Historical, sampling and algorithmic bias can affect model outcomes", "Check subgroup coverage and performance, not only an overall average", "Document methods, assumptions and limitations without overstating results"],
        "A model works well overall but has twice the error rate for a small customer group. What should your evaluation report include?",
        "Explain representation, error costs and subgroup evidence.",
        "Report both overall and subgroup results, uncertainty and sample sizes. Investigate coverage, labels and proxies, assess the consequences of errors, test mitigations and document unresolved limitations before recommending use.",
        "Removing a protected attribute always removes model bias.",
        ["True because the column is gone", "True if accuracy rises", "True if the model is automated", "False because proxies, labels and sampling can still encode bias"], 3,
        "Bias can remain through data selection, historical labels and correlated proxy variables."),

    _lesson("4.4", "Applying Ethical Considerations in statistical inferences", 81368, """
### Inference depends on study design and representation
A mathematically correct test can still support an unfair or misleading conclusion if the sample, question or interpretation is flawed. Evaluate who is represented, how observations were selected, what was measured and which alternative explanations remain.

### Bias and confounding
**Bias** systematically distorts estimates. **Confounding** arises when another factor is related to the exposure or predictor and the outcome, complicating the interpretation of their association. For example, store location may be related to both promotion intensity and sales, so an observed promotion-sales relationship need not be the causal effect of advertising.

Use appropriate design, balanced sampling, relevant covariates or other justified methods to investigate these problems. Disclose remaining limits. Do not claim that a small p-value eliminates confounding or that a regression coefficient alone establishes a cause.

### Transparent reporting and responsible collaboration
Describe sampling, exclusions, tests, confidence intervals and assumptions. Report contradictory findings and unsuccessful tests when relevant to the question. Share only data appropriate for the agreed purpose and access arrangements, and retain enough methodological detail for authorised reviewers to reproduce the work.

#### Exam answer pattern
Statistical finding → design and representation → bias/confounding → mitigation → bounded conclusion and ethical communication.
""", ["Correct arithmetic cannot repair a biased design or unsupported claim", "Confounding is an alternative explanation of an observed association", "Transparent reporting includes exclusions, uncertainty and assumptions", "Responsible collaboration balances reproducibility with appropriate data protection"],
        "Stores with more advertising have higher sales, but they are also in larger cities. Explain the inference problem and a better evaluation.",
        "City size could affect both advertising and sales.",
        "City size is a possible confounder. Consider study design and relevant covariates, compare appropriately similar stores or use a justified experiment, and report uncertainty. The observed correlation alone does not establish advertising's causal effect.",
        "Which statement best describes confounding?",
        ["Another factor complicates the interpretation of a predictor-outcome relationship", "Every extreme value is false", "The mean equals the median", "A model's filename changed"], 0,
        "A confounder is related to the predictor/exposure and outcome and can distort an association's interpretation."),

    _lesson("5.1", "Identifying and Discussing Erroneous Data", 81380, """
### Describe the quality failure precisely
Evaluate accuracy, completeness, consistency, timeliness and reliability. Other useful checks include validity, uniqueness and relevance. **Dirty data** contains faults or inconsistencies; **noisy data** includes unwanted variation; **dark data** is collected but not effectively used. These terms describe different problems.

Use Excel and Power Query to profile missing values, invalid types, duplicates and inconsistent labels. Retain raw data and record the rule used for each change. Counting errors by field and source can reveal where prevention should be focused.

### Discuss errors constructively
An error report should contain a reproducible example, affected records, the violated rule, business impact, proposed action and the owner of the decision. Explain uncertainty if the correct value cannot be determined. Focus on the process rather than assigning blame.

### DAX columns and measures in Power BI
The course introduces DAX, calculated columns, date hierarchies and more complex measures. A calculated column produces row-level values stored in the model. A measure is evaluated in the current filter context, such as a report's selected year or customer group. Explain which one your calculation needs.

For example, a row calculation can derive an order's total; a measure aggregates relevant orders for the current selection. Validate totals against an independent calculation. Keep date types and relationship paths correct so a date hierarchy does not create misleading comparisons.
""", ["Differentiate dirty, noisy and dark data", "Assess accuracy, completeness, consistency, timeliness and reliability", "Communicate a reproducible error, business impact and proposed remedy", "DAX calculated columns and measures use different evaluation contexts"],
        "You need an order-level value and a total that changes with the selected region in Power BI. Explain the difference between a column and a measure.",
        "One belongs to each row; the other is evaluated for the report's current filter context.",
        "Use a row-level calculated column when a stored per-order value is needed. Use a measure for the regional total evaluated under the current filter context. Check both against source values and ensure relationships filter the intended records.",
        "Which calculation is most naturally a measure?",
        ["An imported customer ID", "Total sales for the current report filters", "A stored booking date", "A source filename"], 1,
        "A measure recalculates its aggregate according to the current context."),

    _lesson("5.2", "Confidence in Data: Methods and Approaches", 81392, """
### Confidence comes from evidence about the whole workflow
Data confidence involves source provenance, completeness, representativeness, consistent processing, valid methods and uncertainty. It is broader than selecting a confidence level for a statistical interval.

### Adapt the method to the problem domain
Use a structured template: business question, stakeholders, population, variables, data sources, quality rules, ethical requirements, analytical method, validation and decision criteria. Different domains have different constraints: timeliness in streaming systems, rare outcomes in health data, seasonality in retail and changing patterns in financial data.

The course surveys advanced techniques, including Complex Event Processing (CEP) and neural networks. CEP analyses patterns of events in a stream; neural networks learn complex mappings from examples. An advanced method requires appropriate data, validation and a reason it improves the intended decision.

### Assess confidence after analysis
Audit sources and transformations, examine missingness and sampling, check assumptions, test sensitivity to reasonable processing choices, validate predictions appropriately and obtain domain review. Track whether changed conditions undermine the analysis.

### Reporting
State the result, the evidence supporting it, assumptions, uncertainty and any limitation that could change the recommendation. Data governance and regular audits support confidence by making ownership and checks consistent over time.
""", ["Data confidence covers source quality, methods, uncertainty and validation", "Adapt analysis to a structured problem-domain template", "Advanced techniques such as CEP and neural networks need a justified use case", "Audit and sensitivity checks test confidence after analysis"],
        "A reliable model was trained two years ago. How would you decide whether it supports this month's decision?",
        "Check whether data, population, definitions and operations have changed.",
        "Audit current sources and transformations, compare input distributions and outcome definitions, evaluate on recent data and inspect subgroup performance. If drift or changed conditions weaken the evidence, update or limit the recommendation and report the uncertainty.",
        "What most strengthens data confidence?",
        ["Choosing the most complicated model", "Hiding uncertain results", "Traceable sources, quality checks and appropriate validation", "Using a larger font"], 2,
        "Confidence is supported by evidence throughout collection, preparation, analysis and evaluation."),

    _lesson("5.3", "Collaboration Tools and Version Control", 81402, """
### Make changes traceable and results reproducible
The course compares collaboration and version-control systems including Git, SVN and Mercurial. Their shared purpose is to record changes and coordinate work. Agree on naming, review, ownership, storage and access before several people modify the same analysis.

### A practical Git workflow
Start from the agreed baseline, create a branch for a coherent change, inspect the difference, make a meaningful commit, review it and merge deliberately. Resolve conflicts by understanding both changes. Record which raw-data version and transformation produced the report.

Large binary workbooks cannot be reviewed like line-based code. Use an appropriate storage and versioning process, plus a change log and ownership rules. Avoid ambiguous filenames, unreviewed overwrites and simultaneous incompatible edits.

### Ethical collaboration
Respect data ownership and appropriate access. Share methodology and approved outputs rather than leaking private rows or credentials. Make uncertainty and conflicts of interest visible. Clear communication is part of reproducibility.

### Power BI calculations
The course applies Excel-like financial and statistical calculations in Power BI. Explain row context versus filter context, validate aggregate measures against the source and state the units, period and assumptions behind financial calculations. Do not assume that every spreadsheet formula transfers unchanged into DAX.
""", ["Version control coordinates changes and records a reproducible history", "Use branches, meaningful commits and deliberate conflict resolution", "Dataset and workbook versions need explicit storage and review rules", "Power BI financial/statistical calculations require context, units and verification"],
        "A colleague changes a cleaning rule while you change a KPI definition. How should the team integrate these changes?",
        "Review each effect separately and record the resulting dataset/report versions.",
        "Keep both changes identifiable, compare differences, agree intended definitions and run validation before merging. Recompute the KPI from the resulting data and record source version, transformations, definition and review decision.",
        "What makes an analytical result reproducible?",
        ["Keeping only the latest screenshot", "Using final_final.xlsx", "Deleting earlier transformations", "Recording dataset, code/transformation and definition versions"], 3,
        "A result can be reproduced when the inputs, methods and definitions that produced it are known."),

    _lesson("5.4", "Advanced Communication Strategies Specific to Data Analysis", 81413, """
### Explain findings for the audience's decision
Lead with the business question and a supported finding. Explain the practical meaning, uncertainty, limitations and recommended action. For non-experts, replace unexplained technical vocabulary with plain language and a concrete example; retain technical details for reviewers who need them.

### A useful communication structure
Question → evidence → interpretation → recommendation → limitations and next check. Tables and simple visuals can expose comparisons; a narrative should not imply stronger evidence than the analysis supports. State both the size of an effect and uncertainty around it.

### Team and project communication
Agree responsibilities, decision owners, deadlines and escalation routes. Record risks and mitigation actions. In diverse, remote or hybrid teams, provide accessible shared notes, clear definitions and opportunities to clarify assumptions. Cultural or disciplinary differences can change how the same finding is interpreted.

### Statistical results in Power BI
The lesson also covers regression and ANOVA in the Power BI workflow. Explain what the dependent variable, predictor or grouping variable represents, which calculation produced the output and how assumptions were checked. Regression studies numerical relationships; ANOVA compares group means. Neither automatically establishes a cause.

#### Exam answer pattern
Write the conclusion in ordinary language, support it with the relevant statistic, disclose uncertainty and specify a feasible next action.
""", ["Adapt analytical explanations to stakeholders and decisions", "Connect evidence, interpretation, recommendation and limitations", "Clear roles and risk communication improve team coordination", "Interpret regression and ANOVA in terms of the original variables and design"],
        "A manager asks whether a new process improves service. How would you communicate a small improvement with a wide interval?",
        "Distinguish the estimate from the strength of the evidence.",
        "Explain the estimated improvement and its operational size, then say that the wide interval leaves meaningful uncertainty. Recommend a proportionate next step such as more observations or a controlled pilot, rather than claiming definite success.",
        "Which explanation is most useful to a non-technical decision-maker?",
        ["The estimated improvement, its uncertainty and a justified next action", "Only the software name", "Only the p-value with no context", "An assurance that the model cannot fail"], 0,
        "Communication should connect evidence to a practical decision while retaining its limitations."),

    _lesson("6.1", "The Complete Data Analysis Pipeline", 81440, """
### Guided project: Superstore
Module 6 applies a complete workflow to the **Superstore** dataset, using guided Excel and Power BI steps. Begin with stakeholder objectives and measurable business questions, then assess whether the dataset can answer them.

| Step | Deliverable |
|---|---|
| 1. Business problem | Objectives, stakeholders and success criteria |
| 2. Dataset assessment | Metadata, types, coverage and quality issues |
| 3. Cleaning and processing | Reproducible prepared data and change log |
| 4. EDA | Relevant summaries, comparisons and patterns |
| 5. Interpretation | Meaning, statistical evidence and limitations |
| 6. Conclusion | Supported findings and actionable recommendations |
| 7. Communication | Audience-appropriate explanation and evidence |

### Prepare the dataset
Keep an original copy. Check dates, numeric fields, category labels, business keys, missing values and duplicates. Decide how to handle outliers using both statistics and context. Apply privacy requirements and retain only relevant information. Reconcile row counts and sales/profit totals after transformations.

Power Query can record the cleaning sequence for a repeatable refresh. Check Power BI table relationships before interpreting aggregations. Use the lesson-specific prepared dataset when a later activity supplies one, because different stages may deliberately contain different records.

#### Exam answer pattern
Explain how each step contributes to answering the initial business question, and identify its quality checks and deliverable.
""", ["Follow the seven-step pipeline from business question to communication", "The guided Superstore project connects Excel and Power BI workflows", "Document cleaning decisions and reconcile totals after processing", "Use the dataset version supplied for the specific lesson stage"],
        "Prepare a seven-step plan to investigate falling Superstore profit despite rising sales.",
        "Define both sales and profit, then examine mix, discounts, periods and data quality.",
        "Define the decision and KPIs; assess fields and coverage; document cleaning; explore profit and sales by period, region, category and discount; interpret suitable statistical results; recommend supported actions; communicate evidence, uncertainty and the next monitoring step.",
        "Which step should establish objectives and success criteria?",
        ["Communication only", "The business-problem step", "Deleting outliers", "Choosing colours"], 1,
        "Analysis starts by identifying the question, intended decision and relevant success measures."),

    _lesson("6.2", "Exploratory Data Analysis (EDA) - Part 1", 81448, """
### Superstore: compare time and location
Use the supplied prepared dataset to examine total sales and profit by year and quarter, then region, state and city. The course guides these comparisons using Excel PivotTables and Power BI aggregations.

### Build meaningful summaries
Derive date fields from properly typed dates. Group records by the relevant period or location and aggregate sales and profit using sums. Count transactions when volume is relevant. Reconcile grand totals before interpreting a regional breakdown.

| Analysis | Question to ask |
|---|---|
| Yearly and quarterly totals | Are trends and seasonality visible? |
| Regional sales and profit | Does high revenue also produce profit? |
| State and city comparisons | Is performance concentrated in certain areas? |
| Customer/segment breakdowns | Which groups contribute to the outcome? |

### Avoid misleading comparisons
Check whether every period is fully observed. A partial year's total should not be directly treated as a full-year decline. Separate the amount sold from profitability. A location with high sales may have weak profit because of costs or discounts.

Use the business question to guide further investigation. EDA exposes a pattern; it does not automatically identify its cause. Retain filters, denominators and time coverage so another analyst can reproduce the comparison.

#### Exam answer pattern
State the comparison, aggregation and population; describe the finding; check coverage; explain a justified next investigation.
""", ["Compare Superstore sales and profit by year, quarter and location", "Use sums, counts and date grouping appropriate to the question", "Check full-period coverage and reconcile grand totals", "High sales and high profitability are different outcomes"],
        "Region A sells 100,000 with profit 5,000; Region B sells 60,000 with profit 9,000. Compare revenue and profit margins.",
        "Margin equals profit divided by sales; explain both volume and efficiency.",
        "A has higher sales but a 5% margin. B has a 15% margin and higher absolute profit. Investigate product mix, discounts and costs rather than judging success only by sales volume.",
        "A location has the highest revenue. What can you conclude immediately?",
        ["It has the highest margin", "Its discounts are optimal", "It has the highest recorded revenue for the stated scope", "It caused company growth"], 2,
        "Revenue alone does not establish profitability, efficiency or causation."),

    _lesson("6.3", "Exploratory Data Analysis (EDA) - Part 2", 81453, """
### Superstore: examine products and customer segments
Continue the guided EDA by comparing categories and sub-categories across regions and states. Identify high- and low-profit products, customer patterns and the implications for rewards or targeted business actions.

### Calculate the quantity you intend to compare
For each relevant group, report sales, profit, transaction count and margin where appropriate. A group's margin is `SUM(Profit) / SUM(Sales)`; an unweighted average of row margins can give a different answer. State the denominator and treat zero sales deliberately.

Use descriptive statistics to assess typical values and spread. Mean, median and mode answer different questions. A few large orders can raise the mean while the median remains low. Inspect outliers and category mix before interpreting a segment as uniformly valuable.

### Investigate business implications
High sales with negative profit warrants examination of discounts, product costs, returns and mix. Customer segmentation can guide an investigation or tailored offer, but an observed group pattern is not evidence that every individual in that group behaves identically.

### Reproduce the analysis
Retain the dataset version, grouping fields, filters and aggregation choices in the workbook or report. Compare totals across Excel and Power BI where both workflows are used. Follow up with a focused hypothesis or model when the question requires more than descriptive evidence.
""", ["Analyse category/sub-category, product and customer-segment performance", "Use aggregate profit divided by aggregate sales for a group margin", "Descriptive statistics reveal both typical values and variation", "Observed segments guide investigation without proving a causal explanation"],
        "A product generates 20,000 sales and −2,000 profit. What would you investigate before recommending that it be discontinued?",
        "A negative result is a signal, but product role and costs matter.",
        "Verify cost/profit calculations, examine discounts, returns, customer mix and period coverage, and consider the product's strategic role and linked purchases. Compare feasible pricing or process changes before recommending discontinuation.",
        "Which is the appropriate aggregate profit-margin calculation?",
        ["SUM(Sales) divided by record count", "Average category label", "SUM(Profit) multiplied by SUM(Sales)", "SUM(Profit) divided by SUM(Sales)"], 3,
        "The group margin uses aggregate profit over aggregate sales, with a stated scope and valid denominator."),

    _lesson("6.4", "Interpreting Results, Formulating Conclusions and Effective Communication", 81458, """
### Superstore: turn analysis into an evaluated conclusion
Step 5 interprets analytical outputs, Step 6 draws supported conclusions and recommendations, and Step 7 communicates findings. Keep each result tied to the original business question.

### Regression
Specify Y and the predictors, state units and check the relevant assumptions. Interpret each coefficient conditional on the other included variables. Review R²/adjusted R², coefficient uncertainty, residuals and suitable validation. Prediction or association does not automatically imply a causal effect.

### ANOVA and hypothesis tests
For one-way ANOVA, organise the same numerical outcome into groups defined by a categorical factor. H₀ states equal population means; H₁ states that at least one differs. The F statistic compares between-group variation with within-group variation. Check assumptions, use the p-value and selected alpha, and do not claim which groups differ without further suitable comparisons.

Do not put arbitrary category codes and the outcome into two columns and treat them as comparable samples. Category codes identify groups; they are not measurements of the outcome.

### Recommend and communicate
Combine numerical findings with business context, uncertainty and practical costs. Distinguish what was observed from what is inferred. Recommend a concrete action, responsible owner and follow-up measure. Use concise tables, plain-language interpretation and explicit limitations rather than only output screenshots.

#### Exam answer pattern
Method and hypotheses → appropriate output → statistical decision → practical interpretation → recommendation and limitations.
""", ["Interpret model output in relation to the business question", "ANOVA compares the same numeric outcome across categorical groups", "Statistical significance is not the same as business importance or causation", "Communicate a supported conclusion, action and follow-up measure"],
        "One-way ANOVA finds p = 0.03 for profit across three product categories at alpha 0.05. What does this support, and what does it not show?",
        "The alternative is at least one differing mean, not every pair being different.",
        "Subject to assumptions, reject equal population means: at least one category mean differs. The result alone does not show which pairs differ, establish cause or quantify business value. Examine effect sizes and suitable follow-up comparisons before recommending action.",
        "A significant one-way ANOVA shows that:",
        ["At least one group mean differs, subject to the test assumptions", "Every pair differs", "The factor necessarily causes the outcome", "All groups have identical variance"], 0,
        "ANOVA's alternative hypothesis is that not all population means are equal."),

    _lesson("7.1", "The Complete Data Analysis Pipeline", 81472, """
### Independent project: Splendor Hotel Groups (SHG)
Module 7 repeats the seven-step pipeline with less guidance, using the **SHG hotel-booking dataset**. The aim is to make and justify analytical choices rather than only follow instructions.

### Steps 1–3: question, assessment and preparation
Define stakeholder goals around bookings, cancellations and revenue. Inspect the supplied data, field meanings, types, coverage and potential quality problems. Preserve a raw copy and record each preparation decision.

The lesson includes missing country values, duplicate checks, date formatting and interpretation of cancellation indicators. Use `Unknown` or another justified treatment for missing country rather than automatically assigning the most common country. Check business fields for duplicate bookings while understanding the role of Booking ID.

### Examine outliers and derived fields
A z-score beyond ±3 flags a potentially unusual revenue value. Check context and the influence on conclusions before excluding it. Correctly interpret 0/1 cancellation values; keep a clear definition for each derived label.

Use the exact dataset supplied at each stage. Later files are prepared teaching versions and need not exactly match a locally cleaned earlier file. Record those differences when reconciling results.

#### Exam answer pattern
Explain the decision, assess whether the data fits, justify preparation choices and show how they protect the eventual interpretation.
""", ["Module 7 applies the pipeline independently to SHG hotel bookings", "Assess definitions, coverage, types and quality before EDA", "Justify missing-country, duplicate and outlier decisions", "Stage-specific datasets can differ; record which version produced each result"],
        "SHG contains blank country values and apparently duplicate bookings with different IDs. Explain how you would prepare these fields.",
        "Blank-country handling and business-record identity need explicit rules.",
        "Inspect why country is missing and retain an Unknown group if appropriate. Define business fields that identify an actual booking and distinguish duplicate records from genuine separate bookings. Record exclusions and reconcile counts before analysing country and revenue.",
        "Why does Module 7 provide less step-by-step guidance?",
        ["Data quality no longer matters", "To practise independent analytical decisions and justification", "Statistical assumptions are unnecessary", "Every dataset gives the same results"], 1,
        "The independent project tests whether the complete workflow can be applied with professional judgement."),

    _lesson("7.2", "Exploratory Data Analysis (EDA) - Part 1", 81480, """
### SHG: booking patterns and lead time
Derive year and month from valid booking dates and compare booking counts over time. Check which months and years are fully observed before interpreting seasonality or growth. The lesson's dataset has unequal time coverage, so totals require context.

**Lead time** is the interval between booking and arrival. Compare its average across distribution channels and customer types. Offline and online travel agents, corporate and direct bookings represent different channels; their labels do not form a numerical scale.

### PivotTables and derived ranges
Count Booking IDs by channel and calculate each channel's share using a stated denominator. Define mutually exclusive lead-time bands such as 0–7, 8–14, 15–30 and over 30 days; validate their counts against the total.

### Encoding categories
The lesson introduces **one-hot encoding** to create separate 0/1 indicators for categories. Each indicator has an interpretable meaning. Arbitrary codes such as Email=0 and Phone=3 do not imply a distance of three units or an ordering suitable for a single linear slope.

### Interpret with restraint
A longer booking lead time is not automatically worse performance. It can matter for forecasting, cancellation exposure or staffing depending on the business question. Separate the observed difference from a claim about why it exists or which channel should be prioritised.
""", ["Analyse SHG bookings by month/year with comparable coverage", "Compare lead time across distribution channels and customer types", "Use mutually exclusive bands and validate counts and percentages", "One-hot encoding represents categories without inventing numerical distances"],
        "One channel has a longer average lead time. What additional evidence would you consider before changing the channel strategy?",
        "Consider booking volume, cancellations, revenue and costs as well as timing.",
        "Verify the definition and distribution of lead time and compare volume, margin, cancellations and acquisition costs over comparable periods. A long lead time may support planning but also expose cancellation risk; the average alone does not justify prioritising or removing a channel.",
        "Why use one-hot indicators for nominal categories?",
        ["To create a meaningful order among all labels", "To remove every category", "To represent group membership without arbitrary numeric distances", "To guarantee causation"], 2,
        "A separate binary indicator represents each category rather than imposing an artificial scale."),

    _lesson("7.3", "Exploratory Data Analysis (EDA) - Part 2", 81486, """
### SHG: cancellations, deposits and revenue
Continue EDA using the lesson's prepared dataset. Compare guest country, cancellation rates, customer types, deposit types, time to cancel and revenue associated with cancelled bookings. Use descriptive statistics to show centre and spread alongside group totals.

### Rates require the correct denominator
For each customer type, `cancellation rate = cancelled bookings in that group / all bookings in that group`. A group with many cancellations may simply contain many bookings. Compare both counts and rates.

| Measure | What it tells you |
|---|---|
| Booking count | Group volume |
| Cancellation rate | Cancellation frequency relative to group size |
| Revenue on cancelled bookings | Revenue associated with cancellations under the dataset definition |
| Typical lead time and spread | Timing and variability |

### Deposits and interpretation
Deposit type may be associated with cancellations, but customer mix, channel and lead time may also differ. Do not infer the causal effect of a deposit policy from an unadjusted comparison alone. Define whether recorded revenue is potential, gross or realised; it should not automatically be treated as proven net loss.

### Useful conclusions
Investigate where cancellation exposure is concentrated, which patterns are robust and which further evidence is needed. Separate a customer's country or type from assumptions about individual behaviour. Recommend a proportionate policy test and monitor cancellation rate, realised revenue and customer impact.
""", ["Compare SHG cancellations by country, customer and deposit type", "Use within-group cancellation denominators and show group sizes", "Clarify the meaning of revenue associated with cancelled bookings", "Deposit associations can reflect customer mix and do not prove policy effects"],
        "Group A has 200 cancellations from 1,000 bookings; Group B has 80 from 200. Which has higher cancellation frequency, and what else should management consider?",
        "Compare rates as well as absolute volume and revenue exposure.",
        "A's rate is 20%; B's is 40%. B has higher relative cancellation frequency, while A has more cancellations. Consider revenue, deposit rules, channel and lead-time mix, uncertainty and the feasibility of interventions before changing policy.",
        "Which group has the higher cancellation rate: 200/1,000 or 80/200?",
        ["200/1,000 because 200 is larger", "Both are identical", "It cannot be calculated", "80/200, which equals 40%"], 3,
        "A rate compares events with the relevant group's total, not only event counts."),

    _lesson("7.4", "Interpreting Results, Formulating Conclusions and Effective Communication", 81491, """
### SHG: complete the independent evaluation
The final lesson joins interpretation, conclusions and communication. Use the prepared stage-specific dataset and retain an audit trail linking each output to its inputs.

### Multiple regression example
The lesson models **Avg Daily Rate** as Y using **Lead Time**, **Nights** and **Guests** as predictors. State the equation `ADR = b0 + b1×LeadTime + b2×Nights + b3×Guests + error`. Interpret each coefficient in its units while holding the other included predictors constant. Review model fit, uncertainty, residuals and suitability for prediction.

### Group comparisons
For ANOVA, choose a numerical outcome and put its observations into groups defined by the relevant factor. Explain H₀ and H₁, the between/within-group variance comparison, p-value, assumptions and practical size of differences. Select parametric or non-parametric methods according to the study design and assumptions.

### Conclusions and recommendations
Synthesize evidence about bookings, lead time, cancellations, deposits and revenue. Distinguish descriptive patterns from model estimates and causal claims. Recommend actions supported by the available data, identify an owner and measure, and acknowledge alternative explanations and incomplete coverage.

### Communication
Use simple descriptive statistics, counts, percentages and readable tables to explain the findings. A strong narrative connects the business question, method, result, uncertainty and action. State limitations and propose the next test instead of presenting unsupported certainty.

#### Exam answer pattern
Question → data version → method and assumptions → result and uncertainty → practical conclusion → recommendation and monitoring.
""", ["Model SHG Avg Daily Rate using Lead Time, Nights and Guests", "Interpret multiple-regression coefficients conditionally and validate the model", "Use correctly grouped outcomes for ANOVA and choose tests by assumptions", "Communicate supported conclusions, limitations and measurable recommendations"],
        "Write a short evaluation plan for predicting SHG average daily rate using lead time, nights and guests, and explain how you would communicate the model's limits.",
        "State Y, X variables, assumptions, validation and what prediction does not establish.",
        "Use ADR as Y with the three predictors, inspect preparation and residuals, interpret coefficients conditionally, report fit and uncertainty and validate on appropriate held-out bookings. Explain that associations do not establish pricing causes and that forecasts may change with season, customer mix or new operating conditions.",
        "In multiple regression, a coefficient usually describes:",
        ["The expected outcome change per predictor unit while other included predictors are held constant", "The outcome's total without assumptions", "A guaranteed causal effect", "The number of bookings in every category"], 0,
        "The coefficient is conditional on the other included predictors and requires interpretation within the model and study design."),
]


def get_evo_course_lessons():
    """Return fresh records so UI-specific additions cannot mutate the curriculum."""
    from evo_tasks import task_index_markdown
    lessons = deepcopy(EVO_LESSONS)
    for lesson in lessons:
        if lesson["lesson_number"] in LESSON_WALKTHROUGHS:
            from evo_tasks import get_evo_task_guides
            from exam_resolver_ui import get_task_display_title
            lesson["content"] += "\n\n#### Original activities and tasks\n\n" + "\n".join(
                f"- [{g['id']}: {get_task_display_title(g)}]({g['source_url']})"
                for g in get_evo_task_guides(lesson["lesson_number"]))
        else:
            lesson["content"] += task_index_markdown(lesson["lesson_number"])
    return lessons


def get_evo_training_modules():
    """Adapt the official seven modules to the existing Training Center schema."""
    modules = {}
    for number, title in enumerate(MODULE_TITLES, start=1):
        lessons = [lesson for lesson in get_evo_course_lessons() if lesson["module_number"] == number]
        name = f"EVO Module {number}: {title}"
        modules[name] = {
            "course": COURSE_NAME,
            "course_code": COURSE_CODE,
            "module_number": number,
            "description": f"Noroff module {number}, lessons {number}.1–{number}.4. Original revision notes, practice and illustrations aligned with the lesson book.",
            "source_url": f"https://learning.noroff.no/mod/book/view.php?id={22832 + number}",
            "lessons": lessons,
            "exercises": [deepcopy(lesson["exercise"]) for lesson in lessons],
            "quiz": [deepcopy(lesson["quiz"]) for lesson in lessons],
        }
    return modules
