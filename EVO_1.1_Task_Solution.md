# Evaluation of Outcomes — Lesson 1.1 Task

## Data Analysis, Key Performance Indicators (KPIs), and Version Control

**Course:** FI1BBEO10 Evaluation of Outcomes · Module 1, Lesson 1.1

Answers to all 22 questions. Each answers the lesson text first, since that is what is being assessed, and then adds the evaluation depth the course expects at level 5.1 where it is useful.

---

## 1. Definitions of quantitative and qualitative KPIs, with the examples from the text

**Quantitative KPIs** are metrics based on **numerical data**, allowing straightforward measurement and comparison. They hinge on structured data, which aligns in tables, rows and columns and is therefore responsive to automation.

*Examples from the text:* sales revenue, profit margins, return on investment, customer acquisition cost, website traffic, employee turnover rate.

**Qualitative KPIs** are metrics focusing on **non-numerical data**, offering insight into subtler aspects of business performance. Being non-numerical makes them **subjective**, and their power is reaching areas that are less responsive to straightforward numerical measurement.

*Examples from the text:* customer satisfaction and employee engagement.

The full classification:

```
KPIs ├─ Quantitative ├─ Financial     — sales revenue, profit margins, ROI
     │               └─ Non-financial — CAC, website traffic, employee turnover
     └─ Qualitative  ├─ Customer satisfaction — surveys, interviews, NPS
                     └─ Employee engagement   — reviews, satisfaction surveys, one-on-ones
```

---

## 2. Two financial and two non-financial quantitative KPIs

| Type | KPI |
|---|---|
| **Financial** | Sales revenue |
| **Financial** | Return on Investment (ROI) |
| **Non-financial** | Customer Acquisition Cost (CAC) |
| **Non-financial** | Employee turnover rate |

---

## 3. Why each matters for organisational performance

**Sales revenue.** Total income generated from business operations *before expenses are deducted*. It indicates market demand and is essential for planning future growth. Its limitation is built into that definition: sitting before expenses, it says nothing about whether the business kept any of it. Revenue rising while margin falls is a common and genuinely bad pattern that revenue alone cannot show.

**Return on Investment.** A comprehensive measure of an investment's effectiveness, comparing the return received to the capital invested, usually as a percentage. It is pivotal for capital allocation, because it is how competing uses of money are ranked. Its importance also makes it the financial KPI most easily flattered, since both halves of the ratio are choices.

**Customer Acquisition Cost.** The cost of acquiring a single customer, and the fundamental measure of marketing effectiveness. Its organisational importance is that it sets a ceiling on sustainable growth: a business whose CAC exceeds what a customer is worth cannot grow its way out of the problem. A low CAC *relative to customer lifetime value* is what indicates a healthy business model.

**Employee turnover rate.** An **organisational health check**. High turnover typically signals dissatisfaction or a problematic work environment, and it carries direct financial consequences through the cost of hiring and training replacements. It matters disproportionately because it is a *leading* indicator: it appears before the productivity and capability losses it causes.

---

## 4. How each is measured and interpreted in a real-world scenario

Scenario: **Nordtre AS**, a Norwegian sustainable-furniture company with a webshop, retail partnerships and a B2B contract arm.

| KPI | Measured by | Interpretation in the scenario |
|---|---|---|
| **Sales revenue** | Financial software, reconciled against CRM closed-won deals | NOK 18.4m across three channels. Read *by channel*, since the three have very different economics and a blended figure hides a mix shift |
| **ROI** | (Gain from investment ÷ cost of investment) × 100 | A NOK 3.0m production investment returning NOK 780k a year gives 26% in year one — but payback is 3.85 years, so cumulative three-year ROI is −22% |
| **CAC** | Acquisition spend ÷ new customers, from marketing platforms and the CRM | D2C NOK 100, B2B NOK 5,000, blended NOK 176. Blended CAC fell 28% year on year, yet total acquired lifetime value was flat — the "improvement" was a mix shift toward cheap, low-value customers |
| **Employee turnover** | HRM or payroll system: departures ÷ average headcount | 20.6% company-wide, but 11.8% regretted-only, and both design leavers were senior product designers. At NOK 95,000 per replacement, seven departures cost 36% of operating profit |

