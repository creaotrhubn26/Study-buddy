# EVO 1.2 — dekningsoversikt

Hva som allerede er integrert i Study Buddy fra **1.2 Statistical Inference, Result
Table Analysis, and Critical Tools**. Skann denne før du sender nytt materiale, så
slipper du å lime inn noe som allerede ligger inne.

Generert 2026-09-13 · leksjonen er nå 222 205 tegn.

`####` er hovedbolker, `#####` er underavsnitt.

---

- **Introduction**
  - The triad, and why it takes all three
  - The failure that belongs to each
  - "Raw data into actionable intelligence"
  - Where this sits relative to Lesson 1.1
  - What this lesson covers, and what moves to Lesson 1.3
- **Advanced result table analysis in data analysis**
- **Unpacking the insights: hypothesis testing, confidence intervals, and effect sizes in result tables**
  - Testing hypotheses: hypothesis basics
  - Interpreting p-values
  - What a p-value is not
  - Cohen's d: effect size
  - Worked example: significant, and small
  - The four cases, and what each one means
  - How this is applied in an exam task
- **Case study: testing the efficacy of a new sales strategy**
  - Hypothesis formation
  - Four things to notice about this case
  - How the case should be reported
- **Confidence intervals**
  - Where the confidence level's probability actually lives
  - What determines the width
  - The interval and the test are the same statement
  - Applying it to the Nordtre worked example
- **Understanding a political poll with the use of a confidence interval**
  - Reading this poll as an evaluator
  - Exam use
- **Diving deeper with result table analysis**
  - Multivariate analyses
  - Normalised metrics
  - Residual analysis
  - The three together
- **Understanding the significance of statistical inferences**
  - Statistical inference defined
  - Bridging sample and population
  - What statistical inference is for: five roles
  - The conclusion, and the metaphor
  - Parameter and statistic: the notation this lesson uses
  - The two branches, and where this lesson uses each
  - Every evaluation you perform is an inference
  - The case where inference is unnecessary — and the error it causes
- **Statistical inferences for sampled sets**
  - Purpose and necessity
  - The principle of representativeness
- **Random vs. stratified sampling**
  - Random sampling
  - Stratified sampling
  - Choosing between them
- **Importance of sampling methods in outcome evaluation**
- **Potential pitfalls and biases in sampled sets**
  - The four pitfalls, sorted by what fixes them
  - The five sampling methods, and the risk in each
  - The keyhole
- **Sample size and why small samples mislead**
- **Quantitative and qualitative evidence**
- **Linear regression**
  - Anatomy of the equation
  - How "best" is decided: least squares
  - Two precision notes on the definition
  - What the picture shows, and what it leaves out
- **Linear regression: evaluation outcomes and results**
  - Assumption 1 — linearity
  - What "proportional" is really claiming
  - Why the failure is worse than random error
  - How to detect it
  - How to fix it — and the distinction that trips people up
  - The evaluator's version
  - Case: boligpriser — the example the course gives
  - Why this case is the right one to remember
  - The trap this case sets, and it is the exam-relevant part
  - What the log model buys beyond fixing the fit
  - Assumption 2 — no internal causation of the regressors
  - What the error term actually contains
  - The three routes in, and what each does to the estimate
  - "Biased and inconsistent" — two words, two different problems
  - Why this is the assumption the diagnostics cannot check
  - What to do about it
  - Case: educational impact — class size, and the instrument that could backfire
  - Signing the bias, and why "overestimated" needs unpacking
  - Testing the proposed instrument against the three conditions
  - The finding worth carrying: a bad instrument is worse than none
  - What a defensible design looks like
  - Recognising, testing, rectifying — the assumptions in one place
  - The sorting that actually matters: what breaks, and what survives
  - The three verbs as a routine
- **Advanced regression metrics**
  - Adjusted R-squared
  - The F-statistic
  - When F and the individual t-tests disagree
  - Standard errors
  - The four numbers are one number
  - Reading a result table with all three
  - The t-statistic
  - "More significant" is not "more important"
  - Can you rank predictors by their t-statistics?
  - The three questions, and the metric for each
  - Closing the section
