# Evaluation of Outcomes — curriculum coverage

Course: **FI1BBEO10**. Source books checked through the signed-in Noroff browser on **2026-10-13**.

## Integration

- Learn & Practice: 28 numbered revision lessons under the official course code.
- Training Center: seven official module topics, four lessons/exercises/quiz questions each.
- Existing six supplemental EVO topics and all existing progress keys are retained.
- The exam resolver can select all 28 lessons individually and use their explanations/key points.
- The resolver also indexes all 98 activity/task guides as distinct sources, matches exact task numbers, and offers Lessons + task guides / Task guides only source pools. Matched tasks expose their complete scaffold, source link, workbook and module illustration directly in the resolver. Manual/specific AI source selection includes the task's teaching lesson; bounded AI contexts carry the working guide and its limitations.
- One imagegen illustration per module, with a text explanation and PNG download.
- 98 separately selectable activity/task guides in Norwegian, each with a tailored procedure, method explanation, fill-in answer scaffold and source link. Multi-part tasks cover both Task 1 and Task 2 where present.
- Three downloadable Excel workbooks: reusable calculations (11 sheets), Module 6 tasks (17 sheets), and Module 7 tasks (21 sheets). The module workbooks contain native Raw/Prepared Tables, quality logs, one sheet per analysis objective and four conclusion sheets.

## Content boundary

The added text consists of original study explanations, original worked examples and practice questions. It is not a verbatim reproduction of Noroff books, embedded H5P activities, downloadable solution workbooks or assessment responses. Source links provide the complete school lesson and its original datasets. Power BI setup/licensing is treated as course orientation; the current vendor instructions remain the source for installation.

The notes distinguish statistical association from causation, group codes from numerical measurements, sampling variability from sampling bias, and outlier flags from confirmed errors. These distinctions prevent misleading conclusions when revising.

## Dataset and instruction checks

Module 6 lesson demonstrations use Superstore; its separate activities use CoffeeChain. The continuing **tasks** use Online Shop Customer Sales (12 columns). Module 7 demonstrates SHG hotel bookings; its separate activities use Airbnb. The continuing **tasks** use marketing_campaign_fixed.csv (29 columns). The original course CSVs and solution files are not bundled in this repository.

The task guides explicitly address these source issues:

- Activity 1.3.1 contains inconsistent arithmetic: for 2,4,4,4,5,5,7,9, mean=5 and squared deviations sum=32; population variance=4, sample variance=32/7.
- Activity 3.2.2 contains polling terminology that does not match the retail dataset.
- Activity 3.4.2 has overlapping/conflicting conditional-formatting thresholds; the guide calls for documenting and resolving the source ambiguity.
- Activity number 5.3.2 occurs in two chapters. The UI identifies each by chapter and title.
- Financial time-value tasks need an explicit rate period/horizon and distinguish discounted receipts from full project NPV.
- Z_Revenue is constant (11) in all 2,240 marketing rows. It cannot support a correlation or product-profitability claim. Costs/margins and a CLV model are additional requirements.
- Complain is a flag, not a measured complaint cause. Airbnb availability 365 is a snapshot, not a seasonal time series.

## Validation and limits

Fifteen offline tests cover startup, all 28 lessons, resolver selection, seven Training Center modules, illustration downloads, all 98 guides, task selection and native workbook structure. Resolver checks include exact-task matching, task-only selection with the correct workbook, identifier boundaries, AI context selection with the parent lesson, all five Task 7.2 objective views, scaffold refresh/preserved edits, stale AI answer disclosure, and the general statistical calculator. Tests run in temporary directories to preserve saved progress. The AI context construction is tested offline; no live model answer is asserted by these tests.

The resolver has a numbered question → resources → answer flow. File attachments, settings, syllabus excerpts and alternative drafts are collapsed by default. Task 7.2 offers English steps for one objective at a time, with the exact worksheet name and its data limitations. Its complete resolver guide is also available in English. AI answers are instructed to use English regardless of the question language. Other existing lesson/activity guide content retains its source wording.