**The interpretation principle running through all four:** none of them means anything as a bare number. Each needs a comparison — against history, a target, a benchmark, a segment, or normal variation. *Isolated numbers seldom tell the whole tale.*

Two specific traps the scenario shows:

- **"Profit margin" is ambiguous.** Nordtre's gross, operating and net margins are 45.0%, 10.0% and 7.8% — a factor of nearly six. Any target or comparison stated as "profit margin" is meaningless until the variant is named.
- **Blended CAC is total spend ÷ total customers**, never the average of segment CACs. Averaging NOK 100 and NOK 5,000 gives NOK 2,550, wrong by a factor of fourteen, because one segment has 64 times the volume.

---

## 5. Tools and methodologies for collecting quantitative KPIs

From the text:

| Category | Platforms named | KPIs produced |
|---|---|---|
| **Web analytics tools** | Google Analytics | Visitor count, time on page, bounce rate, conversion |
| **CRM systems** | Salesforce, HubSpot, Microsoft Dynamics | CAC, average deal size, pipeline, win rate |
| **HRM software** | Workday, SAP SuccessFactors | Turnover rate, time to hire, training costs |
| **Inventory and supply chain** | Oracle NetSuite, SAP Integrated Business Planning | Inventory turnover, order fulfilment rate, supply chain wastefulness |
| **Financial software** | QuickBooks, Sage | Revenue growth, net profit margin, cash conversion cycle |
| **Custom in-house tools** | Purpose-built | Whatever the standard platforms do not cover |

---

## 6. One tool researched further: CRM systems

**Features**

- Contact and account records as a single source of customer truth
- Pipeline and deal-stage tracking, with probability weighting
- Activity logging: calls, emails, meetings, tied to the account
- Built-in analytics and configurable dashboards
- Workflow automation: follow-up reminders, stage-change triggers
- Integration with marketing platforms, email, and financial software

**Pros**

- **Centralised data.** One record per customer instead of knowledge held in individuals' inboxes
- **Enhanced communication.** Anyone picking up an account can see its history
- **Customer data analysis.** Sales KPIs — CAC, average deal size, win rate, cycle length — become computable rather than estimated
- **Continuity.** The account survives the salesperson leaving, which is the same argument as version control for data

**Cons**

- **High cost**, especially per-seat licensing at enterprise tier
- **Complexity**, and heavy configuration to fit an actual sales process
- **Training requirements**, without which adoption fails
- **Scale mismatch.** Salesforce is built for large sales organisations; a small business often pays more in configuration than it recovers

**The evaluation point.** A CRM's data quality depends entirely on the discipline of the people entering it. Every field is typed in by a person, so a deal stage updated late corrupts every cycle-length KPI while the dashboard continues to look authoritative. **An automated dashboard on a manually maintained field is a human process wearing automation's clothes.** Before trusting a CRM-derived KPI, ask what proportion of records are complete and how quickly stages are updated.

---

## 7. One metric from each qualitative area

| Area | Metric chosen |
|---|---|
| **Customer satisfaction** | Surveys |
| **Employee engagement** | Performance reviews |

---

## 8. How each is assessed, and the data collection methods

### Customer satisfaction surveys

**Assessment.** Detailed questionnaires using Likert scales, multiple-choice questions or open-text fields, sent post-purchase or periodically. Analysis works from the response distribution rather than a single average.

**Collection methods:** email or in-app questionnaires; Likert-scale items for comparability; open-text fields for the reasons; NPS as a single-question variant.

**Real-world scenario.** Nordtre sends a post-purchase survey to 1,200 customers and receives 348 responses — a 29% response rate. Reported as a distribution rather than a mean, because a Likert scale is **ordinal**: the gap from "Strongly Disagree" to "Disagree" is not guaranteed to equal the gap from "Agree" to "Strongly Agree". The safer summary is the top-two-box share.

