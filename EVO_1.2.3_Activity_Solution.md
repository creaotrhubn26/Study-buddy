<!--
EVO — Evaluation of Outcomes (FI1BBEO10)
Module 1, Lesson 1.2 — Activity 1.2.3
Own answers plus an appraisal of the supplied model answers.
Generated 2026-09-13.
-->

# Activity 1.2.3 — Understanding linear regression diagnostics and applications

Eight short questions covering the diagnostics in this lesson. The activity ships with model answers, and this time **two of them are wrong, one declines to answer a question the course does answer, and one carries the same text corruption flagged earlier in this lesson**. Both the original answers and the appraisal are below, because knowing *why* a plausible answer is wrong is the assessed skill.

## Q1 — What is the assumption of linearity in linear regression?

**Answer.** That the relationship being modelled is **linear in the parameters** — the outcome is a weighted sum of the terms, each multiplied by one coefficient. In its ordinary form this means each predictor has a **constant marginal effect**: a one-unit increase in x changes y by the same amount whether x is small or large, and that amount does not depend on the level of any other variable.

The business translation, which is what makes it examinable: the model is claiming **this driver works the same way at every level**. Stated that way it is obviously wrong for advertising spend, for discounting, and for house size — all of which saturate.

**The distinction the model answer misses.** Linearity is a requirement on the **parameters**, not on the variables. This is why both remedies offered in the boligpriser case remain linear regression:

| Model | Linear in the variables? | Linear in the parameters? | Still linear regression? |
|---|---|---|---|
| y = β₀ + β₁x | Yes | Yes | Yes |
| y = β₀ + β₁x + β₂x² | **No** | Yes | **Yes** |
| log y = β₀ + β₁ log x | No | Yes | **Yes** |
| y = β₀ + x^β₁ | No | **No** | **No** — needs non-linear least squares |

**Appraisal of the model answer.** Accurate as far as it goes, and the phrase "the change in the dependent variable is proportional to the change in the independent variable(s)" is a fair statement of constant marginal effect. But it defines linearity over the *variables*, which leaves a student unable to explain why adding a squared term does not abandon the method — a point the lesson makes explicitly. **Incomplete rather than wrong.**

## Q2 — In the real estate pricing case study, what pattern did the plot of house sizes against their prices reveal?

**Answer.** A **curved pattern**: as houses became larger, the **price per square metre fell**. Price rose with size throughout, but at a decreasing rate — the relationship saturates. The case attributes this to two business facts: luxury homes pay for amenities other than floor area, and larger homes sit disproportionately outside city centres.

Two details worth carrying:

- **The diagnostic came from a derived quantity.** What the agency noticed was *price per square metre falling*, not "the scatter looks bent". Plotting the ratio is often sharper than plotting the level
- **A straight line still returns a high R²** on this data — around 0.93 — while systematically under-predicting small and large homes and over-predicting mid-sized ones. The fit statistic is not what reveals the problem

> ⚠️ **The model answer answers a different question.** It says: *"The residual plots revealed signs of heteroscedasticity, suggesting that a transformation such as using a logarithmic scale might better stabilise variance."*
>
> That describes **Case study 2 (Alpha Estates)**, a different case, at a different stage, using a different plot. The question asks about **the plot of house sizes against their prices** — the raw scatter, from the linearity section — and that plot revealed **curvature**, not heteroscedasticity.

The two are genuinely different findings and it is worth being able to separate them:

| | Linearity case | Alpha Estates |
|---|---|---|
| **What was plotted** | Price against size (raw scatter) | Residuals against fitted values |
| **What it showed** | A **curve** — the shape of the relationship is wrong | A **funnel** — the spread of the errors is not constant |
| **Which assumption** | Linearity | Homoscedasticity |
| **What breaks** | The **coefficients** are biased; predictions are systematically wrong | The coefficients are **fine**; the standard errors are wrong |
| **Remedy** | Polynomial or log **to fit the shape** | Log, weights or robust errors **to fix inference** |

That the log transformation happens to appear in both remedies is presumably what made the answers collapse into one. **It is a coincidence of remedy, not of diagnosis** — and an exam answer that treats curvature and heteroscedasticity as the same finding has lost the distinction the whole section is built on.

## Q3 — What is endogeneity in the context of linear regression?

**Answer.** Endogeneity is **correlation between an independent variable and the error term**. Since the error term contains everything that affects y and is not in the model, the condition says: *whatever else moves the outcome must not also move with your predictor.* When it does, the model cannot tell which of the two produced the change, and assigns the whole thing to x, because x is the only one it can see.

The three routes in, with what each does:

| Route | Mechanism | Direction of the damage |
|---|---|---|
| **Omitted variable** | A driver of y that correlates with x is left out | Sign is predictable: b_omitted × cov(x, omitted) ÷ var(x) |
| **Measurement error in x** | The recorded x differs from the true x | **Attenuation** — the coefficient is pulled toward zero |
| **Simultaneity** | y also causes x | Direction depends on the feedback's sign |

