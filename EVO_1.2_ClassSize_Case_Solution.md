# EVO — Lesson 1.2 case
## Educational impact: class size, endogeneity and instrumental variables

**Course:** FI1BBEO10 Evaluation of Outcomes · **Module 1, Lesson 1.2** · assumption 2, no internal causation of the regressors

---

## The case as given

| | |
|---|---|
| **Scenario** | A study is designed to evaluate the impact of **class size on student performance** |
| **Analysis** | Schools with smaller class sizes might have **more resources**, leading to better overall education quality. If this is not accounted for, the effect of class size on performance might be **overestimated** due to omitted variable bias |
| **Action** | To address potential endogeneity, researchers could employ an **instrumental variable**, such as state-wide educational policies, that affect class sizes but are not directly tied to individual school resources |

---

## Part 1 — Diagnosing the problem precisely

### 1.1 Name the variables

| Role | Variable |
|---|---|
| Outcome (y) | Student performance — a test score |
| Regressor of interest (x) | Class size, in pupils |
| **Confounder (unobserved)** | School resources — funding, facilities, teacher experience |
| Instrument candidate (z) | State-wide educational policy |

### 1.2 Why this is endogeneity and not just noise

Resources sit in the error term, because they are not in the model. The assumption requires the regressor to be uncorrelated with that error term, and here it plainly is not: **well-resourced schools run smaller classes.**

So the two paths into performance are tangled:

- Class size → performance (the effect we want)
- Resources → class size, and resources → performance (the path that contaminates it)

The regression sees only class size. Everything arriving through the resources path gets attributed to class size, because class size is the only variable in the model that moves with it.

### 1.3 The direction of the bias — stated carefully

"Overestimated" needs unpacking, because the true coefficient is **negative**: larger classes mean worse performance.

> **Bias = b_resources × cov(class size, resources) ÷ var(class size)**

| Term | Sign | Why |
|---|---|---|
| b_resources | **positive** | More resources improve performance |
| cov(class size, resources) | **negative** | Better-resourced schools have *smaller* classes |
| **Product** | **negative** | The bias is negative |

Adding a negative bias to an already-negative coefficient makes it **more negative** — larger in magnitude. In plain terms: **the apparent benefit of shrinking classes is exaggerated.** The course text's "overestimated" refers to the size of the estimated benefit, and that is correct — but write it out this way, because "overestimated" applied to a negative number is ambiguous and a marker will want to see that you know which way it goes.

### 1.4 How large? A quantified demonstration

Simulated with a **known** true effect, so the bias can be measured rather than asserted. True effect: **−0.80** points per additional pupil in the class. Resources are real and omitted.

| Estimate | Value | |
|---|---|---|
| **True effect** | **−0.800** | What we are trying to recover |
| **Naive OLS**, resources omitted | **−1.575** | The apparent benefit is nearly **double** the real one |
| Predicted bias from the formula | −0.779 | −0.800 + (−0.779) = −1.579, against −1.575 observed |
| OLS **controlling for resources** | −0.819 | Recovers the truth — *if you can measure resources* |
| **2SLS with a valid instrument** | **−0.841** | Recovers it without measuring resources at all |

The formula predicts the observed bias to within 0.004. This is not a vague worry: **omitted variable bias is calculable, and here it roughly doubles the policy conclusion.**

### 1.5 Why more data does not help

The naive estimate is **inconsistent**. Add a million schools and it converges on −1.575, not on −0.80, with a confidence interval so tight it looks decisive. A policy costing billions would be justified on a number that is wrong by a factor of two and precise to three decimals.

---

## Part 2 — Evaluating the proposed instrument

An instrumental variable must satisfy three conditions. The course text asserts the second; it is the one most likely to fail here.

### 2.1 Relevance — does the instrument actually move class size?

**Testable, and plausibly satisfied.** State-wide policies on class-size caps, funding formulas and teacher-pupil ratios do change class sizes.

