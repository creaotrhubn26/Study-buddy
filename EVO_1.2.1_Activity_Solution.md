# EVO — Activity 1.2.1
## Statistical Interpretation: Sales Strategy and Political Poll Analysis

**Course:** FI1BBEO10 Evaluation of Outcomes · **Module 1, Lesson 1.2**
**Activity:** Statistical interpretation — hypothesis testing, confidence intervals, z-scores and critical tools

---

### How this document is organised

| Part | What it contains |
|---|---|
| **1** | Scenario 1 — the two questions answered, with the reasoning |
| **2** | Scenario 2 — the five questions answered, with the reasoning |
| **3** | Formula reference — every formula used, and how to apply it in an exam |
| **4** | Why each answer was reached — the rationale behind the wording chosen |
| **5** | Appraisal of the supplied model answers — where they are right, and the two places they are not |

The activity comes with a set of "potential answers". Those are **not** reproduced here. Every answer below was worked independently, and Part 5 compares the two.

---

## Part 1 — Scenario 1: XYZ Corporation, sales strategy analysis

**The scenario.** XYZ Corporation implemented a new sales strategy. Analysts compared average sales figures before and after implementation.

- **H₀:** the new sales strategy has not led to a statistically significant increase in sales
- **Hₐ:** the new sales strategy has resulted in a statistically significant increase in sales
- **p-value:** 0.03

---

### Q1. What does the p-value indicate about the null hypothesis?

**The answer.**

A p-value of 0.03 means: **if the null hypothesis were true — if the strategy had made no difference at all — the probability of observing a sales increase at least as large as the one recorded is 3%.**

Against the conventional threshold of α = 0.05, 0.03 falls below it. The result is therefore treated as sufficiently unlikely under the null that the null is **rejected**, and the increase is described as *statistically significant*.

**Three precisions that separate a correct answer from a good one.**

| The precision | Why it matters here |
|---|---|
| The probability is **conditional on H₀** | It is not the probability that H₀ is true. It is the probability of this data *given* H₀. The two are different quantities, and only the second is computable from the test |
| "As large as, **or larger than**" | The p-value is a tail probability. It includes every outcome more extreme than the one observed, not just the one observed |
| Rejecting is not **disproving** | 3% is small, not zero. If this exact study were repeated a hundred times in a world where the strategy did nothing, roughly three would produce a result this striking. This may be one of those three |

**And the symmetric point, which the question invites.** Had the p-value come out at 0.06, the correct conclusion would **not** have been "the strategy had no effect". It would have been "the evidence was not strong enough to reject the null at this threshold". You never accept H₀; you fail to reject it. The asymmetry is deliberate — the burden of proof sits on the claim of effect.

---

### Q2. What conclusion could XYZ Corporation draw regarding the new sales strategy?

**The answer in one sentence.**

> XYZ Corporation can conclude that **sales increased by more than would plausibly be explained by ordinary variation**, and that this is consistent with the new strategy having worked — but the study as described does not establish that the strategy *caused* the increase, and does not say whether the increase is large enough to justify the investment.

That is the whole answer. The rest of this section is why each clause is in it.

#### What the test does support

1. **An increase occurred that is unlikely under "no change".** This is a real finding and it is the finding the test was designed to produce.
2. **It is reasonable to continue.** A significant result is adequate grounds for keeping the strategy running while gathering better evidence. It is not adequate grounds for a large expansion.

#### What the test does not support, and why

**(a) It does not establish causation.** The design is a **before-and-after comparison with no control group**. Three specific alternatives remain open:

| Alternative explanation | Why it is live in this case |
|---|---|
| **Seasonality and market movement** | Sales rise and fall on their own. If "after" covers a stronger part of the year than "before", the comparison is measuring the calendar |
| **Concurrent changes** | A strategy is rarely introduced alone. A product launch, a price change, a competitor's difficulties, or new sales staff would all show up in the same figures |
| **The attention effect** | Measuring a process, and telling a sales team they are being measured, tends to improve it regardless of the intervention |

