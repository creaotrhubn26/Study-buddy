# Evaluation of Outcomes — Activity 1.1.2

## Understanding and Practising Data Collection for KPIs

**Course:** FI1BBEO10 Evaluation of Outcomes · Module 1, Lesson 1.1
**Companion workbook:** `EVO_1.1.2_KPI_Data_Collection_Nordtre.xlsx` (37 live formulas)
**Organisation:** Nordtre AS, carried over from Activity 1.1.1

**Objective:** to familiarise myself with practical tools and methods for quantitative and qualitative KPI data collection.

---

## Step 1: Exploring tools for quantitative KPIs

Nordtre AS is a 34-person Norwegian sustainable furniture company with three channels: a D2C webshop, retail partnerships, and a B2B contract arm. **Fit-for-size is part of the evaluation, not an afterthought** — choosing a tool is a decision with a cost.

| Category | Platforms explored | What it offers | Fit for Nordtre | Verdict |
|---|---|---|---|---|
| **Web analytics** | Google Analytics 4 | Sessions, unique users, time on page, bounce rate, traffic source, funnel and conversion events; integrates with ad platforms and reports KPIs automatically | Strong. Free at this volume, and D2C is the one area with a genuine traffic question | **Adopt** as the primary traffic source |
| **CRM** | Salesforce, HubSpot | Pipeline value, deal stage, win rate, average deal size, sales cycle length, CAC; built-in analytics and custom dashboards | HubSpot fits the 140-account B2B arm. Salesforce is built for far larger sales organisations | **Adopt HubSpot**, reject Salesforce on scale |
| **HRM** | Workday, SAP SuccessFactors | Turnover rate, average time to hire, training cost per head, headcount history, review cycles, real-time monitoring | Both are sized for thousands of employees. At 34 staff the same KPIs come from payroll plus a leavers register | **Reject on scale** |
| **Financial** | QuickBooks, Sage | Revenue growth rate, net profit margin, cash conversion cycle, cost lines, real-time dashboards | Good in principle, but the Norwegian equivalents (Tripletex, Fiken) handle MVA and SAF-T reporting that QuickBooks does not | **Adopt the local equivalent** |
| **Custom in-house** | Purpose-built script | Anything the standard platforms do not cover, pulling from several systems at once | Needed for CAC, which requires customer counts from the CRM and spend from finance and ad platforms | **Build** a small reconciliation job |

### What the exploration actually revealed

Two of the four named platforms are the wrong size for a 34-person company, and one is the wrong jurisdiction. That is a legitimate finding rather than a failure to complete the step. **"The KPI is available in Workday" is not a reason to buy Workday.**

The more useful conclusion is that the KPI *definition* matters more than the platform. Employee turnover is departures divided by average headcount whether SAP computes it or a spreadsheet does — and the definition is the part that drifts, not the arithmetic.

### Practical exercise — quantitative KPI

**KPI: D2C website conversion rate.** Chosen because Activity 1.1.1 identified it as Nordtre's actual constraint: sessions rose 38% while conversion fell 12%, so orders grew only half as fast as traffic.

**Tools used: Google Analytics 4 for sessions, the order system for orders.** Two sources on purpose.

| Measure | Value | Source |
|---|---:|---|
| Monthly sessions | 21,500 | GA4 |
| Monthly unique users | 14,800 | GA4 |
| Monthly D2C orders | 250 | Order system |
| Monthly orders as GA4 records them | 231 | GA4 purchase events |
| **Conversion rate (order system)** | **1.16%** | 250 ÷ 21,500 × 100 |
| Conversion rate (GA4 events) | 1.07% | 231 ÷ 21,500 × 100 |
| **Discrepancy between sources** | **7.6%** | (250 − 231) ÷ 250 × 100 |

**Why two sources rather than one.** The activity asks you to use a tool to collect the data. Using two independent tools for the same figure is data ensembling in miniature: agreement raises confidence, disagreement locates the problem. GA4 records 7.6% fewer purchases than the order system, which is normal and explained by consent refusals and ad blockers — analytics tracking is client-side and therefore lossy.

Knowing the size of that gap is what makes the GA4 figure usable. Not knowing it is how a KPI quietly understates performance every single month without anything appearing to be wrong.

---

## Step 2: Understanding qualitative KPIs

