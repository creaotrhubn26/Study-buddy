"""Original English walkthroughs checked against Noroff lessons 7.3–7.4."""

LESSON_ILLUSTRATIONS = {
    "7.3": ("lesson-7-3-customer-insight.png", "Seven marketing objectives: complaints, personas, response/spending, customer segments, household/channels, web engagement and response prediction. The image is conceptual; use your own cleaned data for results."),
    "7.4": ("lesson-7-4-evidence-to-decision.png", "Objective → method → evidence → interpretation → limitation → recommendation and KPI. Choose four objectives and write about half a page each in Conclusion 1–4. Use verified results, not invented CLV, profit or complaint causes."),
}

LESSON_WALKTHROUGHS = {
    "7.3": """
### Lesson 7.3: extend EDA and interpret customer behaviour

Keep the three contexts clear: the guided lesson uses **Splendor Hotel Groups (SHG)** bookings; the separate activity continues its earlier activity dataset; **Task 7.3 uses your cleaned marketing_campaign_fixed.csv** from Tasks 7.1–7.2. The task walkthrough above covers all seven marketing objectives and their Excel worksheets.

### Step 1 — prepare a traceable comparison

Keep Raw unchanged and use the cleaned copy in Prepared. Check variable definitions, numeric types, missing values, duplicate records and unusual observations. Record exclusions, filters, units and the observation period. A historical dataset needs a documented reference year for age; today's year can give misleading ages.

### Step 2 — compare hotel bookings and revenue by country

Use a PivotTable with guest country in Rows and booking count and revenue in Values. Inspect both volume and the revenue distribution, rather than ranking countries by totals alone. Check whether revenue is potential, gross or realised before interpreting it. Country is a grouping label, not an explanation of an individual customer's behaviour.

### Step 3 — compare cancellation rates by customer type

Within each group, calculate **cancelled bookings / all valid bookings in that group**. For a validated numeric 0/1 cancellation flag, its group average is the cancellation rate. Show the count of valid flags alongside the rate; missing flags are not zero.

| Measure | Interpretation |
|---|---|
| Booking count | Group volume |
| Cancellation count | Absolute cancelled volume |
| Within-group cancellation rate | Frequency relative to the group's valid bookings |
| Revenue associated with cancellations | Exposure under the dataset's revenue definition |

A group can have more cancellations but a lower rate because it has more bookings. Compare both measures.

### Step 4 — examine deposits and cancellation exposure

Compare deposit categories, customer types, counts, cancellation rates and revenue associated with cancelled bookings. Use a customer-type × deposit-type cross-tab to inspect whether group composition differs. An association between deposits and cancellations does not establish that a deposit policy caused the pattern. Recorded revenue on a cancelled booking is not automatically proven net loss.

### Step 5 — examine time to cancel and distributions

Compare the time-to-cancel distribution and its mean/median/spread across comparable years and groups. Check what date interval the field actually measures. A shorter time to cancel does not itself mean that the cancellation rate decreased. Restrict timing summaries to records with valid timing values and explain the denominator.

### Step 6 — connect Task 7.3 to seven marketing questions

Use **EVO Module 7 Tasks.xlsx**. Select a task objective above to see its fields, method, worksheet and interpretation check:

1. **Complaints:** compare validated complaint rates and purchase patterns. A flag does not record complaint causes or overall satisfaction.
2. **Personas:** combine recorded demographics, household composition, preferences and channel use. Do not invent personality traits.
3. **Response spending:** compare responders and non-responders with valid counts. Spending differences do not prove campaign lift.
4. **Detailed segments:** define explicit demographic/income boundaries and compare spending patterns. Check tiny groups and unusual values.
5. **Household channels:** reuse household groups and compare store, web and catalogue purchasing over compatible periods.
6. **Web engagement:** inspect complete visits/purchases pairs with a scatterplot. Correlation is an association; a conversion rate needs compatible units and periods.
7. **Response prediction:** verify predictor timing, keep evaluation customers separate and compare a classifier against a training-set baseline. Avoid leakage and test-set tuning.

### Step 7 — write a finding you can defend

Use: **method → result with n and units → interpretation → limitation → proposed test**.

Writing template: “I compared […] using […]. The result was […] across […] valid observations. This suggests […], although […]. I recommend testing […] and measuring […].”

Use your own numerical outputs. The illustration and workbook are study scaffolds, not calculated findings. [Original Task 7.3](https://learning.noroff.no/mod/book/view.php?id=22839&chapterid=81490).
""",
    "7.4": """
### Lesson 7.4: from evidence to a decision

This lesson completes **Step 5: interpretation**, **Step 6: conclusions** and **Step 7: communication**. A finding reports what the data showed; a conclusion answers the business question; a recommendation proposes a justified action to evaluate.

The guided examples use **Splendor Hotel Groups (SHG)**. **Task 7.4 continues your cleaned marketing_campaign_fixed.csv** and your analyses from Tasks 7.2–7.3. Keep the hotel examples, separate activity and marketing task distinct.

### Step 1 — interpret multiple linear regression

The hotel example models **Avg Daily Rate** as Y using **Lead Time, Nights and Guests** as X variables:

`ADR = b0 + b1 × LeadTime + b2 × Nights + b3 × Guests + error`

Prepare aligned numeric rows and document exclusions. In desktop Excel, enable Analysis ToolPak if needed, then use **Data → Data Analysis → Regression** with the Y column and adjacent X columns. Output results on a separate sheet.

Interpret each coefficient in its units **while holding the other included predictors constant**. Report uncertainty and model fit; inspect residual patterns and influential observations. If claiming predictive performance, evaluate on observations not used to fit or select the model. A fitted association does not establish a causal pricing effect.

### Step 2 — compare group means with ANOVA

Choose a numeric outcome and the categorical factor named in your question. The lesson page asks about **Revenue by Distribution Channel**, but its instructions also name **Customer Type**. These answer different questions: state which one you analyse and use the matching factor.

For Excel's **ANOVA: Single Factor**, arrange the actual numeric outcome observations in separate columns for each group. One-hot indicators are not the revenue observations and should not replace them in this test.

State H₀ (population means equal) and H₁ (at least one differs). Check independence, residual distributions and comparable variances; reconsider the test when assumptions are unsuitable. Report group sizes, means, spread, F, degrees of freedom and p-value, plus the practical size of any difference. A significant overall result does not identify the differing pairs without suitable follow-up comparisons.

### Step 3 — match hypotheses to the question

For “Do customer types book different average numbers of nights?”, use **Nights** as the outcome and **Customer Type** as the factor. The page's references to Categories, Numerical_Category and Sales do not match this hotel question.

Choose the significance level before inspecting results. If evidence is insufficient, write “we did not find sufficient evidence of a difference”; do not claim the groups are proven equal. A p-value is not the probability that the null hypothesis is true. [Original statistical examples](https://learning.noroff.no/mod/book/view.php?id=22839&chapterid=81492).

### Step 4 — choose four task objectives

Task 7.4 requires **four objectives from your analyses in Tasks 7.2 and 7.3**, about **half a page per objective**, addressed to the shareholders. Choose objectives with reliable evidence. The suggested selection in the task walkthrough can be changed; it is not a requirement to use those four.

Use **Conclusion 1, Conclusion 2, Conclusion 3 and Conclusion 4** in **EVO Module 7 Tasks.xlsx**. For each section, cite the analysis worksheet or chart, method, filters, valid n, units and period.

### Step 5 — build an evidence-based conclusion

Follow this sequence for every objective:

1. State the business question and method.
2. Give one or two verified numerical findings and a comparison.
3. Explain what the finding means for the business.
4. State an important limitation or alternative explanation.
5. Recommend a concrete action or pilot, an owner, an evaluation period and a KPI with a suitable comparison.

Historical product spending is not calculated CLV. Profit and ROI need costs and margins. A complaint flag does not reveal why the customer complained. Describe recommendations as proposals to test, not proven effects.

### Step 6 — communicate to the shareholders

Lead with the conclusion, then support it with evidence. Use clear tables or simple plots when useful; label units, periods and denominators. Explain practical meaning, limitations and next steps. Keep each task objective to approximately half a page and make every claim traceable to your own analysis.

Writing template: “We analysed […] using […]. The result was […] across […] valid observations, documented in […]. This suggests […], although […]. We recommend […] for […], evaluated by […] over […] using […] against […].”

### Step 7 — review with Exam Resolver

Enter **Task 7.4** in Universal Exam Resolver, choose four objectives and work through Conclusion 1–4. Supply your actual findings before asking for an English review. Ask it to check evidence, interpretation, limitations and KPI design, and flag missing information. Compare every generated claim against your workbook before adopting it.

[Original Task 7.4](https://learning.noroff.no/mod/book/view.php?id=22839&chapterid=81496). [Microsoft: Excel Analysis ToolPak](https://support.microsoft.com/en-us/excel/use-the-analysis-toolpak-to-perform-complex-data-analysis). [NIST: comparing group means](https://www.itl.nist.gov/div898/handbook/prc/section4/prc43.htm).
""",
}