A p-value cannot distinguish between these and the strategy. It only says the increase is unlikely to be noise — and "not noise" is not the same as "caused by the thing we changed".

**(b) The strategy is a bundle, not a variable.** The lesson describes it as a revamped marketing campaign, product bundling for discounts, and an aggressive social media presence. Even accepting that the bundle worked, the test cannot say **which part** worked, and it is entirely possible that one component is carrying the result while another is losing money. Any decision to expand should be preceded by testing the components separately.

**(c) No effect size is reported, so the business value is unknown.** This is the most consequential gap, and it can be demonstrated rather than asserted.

#### Demonstration: the same p = 0.03 from two entirely different businesses

Take monthly sales averaging 1 000 units with a standard deviation of 120 units, and a one-tailed test at exactly p = 0.03. What increase produces that p-value?

| | **Case A:** 12 months before, 12 after | **Case B:** 200 stores before, 200 after |
|---|---|---|
| Degrees of freedom | 22 | 398 |
| Critical t at one-tailed p = 0.03 | 1.983 | 1.886 |
| Standard error | 120 × √(2/12) = **49.0** | 120 × √(2/200) = **12.0** |
| Increase required | **97.1 units** | **22.6 units** |
| As a percentage lift | **9.7%** | **2.3%** |
| Cohen's d | **0.81** — large | **0.19** — below the 0.2 "small" benchmark |

**Both rows report p = 0.03.** One describes a business whose sales jumped a tenth; the other describes a business whose sales moved 2.3%, detectable only because 400 stores were measured. A 9.7% lift transforms the case for the strategy. A 2.3% lift may not cover what the campaign cost.

The p-value is identical in both. **It therefore cannot be the basis of the investment decision**, and any conclusion drawn from it alone is incomplete regardless of how correctly it is stated.

#### What XYZ should ask for before deciding

| Missing | Why it is needed |
|---|---|
| **The mean difference in units and in kroner** | Turns "significant" into "worth this much" |
| **A confidence interval on the difference** | Says how precisely the gain is known. A wide interval means the payback is not established, as the Nordtre redesign case in Lesson 1.2 shows |
| **Cohen's d** | Places the difference on a comparable scale |
| **The periods compared, and their length** | A one-quarter window cannot separate the strategy from the season |
| **What else changed in the window** | The confounders above, listed rather than assumed away |
| **The cost of the strategy** | Without it there is no ROI, only a lift |

#### The defensible write-up

> "Average monthly sales after the strategy's introduction were significantly higher than before (one-tailed p = 0.03), an increase of X units, or Y%, with a 95% confidence interval of [L, U] and Cohen's d of Z. The design is a before-and-after comparison without a control group, so the increase cannot be attributed to the strategy alone; seasonality, the concurrent product launch, and heightened attention on the sales team are not excluded. On the point estimate the strategy returns R against a cost of C. Recommendation: continue the strategy and run a regional holdout in the next quarter so the effect can be attributed."

That version reaches the same practical decision as the shorter one and cannot be knocked over by anyone who asks a second question.

---

## Part 2 — Scenario 2: Political poll and confidence interval analysis

**The scenario.** A poll puts a candidate's support at 52%, with a 95% confidence interval from 50% to 54%.

---

### Q1. What does the confidence interval tell us about the candidate's support level?

**The answer.**

The interval says that, on the evidence of this sample, the candidate's **true level of support in the whole population plausibly lies between 50% and 54%**, and the 52% is the single best estimate within that range.

The 95% belongs to the **method**, not to this one interval. Stated exactly: if the poll were repeated many times and an interval computed the same way from each sample, about 95% of *those intervals* would contain the true support level. This particular interval either contains it or it does not — we cannot know which, and that is why the confidence attaches to the procedure that generated it.

**Three things the interval tells you that "52%" alone does not.**

