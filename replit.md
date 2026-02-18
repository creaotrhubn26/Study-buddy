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
