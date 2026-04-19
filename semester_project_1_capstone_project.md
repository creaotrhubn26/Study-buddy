# Semester Project 1 Capstone: Retail Performance Analysis

## Project Scenario

You work as a junior data analyst for a retail company that sells Budget, Standard, and Premium products across four regions and two sales channels. Management wants to understand annual performance and decide how to improve the next quarter.

Dataset: `/workspaces/Study-buddy/semester_project_1_retail_sales.csv`

The project combines knowledge from:

- `01. Data Analysis Fundamentals`
- `02. Spreadsheet Fundamentals`
- `03. Data Driven Decision-Making`
- `04. Statistical Tools`

## Business Problem

The company needs to understand which regions, channels, and product segments drive revenue and profit, whether campaigns and holidays affect performance, and what actions should be taken next quarter.

## Project Deliverables

- Cleaned dataset
- Data dictionary
- Excel or Google Sheets workbook with calculations
- Dashboard or chart pack
- Short written report
- 5-8 slide presentation
- Reflection on limitations and next steps

## Recommended Workbook Tabs

1. `Raw_Data`
2. `Clean_Data`
3. `Data_Dictionary`
4. `Descriptive_Stats`
5. `Pivot_Analysis`
6. `Statistical_Tests`
7. `Forecasting`
8. `Dashboard`
9. `Recommendations`

## How to Use the Semester Project CSV Resolver

If you receive a new semester-project dataset, upload the CSV in the Universal Exam Resolver under:

`Semester Project CSV Resolver (upload dataset)`

The resolver will automatically generate:

- dataset overview
- data dictionary starter
- missing-value checks
- cleaned dataset with simple imputation rules
- KPI summary
- pivot-style category analysis
- z-score outlier detection
- correlation checks
- simple forecasting if a time column exists
- automatic charts
- method recommendations
- grading checklist
- defense questions and model answers
- presentation outline
- report draft
- downloadable ZIP project package
- optional AI executive summary based only on computed facts

Important: the resolver does not replace your judgement. It gives you a structured first draft. You still need to explain why each method is appropriate, check whether outliers are real or errors, and adapt recommendations to the exact assignment.

## Part A: Data Analysis Fundamentals

### Tasks

1. Define the business problem.
2. Identify internal and external data sources.
3. Classify variables as categorical, numerical, binary, or time-based.
4. Identify data quality issues.
5. Explain ethical and GDPR considerations.

### Suggested Solution

Problem statement:

The retail company needs to understand annual revenue and profit performance across regions, channels, product segments, campaigns, and holiday periods in order to recommend actions for next quarter.

Variable classification:

| Field | Type | Use |
|---|---|---|
| `month` | Time / numerical | Trend and forecasting |
| `region` | Categorical | Regional comparison |
| `channel` | Categorical | Online vs Store comparison |
| `segment` | Categorical | Product segment comparison |
| `units_sold` | Numerical | Demand measure |
| `avg_price` | Numerical | Pricing analysis |
| `discount_rate` | Numerical | Promotion analysis |
| `marketing_spend` | Numerical | Campaign investment |
| `holiday` | Binary | Holiday effect |
| `campaign` | Binary | Campaign effect |
| `customer_satisfaction` | Numerical | Customer KPI |
| `returns` | Numerical | Quality / return KPI |
| `inventory_on_hand` | Numerical | Inventory risk |
| `revenue` | Numerical | Main sales KPI |
| `profit` | Numerical | Main financial KPI |

Data quality findings:

- `customer_satisfaction` has 1 missing value.
- `discount_rate` has 1 missing value.
- `units_sold` has 1 major outlier: `190`.
- Some negative or unusual profit values should be investigated before removal.

Ethics and GDPR:

- This dataset does not include direct personal identifiers.
- If customer-level data is added later, consent, purpose limitation, minimization, and anonymization must be documented.

## Part B: Spreadsheet Fundamentals

### Tasks

1. Import the CSV into Excel or Google Sheets.
2. Clean missing values.
3. Create calculated KPI columns.
4. Build pivot tables.
5. Create charts for management.

### Cleaning Solution

Use these cleaning rules:

- Replace missing `customer_satisfaction` with the median satisfaction value: `3.87`.
- Replace missing `discount_rate` with `0`, assuming no discount was recorded.
- Keep the units outlier but flag it for investigation.

Useful formulas:

```excel
=MEDIAN(K2:K289)
=IF(ISBLANK(K2),$K$median_cell,K2)
=IF(ISBLANK(G2),0,G2)
```

KPI formulas:

```excel
Profit Margin = profit / revenue
Return Rate = returns / units_sold
Revenue per Unit = revenue / units_sold
Campaign ROI proxy = profit / marketing_spend
```

Recommended pivot tables:

| Pivot | Rows | Values | Purpose |
|---|---|---|---|
| Revenue by Region | region | Sum of revenue | Find strongest market |
| Profit by Segment | segment | Sum of profit | Find most profitable segment |
| Channel Performance | channel | Sum revenue, sum profit | Compare Online vs Store |
| Monthly Trend | month | Sum revenue, sum profit | Identify seasonality |
| Campaign Impact | campaign | Average revenue, average profit | Compare campaign vs non-campaign |

## Part C: Data Driven Decision-Making