**1. The precision, and therefore the sample size.** The interval is symmetric around 52%, so the margin of error is **±2 percentage points**. That is enough to recover the sample:

> n = z² × p(1 − p) ÷ margin² = 1.96² × 0.52 × 0.48 ÷ 0.02² ≈ **2 400 respondents**

Running the check the other way: a poll of 600 would carry a margin of ±4.0 points, so any poll claiming ±2 on a few hundred respondents is claiming precision its sample cannot deliver.

**2. The finding hiding at the lower bound.** In a two-candidate race, **50% is the line between leading and tied**. This interval reaches down to exactly that line. The poll is therefore consistent with the candidate holding a genuine majority *and* consistent with the race being level, and it does not support a headline saying the candidate leads.

This is the practical use of an interval: the point estimate of 52% suggests a lead, and the interval says the lead is not established. Two supporters could read the same poll and claim 51% and 53%, and both would be within what the data supports.

**3. What the interval does not cover.** The ±2 points quantifies **sampling error only** — the variation that comes from surveying 2 400 people rather than everybody. It assumes the sample was drawn properly, and it says nothing about the errors that usually dominate real polling:

| Source of error | Inside the ±2? |
|---|---|
| Random sampling variation | **Yes** — this is the entire content of the interval |
| Non-response bias — who declines to answer | No |
| Coverage bias — who is reachable at all | No |
| Question wording and question order | No |
| Respondents misreporting their intention | No |
| Turnout — support is not the same as votes cast | No |

**A tight interval on a badly drawn sample is a precise wrong answer**, and it looks exactly as reassuring as a tight interval on a good one. This is why the sampling method must be evaluated before the interval is read.

---

### Q2. What is a z-score, and how is it calculated?

**The answer.**

A **z-score** measures how many standard deviations a data point lies from the mean of its distribution.

> **Z = (x − μ) ÷ σ**

| Symbol | Meaning |
|---|---|
| **x** | The individual value being standardised |
| **μ** (mu) | The mean of the distribution |
| **σ** (sigma) | The standard deviation of the distribution |
| **Z** | The result — the distance from the mean, counted in standard deviations |

μ and σ are the **population** values. When they are unknown and a sample is used instead — which is almost always — the identical formula is written **z = (x − x̄) ÷ s**, with the sample mean and sample standard deviation.

**What the arithmetic is doing.** Subtracting the mean re-centres the distribution on zero, so the result is a *distance from average* rather than a raw value. Dividing by the standard deviation re-scales it into units of ordinary variation, so the result is *how far, relative to how far things usually are*. Together they strip out both the origin and the units — which is exactly what makes two variables measured in different units comparable.

**Worked both directions.** Nordtre AS order values have μ = NOK 742 and σ = NOK 210.

- **Forwards** — how unusual is one order? An order of NOK 1 240: Z = (1 240 − 742) ÷ 210 = 498 ÷ 210 = **+2.37**
- **Backwards** — what value sits at a chosen threshold? At Z = 1.96, the 95% cut: x = μ + Z × σ = 742 + 1.96 × 210 = **NOK 1 154**

The second direction is the more useful one in practice, because it converts a chosen confidence level into a number in business units — which is how a z-score becomes an alert threshold on a dashboard rather than a figure in a report.

---

### Q3. What does a z-score tell you about a data point?

**The answer.**

It tells you **where the point sits relative to the rest of the distribution**, on a scale that carries no units.

| Z | Reading |
|---|---|
| **0** | Exactly at the mean |
| **Positive** | Above the mean |
| **Negative** | Below the mean |
| **Larger absolute value** | Further from average, and therefore more unusual |

Under a roughly bell-shaped distribution, the magnitudes translate into rarity:

| \|Z\| | Roughly how much of the distribution is further out | Reading |
|---|---|---|
| 1 | 32% | Ordinary variation |
| 1.96 | 5% | The conventional 95% boundary |
| 2.37 | 1.8% (one tail: 0.9%) | Unusual, worth a look |
| 2.58 | 1% | Rare |
| 3 | 0.3% | Investigate |