**Customer satisfaction** delves into the emotional and psychological aspects of customer interaction. It is gauged through surveys (Likert scales, multiple choice, open text), in-depth customer interviews that reveal nuances broader surveys miss, and Net Promoter Score — which appears numeric but whose insight requires qualitative interpretation of *why* a customer scored as they did.

**Employee engagement** is a barometer for the internal health of an organisation. It is gauged through performance reviews (holding both the employee's and management's perspective), employee satisfaction surveys covering work-life balance, career progression and culture, and one-on-one interviews that elicit more candid feedback than formal mechanisms.

### Practical exercise — qualitative KPI

**KPI: Customer satisfaction. Method: Net Promoter Score, plus a mandatory open-text follow-up.**

After each purchase, customers are asked *"How likely are you to recommend Nordtre to a friend or colleague?"* on a 0–10 scale, followed by one open question asking why.

| Field | Value |
|---|---:|
| Surveys sent | 1,200 |
| Responses received | 348 |
| **Response rate** | **29.0%** |

**Full 0–10 distribution, kept rather than discarded:**

| Score | 0 | 1 | 2 | 3 | 4 | 5 | **6** | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Responses | 3 | 2 | 4 | 6 | 9 | 18 | **35** | 47 | 57 | 72 | 95 |

| Band | Responses | Share |
|---|---:|---:|
| Promoters (9–10) | 167 | 48.0% |
| Passives (7–8) | 104 | 29.9% |
| Detractors (0–6) | 77 | 22.1% |
| **NPS** = %Promoters − %Detractors | | **+25.9** |
| Mean score (0–10) | | 7.89 |

### What the banding hides — two sensitivity tests

Both are computed from the same distribution, which is why keeping the full 0–10 data matters.

| Scenario | New NPS | Change | What actually happened |
|---|---:|---:|---|
| Every 6 moves to a 7 | +35.9 | **+10.1** | 35 detractors become passives. Not one new promoter |
| Every 0–5 improves to a 6 | +25.9 | **0.0** | 42 unhappy customers become much less unhappy. The score does not move |

Note the 35 respondents sitting at exactly 6 — one point from being classified as passive. A nine- or ten-point NPS swing can rest entirely on a handful of customers crossing that single boundary.

**This is why the course text says NPS insight requires qualitative interpretation.** The score gives direction only. The open-text follow-up is where the reason lives, and the reason is the part Nordtre can act on.

### Explored alongside: an employee engagement instrument

Not adopted as this activity's qualitative KPI, but designed because Nordtre's turnover finding in Activity 1.1.1 makes engagement the natural early warning.

Eight statements answered Strongly Disagree to Strongly Agree, 27 of 34 staff responding (79%). Responses to statement 2, *"I have a clear path to develop in this company"*:

| Response | Strongly Disagree | Disagree | Neutral | Agree | Strongly Agree |
|---|---:|---:|---:|---:|---:|
| Count | 6 | 9 | 5 | 5 | 2 |

| Summary | Value | How it reads to a manager |
|---|---:|---|
| Mean score | 2.56 / 5 | "2.6 out of 5" — mildly disappointing |
| Bottom-two-box | **55.6%** | "56% disagree" — a retention problem |
| Top-two-box | 25.9% | Only a quarter see a path |

Same 27 answers, two very different messages. **A Likert scale is ordinal**, so the mean does arithmetic on ranks and pulls the answer toward the middle; the box shares keep the shape of the distribution.

Statement 2 is about career progression — precisely the contributing factor identified for Nordtre's production turnover in Activity 1.1.1. This instrument would have flagged it *before* the departures happened.

---

## Step 3: Report

### Findings and the experience of using the tools

**Google Analytics 4** was straightforward for traffic and behaviour: sessions, users, sources and funnel events are available immediately, and KPI reporting can be scheduled without engineering work. Its limitation is structural rather than a configuration problem — tracking runs client-side, so ad blockers and refused consent remove real visits. Measuring that gap against the order system turned an unknown into a known 7.6% undercount.

**The CRM platforms** are clearly powerful for sales KPIs, but the experience highlighted that they are only as good as the sales process behind them. Every field is filled in by a person, so a deal stage updated late corrupts any cycle-length KPI while the dashboard continues to look authoritative.

