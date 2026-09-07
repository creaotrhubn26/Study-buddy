# Data Analyst Study App

## Overview
A comprehensive student study app for the Data Analyst 2 (PDAN) vocational program at Noroff. Helps students learn course content, practice with hands-on exercises, and track progress toward learning outcomes.

## Features
- **Overview**: Dashboard with study progress metrics and semester breakdown
- **Course Plan**: Full course list with filtering, search, and credits visualization
- **Training Center**: Hands-on learning environment with:
  - Step-by-step lessons for each topic
  - Practical exercises with hints and AI-powered answer checking
  - Multiple-choice quizzes with scoring and explanations
  - Progress tracking per topic
- **Learn & Practice**: 
  - Detailed course content with knowledge, skills, and competence outcomes
  - AI-powered practice questions (general, knowledge-based, skills-based, case studies)
  - Answer checking with feedback
- **Progress**: Track completed courses with checkboxes
- **Study Notes (Enhanced)**: 
  - Categories (lecture, exercise, exam, tips, summary) with filtering
  - Note templates (concept summary, case study, formula sheet, comparison chart)
  - Importance markers (normal, important, critical for exam)
  - Link notes to specific learning outcomes
  - Version history tracking (last 10 edits)
  - AI assistant for generating course summaries, key concepts, exam prep
  - Statistics dashboard (notes by category, course, importance)
- **Learning Outcomes**: Track program-level knowledge, skills, and competence goals (based on NQF)
- **About**: Program information, career opportunities, and study details

## Training Modules

### Concept-Based Training
- Introduction to business intelligence and big data
- Statistical methodologies to extract KPIs
- Correlation, regression, ANOVA, histogram and covariance analysis
- Z-scores and z-testing for outlier reduction

### Data Driven Decision-Making (FI1BBDD75)
- **Four Analysis Philosophies**: Descriptive, Diagnostic, Predictive, Prescriptive analytics with business examples
- **Data Lifecycle**: Define → Collect → Clean → Analyze → Interpret → Act (with SMART goals)
- **Case Studies**: Retail inventory, healthcare readmission, marketing optimization (with before/after metrics)
- **KPI Selection & Tracking**: SMART KPIs, KPIs by function, dashboard design, RAG status, target setting

### Semester Project 1 (FI1BBP175)
- **Project Planning & Execution**: Scope definition, project timeline (phase percentages), deliverables management, solo/team work practices
- **Data Ethics & GDPR**: Ethical principles, GDPR fundamentals (7 principles, legal bases, rights), anonymization techniques
- **Documentation & Presentation**: Analysis report structure, visualization best practices, presentation building, reflection reports
- **Soft Skills for Data Analysts**: Communicating with non-technical stakeholders, active listening, working with different roles, handling feedback

### Evaluation of Outcomes (FI1BBEO10)
Semester 2 course. Assessed by a one-week individual Course Assignment graded
Pass / Fail (level 5.1), so the lesson material is written around producing a
reviewable piece of evaluation work rather than around a timed exam.

**Detailed lessons** (in `course_lessons`, shown in Learn & Practice). These follow
the official Module 1 structure from the LMS:
- **1.0 Course Overview and Assignment Strategy**: module overview and structure, official learning outcomes, outcome-to-lesson map, the four-step evaluation answer structure, the ethical dimension
- **1.1 Data Analysis, Key Performance Indicators (KPIs), and Version Control**: why gut instinct is insufficient, KPIs as lens and yardstick, lagging vs leading as the two main types, quantitative KPIs split into financial and non-financial metrics with the six named metrics, contextualisation, strategic alignment, heuristics, KPI types and industry applications, six real-world case studies, steps for establishing a KPI dashboard, version control for data integrity and collaboration, and **Activity 1.1.1** (the lesson task) with its formula list, method, and a worked example
- **1.2 Statistical Inference, Result Table Analysis, and Critical Tools**: sampled sets and sampling bias, sample size, quantitative vs qualitative evidence, reading a regression result table, R squared and leakage, z-scores and z-testing, a critical-tools table of what each tool cannot tell you
- **1.3 Variance Measurement, Confidence Levels, and Problem Solving**: variance and standard deviation as reliability, five-point summaries and IQR fences, what a confidence level claims, a work method for setting the level by problem domain, multiple probability outcomes with planned responses, sensitivity checks, a problem-solving routine
- **1.4 Iterative Error Elimination Techniques, Ethical Principles, and Solution Facilitation**: the detect-to-prevent cycle, error taxonomy, Five Whys, fishbone categories, tooling, ethical principles and selective evaluation, delivering findings and facilitating solution discussions
- **1.5 Supplementary: Ensembling Techniques and ETL Systems**: covers the two curriculum outcomes (ensambling, ETL) that are not among the four Module 1 lesson titles — bias vs variance, bagging, boosting, stacking, ensembling applied to data, pipeline failure points, ELT, versioning data as well as code

