# EVO — Activity 1.2.2
## Exploring the Role of Statistical Inferences in Understanding Results

**Course:** FI1BBEO10 Evaluation of Outcomes · **Module 1, Lesson 1.2**

The activity ships with a set of model answers. Those are **not** reproduced here — every answer below was worked independently, and Part 3 compares the two.

---

## Part 1 — The fifteen questions

### 1. Define statistical inference in your own words.

**Statistical inference is the discipline of saying something about a population you cannot observe, using a sample you can — and stating how far wrong you might be.**

The second half is what makes it a discipline rather than a guess. Anyone can extrapolate from a sample; inference attaches a *quantified* uncertainty to the extrapolation, so the claim carries its own margin for error.

The course phrases it as drawing conclusions from **data subject to random variations**. That qualifier is the whole scope of the field: inference is the mathematics of the variation caused by *which units happened to be sampled*. It says nothing about variation caused by a badly drawn sample, and it cannot.

### 2. Explain the primary purpose of statistical inference in research and analysis.

To let a decision be made about a population on the basis of partial evidence, **with the strength of that evidence stated rather than assumed**.

Three things follow, and each is a different job:

| Purpose | What it produces |
|---|---|
| **Estimation** | A value for an unknown population quantity, plus the range it plausibly sits in |
| **Testing** | A verdict on whether the data is consistent with a specific claim |
| **Generalisation** | Licence to apply a finding beyond the units actually measured |

The word *primary* invites a single answer, and if one is needed: inference exists so that the honest response to "how confident are you?" is a number rather than an adjective.

### 3. Why is studying an entire population often impractical or impossible?

Four reasons, and the fourth is usually left out:

| Reason | |
|---|---|
| **Cost** | A survey of 400 costs a fraction of one of 40 000 |
| **Time** | A result that arrives after the decision has been taken is worth nothing |
| **Feasibility** | Some populations cannot be enumerated at all — future customers, prospective patients, all possible outputs of a process. Some measurements are destructive: a lightbulb tested to failure is a lightbulb you cannot sell |
| **Quality** | **A well-run sample often beats a badly-run census.** Resources concentrated on 400 people can chase non-responders, verify answers and control conditions. The same budget spread across 40 000 cannot, and a census with a 20% response rate is a self-selected sample wearing a census's clothes |

That last row matters for an assignment, because "we surveyed everyone" is usually offered as a strength and is frequently the opposite.

### 4. How does statistical inference assist in extrapolating results from a sample to a broader population?

By supplying a **model of how samples behave**, which converts the leap from sample to population into a calculation.

The mechanism is the **sampling distribution**. A single sample gives one number; but if you imagine drawing many samples the same way, their results form their own distribution, and that distribution is describable:

- It is **centred** on the population value, if the sampling was random
- Its **spread** — the standard error — shrinks in proportion to √n
- For sample means it is approximately **normal** at reasonable n, whatever shape the population has

> **Standard error of a mean: SE = s ÷ √n** · **of a proportion: SE = √(p(1−p)/n)**

Because that behaviour is known, the distance between the sample result and the population value can be bounded: the interval, the margin of error and the p-value are all expressions of it.

**The condition attached.** The extrapolation is valid only from the population the sample was actually drawn from. A sample of one city extrapolates to that city. Random selection is what centres the sampling distribution on the truth; without it the arithmetic still runs and the interval no longer means what it says.

### 5. Explain how statistical inference helps in quantifying uncertainty in the results.

By replacing a single number with a **number plus a range**, and by putting a figure on how surprising a result would be under a stated assumption.

| Tool | Quantifies |
|---|---|
| **Confidence interval** | The range the population value plausibly occupies, at a stated level |
| **Margin of error** | Half that range — the estimate's precision in one figure |
| **Standard error** | How much the estimate would move from sample to sample |
| **p-value** | How unusual this data would be if the null hypothesis were true |
| **Effect size** | The magnitude, on a comparable scale, so uncertainty can be read against something |

