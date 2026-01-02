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
- **Learning Outcomes**: Track program-level knowledge, skills, and competence goals (based on NQF)
- **About**: Program information, career opportunities, and study details

## Training Modules

### Concept-Based Training
- Introduction to business intelligence and big data
- Statistical methodologies to extract KPIs
- Correlation, regression, ANOVA, histogram and covariance analysis
- Z-scores and z-testing for outlier reduction

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
- **Statistical Analysis**: Correlation, regression, ANOVA, histogram, covariance, descriptive statistics (using scipy)
- **Power Query Simulator**: Data transformation steps (deduplication, fill missing, trim, case standardization, calculated columns)
- **Z-Score & Outlier Tool**: Calculate z-scores, detect outliers, apply handling methods (remove, cap, replace)

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