Spreadsheet formulas were recalculated with artifact-tool and checked against numerical fixtures (variance, t critical value, KPI ratios, regression, alpha, classification, scenarios, FV and NPV). Blank inputs and genuine zeros were tested. All 49 workbook sheets were rendered for inspection; no formula errors remained in exported sheets. Native Excel was not used for the final verification. The workbooks are starting templates: students import the original data and create the actual PivotTables, regressions and PBIX outputs.

The calculation runtime could not correctly evaluate T.INV.2T/TINV. The confidence-interval template instead uses a documented Student t quantile table generated with scipy.stats.t.ppf for df 1–39 and confidence 90%, 95%, 99%; INDEX/MATCH selects the value. The table is independently checkable in Excel using T.INV.2T.

## Lesson map

| Module | Lesson | Title | Original chapter |
|---|---|---|---|
| 1 | 1.1 | Data Analysis, Key Performance Indicators (KPIs), and Version Control | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22833&chapterid=81121) |
| 1 | 1.2 | Statistical Inference, Result Table Analysis, and Critical Tools | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22833&chapterid=81137) |
| 1 | 1.3 | Variance Measurement, Confidence Levels, and Problem Solving | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22833&chapterid=81152) |
| 1 | 1.4 | Iterative Error Elimination techniques, Ethical Principles, and Solution Facilitation | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22833&chapterid=81168) |
| 2 | 2.1 | Ensembling Data and Industry Techniques | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22834&chapterid=81184) |
| 2 | 2.2 | Quantitative and Qualitative methods in data analysis | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22834&chapterid=81201) |
| 2 | 2.3 | ETL Systems, Data Analysis Lifecycle, and Ensuring Reliability | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22834&chapterid=81213) |
| 2 | 2.4 | Mastery of Tools, Ethical Decision-making, and Collaborative Frameworks | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22834&chapterid=81229) |
| 3 | 3.1 | Problem-solving Using Statistical Inferences | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22835&chapterid=81257) |
| 3 | 3.2 | Iterative Error Elimination in Practice | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22835&chapterid=81272) |
| 3 | 3.3 | Scenario Building With Confidence Levels | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22835&chapterid=81285) |
| 3 | 3.4 | Critical Assessment of Data Models | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22835&chapterid=81297) |
| 4 | 4.1 | Implementing Reliability Checks and Error Detection | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22836&chapterid=81323) |
| 4 | 4.2 | Evaluative Techniques for Data-driven Outcomes | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22836&chapterid=81336) |
| 4 | 4.3 | Ethical Principles in Data Analysis | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22836&chapterid=81352) |
| 4 | 4.4 | Applying Ethical Considerations in statistical inferences | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22836&chapterid=81368) |
| 5 | 5.1 | Identifying and Discussing Erroneous Data | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22837&chapterid=81380) |
| 5 | 5.2 | Confidence in Data: Methods and Approaches | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22837&chapterid=81392) |
| 5 | 5.3 | Collaboration Tools and Version Control | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22837&chapterid=81402) |
| 5 | 5.4 | Advanced Communication Strategies Specific to Data Analysis | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22837&chapterid=81413) |
| 6 | 6.1 | The Complete Data Analysis Pipeline | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22838&chapterid=81440) |
| 6 | 6.2 | Exploratory Data Analysis (EDA) - Part 1 | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22838&chapterid=81448) |
| 6 | 6.3 | Exploratory Data Analysis (EDA) - Part 2 | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22838&chapterid=81453) |
| 6 | 6.4 | Interpreting Results, Formulating Conclusions and Effective Communication | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22838&chapterid=81458) |
| 7 | 7.1 | The Complete Data Analysis Pipeline | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22839&chapterid=81472) |
| 7 | 7.2 | Exploratory Data Analysis (EDA) - Part 1 | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22839&chapterid=81480) |
| 7 | 7.3 | Exploratory Data Analysis (EDA) - Part 2 | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22839&chapterid=81486) |
| 7 | 7.4 | Interpreting Results, Formulating Conclusions and Effective Communication | [Noroff](https://learning.noroff.no/mod/book/view.php?id=22839&chapterid=81491) |