### KPI Dashboard Solution

| KPI | Result | Target | Status | Interpretation |
|---|---:|---:|---|---|
| Total Revenue | 608018.76 | 600000 | Green | Revenue target reached |
| Total Profit | 165521.63 | - | Monitor | Needs margin context |
| Profit Margin | 27.22% | 32.00% | Amber | Revenue is strong, margin is weak |
| Return Rate | 5.40% | 5.50% max | Green | Returns are controlled |
| Avg Satisfaction | 3.87233 | 3.80 | Green | Customer satisfaction is above target |

Key performance findings:

- Highest revenue region: `East` with `172181.93`.
- Highest profit region: `East` with `48922.13`.
- Highest revenue channel: `Online` with `332739.28`.
- Highest profit channel: `Online` with `88742.73`.
- Highest revenue segment: `Premium` with `237634.40`.
- Highest profit segment: `Premium` with `81592.48`.

Decision recommendation:

Focus next quarter on Premium products and Online channel growth, but review campaign profitability because campaigns increase revenue more clearly than profit.

## Part D: Statistical Tools

### Descriptive Statistics

For `units_sold`:

- Mean: `31.61458`
- Population standard deviation: `16.93392`
- Outliers using `ABS(z) > 3`: `1`
- Outlier record: `units_sold = 190`
- Z-score for 190: `9.35314`

Excel / Sheets:

```excel
=AVERAGE(E2:E289)
=STDEV.P(E2:E289)
=(E2-$mean_cell)/$std_cell
=IF(ABS(z_cell)>3,"Outlier","Non Outlier")
```

### Correlation and Covariance

Useful correlation findings:

| Pair | Correlation | Interpretation |
|---|---:|---|
| marketing_spend vs revenue | 0.26175 | Weak positive relationship |
| marketing_spend vs profit | -0.03093 | Almost no linear relationship |
| discount_rate vs units_sold | 0.35116 | Discounts are moderately associated with units sold |
| campaign vs revenue | 0.25053 | Campaign periods are associated with higher revenue |
| holiday vs revenue | 0.25644 | Holiday periods are associated with higher revenue |

Excel / Sheets:

```excel
=CORREL(marketing_spend_range,revenue_range)
=COVARIANCE.P(marketing_spend_range,revenue_range)
```

### ANOVA Example

Question: Is average profit different across regions?

Summary:

| Region | Count | Sum Profit | Average Profit |
|---|---:|---:|---:|
| North | 72 | 41431.28 | 575.43 |
| South | 72 | 37476.03 | 520.50 |
| East | 72 | 48922.13 | 679.47 |
| West | 72 | 37692.19 | 523.50 |

ANOVA result:

- F-statistic: `3.60250`
- Interpretation: There is evidence that average profit differs by region, with East performing strongest.

Excel ToolPak:

`Data -> Data Analysis -> ANOVA: Single Factor`

### Regression and Forecasting

Monthly revenue regression:

```text
Revenue = 50550.81409 + 18.06399 * month
```

Forecasts:

| Month | Forecast Revenue |
|---:|---:|
| 13 | 50785.64591 |
| 14 | 50803.70990 |
| 15 | 50821.77388 |

Excel / Sheets:

```excel
=SLOPE(monthly_revenue_range,month_range)
=INTERCEPT(monthly_revenue_range,month_range)
=FORECAST.LINEAR(13,monthly_revenue_range,month_range)
```

Important interpretation:

The simple trend forecast is weak because revenue has seasonality and holiday effects. A better project recommendation is to combine regression with seasonal variables such as `holiday` and `campaign`.

## Final Recommendations

1. Prioritize the `Premium` segment because it has the highest profit contribution.
2. Continue investing in `Online`, but evaluate campaign efficiency because marketing spend has weak correlation with profit.
3. Investigate the `units_sold = 190` outlier before using it for forecasting.
4. Maintain holiday planning because holiday periods are associated with higher revenue.
5. Improve profit margin from `27.22%` toward the `32%` target through pricing, campaign efficiency, or return reduction.

## Suggested Report Structure

1. Executive summary
2. Business problem and scope
3. Data description and cleaning
4. Descriptive analysis
5. Statistical analysis
6. Forecasting
7. Dashboard and KPIs
8. Recommendations
9. Limitations
10. Appendix with formulas

## Suggested Presentation Structure

1. Title and business question
2. Dataset and cleaning choices
3. KPI dashboard
4. Region/channel/segment findings
5. Statistical evidence
6. Forecast
7. Recommendations
8. Limitations and next steps

## Grading Rubric

| Area | Excellent |
|---|---|
| Problem definition | Clear business problem, scope, and stakeholders |
| Data preparation | Cleaning decisions documented and justified |
| Spreadsheet work | Correct formulas, pivot tables, charts, and workbook structure |
| Statistical analysis | Correct use of descriptive stats, z-scores, correlation, ANOVA, and forecasting |
| Decision-making | KPIs linked to recommendations |
| Communication | Clear report, accessible visuals, honest limitations |
| Professionalism | Reproducible workbook and documented assumptions |

## Exam-Safe Summary

This project shows the full analyst workflow: define the problem, import and clean data, calculate KPIs, analyze patterns, apply statistical tools, forecast future performance, and turn findings into decisions.