**The HRM platforms** were the clearest case of tool-to-need mismatch. They deliver exactly the employee KPIs described, and they are built for organisations two orders of magnitude larger than Nordtre.

**NPS** was quick to deploy and produced a usable direction within a month. The instructive part was what the calculation throws away: banding 0–10 into three groups discards most of the underlying data, and the two sensitivity tests showed a 10-point swing from one boundary crossing and a zero-point response to a genuine improvement.

**The Likert instrument** produced the sharpest single result of the activity — a mean of 2.6 hiding a 56% disagreement rate on career progression.

### Why quantitative and qualitative KPIs together give a comprehensive view

| | What it told us about Nordtre |
|---|---|
| **Quantitative** | Conversion is 1.16% and falling, so the traffic growth is not converting. It measured the *size* of the problem precisely |
| **Qualitative** | NPS of +26 with open-text comments, and 56% of staff disagreeing that they have a development path. It supplied the *reasons* |

Neither half is sufficient. The conversion rate says how much revenue is being lost but nothing about why customers leave the checkout. The NPS comments explain the why but cannot size it. **The quantitative KPI detects that something changed; the qualitative evidence explains what changed.**

---

## Step 4: Reflection

**On using different tools for different data types.** The most valuable thing this activity taught was not how any single platform works, but that *every collection tool has a characteristic blind spot, and knowing the blind spot is part of knowing the number.* Analytics undercounts because tracking is client-side. CRM data is only as current as the last person who updated a field. HRM systems are accurate but sized for organisations that need them. Financial software is precise and almost entirely backward-looking. A KPI cannot be evaluated without knowing which system produced it and what that system cannot see.

**On what each data type contributes.** Quantitative data shows trends and efficiencies; qualitative feedback uncovers satisfaction and areas for improvement. Working through both for the same organisation made the relationship concrete rather than theoretical: the quantitative KPIs in this activity were all *lagging or constraining* measures of things already happening, while both qualitative instruments were *leading* — NPS leads churn by one to three quarters, and engagement leads regretted turnover by two to four. The qualitative side is where a business gets warning, and the quantitative side is where it gets proof.

**On automation.** Automation delivers the number on time, calculated the same way every period, free of transcription errors. It guarantees nothing about whether the definition still means what you assume. A dashboard fed automatically from a CRM will keep reporting a churn rate long after somebody changed what counts as churn — nothing breaks, no cell shows an error, and the number simply stops meaning what it used to.

**On regular monitoring.** Every finding in this activity came from a comparison rather than a snapshot: two sources against each other, one band against another, the mean against the distribution, this period against last. A KPI measured once is a number; a KPI measured repeatedly is a signal. Regular use of diverse collection tools is what keeps decision-makers informed and able to move early, which is the whole reason leading indicators are worth collecting at all.

---

## Appendix: method choices

| Decision | What I chose | Why | What I rejected |
|---|---|---|---|
| Organisation | Nordtre AS again | The collection design can be checked against KPIs that already exist, and the engagement instrument can target the turnover cause 1.1.1 found | A fresh business — the activities would not connect |
| Quantitative KPI | D2C conversion rate | It is the constraint 1.1.1 identified, so collecting it well is the highest-value measurement available | Sessions (a vanity metric) or revenue (already reliably collected) |
| Quantitative tool | GA4 **and** the order system | Two independent sources quantify GA4's undercount instead of leaving it unknown | GA4 alone — conversion would be understated 7.6% every month |
| Tool fit | Rejected Salesforce, Workday, SAP on scale | Choosing a tool is a decision with a cost, and the definition matters more than the platform | Adopting the named enterprise tools uncritically |
| Qualitative KPI | Customer satisfaction via NPS **plus open text** | The score gives direction, the text gives the reason, and only the reason is actionable | NPS alone — the course text itself says the insight needs qualitative interpretation |
| NPS data retained | Full 0–10 distribution | Banding discards most of the data; keeping it makes both sensitivity tests possible | Storing only the three band counts |
| Engagement summary | Top- and bottom-two-box, mean shown for contrast | Likert is ordinal, so the mean pulls toward the middle and understates the problem | The mean alone — the standard choice, and misleading here |
| Response rate | Reported for both instruments | Self-selection is the standard survey bias, so a score without a response rate cannot be evaluated | Reporting the score only |