The consequence is **bias and inconsistency**, and inconsistency is the harsher word: the estimate does not converge to the truth even with infinite data. **More data does not help.** The remedies are instrumental variables, panel or fixed-effects designs, or a natural experiment.

**Appraisal.** Accurate, complete on the three routes, and correctly names both bias and inconsistency. **The best of the eight model answers** — nothing to correct.

## Q4 — What did researchers realise about schools with smaller class sizes?

**Answer.** That schools with smaller classes are **not otherwise comparable** to schools with larger ones — they tend to have **more resources**, and resources independently improve results. Class size is therefore correlated with something in the error term, which is textbook endogeneity, and the naive regression **overstates the benefit of small classes**.

Working the signs, since "overestimated" is ambiguous when the true coefficient is negative:

| Term | Sign | Why |
|---|---|---|
| Effect of resources on performance | **+** | More resources, better results |
| cov(class size, resources) | **−** | Better-resourced schools run smaller classes |
| **Bias** = (+) × (−) | **−** | Added to an already negative coefficient |

A negative number made more negative is **larger in magnitude**, so the estimated advantage of small classes is inflated. In the lesson's worked figures the naive regression returns **−1.60** where the instrumented estimate is **−0.79** — the benefit is overstated by a factor of about **2.0**.

> ⚠️ **The model answer declines to answer.** It opens: *"Although not explicitly mentioned in the provided cases…"* and then gives a generic account of class-size research.
>
> The case **is** in the course material, under Assumption 2, with the scenario, the analysis and the proposed remedy all stated. A model answer that cannot locate a case the question refers to by name is a signal about how these answers were produced, and it is worth treating the whole set with corresponding caution — as Q2 and Q6 confirm.

The generic content it offers is not wrong: schools with smaller classes may differ in funding or demographics, complicating causal interpretation. It simply is not an answer to the question asked, and it omits the case's own remedy — **an instrumental variable, namely state-wide educational policies**. The lesson also notes that this instrument has a **doubtful exclusion restriction**, because class-size legislation arrives bundled with funding and teacher training, which is the very confounder being escaped.

## Q5 — What is the purpose of the adjusted R-squared?

**Answer.** To make R² comparable **across models with different numbers of predictors**. R² can never fall when a variable is added, so it cannot be used to choose between nested models. Adjusted R² applies a penalty for parameters:

> **Adjusted R² = 1 − (1 − R²) × (n − 1)/(n − k − 1)**

so it **can** fall, and a fall says the added variable did not pay for its degree of freedom.

Three properties that make an answer complete:

- **The penalty is weak.** Adding a predictor raises adjusted R² whenever its **|t| > 1** — around p = 0.32, nowhere near significance. Adding pure noise raises it about **a third of the time**
- **It says nothing about generalisation.** It is computed entirely in-sample. Across polynomials of rising degree it moved only from 0.716 to 0.705 while out-of-sample error went from 2.79 to **277.16**
- **It is blind to selection.** Keeping the best 8 of 80 pure-noise candidates gave adjusted R² up to **0.42 on data containing no signal**, because it charges for the predictors kept, not for those examined

**Appraisal.** Correct on purpose and mechanism. "It penalises the addition of irrelevant variables" is right in direction and **overstated in strength** — a penalty that lets a third of pure-noise variables through is a mild deterrent, not a filter. And "a more accurate measure of model quality" is loose: it is a better measure **for comparing nested models on the same data**, which is a narrower and more useful claim.

## Q6 — What does a significantly high F-statistic imply?

**Answer.** That **at least one predictor has a non-zero coefficient** — the model does better than the intercept alone. That is the whole of it.

The null is that *every* slope is zero simultaneously, so rejecting it clears a very low bar, and the bar falls as the sample grows:

| True R² | n = 100 | n = 420 | n = 5 000 |
|---|---|---|---|
| 0.02 | p = 0.16 | **p = 0.0037** | **p < 0.0001** |
| 0.05 | **p = 0.025** | **p < 0.0001** | **p < 0.0001** |

A model explaining **2% of the variance** is significant at n = 420.

> ⚠️ **The model answer contains the error and the correction in one sentence.** It says: *"A significantly high F-statistic suggests that the regression model provides a good fit for the data **and** that at least one of the predictors is significantly related to the dependent variable."*
>
> The second clause is exactly right. The first does not follow from it, and joining them with "and" implies the F-test delivers both. It delivers only the second.

This is the same error the Alpha Estates case makes, which is worth noticing: it is not a slip, it is a **standard misreading** that the course material reproduces in two places. Fit is a separate question, answered by R², the residual plots, and out-of-sample error.