### Employee performance reviews

**Assessment.** Structured one-on-one meetings holding **two perspectives at once** — how the employee views their role and contribution, and how management perceives them — covering skills, competencies and areas for improvement.

**Collection methods:** scheduled review meetings; self-assessment forms completed in advance; manager assessment against defined competencies; written outcomes with agreed development actions.

**Real-world scenario.** Nordtre runs semi-annual reviews across 34 staff. The reviews are read alongside an anonymous engagement survey, because the two answer different questions: the review captures a manager–employee conversation, and only the anonymous instrument captures what someone would not say to their manager.

---

## 9. Challenges in measuring and interpreting these metrics

The text names **subjectivity, non-standardised metrics, and the potential for biased or skewed results**. In practice these break down as:

| Challenge | What it looks like |
|---|---|
| **Subjectivity** | The same response can be read differently by different people, and the same rater's standards drift over time |
| **Non-standardised metrics** | Reworded questions produce different scores from identical underlying attitudes, so periods are not comparable |
| **Self-selection** | Surveys are answered by people with something to say. A survey answered mainly by customers who contacted support measures only their satisfaction |
| **Rater inconsistency** | Two managers apply the same review scale differently, so scores are not comparable across teams |
| **Ordinal data treated as interval** | Averaging a Likert scale does arithmetic on ranks. A mean of 3.7 can come from everyone answering 3 and 4, or from half answering 1 and half answering 5 |
| **The anonymity trade-off** | Anonymity buys candour and costs follow-up. One-on-ones buy depth and lose anonymity |
| **Low volume** | Qualitative collection is manual, so samples are small and single unusual responses carry disproportionate weight |
| **Reviews are not anonymous** | An employee will not tell their manager that the manager is the problem |

**The practical defences:** report the response rate always, keep question wording fixed between periods, report box shares rather than means, and run both an anonymous and a non-anonymous instrument so each covers the other's blind spot.

---

## 10. The ethical considerations from the text

| Consideration | What it means |
|---|---|
| **Transparency** | Not an optional best practice but an **ethical imperative**. A lack of clarity in how KPIs are calculated breeds suspicion, undermines trust and can invite legal scrutiny |
| **Data integrity** | Manipulating data to produce more favourable KPIs is unethical and potentially disastrous. "Cooking the books" risks stock market devaluation, legal repercussions and a tarnished reputation |
| **Inclusivity** | Involving stakeholders from different departments and levels of seniority in KPI selection mitigates **biased or myopic** indicators and produces a fairer, more representative set |
| **Ethical responsibility to shareholders and stakeholders** | Manipulating or misrepresenting KPIs cascades beyond the organisation, affecting shareholders, employees and the market at large |

---

## 11. Reflection: why these matter for decision-making

Ethical considerations in selecting and interpreting KPIs ensure an accurate representation of organisational performance, which is the foundation of trust and of informed decision-making. Adhering to them safeguards against legal repercussions and promotes a fair, comprehensive evaluation, strengthening organisational integrity and stakeholder confidence.

The effect on decision-making is concrete rather than abstract. **A decision is only as good as the picture it was made from.** If a KPI is calculated in a way nobody outside the team can describe, then nobody outside the team can challenge a decision based on it — the decision has become unaccountable without anyone intending it. If figures are adjusted until they clear a threshold, the organisation ends up allocating real money against a picture it invented. And if the KPI set was chosen entirely by the department it measures, the organisation will systematically direct effort toward what that department already does well.

Two points sharpen this beyond the general statement.

**Most ethical failure in KPI work is not falsification.** It is a sequence of individually defensible choices that all happen to point the same way: quoting the most flattering margin variant, removing outliers until the model looks better, extending a time window until a trend appears. Each is arguable in isolation; together they are **selective evaluation**. The defence is procedural — decide and document the method before seeing the result.