**The essential qualification.** All of these quantify **sampling** uncertainty — the luck of the draw. None of them quantifies **bias**. A confidence interval widens with noise and does not widen with a badly chosen sample, and it looks equally reassuring in both cases. So "quantifying uncertainty" means quantifying *one kind* of uncertainty, and an evaluation has to address the other kind by examining the design.

### 6. Give an example of a statement that indicates the use of statistical inference in quantifying uncertainty.

> **"Based on a random sample of 1 200 customers, we estimate mean satisfaction at 4.4 on a 5-point scale, with a 95% confidence interval of 4.3 to 4.5."**

What makes it an inferential statement rather than a descriptive one, element by element:

| Element | Why it is there |
|---|---|
| "Based on a random sample of 1 200" | Names the evidence and the sampling method, so the reader can judge whether extrapolation is licensed |
| "We **estimate**" | Signals a claim about the population, not a description of the sample |
| "Mean satisfaction … on a 5-point scale" | States the quantity and its units |
| "95% confidence interval" | Names the level, which is a choice and must be visible |
| "4.3 to 4.5" | The range — a width of 0.2, so the estimate is tight |

Contrast: *"Our customers rate us 4.4"* is descriptive, carries no uncertainty, and cannot be argued with or checked.

A second form, for a test rather than an estimate: *"Sales after the redesign were higher than before (p = 0.03), an increase of 4.2% with a 95% interval of 0.8% to 7.6%."*

### 7. What is hypothesis testing, and how is it related to statistical inference?

**Hypothesis testing is a procedure for deciding whether data is consistent with a specific claim about a population parameter.**

It works through a pair:

- **H₀, the null hypothesis** — a statement of no effect or no difference. The default, held unless evidence overturns it
- **Hₐ, the alternative** — the claim that some effect exists

The data produces a test statistic, the test statistic produces a **p-value**, and the p-value is compared with a significance level **α** chosen in advance. Below α, the null is rejected.

**Its relation to inference: it is one of the two branches.** Inference divides into **estimation** (what is the value, and how precisely known?) and **testing** (is this consistent with a specific claim?). Both work from the same sampling distribution, and they always agree — a 95% interval that excludes the null value corresponds exactly to rejection at α = 0.05.

Three properties worth stating in any answer about testing:

1. **The asymmetry.** You never *accept* H₀, only fail to reject it. Failing to reject means the evidence was insufficient, not that no effect exists.
2. **The two errors.** Type I is a false alarm, at probability α; Type II is a missed effect, at probability β, and 1 − β is the test's power. Which costs more is a business question, not a statistical one.
3. **It answers only one question.** A test says *detectable*. It does not say *large*, and it does not say *caused by*.

### 8. Provide a hypothetical example where statistical inference can be used to test an assumption about a population parameter.

**The scenario.** A coffee chain states publicly that its customers rate it **at least 4.5 out of 5**. Marketing wants to keep using the claim; the quality team suspects it no longer holds.

**Setting up the test.**

| | |
|---|---|
| Parameter | μ, the mean rating across all customers |
| H₀ | μ ≥ 4.5 — the claim stands |
| Hₐ | μ < 4.5 — the claim is no longer supported |
| Test | One-sample, one-tailed t-test |
| α | 0.05, set before the data |

**The data.** A random sample of **n = 120** customers gives **x̄ = 4.34** with **s = 0.82**.

**The calculation.**

> SE = s ÷ √n = 0.82 ÷ √120 = **0.0749**
> t = (x̄ − μ₀) ÷ SE = (4.34 − 4.5) ÷ 0.0749 = **−2.14**, df = 119
> One-tailed **p = 0.017**

**The interval.** 95% CI = 4.34 ± 1.980 × 0.0749 = **[4.19, 4.49]** — which excludes 4.5, exactly consistent with the test.

**The reading.** p = 0.017 is below α, so H₀ is rejected: the evidence does not support a mean of 4.5 or above, and the public claim should be withdrawn or restated.

**And the part that earns the marks.** The shortfall is **0.16 of a point on a five-point scale**, giving Cohen's d = 0.16 ÷ 0.82 = **0.195**, sitting right on Cohen's 0.2 benchmark for a *small* effect. So the finding is *statistically established and practically minor*. That combination has a specific consequence here: the claim is not defensible as stated, which is a compliance matter rather than a customer-experience crisis. Restating it as "customers rate us 4.3 out of 5" is honest and costs almost nothing.