**The second thing it gives you, which is arguably more valuable: comparability.** A customer's order value is in kroner and their order frequency is a count. They cannot be compared directly. Standardised, both become "how far from typical", and a customer at z = +2.1 on value but z = −0.4 on frequency is immediately legible as a rare-but-large buyer. This is the same mechanism behind standardised regression coefficients, which is how you rank predictors measured on different scales.

**And the three things a z-score does not tell you** — the part that distinguishes an evaluation answer from a definition:

1. **It does not say the value is wrong.** It says the value is far from the mean. Whether that is an error, a rare genuine event, or a sign that the model is missing a variable is a separate investigation. The Black Friday residual from Lesson 1.2 was extreme *and* entirely correct.
2. **It assumes a roughly symmetric distribution.** On strongly skewed data — income, response times, order values — z-scores label ordinary values as extreme and miss genuine outliers on the compressed side. For skewed data the IQR fences from Lesson 1.3 are the better tool.
3. **It is computed from a mean and standard deviation that the outlier itself inflates.** One enormous value pulls the mean up and the standard deviation up, which can drag its own z-score back below the threshold and mask other real outliers at the same time.

**And the reference distribution must be stated.** A z-score is always relative to *some* μ and σ. The same customer standardised against this month, against the year, and against the industry gets three different z-scores. An unlabelled z-score is a number without a denominator.

---

### Q4. Name two statistical software programs mentioned for generating comprehensive result tables.

**The answer: R and Python.** The lesson names a third, SPSS.

| Software | What it is | What it produces for result-table work |
|---|---|---|
| **R** | A language built for statistics | Regression tables, ANOVA and post-hoc output, and the widest range of diagnostics, largely in the base language |
| **Python** — with **pandas** and **statsmodels** | A general language with statistical libraries | `statsmodels` produces R-style summary tables; `pandas` handles the data preparation around them |
| **SPSS** — Statistical Package for the Social Sciences | A menu-driven statistics package | Standard result tables without programming, long established in social science |

**What the lesson says they are *for*** — and this is the part of the question that carries the marks: they generate comprehensive result tables **and provide the functionality to delve deeper, test assumptions, and run post-hoc tests.** Producing the table is the least of it. What distinguishes these tools from a spreadsheet is that they can check whether the table is trustworthy: residual diagnostics, tests for heteroscedasticity and multicollinearity, and corrections for multiple comparisons.

**The property worth naming even though the question does not ask for it.** R and Python are **scripted**, and SPSS is typically driven by menu clicks. A script is a record of exactly what was done; a click sequence is not. Six months later, "how was this figure produced?" has an answer in one case and not the other. That is the version control argument from Lesson 1.1 applied to the analysis instead of to the data, and it is the strongest single reason to prefer a scripted tool.

---

### Q5 (optional). How do visualisation tools like Tableau or Power BI aid in data analysis?

**The answer.**

They translate table results into visual form, which serves four distinct purposes:

| Purpose | What it does |
|---|---|
| **Comprehension** | Patterns, trends and anomalies that a table hides become visible at a glance. The lesson notes this matters most with **complex multivariate results**, where six coefficients with interactions are unreadable as numbers but immediately legible as a coefficient plot |
| **Exploration** | Filtering, segmenting and drilling down let a user ask follow-up questions themselves, instead of returning to the analyst for each one |
| **Monitoring** | Live connections turn a one-off analysis into a standing dashboard that tracks the metric over time |
| **Communication** | A visual result crosses the boundary between analysts and decision-makers, which is where most analysis fails to have any effect |

**Two qualifications an evaluation answer should carry.**