**Ethics is inspectable through artefacts, not intentions.** An evaluator cannot audit someone's good faith, but they can read a versioned definition, re-run a reproducible pipeline, and check whether limitations were stated alongside the number. That is why the ethical practices in this lesson are the same practices as the technical ones, seen from the outside. Documentation is not administrative tidiness — **it is the only thing a cognitive shortcut or a convenient framing cannot quietly rewrite.**

---

## 12. What heuristics are, and how they relate to decision-making

Heuristics are **mental shortcuts or "rules of thumb"** that people use to simplify decision-making and problem-solving. Instead of methodically analysing every aspect of a decision, they facilitate quick and often **subconscious** judgments. They result from the brain's strategy to save effort and function efficiently, particularly under conditions of **uncertainty or information overload**.

Their relation to decision-making is direct: most real decisions are made without complete information and without time for full analysis, so heuristics are what makes deciding possible at all. The relevance to this course is that **a KPI is itself a heuristic** — a measurable proxy chosen because it supports a decision faster than a full analysis would, and one that can therefore be wrong.

---

## 13. Who popularised the concept, and what they contributed

**Daniel Kahneman and Amos Tversky**, in the **1970s**, popularised the concept of heuristics in cognitive psychology. They studied how people make decisions and solve problems, and discovered that individuals often rely on heuristics, especially when facing complex issues or incomplete information.

Their central contribution for this course is that the resulting errors are **systematic rather than random**. People do not err unpredictably under uncertainty; they make the same errors in the same directions. That is what makes the errors anticipatable — and therefore something an organisation can design against with written definitions, review dates and documented method.

---

## 14. Benefits and drawbacks of heuristics

**Benefits**

- **Efficiency.** Quicker decisions without the need for detailed analysis.
- **Functionality in uncertainty.** Complete information is often unavailable; heuristics let people decide and act anyway.

**Drawbacks**

- **Inaccuracy.** Shortcuts can lead to errors or biases.
- **Over-reliance.** Depending on them without regard for their limitations produces **systematic errors or consistent biases** in judgment.

**The asymmetry worth stating.** Inaccuracy is occasional and tolerable — it is the price of speed, and a heuristic that is right eight times in ten and free is a good rule. Over-reliance is the serious one, because a consistent bias **does not average out** across many decisions; it accumulates in the same direction. An organisation that anchors on every launch month will misjudge every product it ships, the same way, every time.

---

## 15. The availability heuristic in a KPI scenario

**How it operates.** Decision-making based on the **most readily available information** — the most recent data, or whatever left a strong impression. In KPI work it means stakeholders act without delay on the most recent numbers.

**Strengths.** **Rapid response.** Quick decisions are crucial in certain industries and scenarios, such as crisis management or live events, where the cost of delay exceeds the cost of an imperfect diagnosis.

**Weaknesses.** **Surface-level insights.** Relying exclusively on immediately available information produces superficial analyses that miss deeper, less apparent trends or anomalies.

**The text's example.** A social media company notices a sudden drop in user engagement and focuses on a recent platform update as the culprit. The decline could instead be part of a broader industry trend, or the effect of a concurrent event such as a major global sports competition distracting users.

**What makes this instructive.** The update was not chosen because the evidence pointed at it. It was chosen because it was the change everyone knew about — a sports final is not on anyone's dashboard. The defence is one question that costs nothing: **what else changed in the same window?** Followed by a second: is the drop larger than normal variation at all?

The consequence of getting it wrong compounds. Roll back the update, and engagement does not recover — because the real cause is still running, and a change that may have been an improvement has now been discarded. The team also learns a false lesson about updates.

---

## 16. The anchoring heuristic in sales KPIs

**How it operates.** Anchoring is the tendency to rely heavily on an **initial piece of information** — the *anchor* — when making subsequent judgments.