**Which side the claim sits on matters.** Had H₀ been *μ = 4.5* with Hₐ *μ ≠ 4.5*, the burden would fall the same way. But had the company set H₀ as *μ < 4.5* and tried to prove the claim, failing to reject would not have established 4.5 either — you never prove a null. **Putting the claim in Hₐ is what forces it to earn its place.**

### 9. How can statistical inference inform managers about the likely outcomes and risks of different decisions?

By converting evidence into a **range of outcomes with probabilities attached**, which is the form a decision actually needs.

| What a manager needs | What inference supplies |
|---|---|
| The likely outcome | The point estimate |
| The **range** of outcomes | The confidence interval — including the bad end, which is the risk |
| Whether an observed difference is real | The test and its p-value |
| Whether it is big enough to act on | The effect size, converted into money |
| How much a decision could be wrong by | The interval width, and the cost at each end |

**The interval is the risk statement.** This is the part most often skipped. A point estimate of a 20-month payback reads as decisive; an interval running from 10 months to 21 years says the investment case is unresolved. Same data, same p-value, opposite decisions — and only the interval exposes it. Managers are being asked to bear the downside, so the lower bound is the number they most need.

**What it cannot do.** Inference describes what the data supports. It does not weigh the cost of being wrong in one direction against the other — that is the Type I versus Type II trade-off, and it is a management judgement, not a calculation. Inference sizes the risk; someone still has to decide how much of it to accept.

### 10. Provide an example scenario where a company can use statistical inference before launching a new product.

**The scenario.** A hardware firm tests a new device with **200 recruited users** before committing to a national launch. **124 (62%)** say they would buy it at the proposed price.

**What inference gives them.**

> Margin of error = 1.96 × √(0.62 × 0.38 ÷ 200) = **±6.7 percentage points**
> 95% CI for intent to buy: **[55.3%, 68.7%]**

**How to read it.** The interval is **13.5 points wide**. That is a serviceable estimate for a go/no-go decision and much too vague for a production volume — planning inventory at 62% when the honest range reaches 55% is how a launch ends in unsold stock.

**Three things the number cannot survive without.**

1. **Intent is not purchase.** Stated intent overstates behaviour substantially, and by an amount that varies by category. If roughly half of stated intent converts, the real range is **28% to 34%**; at a third, it is **18% to 23%**. The confidence interval is exact about the wrong quantity, and no amount of extra sampling fixes that.
2. **How were the 200 recruited?** If they are enthusiasts, existing customers or a self-selected panel, the inference runs from a favourable sample to a general market and the interval understates the real uncertainty badly. Recruitment method belongs in the report.
3. **A pilot is not a rollout.** Pilots get attention, dedicated staff and novelty that a national launch cannot reproduce, so the pilot figure is an **upper bound** rather than a forecast.

**The defensible use.** Treat the test as evidence that demand is *plausibly* in a stated range under stated assumptions, launch regionally with a comparison area, and size the first production run from the lower bound rather than the point estimate.

### 11. How does statistical inference enhance the reliability and credibility of research findings or decisions?

Through three mechanisms, and each has a limit worth naming.

| Mechanism | What it does | Its limit |
|---|---|---|
| **It makes the uncertainty explicit** | The claim carries its own margin, so a reader can judge it rather than trust it | The margin covers sampling error only |
| **It imposes a standard set in advance** | A stated α and a stated hypothesis mean the conclusion was not chosen to fit the data | Only if they really were stated in advance |
| **It makes the work repeatable** | A named test, sample and threshold let someone else check the reasoning | The reader has to be told all three |

**The honest qualification.** Statistical machinery earns trust *whether or not it was applied well* — a p-value confers credibility on the page regardless of how it was produced. Twenty comparisons with the one significant result reported looks identical, in a written report, to a single comparison planned in advance.

So what actually generates credibility is not the presence of a test but **what was fixed before the data was seen**: the hypothesis, the direction, the α, the exclusion rules, and which comparison was the one being made. State those and the credibility is earned. Omit them and the reader is trusting the format.