Also has curated flashcards, exam-bank entries, and practice questions.

**Activity 1.1.1** (KPI analysis for a hypothetical business) appears in two places:
the brief, method and worked example are a section of lesson 1.1, and six interactive
exercises sit in the `KPIs & Decision Heuristics` training module. The full worked
solution lives in `EVO_1.1.1_Activity_Solution.md` and
`EVO_1.1.1_KPI_Analysis_Nordtre.xlsx` at the project root.

**Training modules** (hands-on, in the Training Center):
- **KPIs & Decision Heuristics**: KPIs as heuristics, thresholds/alerts, decision trees, KPI-driven escalation
- **Statistical Result Analysis**: Regression interpretation, variance/spread analysis, z-testing for significance, sampled sets and statistical inference
- **Confidence Levels & Scenarios**: Understanding confidence intervals, probability scenario building, decision-making under uncertainty
- **Iterative Error Elimination**: 5 Whys root cause analysis, common error types, debugging techniques, error prevention, plus ethical model evaluation (bias detection, fairness, escalation)
- **Data Ensembling & Reliability**: Bagging, boosting, stacking ensemble methods, improving model reliability, data quality ensembling
- **ETL & Version Control**: ETL pipeline design, Git fundamentals, branching strategies, collaborative workflows

### Data Visualisation (FI1BBDV15)
- **Introduction to Data Visualization**: Why visualization matters, the visualization process, types of visualizations
- **Choosing the Right Chart Type**: Decision framework, common mistakes to avoid, chart selection examples
- **Design Principles**: Data-ink ratio, color usage, typography, layout, accessibility checklist
- **Data Storytelling**: Story structure (setup → insight → action), presentation tips, slideshow best practices
- **Visualization Tools**: Excel/Sheets, Tableau, Power BI, Python libraries comparison
- **Ethics in Visualization**: Truncated axes, cherry-picking, missing context, ethical guidelines

### Analysis Reporting (FI1BBAR05)
- **Introduction to Analysis Reporting**: Purpose of reports, types (ad-hoc, regular, research), audiences
- **Report Structure & Organization**: Executive summary, sections (intro, methods, findings, recommendations), appendix usage
- **Academic Writing Style**: Clarity, objectivity, avoiding jargon, present/past tense conventions
- **Integrating Visualizations**: Figure/table placement, captions, referencing in text, chart selection for reports
- **Universal Design & Accessibility**: Alt text, color contrast, logical reading order, accessibility checklist
- **Report Tools & Distribution**: Word/LaTeX/Markdown, PDF vs interactive, versioning, stakeholder review
- **Ethical Reporting**: Data limitations, uncertainty, avoiding misleading conclusions, reproducibility

### Exam Project 1 (FI1BBP275)
- **Understanding the Exam Project**: Project options (individual, group, internship), scope requirements, industry standards, success factors
- **Project Planning & Scoping**: Problem statements, in-scope/out-of-scope definition, timeline planning, milestone setting, risk planning
- **Working with Real-World Data**: Internship projects, public data sources (SSB, Kaggle, EU Open Data), ethical sourcing, data quality assessment
- **Executing Your Analysis**: Applying Semester 1-2 skills (spreadsheets, statistics, Python, SQL, visualization), analysis workflow, common pitfalls
- **Professional Documentation**: Project/technical/analysis documentation, report structure, version control
- **Presentation & Defense**: Presentation structure, visual design, delivery tips, handling questions, professional terminology
- **Quality & Self-Assessment**: Quality checklists, self-reflection, getting feedback, lessons learned