**In sales.** The initial monthly revenue after a product launch sets expectations. If the first month sees high sales, driven by promotional effort and launch publicity, the anchoring heuristic establishes that figure as the norm. Subsequent months are then perceived as **underperforming**, even when they reflect a more sustainable sales pattern. If the initial data or benchmark is flawed or outdated, it distorts every analysis that follows.

**The strength, which is real.** Anchoring provides a **consistent reference**. Analysis needs a fixed point; without one, every month is evaluated from scratch and comparison is impossible. Anchoring is what makes a baseline usable at all.

**Why it is hard to catch.** An anchor stops looking like a claim and starts looking like neutral background. Nobody re-examines the furniture. The damage is also indirect: months of good performance reported as shortfall push a sales team toward discounting to close the perceived gap — cutting gross margin to hit a revenue figure that was never sustainable.

**The defence is one sentence.** *"Month one was 40% promotional and is not a baseline."* More months of data would not have helped; information **about the anchor** would have. Date the anchor and record the conditions that produced it, and put review dates on thresholds for the same reason.

---

## 17. The role of KPIs in business decision-making

KPIs are **invaluable signposts** within the complex landscape of business decision-making. They are not merely data points but strategic metrics serving three specific purposes:

- **Data-driven decisions.** They provide empirical, often real-time data that acts as a **counterbalance to the cognitive biases** that commonly infiltrate decision-making, giving factual ammunition for robust choices.
- **Focus and prioritisation.** In a sea of information, they act like a **lighthouse**, directing attention to critical performance aspects so energy is spent where impact is greatest.
- **Accountability and objectivity.** They permit evaluation that **transcends individual biases and subjectivities**, setting a bar against which outcomes can be objectively measured. Bonuses tied to KPIs can be equitable, since everyone knows the success criteria.

**The condition attached to the first purpose.** A KPI counterbalances bias only when it is presented **with its context** — history, target, benchmark, normal variation. A bare number does the opposite: it is recent, on a screen and instantly available, which is precisely the kind of evidence the availability heuristic runs on. Presented alone, a KPI *is* the anchor.

**And on the third.** Attaching money to a KPI is the strongest possible pressure on it. Goodhart observed in 1975 that a statistical regularity collapses once pressure is placed on it for control purposes. A bonus-linked KPI is equitable when it is close to the goal, paired with a guard KPI, fixed before the period, and reviewed for gaming — and harmful otherwise.

---

## 18. How KPIs help rectify customer satisfaction issues

If a KPI highlights an **increasing customer churn rate**, that serves as a concrete impetus to investigate and rectify the underlying issues, supplying factual data rather than an impression to work from.

**But the signpost points; it does not arrive.** Six checks come before the fix:

| Step | Question |
|---|---|
| 1 | Is the rise larger than normal month-to-month variation? |
| 2 | Which definition of churn, and has it changed? |
| 3 | Is it concentrated in a segment, or spread evenly? |
| 4 | What else changed in the same window? |
| 5 | What does the qualitative evidence say about *why*? |
| 6 | What action, and what would tell us it worked? |

Only step 6 is the decision. Step 5 is where the rectification actually comes from: the churn rate says how many customers left and can never say what made them leave. **The quantitative half supplies the size; the qualitative half supplies the cause**, and you cannot prioritise without a size or act without a cause.

---

## 19. The KPIs Amazon focuses on

Amazon does not treat customer satisfaction broadly but drills into specific metrics:

| KPI | What it does |
|---|---|
| **Customer Lifetime Value (CLV)** | Predicts the revenue reasonably expected from a single customer account, projecting the total contribution across the whole relationship |
| **Net Promoter Score (NPS)** | Assesses loyalty by measuring willingness to recommend, calculated as % promoters − % detractors |
| **Customer retention rate** | Tracks the proportion of customers kept over a period |

These tailor **inventory, pricing, customer service and technological innovation**.

Alongside them Amazon scrutinises operational KPIs — **order fulfilment time** and **inventory turnover rate** — which is what makes one-day delivery a logistical achievement guided by exacting real-time measurement rather than a marketing claim.