### 12. Explain the significance of ensuring the results are not just sample artefacts or coincidences.

Because a pattern that exists **only in this sample** will not survive contact with reality, and every decision taken on it is taken on nothing.

**Why coincidences are guaranteed, not merely possible.** At α = 0.05, one test in twenty produces a significant result when nothing is happening. Test twenty KPIs against last quarter and on average one comes back significant from noise alone. This is the mechanism behind a review that always finds something: the finding was manufactured by the number of comparisons.

The defences: decide in advance which comparison is being tested, or apply a correction — Bonferroni divides α by the number of tests, so twenty tests at an overall 0.05 means judging each against 0.0025.

**The cost of failing.** A sample artefact taken as real gets a budget, a strategy and a set of decisions built on it, and because it is not real the results never arrive. It then costs a second time, because the failure is usually attributed to execution rather than to the finding.

**And the limit that must be stated.** Significance testing guards against **chance**, not against **bias**. A biased sample produces a pattern that is entirely real *within the sample* and entirely wrong about the population, and it will pass every significance test comfortably — more comfortably, in fact, since bias is systematic and shows up consistently. Inference is the defence against coincidence. **The defence against bias is the sampling design, and it has to be inspected separately.**

### 13. How does statistical inference help understand the relationships between multiple variables simultaneously?

By fitting a model in which each variable's contribution is estimated **while the others are held constant**, so effects that are entangled in the raw data can be separated.

| Question | Technique |
|---|---|
| How does an outcome depend on several predictors at once? | Multiple / multivariate regression |
| Do several group means differ? | ANOVA, then post-hoc tests for which pairs |
| Does one predictor's effect depend on another's level? | An interaction term |
| Which predictor matters most, across different scales? | Standardised coefficients (β) |
| Are two predictors too entangled to separate? | Variance inflation factor |

**The mechanism, concretely.** In a simple regression, advertising spend might carry a coefficient of 8.2. Add discount depth to the model and it falls to 5.1 — a 38% drop, with nothing about advertising having changed. The first figure silently includes the fact that heavier campaigns also ran deeper discounts; the second isolates advertising among months at the same discount depth. **That separation is what "simultaneously" buys**, and it is why a coefficient reported without the model's full variable list cannot be interpreted.

**Two cautions.** Adding predictors always raises R², so models of different sizes must be compared on **adjusted R²**. And "holding constant" is a statement about the arithmetic, not the world: on observational data it never licenses a causal claim.

### 14. Provide an example of a tool or methodology mentioned in the text for handling complex and multifaceted data.

**Multivariate regression** — named directly in the lesson as the tool that examines relationships between several variables at once.

| | |
|---|---|
| What it does | Models one outcome from several predictors, estimating each contribution holding the others constant |
| Equation | y = b₀ + b₁x₁ + b₂x₂ + … + ε |
| Output | A coefficient, standard error, t and p-value per predictor, plus R² and adjusted R² |
| Why it suits multifaceted data | It disentangles predictors that move together, which is the defining problem of real-world data |

The lesson names others alongside it: **statistical software** (R, Python with pandas and statsmodels, SPSS) for producing and interrogating result tables, **visualisation tools** (Tableau, Power BI, Seaborn, Matplotlib, ggplot2) for making multivariate output legible, and **model diagnostics** for multicollinearity and fit. **ANOVA** belongs on the list for comparing several groups at once.

### 15. Explain the difference between random and stratified sampling based on the text.

| | **Random sampling** | **Stratified sampling** |
|---|---|---|
| **Method** | Every member of the population has an **equal chance** of selection | The population is divided into **strata**, and a random sample is drawn **within each** |
| **Course example** | Studying a town's television viewing habits by randomly selecting households, so every resident has an equal chance irrespective of age, gender or occupation | A car manufacturer dividing customers by model, then randomly selecting owners of each, so every model is represented |
| **Guarantees** | Fairness, and an unbiased estimate — *on average* | Coverage of every stratum, in this sample, with certainty |
| **Requires** | A complete list of the population | The strata and their sizes known in advance |
| **Best when** | The population is fairly homogeneous and only an overall figure is needed | Subgroups differ on the outcome, some are small, or per-subgroup estimates are needed |