**And where F is genuinely useful**, since a complete answer should say: in **multivariate** models, and especially under collinearity, where every individual t can be insignificant while F is overwhelming. That combination is informative — the predictors matter jointly, but the credit cannot be assigned to any one of them. In a **simple** regression F carries no information at all, because it is algebraically **t²**: on the Alpha Estates model, t = 48.3782, t² = 2340.4478, F = 2340.4478.

## Q7 — How is the standard error used with regression coefficients?

**Answer.** The standard error is the **estimated standard deviation of the coefficient's sampling distribution** — how much the estimate would vary if the study were repeated. It is the denominator that converts a coefficient into a test statistic and the half-width that converts it into an interval:

| Use | Formula | What it gives |
|---|---|---|
| **t-statistic** | t = b ÷ SE | How many standard errors the estimate sits from zero |
| **Confidence interval** | b ± t(crit) × SE | The range of coefficient values the data are consistent with |
| **Comparing precision** | — | A coefficient with a wide SE is weakly identified, whatever its p-value |

The interpretation to hold on to: **a smaller standard error means a more precise estimate**, and precision is not accuracy. A biased coefficient with a tiny standard error is confidently wrong — which is exactly the state Alpha Estates put itself in by dropping a variable to shrink an SE by 69%.

What drives the size of a standard error: **residual variance** (noisier outcome, wider SE), **sample size** (SE falls with √n), **spread of the predictor** (more variation in x, tighter SE), and **collinearity** (√VIF times wider).

> ⚠️ **The model answer is corrupted by the same automated synonym substitution flagged earlier in this lesson.** It reads: *"**More minor** standard errors indicate more precise estimates."* The intended word is **smaller**.
>
> This matters beyond tidiness, because it confirms the diagnosis made earlier. The lesson's own standard-errors paragraph contains the same class of damage — *"A more standard **minor mistake**… a more **significant** standard error… the **assessment** is less precise"*, where smaller, larger and estimate are meant. The corruption is in the **source material**, not in one stray sentence, so expect it elsewhere and read technical passages for sense rather than trusting the wording.

One further slip: "measures the **accuracy** with which a regression coefficient is estimated" should be **precision**. Same accurate-versus-precise confusion as the collinearity definition, which claimed collinearity causes "inaccurate results" when it causes imprecise ones. **Three separate places in this course conflate the two words**, and the distinction decides the Alpha Estates decision.

## Q8 — What issue is indicated by heteroscedasticity in residual plots?

**Answer.** That the **variance of the errors is not constant** across the range of the fitted values or the predictors — the assumption of homoscedasticity is violated. The critical point is **what survives and what does not**:

| | Status under heteroscedasticity |
|---|---|
| Coefficient estimates | **Still unbiased.** They remain centred on the truth |
| Coefficient estimates | **No longer efficient** — a better-weighted estimator exists |
| Standard errors | **Wrong**, and typically **too small** |
| t, p and confidence intervals | **All unreliable**, and biased toward finding effects |

Measured across 3 000 simulated datasets, the classical standard error **understates** the true variability in every heteroscedastic pattern tested: −6% when variance grows with x, −18% when it grows with x², −26% when it shrinks with x. The direction is consistent, so the tests **reject too often**.

The remedies, in the order to try them: **transform the outcome** if the variance is proportional (log is usually right for prices, revenues and counts); **robust standard errors** if you only need valid inference and want to keep the coefficients as they are; **weighted least squares** if efficiency genuinely matters and you can model the variance. And before any of them — **check whether the funnel is really a missing variable**, since a driver you failed to include will often show up as non-constant spread.

**Appraisal.** Accurate and well-phrased. "Inefficient estimates and unreliable hypothesis testing" is precisely correct, and the answer avoids the common error of claiming the coefficients become biased. **The second-best of the eight**, needing only the direction of the standard-error error to be complete.

## What this activity is really testing

Tallying the supplied answers:

| Q | Topic | Verdict on the model answer |
|---|---|---|
| 1 | Linearity | Incomplete — defines it over variables, not parameters |
| 2 | Real estate pattern | **Wrong case.** Describes heteroscedasticity where curvature is asked about |
| 3 | Endogeneity | **Correct and complete** |
| 4 | Class size | **Declines a question the course answers**, then answers generically |
| 5 | Adjusted R² | Correct, overstates the strength of the penalty |
| 6 | F-statistic | **Wrong first clause**, correct second, joined by "and" |
| 7 | Standard error | Correct in substance, **corrupted wording**, accuracy/precision slip |
| 8 | Heteroscedasticity | **Correct and complete** |

Two of eight correct as written, two containing outright errors. **The lesson to draw is not that the material is unreliable but that a plausible-sounding answer needs checking against the mechanism**, and every error here is catchable by asking one question: *what would have to be true for this to follow?* A significant F would have to rule out poor fit — it does not. A residual plot would have to be the same thing as a scatter plot — it is not.