- **Residual analysis**
  - Patterns in residuals
  - Heteroscedasticity
  - "Inefficient, though unbiased" — the most precise phrase in the section
  - "Can bias tests of significance" — and in which direction
  - A note on the spelling, and on the roots
  - Detecting and fixing it
  - Why heteroscedasticity is so common in business data
  - Case study 1: e-commerce sales
  - Solving it: why the funnel is there, and which fix to choose
  - Model misspecification
  - Outliers and influential points — not the same thing
  - The two ingredients, and why Cook's distance combines them
  - Thresholds, and what to do when a point is flagged
  - Case study 2: real estate pricing — Alpha Estates (advanced analysis)
  - What is different about this case
  - Diagnostic 1 — the heteroscedasticity, and why the log is the right call
  - Diagnostic 2 — the VIF, and the conclusion that does not follow
  - The course's two definitions, and the word in them that is wrong
  - The four remedies the course lists — and which one the case should have used
  - Back to the case
  - What dropping the variable actually did
  - The collision the case does not mention
  - The business consequence, in one number
  - So what should Alpha Estates have done?
  - When dropping the collinear variable *is* right
  - The two diagnostics together
  - Alpha Estates: advanced insights from the result table
  - The F-statistic here carries no information at all
  - "Adjusted R² of 0.85 means it is not overfitting" — this is the claim to challenge
  - The number the case cites argues against the decision the case made
  - Reading the outcome section as an evaluator
  - Case study 3: retail chain's inventory management with variance analysis
  - First, two different things are both called "variance analysis"
  - MAPE is the wrong metric for the categories this case created
  - The two findings, and what they do not establish
  - The recommendation runs against the finding
  - Case study 4: tech startup and churn prediction using z-testing
  - What p = 0.04 does and does not buy
  - The three design problems, in order of severity
  - Why the decision was still right, and what actually drove it
  - Case study 5: PharmaCorp's drug trials and five-point summary analysis
  - What is already right about this design
  - What a five-point summary can and cannot do
- **Result table analysis with linear regression**
- **Reading R squared honestly**
- **Correlation is not causation, stated usefully**
- **Z-testing and z-scores**
- **Z-testing as a significance check**
- **Critical tools for enhanced result table analysis**
  - Statistical software
  - Visualisation tools
  - Model diagnostics
  - Choosing a tool, and the property that matters most
  - The section in one paragraph
- **The other kind of tool: which technique answers which question**
- **Worked example: appraising a result table**
- **Activity 1.2.1 — Statistical interpretation: sales strategy and political poll**
  - Scenario 1 — Q1: what does p = 0.03 indicate about the null hypothesis?
  - Scenario 1 — Q2: what can XYZ conclude?
  - Scenario 2 — Q1: what does the 50–54% interval tell us?
  - Scenario 2 — Q2 and Q3: the z-score
  - Scenario 2 — Q4 and Q5: the tools
  - The pattern in the supplied model answers
  - Deliverables
- **Activity 1.2.2 — Exploring the role of statistical inferences**
  - The definition worth memorising
  - How the extrapolation actually works (Q4)
  - Worked example for Q8 — testing a claim
  - Worked example for Q10 — a pilot before launch
  - The three places the model answers overreach
  - The pattern, and why it is the assessed skill
  - Deliverables
- **Common assignment traps**

---

## Ikke dekket ennå

- Resten av **Case study 5 (PharmaCorp)** — kurset sier «We will detail this in more
  detail shortly», så selve fempunktsanalysen mangler.
- Alt etter case-studiene i 1.2, hvis kurset har mer.
- **Leksjon 1.3 og 1.4** er bygget fra titler og læringsutbytte, ikke fra offisiell tekst.
- **Leksjon 1.5** (ensembling og ETL) — uklart om den hører til modul 2.

## Slik sender du nytt materiale raskest

1. Sjekk listen over. Er overskriften der, er innholdet inne.
2. Send bare det som mangler.
3. Eller last ned hele kurset fra Moodle («Download course content») og legg zip-en i
   repoet — da trengs ingen kopiering i det hele tatt.