The test is the **first stage**: regress class size on the instrument and look at the F statistic.

> **Rule of thumb: first-stage F below about 10 means a weak instrument.**

A weak instrument is not merely imprecise — it is **biased toward the naive OLS estimate**, which defeats the entire purpose. In the simulation:

| Instrument strength | First-stage F | 2SLS estimate |
|---|---|---|
| Strong | 1 529 | **−0.783** (true −0.80) |
| Moderate | 106 | −0.970 |
| Weak | **4** | **−1.109** — drifting back toward the biased −1.575 |

**So always report the first-stage F.** An IV analysis without it is an assertion.

### 2.2 The exclusion restriction — and this is where the proposed instrument is doubtful

The condition: **the instrument may affect the outcome only through class size.** No other path.

The course says state-wide policies are "not directly tied to individual school resources". That is the right condition to be worried about, and I do not think it holds:

| Why exclusion is doubtful | |
|---|---|
| **Policies arrive bundled** | A class-size reduction law comes with funding to hire teachers, and often with facilities money. That funding *is* the confounder we are trying to escape |
| **They arrive with other reforms** | Curriculum changes, testing regimes and teacher-training programmes are typically legislated together |
| **Hiring effects** | A sudden statewide demand for teachers can lower average teacher quality — a direct path to performance that has nothing to do with class size |

**And the consequence of getting this wrong is severe.** If the instrument has its own direct effect on performance, 2SLS does not merely fail to fix the bias — it can produce an estimate **worse than doing nothing**:

| Direct effect of the policy on performance | 2SLS estimate |
|---|---|
| None (valid instrument) | **−0.782** — correct |
| Moderate leak | −1.259 |
| Large leak | **−2.344** — nearly three times the truth, and worse than the naive −1.575 |

That is the finding worth carrying: **an invalid instrument is not a partial fix. It is a new bias, and it can point further from the truth than the problem it was meant to solve.**

The exclusion restriction is also, notably, **not testable** with a single instrument. It has to be argued from institutional knowledge of how the policy worked.

### 2.3 Independence — is the instrument itself as good as random?

States that pass class-size legislation differ from states that do not: politically, economically, demographically. If those differences also affect student performance, the instrument is contaminated at the source.

The usual remedies are to exploit variation *within* a policy rather than across states — the timing of implementation, or a threshold in the rule — rather than comparing adopting states with non-adopting ones.

### 2.4 Verdict on the proposed instrument

**Relevant, probably. Excludable, doubtfully. Independent, questionably.** As stated, "state-wide educational policies" is the right *kind* of idea and too coarse to be credible without much more specification: which policy, what exactly it changed, what else it changed at the same time, and why the analyst believes the only route to test scores was through class size.

---

## Part 3 — What a defensible design looks like

Ranked by how convincingly each closes the back door.

| Approach | How it works | Cost |
|---|---|---|
| **1. Randomised assignment** | Assign pupils and teachers to class sizes at random. Class size becomes independent of resources *by construction*, so exogeneity holds because you enforced it. The Tennessee **Project STAR** experiment is the well-known instance | Expensive, slow, and ethically constrained |
| **2. A discontinuity in a rule** | Where a cap forces a cohort to split at a threshold — 30 pupils becoming two classes of 15 or 16 — schools either side of the cutoff are otherwise similar. **Angrist and Lavy's use of Maimonides' rule** is the classic study | Needs the rule and the enrolment data; the estimate applies near the threshold only |
| **3. A sharper instrument** | Cohort-size fluctuations driven by birth-year variation move class size without plausibly touching resources | Weaker first stage; must argue exclusion carefully |
| **4. Measure the confounder** | Add per-pupil spending, teacher experience and facilities to the regression | Only removes what you can measure, and measurement error re-introduces bias by attenuation |
| **5. Fixed effects** | School fixed effects remove everything constant about a school over time | Cannot remove *changing* resources, which is often the issue |
| **6. Report the direction** | Estimate the naive model and state that it overstates the benefit of small classes, with the reasoning | Weakest — but honest, and it beats presenting −1.575 as the effect |