**They are presentation tools, not analysis tools.** Tableau and Power BI are strong at showing a result and weak at establishing one. Neither offers the assumption tests, diagnostics or post-hoc corrections that R, Python or SPSS provide. Using them to *find* a finding is how the multiple-comparison trap happens at speed: clicking through twenty segmentations until one looks interesting is twenty untracked tests, and at α = 0.05 roughly one of them will look interesting for no reason at all.

**Visualisation makes a result easier to grasp, including a wrong one.** A reader checks a number and absorbs a picture. A truncated axis makes a trivial change look dramatic, the wrong chart type answers a different question from the one asked, and status encoded by colour alone is unreadable for a colour-blind viewer. The speed of comprehension is the benefit and the hazard in the same property.

**The honest summary.** These tools enhance the *communication* of findings and support data-driven decisions across an organisation. They do not enhance the *validity* of those findings — that is the job of the statistical software and, before it, of the sampling design.

---

## Part 3 — Formula reference and exam application

Every formula this activity touches, with the spreadsheet pattern and the exam use.

### 3.1 Hypothesis testing

| Quantity | Formula | Spreadsheet |
|---|---|---|
| Pooled standard deviation | s_p = √( [(n₁−1)s₁² + (n₂−1)s₂²] ÷ (n₁+n₂−2) ) | `=SQRT(((n1-1)*s1^2+(n2-1)*s2^2)/(n1+n2-2))` |
| Standard error of a difference | SE = s_p × √(1/n₁ + 1/n₂) | `=sp*SQRT(1/n1+1/n2)` |
| Test statistic | t = (x̄₁ − x̄₂) ÷ SE | `=(m1-m2)/SE` |
| p-value, two-tailed | — | `=T.DIST.2T(ABS(t), n1+n2-2)` |
| p-value, one-tailed | — | `=T.DIST.RT(t, n1+n2-2)` |
| Cohen's d | d = (x̄₁ − x̄₂) ÷ s_p | `=(m1-m2)/sp` |

**Exam use.** State H₀ and Hₐ in the units of the problem and say whether the test is one- or two-tailed *before* computing anything. Compute the statistic, get the p-value, compare against α — and then **always** report the effect size and interval alongside, because the four-case grid (significant/not × large/small) is where the marks sit.

### 3.2 Confidence intervals

| Quantity | Formula | Spreadsheet |
|---|---|---|
| Interval for a mean | x̄ ± t × SE | `=mean - T.INV.2T(0.05,df)*SE` and `+` |
| Interval for a proportion | p ± z × √(p(1−p)/n) | `=p - 1.96*SQRT(p*(1-p)/n)` and `+` |
| Margin of error, proportion | ME = z × √(p(1−p)/n) | `=1.96*SQRT(p*(1-p)/n)` |
| Sample size for a target margin | n = z² × p(1−p) ÷ ME² | `=1.96^2*p*(1-p)/ME^2` |
| Interval for a mean, σ known | x̄ ± CONFIDENCE.NORM | `=CONFIDENCE.NORM(0.05, sd, n)` |

**z for common confidence levels:** 90% → 1.645 · 95% → 1.96 · 99% → 2.576

**Exam use.** Interpret in terms of the *procedure*, not the individual interval. Read the width as precision and say what decision that width does or does not support. Name what the interval excludes. If the question gives a margin, recover n; if it asks for a target precision, solve for n.

### 3.3 Z-scores

| Quantity | Formula | Spreadsheet |
|---|---|---|
| z-score | Z = (x − μ) ÷ σ | `=(x-mean)/sd` or `=STANDARDIZE(x,mean,sd)` |
| Value at a given z | x = μ + Z × σ | `=mean+z*sd` |
| Tail probability above z | — | `=1-NORM.S.DIST(z,TRUE)` |
| Two-tailed probability | — | `=2*(1-NORM.S.DIST(ABS(z),TRUE))` |
| z for a given tail area | — | `=NORM.S.INV(1-alpha)` |

**Exam use.** Run it forwards to describe an observation, backwards to set a threshold. Always state which mean and standard deviation the score is relative to, and flag the normality assumption if the data is skewed.