**What stratification actually buys.** A simple random sample *can* miss a small group by chance; stratified sampling makes that impossible. It also delivers a usable estimate per stratum, and — when the strata genuinely differ — a narrower overall interval for the same n, because between-stratum variation is removed from the sampling error.

**The trap that comes with it.** If the strata are sampled **disproportionately** — equal numbers from unequal groups — the results must be **re-weighted** to the real population shares before any overall figure is quoted. With a base that is 82% D2C and 18% B2B, satisfaction of 74 and 61 gives an unweighted average of 67.5 and a correct figure of 0.82 × 74 + 0.18 × 61 = **71.7**. Over four points of error, purely from forgetting that the design was deliberately not proportional.

**And the shared requirement.** Both are **probability** methods — every member has a known, non-zero chance of selection. That is what licenses the margin of error. Convenience and self-selected sampling are not probability methods, and no interval computed from them means what it says.

---

## Part 2 — Formula reference and exam application

| Quantity | Formula | Spreadsheet |
|---|---|---|
| Standard error of a mean | SE = s ÷ √n | `=s/SQRT(n)` |
| Standard error of a proportion | SE = √(p(1−p)/n) | `=SQRT(p*(1-p)/n)` |
| One-sample t statistic | t = (x̄ − μ₀) ÷ SE | `=(mean-claim)/SE` |
| One-tailed p (lower) | — | `=T.DIST(t, df, TRUE)` |
| One-tailed p (upper) | — | `=T.DIST.RT(t, df)` |
| Two-tailed p | — | `=T.DIST.2T(ABS(t), df)` |
| CI for a mean | x̄ ± t × SE | `=mean ± T.INV.2T(0.05,df)*SE` |
| CI for a proportion | p ± z × √(p(1−p)/n) | `=p ± 1.96*SQRT(p*(1-p)/n)` |
| Sample size for a target margin | n = z² × p(1−p) ÷ ME² | `=1.96^2*p*(1-p)/ME^2` |
| Cohen's d, one sample | d = (x̄ − μ₀) ÷ s | `=(mean-claim)/s` |
| Weighted overall figure | Σ(share × stratum value) | `=SUMPRODUCT(shares,values)` |

**z for common levels:** 90% → 1.645 · 95% → 1.96 · 99% → 2.576

**The routine for a question of this type**

| Step | |
|---|---|
| 1 | Name the **population** and the **parameter** being estimated or tested |
| 2 | State H₀ and Hₐ in the units of the problem; say one- or two-tailed, and why |
| 3 | Compute SE, then the statistic, then the p-value |
| 4 | Compute the **confidence interval** — it carries the verdict, the magnitude and the precision together |
| 5 | Compute the **effect size** and say whether it is large enough to matter |
| 6 | Convert into business units and attach a decision |
| 7 | Name what the interval **excludes**: sampling error only, not bias |

Steps 5 to 7 are where the marks concentrate. Steps 3 and 4 are arithmetic a spreadsheet does.

---

## Part 3 — Appraisal of the supplied model answers

Most are correct and appropriately brief. Three phrasings will cost marks in a course about evaluating outcomes, and two answers are incomplete in the same direction.

### Where they are right

| Q | Assessment |
|---|---|
| 1, 2, 3 | Correct. Q3 covers cost, time and logistics accurately |
| 6 | A good example — it names the level, the interval and the quantity |
| 7 | Correct, and correctly says testing is a core component of inference rather than a separate field |
| 8 | A sound scenario. The coffee-rating claim is exactly the right shape for a one-sample test |
| 10 | Correct in structure |
| 13, 14 | Correct, and Q13 usefully adds **ANOVA**, which the lesson text does not name |
| 15 | Correct on both methods |

### Where the wording is loose

**Q4 — "quantify the likelihood that the sample results accurately reflect the population."** This reads as though inference gives the probability that *this particular result* is accurate. It does not. It describes how the **procedure** behaves across repeated sampling: about 95% of intervals built this way capture the truth. The distinction is the same one that separates a correct reading of a confidence interval from the common wrong one, and this course tests it.