**Approach 2 is the one to name in an exam answer**, because it converts an observational study into something close to an experiment using a rule the system already applies for reasons unrelated to student ability.

---

## Part 4 — Formula reference

| Quantity | Formula |
|---|---|
| Omitted variable bias | bias = b_omitted × cov(x, omitted) ÷ var(x) |
| Biased estimate | b̂ = b_true + bias |
| First stage (2SLS step 1) | x̂ = π₀ + π₁z, keep the fitted values |
| Second stage (2SLS step 2) | y = β₀ + β₁x̂ + ε, and β₁ is the IV estimate |
| Relevance test | F on π₁ in the first stage; **F < 10 means weak** |
| Attenuation from measurement error | b̂ = b_true × σ²ₓ ÷ (σ²ₓ + σ²ᵤ) |

**Exam routine for any endogeneity question**

| Step | |
|---|---|
| 1 | Name the omitted variable, and say why it correlates with the regressor |
| 2 | Sign the bias using the formula — two signs multiplied, then state whether the effect is over- or understated **in plain words** |
| 3 | Say that more data will not fix it, because the estimate is inconsistent |
| 4 | Say that the residual plot cannot detect it, because least squares makes residuals orthogonal to the regressors by construction |
| 5 | Propose a remedy, and test the instrument against relevance, exclusion and independence if you propose one |
| 6 | If no remedy is available, state the direction of the bias |

---

## Part 5 — The answer, written out

> Class size is endogenous in this design. School resources affect both class size and performance, and are not in the model, so they sit in the error term and correlate with the regressor. The bias is the product of the resource effect on performance (positive) and the covariance between class size and resources (negative), so it is negative — and since the true class-size coefficient is also negative, the estimate is inflated in magnitude. **The study will overstate the benefit of smaller classes**, on simulation with a known truth by roughly a factor of two.
>
> This cannot be resolved by collecting more schools: the estimate is biased *and inconsistent*, so a larger sample yields a precise estimate of the wrong number. Nor can it be detected in diagnostics, since least squares constructs residuals orthogonal to the regressors, so the residual plot looks clean however severe the endogeneity.
>
> An instrumental variable is the right family of solution. The proposed instrument — state-wide educational policy — satisfies **relevance**, which should be demonstrated with a first-stage F above 10, but its **exclusion restriction is doubtful**: class-size legislation typically arrives bundled with funding, facilities and training, which is precisely the confounder being escaped. An instrument with its own path to the outcome does not partially fix the bias; simulation shows it can produce an estimate further from the truth than the naive one.
>
> I would instead exploit a **class-size cap discontinuity**, comparing cohorts either side of the enrolment threshold that forces a class to split, since the rule moves class size for reasons unrelated to school resources or pupil ability. Failing that, I would control for measured resources, use school fixed effects, and report the estimate with an explicit statement that it remains an upper bound on the benefit of smaller classes.

---

## One-page summary

| | |
|---|---|
| **The problem** | Resources drive both class size and performance, and are omitted |
| **Direction** | Bias is negative on an already-negative coefficient → the benefit of small classes is **overstated** |
| **Magnitude** | Simulated: true −0.80, naive −1.575. Nearly double |
| **Why data doesn't help** | Inconsistent, not merely imprecise |
| **Why diagnostics don't help** | OLS residuals are orthogonal to regressors by construction |
| **The proposed instrument** | Relevant yes; **exclusion doubtful** — policies come bundled with funding |
| **Cost of a bad instrument** | Simulated −2.344 against a truth of −0.80: worse than no instrument at all |
| **Always report** | The first-stage F. Below 10 the IV drifts back toward the OLS bias |
| **Better design** | Class-size cap discontinuity, or randomisation as in Project STAR |