### 3.4 The one-line summary of the three

| Tool | Answers | Reported as |
|---|---|---|
| **Hypothesis test** | Is there a detectable effect? | p-value against α |
| **Confidence interval** | How precisely is it known? | A range at a stated level |
| **Effect size / z-score** | How big, or how unusual? | Cohen's d, or standard deviations from the mean |

A result carrying only one of the three is incomplete, and which one is missing predicts what the reader will get wrong.

---

## Part 4 — Why each answer was reached

The activity asks for interpretations rather than calculations, so the reasoning behind the *wording* is the substance of the work.

| Answer | The decision made, and why |
|---|---|
| **S1 Q1** — leading with "if the null hypothesis were true" | The conditional is the single most misread part of a p-value. Putting it first makes every following clause correct by construction, and makes it impossible to slide into "3% chance the null is true" |
| **S1 Q1** — including "or larger than" | A p-value is a tail probability. Omitting this makes it sound like the probability of the exact observed result, which is a different and near-zero quantity |
| **S1 Q1** — adding the p = 0.06 counterfactual | The question asks what the p-value indicates *about the null hypothesis*. A complete answer covers both directions, and the asymmetry — reject versus fail to reject — is the conceptual point being tested |
| **S1 Q2** — refusing the word "caused" | This is the substantive judgement in the whole activity. The design is before/after without a control, and the strategy is a bundle of three changes. "Consistent with the strategy having worked" is the strongest claim the evidence carries |
| **S1 Q2** — building the two-case demonstration | Asserting "you also need the effect size" is a claim the reader can accept or ignore. Showing that p = 0.03 is produced by both a 9.7% lift and a 2.3% lift makes the gap impossible to dismiss, and it uses the course's own arithmetic to do it |
| **S1 Q2** — ending with a written recommendation | The question asks what the company could *conclude*, which is a business question, not a statistical one. An answer that stops at "significant" has not answered it |
| **S2 Q1** — separating the procedure from the interval | This is what examiners test on confidence intervals, and it is the difference between reciting the definition and understanding it |
| **S2 Q1** — recovering n from the margin | The question asks what the interval tells us. That it tells us the sample was around 2 400 people is genuinely part of the answer, and it is a check that transfers to any poll |
| **S2 Q1** — the 50% boundary | The most useful observation available about this specific poll, and it comes from reading the *bound* rather than the point estimate. It is why the interval was worth reporting at all |
| **S2 Q2** — giving both μ/σ and x̄/s | An exam paper may use either notation. Knowing they are the same formula prevents a moment of confusion under time pressure |
| **S2 Q2** — working the formula backwards | Forwards, a z-score describes. Backwards, it sets a threshold. The second is what makes it operationally useful, and it links to the dashboard material from Lesson 1.1 |
| **S2 Q3** — adding what a z-score does *not* tell you | The question is "what does it tell you", and the boundary of a tool is part of what it tells you. The skew and self-inflation points are the two that change conclusions in practice |
| **S2 Q4** — naming what the software is *for* | The question says "for generating comprehensive result tables", quoting the lesson. The lesson's sentence continues into assumptions and post-hoc tests, and that continuation is the reason these tools beat a spreadsheet |
| **S2 Q5** — the two qualifications | Listing benefits answers the question; naming that these are presentation rather than analysis tools, and that a chart can mislead faster than a table, is what makes it an *evaluation* answer in a course about evaluating outcomes |

---

## Part 5 — Appraisal of the supplied model answers

The activity ships with a set of "potential answers". Most are correct. Two need qualification, and one is better than the lesson text it came from.

### Where they are right