**Q5 — "express how likely the sample results are to represent the true population values."** Same issue, applied to p-values. A p-value is the probability of **data this extreme given the null hypothesis** — it is conditional *on* a hypothesis and is not a probability *about* the truth. Writing it the other way round is the single most examined error in this material.

**Q11 and Q12 — "not based solely on chance", "validating whether patterns are statistically significant."** True as far as it goes, and it stops one step short. Significance guards against **chance**; it does nothing whatever about **bias**. A biased sample produces a pattern that is real within the sample and wrong about the population, and it passes significance testing comfortably — more comfortably than a good sample, because bias is systematic. Both answers imply that a significant result is thereby credible, which is exactly the inference the lesson's pitfalls section exists to block.

There is a second gap in Q12: at α = 0.05, one significant result in twenty **is** a coincidence. Significance does not eliminate coincidences; it prices them, at a rate you chose. That is why the multiple-comparison correction exists, and no answer about guarding against coincidence is complete without it.

### Where they are incomplete

**Q9 — "provides evidence-based estimates and confidence levels."** Correct and thin. The specific thing inference gives a manager is the **range**, and particularly its **bad end**: a decision-maker bearing the downside needs the lower bound more than the point estimate. Naming the interval as the risk statement is what turns this from a definition into an answer about management.

**Q10 — the 200-user gadget test.** Structurally right, and it omits the two things that would actually invalidate it: **stated intent is not purchase**, typically by a wide margin, and **how the 200 were recruited** determines whether any of it generalises. A pilot is also an upper bound rather than a forecast, since pilots get attention a rollout cannot reproduce.

### The pattern

All five criticisms are the same shape: **the statement is true of the arithmetic and slightly wider than the arithmetic supports.** A conditional probability is described as an unconditional one, a defence against chance is described as a defence against error in general, and a sample estimate is described without the conditions that make it transferable.

That shape is what an evaluation assignment is marked on. None of these questions is hard. Saying exactly as much as the evidence supports — and no more — is the thing being assessed.

---

## One-page summary

| Q | The short answer |
|---|---|
| **1** | Saying something about an unobservable population from an observable sample, **and stating how far wrong you might be** |
| **2** | Decisions on partial evidence with the strength of evidence stated: estimation, testing, generalisation |
| **3** | Cost, time, feasibility — and a well-run sample often beats a badly-run census |
| **4** | Via the sampling distribution: centred if random, spread ∝ 1/√n, approximately normal. Valid only for the population sampled |
| **5** | Interval, margin, standard error, p-value, effect size — all quantify **sampling** uncertainty, none quantifies bias |
| **6** | "From a random sample of 1 200, mean satisfaction is 4.4 (95% CI 4.3–4.5)" |
| **7** | A procedure testing a claim about a parameter via H₀/Hₐ, a statistic, a p-value and α. One of inference's two branches; agrees exactly with the interval |
| **8** | Coffee chain claims μ ≥ 4.5; n = 120, x̄ = 4.34, s = 0.82 → t = −2.14, p = 0.017, CI [4.19, 4.49]. Reject — but d = 0.195, so statistically established and practically minor |
| **9** | Turns evidence into a range with probabilities. **The interval is the risk statement**, and the lower bound is what a manager needs |
| **10** | 200 users, 62% intent → CI [55.3%, 68.7%]. But intent ≠ purchase, recruitment decides generalisability, and a pilot is an upper bound |
| **11** | Explicit uncertainty, a standard set in advance, repeatability — but only if those were genuinely fixed beforehand |
| **12** | A sample artefact costs twice. At α = 0.05 one test in twenty is a coincidence by design, hence corrections. Guards against chance, **not bias** |
| **13** | Estimates each variable's contribution holding others constant, so entangled effects separate. Advertising 8.2 → 5.1 once discount enters |
| **14** | Multivariate regression; also ANOVA, R/Python/SPSS, Tableau/Power BI, diagnostics |
| **15** | Random = equal chance for all; stratified = split into strata, random within each. Both are probability methods. Disproportionate strata must be re-weighted |