### Tool Training Environments (Simulated)
- **Excel & Google Sheets**: Formulas (VLOOKUP, SUMIF, etc.), pivot tables, data cleaning, automation with macros
- **Python Programming**: pandas DataFrames, data manipulation, cleaning scripts, analysis automation
- **SQL & Databases**: SELECT queries, JOINs, GROUP BY aggregations, subqueries, window functions
- **Tableau & Power BI**: Dashboard design principles, chart selection, building visualizations
- **Statistical Analysis**: Descriptive statistics, hypothesis testing, choosing the right test, confidence intervals

## Interactive Playground
Hands-on practice tools with editable data:
- **Python Code Runner**: Guided pandas exercises with sample datasets
- **Excel Formula Simulator**: SUM, AVERAGE, SUMIF, COUNTIF, VLOOKUP, INDEX/MATCH, XLOOKUP, IF statements
- **SQL Query Tester**: In-memory SQLite database with customers/orders tables
- **Chart Builder**: Create bar, line, area, and scatter charts from custom data
- **Data Visualization Studio**: Chart selection advisor, accessibility checker, visualization critique, data story builder
- **Statistical Analysis**: Correlation, regression, ANOVA, histogram, covariance, descriptive statistics (using scipy)
- **Power Query Simulator**: Data transformation steps (deduplication, fill missing, trim, case standardization, calculated columns)
- **Z-Score & Outlier Tool**: Calculate z-scores, detect outliers, apply handling methods (remove, cap, replace)
- **Ethical Analysis Critique**: Real-world scenarios (hiring bias, healthcare, credit scoring, policing) with expert critique comparison and ethical principles rating
- **Error Detection Workshop**: Identify 7 types of data errors, learn impacts/solutions, practice stakeholder communication with templates
- **Confidence Level Planner**: Domain-specific work methods (Medical, Financial, Marketing, Operations, Research), interactive CI calculator, work method document generator
- **Report Writing Workshop**: Executive summary builder, clarity rewriter, report structure planner, caption writer
- **Exam Project Toolkit**: Problem statement builder, project scope planner, quality self-assessment, presentation planner

## Semester Structure
Each entry in `courses_data` carries a `semester_number` (1-4). That field is the
single source of truth for semester grouping: the Training Center derives its
semester/course filter from it, and the Course Plan filters on it. Do not add a
second hardcoded course-to-semester map, which is how the two previously drifted
apart.

The student's actual dates come from `STUDY_PATH_JAN2026` in
`study_buddy_state.py` (JAN 2026 full-time intake). `get_active_study_stage()`
and `get_active_semester_number()` resolve which course and semester are in
progress today, which drives the Training Center's default filter and the
"Current focus" banner.

| Semester | Courses |
|---|---|
| 1 | IC, DAF, SPF, DDM, STT, SP1 |
| 2 | EVO, DVS, ARP, EP1 |
| 3 | Databases and Cloud Services, Programming Fundamentals, Programmatic Data Analysis, Semester Project 2 |
| 4 | Industry Tools, Critical Data Thinking, Big Data, Interactive Dashboards, Exam Project 2 |

## Data Source
Course content is sourced from the official Noroff study catalog:
https://studiekatalog.edutorium.no/voc/en/programme/PDAN/2025-autumn

## Technical Stack
- Python 3.11
- Streamlit
- OpenAI API (via Replit AI Integrations)

## Program Details
- 18 courses across 4 semesters
- Total: 120 credits / 3150 hours
- Program start: Spring 2025 (January)
- Duration: 2 years
- NQF Level: 5.2

## Running the App
```bash
streamlit run app.py --server.port 5000
```

## Excel Profiling Script (Reusable)
Use `excel_profile.py` to inspect any `.xlsx` file and print the most important data profile (sheet size, column types, missing values, duplicates, date ranges, numeric summary, and top categories).

### Quick Run
```bash
python excel_profile.py "/path/to/your-file.xlsx"
```

### Show More/Fewer Top Values
```bash
python excel_profile.py "/path/to/your-file.xlsx" --top 5
```

### Profile One Specific Sheet
```bash
python excel_profile.py "/path/to/your-file.xlsx" --sheet "SheetName"
```

### Save Full Profile to JSON
```bash
python excel_profile.py "/path/to/your-file.xlsx" --json-out profile.json
```