| Answer | Assessment |
|---|---|
| **S1 Q1** | Correct, and correctly framed. It opens with "if the null hypothesis is true", which is the clause that matters. The added phrase "occurred by chance" is redundant once the conditional is stated, but it is not wrong |
| **S2 Q1** | **Correct, and better than the lesson text.** The lesson's own poll section says "95% of those polls would capture the true support level within that 50% to 54% range", which is loose. The model answer says "95% of the resulting intervals would contain the true support level" — which is the precise formulation. Worth noting that the activity fixes an imprecision in the lesson |
| **S2 Q2** | Correct, and it prints the denominator as **σ**. The lesson text renders it as δ (delta), which is a typographical error. The activity has the standard symbol |
| **S2 Q3** | Correct as far as it goes — see the qualification below |
| **S2 Q4** | Correct. Python and R. SPSS would serve equally |
| **S2 Q5** | Correct, and a good list. It omits the cautions |

### Where they need qualification

**1. Scenario 1, Q2 — the causal claim.** The model answer reads:

> "XYZ Corporation can conclude that the new sales strategy led to a statistically significant increase in sales."

**"Led to" is a causal statement, and the design does not support it.** A before-and-after comparison with no control group cannot separate the strategy from seasonality, from concurrent changes, or from the attention effect — and the strategy is itself a bundle of three interventions, so even a genuine effect cannot be attributed to any one of them.

The defensible version changes two words: *sales increased significantly following the strategy's introduction, which is consistent with the strategy having worked.* This is not pedantry. It is the same error the lesson's own case study makes when it writes that the data "proves" the strategy's effectiveness one sentence after conceding that other contributing factors are not ruled out, and it is precisely the reasoning this course exists to correct.

**2. Scenario 1, Q2 — "the results suggest the strategy is effective."** Effective at what scale, and at what cost? The p-value carries no magnitude. As Part 1 demonstrates, the same p = 0.03 is generated by a 9.7% lift and by a 2.3% lift, and only one of those is likely to justify a marketing campaign, a discount programme and a social media operation. A conclusion about effectiveness needs the effect size, the confidence interval and the cost.

**3. Scenario 2, Q3 — the z-score answer is correct but incomplete.** The four bullets describe what a z-score reports. They do not mention that the interpretation assumes a roughly symmetric distribution, that a z-score is computed from a mean and standard deviation the outlier itself inflates, or that the reference distribution has to be stated. In a course about evaluating outcomes, the limits of a measure are part of what the measure tells you.

### The pattern in these three

All three are the same shape: **the arithmetic is right and the claim built on it is wider than the arithmetic supports.** A p-value becomes causation, a significance test becomes a verdict on effectiveness, and a descriptive statistic is presented without the conditions it depends on.

That shape is worth recognising because it is what an evaluation assignment is marked on. The statistics in this activity are not difficult. The discipline of saying exactly as much as the evidence supports, and no more, is the thing being taught.

---

## One-page summary

| Question | The short answer |
|---|---|
| **S1 Q1** | If H₀ were true, there is a 3% probability of an increase this large or larger. Below α = 0.05, so H₀ is rejected — not disproved |
| **S1 Q2** | Sales rose beyond ordinary variation, consistent with the strategy working. Causation is not established (no control, three bundled changes), and without an effect size the business value is unknown |
| **S2 Q1** | True support plausibly lies between 50% and 54%; the 95% describes the procedure. Margin ±2pp implies n ≈ 2 400. The lower bound sits on 50%, so a lead is not established. Sampling error only |
| **S2 Q2** | Z = (x − μ) ÷ σ — distance from the mean in standard deviations. Backwards: x = μ + Zσ |
| **S2 Q3** | Where the point sits relative to the distribution, unit-free. 0 = mean, sign = direction, magnitude = unusualness. Assumes symmetry; does not mean "wrong"; needs its reference distribution stated |
| **S2 Q4** | R and Python (pandas, statsmodels); SPSS also. They matter because they test assumptions and run post-hoc tests, not just print tables |
| **S2 Q5** | Comprehension, exploration, monitoring, communication — but they are presentation tools, and a chart can mislead faster than a table |