*Note on terminology:* CLV here is the same measure this course elsewhere calls **LTV**, lifetime value. Either term may appear. Its purpose is the same in both: **CLV is what makes CAC interpretable**, since a falling acquisition cost is good or bad news entirely depending on whether the customers acquired are worth more or less.

---

## 20. How dashboards enhance accountability

KPI dashboards enhance accountability by providing a **clear, visible display** of performance metrics. That visibility ensures teams and individuals are attuned to their responsibilities and can see, in real time, how their efforts contribute to the organisation's principal objectives.

**The mechanism is visibility, and visibility cuts both ways.** What appears *alongside* a KPI decides what people are actually held accountable for. A tile showing only a team's primary KPI makes them accountable for the **proxy**; a tile showing that KPI with its guard makes them accountable for the **outcome**.

The support desk case in this lesson is the illustration: the team was highly accountable for average handling time, hit the target, and made the service worse. Accountability was working exactly as designed. The design was the problem.

---

## 21. How different users benefit — a CFO versus a sales manager

Different users have different needs, so dashboards should offer **customisation options**, letting individuals tailor views to their roles, objectives and preferences.

| User | Focuses on | Because their decisions concern |
|---|---|---|
| **CFO** | Financial KPIs: margin, cash conversion cycle, cost lines, ROI | Capital allocation and financial position |
| **Sales manager** | Lead and conversion metrics: pipeline, win rate, cycle length | Where the pipeline is stalling this week |

This is the audience-first principle applied per person: **define the audience and the decisions they make, then select the KPIs tied to those decisions.** A single view built for everyone serves nobody, which is data overload in its most common form.

**Two cautions, since customisation has a cost:**

- **The shared set must stay visible.** If each role only sees its own metrics, the trade-offs between them become invisible — the guard-KPI failure at organisational scale. The sales manager needs to see margin, precisely because discounting is how a pipeline target gets hit.
- **The definitions must not fork with the views.** Two roles *filtering* the same KPI differently is fine; two roles *computing* it differently is the disputed-evaluation problem, and it is exactly what written, versioned definitions prevent.

---

## 22. The significance of update frequency

Update frequency ensures stakeholders always base decisions on the **most recent and relevant data**. The right frequency depends on the business and the metric: some dashboards need real-time updates, while daily or weekly refreshes are sufficient for others.

| Frequency | Suits | Fails when |
|---|---|---|
| **Real time** | Operational metrics where intervention is immediate — incidents, stock-outs, system load | Applied to a slow-moving strategic KPI, where it generates daily false alarms |
| **Daily or weekly** | Most operational KPIs | The underlying noise is larger than the reporting interval |
| **Monthly or quarterly** | Strategic and financial KPIs, survey-based measures | A problem needs intervention within days |

**The refresh-rate trap.** More frequent is not automatically better, and this is the part most answers miss. The more often a metric is displayed, the more opportunities there are to **mistake normal variation for a signal**. A KPI that naturally swings a few percent week to week will, shown daily, appear to move meaningfully most days — when nothing has changed except how often someone is looking.

The consequence is **over-steering**: the organisation corrects constantly for movements that would have corrected themselves, and because each correction takes time to show an effect, its result arrives after the next correction has already been made. Cause and effect become impossible to separate.

**Two defences.** Require a **sustained move** rather than a single reading before an alert fires, and state the **normal variation** on the tile so a reader can distinguish a real change from ordinary movement. Also give every tile a **freshness stamp**: a stale number is worse than no number, because it looks current.

---

## Appendix: the thread running through all 22

Almost every answer above resolves to the same move.

A KPI is a heuristic. A heuristic can be wrong. A wrong heuristic is invisible from the inside — so you **replace a judgement with a record**.

That is what a written definition is (Q10, Q21), what version control is (Q11), what a dated anchor is (Q16), what "what else changed in the window" is (Q15), what a stated response rate is (Q9), and what a documented method is (Q11). The task looks like 22 questions. It is one habit, tested 22 times.
