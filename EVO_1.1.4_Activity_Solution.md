# Evaluation of Outcomes — Activity 1.1.4

## Understanding and Identifying Heuristics

**Course:** FI1BBEO10 Evaluation of Outcomes · Module 1, Lesson 1.1

**Objective:** to identify and analyse the application of heuristics — availability, representativeness and anchoring — in real-world decision-making scenarios.

---

## Step 1: Understanding heuristics

Heuristics are mental shortcuts that let people decide and solve problems quickly and efficiently, especially under uncertainty or information overload. The three examined here:

| Heuristic | What it does | The hard question it replaces |
|---|---|---|
| **Availability** | Decides on the most readily available information — the most recent, or whatever left a strong impression | "How common is this?" becomes "What comes to mind?" |
| **Representativeness** | Judges a case by how closely it resembles a known pattern, prototype or stereotype | "How probable is this?" becomes "How much does it look like something I know?" |
| **Anchoring** | Relies heavily on the first piece of information encountered | "What is the right value?" becomes "How far is it from the first number I saw?" |

The right-hand column is worth carrying through the whole activity. Each heuristic substitutes an **easier question** for the one actually being asked. The substituted question is always faster to answer, which is why the shortcut exists, and always answers something slightly different, which is why it misleads.

---

## Step 2: Real-world scenarios

Each heuristic is given **two** examples: one everyday, one from KPI work. The pairing is deliberate, because Step 4 asks how awareness of these shortcuts improves KPI interpretation, and the mechanism is easier to see in the everyday case before it is applied to the business one.

### Availability

**Everyday.** After being stuck on a delayed train once, I start driving to Trondheim instead. The delay was memorable and recent, so it comes to mind whenever I plan the trip. The actual punctuality rate — around nine journeys in ten arriving on time — does not come to mind at all, because nothing about it was memorable.

**In KPI work.** Nordtre's D2C conversion rate falls. The webshop redesign shipped three weeks ago, everyone knows about it, and it becomes the explanation within minutes. Two other things happened in the same window that nobody mentions: the payment provider had an outage, and the Norwegian summer holiday began. Neither is on the dashboard, so neither is available.

### Representativeness

**Everyday.** Choosing a restaurant because it *looks* like a good restaurant — busy at eight, short handwritten menu, no laminated photographs outside. Those features correlate with quality, which is exactly why the shortcut is used. They are not quality itself, and a new place with an empty dining room on its second week fails a test it could not yet pass.

**In KPI work.** A Nordtre B2B enquiry goes quiet for eleven weeks after the quote. Normal B2B deals close in about six, so the pipeline report marks it lost. It was a municipal procurement, where a five- to six-month cycle is ordinary. The case was judged on a familiar case's timescale.

### Anchoring

**Everyday.** A sofa is marked "was 12 000, now 7 900". The 7 900 is evaluated against the 12 000 rather than against what a sofa is worth, and it feels like a good deal even if it is not. The first number did all the work.

**In KPI work.** Nordtre's launch month produced NOK 980 000 in D2C revenue, driven by launch promotion and press coverage. That figure became the internal reference. Every subsequent month at NOK 600 000 was discussed as a shortfall, even though 600 000 is the sustainable, unpromoted run rate and the business is healthy at it.

---

## Step 3: Analysis

For each: how it produces efficient decisions, how it produces error, what the outcomes are, and whether more time and information would have helped.

### Availability

**Where it is efficient.** It is genuinely the right tool under time pressure. In crisis management or a live incident, acting on the most recent signal without waiting for a full analysis is correct, because the cost of delay exceeds the cost of an imperfect diagnosis. The train example is also cheap to get wrong: driving occasionally when the train would have been fine costs very little.

**Where it errs.** It produces **surface-level insights**. Relying only on what is immediately available misses deeper or less apparent trends, and it systematically overestimates rare vivid dangers while underestimating common dull ones.

**Outcomes.** In the everyday case, a small recurring cost in money and time, based on a risk estimate that is simply wrong. In the KPI case, the outcome is worse and less visible: the redesign gets rolled back. Conversion does not recover, because the redesign was not the cause. Now two things are true — the real cause is still running, and a change that may have been an improvement has been discarded. The team also learns a false lesson about redesigns.

**Would more time and information have helped?** In the everyday case, marginally: five minutes checking punctuality statistics would settle it, and the stakes do not justify much more. In the KPI case, decisively. One question — "what else changed in this window?" — costs almost nothing and would have surfaced both the outage and the holiday. This is the difference the lesson's conclusion points at: **the higher the stakes, the less the shortcut is worth.**

### Representativeness

**Where it is efficient.** With a robust history of comparable cases, pattern matching is fast and usually right. Most restaurants that look good are good; most B2B deals really do close in six weeks. A rule that is right eight times out of ten and free is a good rule.

**Where it errs.** **Misclassification of anomalies.** The failure is specifically about the unusual case, because the heuristic works by resemblance and an unusual case does not resemble anything. Worse, it fails silently: the case is filed under a familiar label and stops being examined.

**Outcomes.** The restaurant case costs one mediocre meal, and a good new place loses a customer it never knew it had. The B2B case is more expensive: a live municipal procurement is dropped from the pipeline, follow-up stops, and the deal is lost to a competitor who kept calling. The KPI consequences compound — the pipeline report now understates real pipeline, and the sales-cycle-length KPI is computed on a truncated set, so the "normal six weeks" belief is reinforced by data the belief itself created.

**Would more time and information have helped?** Yes, and cheaply. The useful move is not more analysis but a different default: where a case does not resemble the pattern, set a **review date** rather than a verdict. One question — "what would this look like if it were genuinely different?" — would have prompted someone to note that municipal buyers run longer cycles.

### Anchoring

**Where it is efficient.** It provides a **consistent reference**. Analysis needs a fixed point; without one, every month is evaluated from scratch and comparison becomes impossible. Anchoring is what makes a baseline usable at all.

**Where it errs.** **Over-reliance on the initial value.** If the anchor is flawed, unrepresentative or outdated, it distorts everything downstream — and because it feels like neutral background rather than a claim, nobody re-examines it.

**Outcomes.** The sofa case costs some money. The revenue case causes real damage: months of good performance are reported as failure, which pushes the team toward discounting to close the gap. Discounting cuts gross margin to hit a revenue figure that was never sustainable — a KPI-driven behaviour that harms the goal, which is the guard-KPI failure this lesson describes elsewhere. Morale suffers for a target that was an artefact.

**Would more time and information have helped?** More time would not have. More **information about the anchor** would have, and it fits in one sentence: *"Month one was 40% promotional and is not a baseline."* The problem was never a shortage of data about later months; it was that nobody questioned the reference point. The remedy is to **date the anchor and record what produced it**.

---

## Step 4: Reflection on the impact of heuristics

### Advantages

**Cognitive efficiency.** Heuristics deliver decisions without full analysis, which matters because full analysis is often unavailable and always expensive. A business that analysed every decision completely would decide nothing.

**Functionality under uncertainty.** Complete information is usually not available. Heuristics let people act anyway, and acting on partial information is generally better than not acting.

**A shared reference.** Anchoring in particular makes comparison possible. A baseline everyone recognises, even an imperfect one, allows a conversation that a floating reference does not.

### Drawbacks

**Inaccuracy.** Shortcuts sometimes produce errors and biases. On its own this is tolerable; it is the price of speed.

**Over-reliance.** This is the serious one. A consistent bias does not average out over many decisions — it accumulates in the same direction. An organisation that anchors on every launch month will misjudge every product it ever ships, in the same way, every time.

**Invisibility.** None of these three announce themselves. Each feels like ordinary reasoning from the inside, which is why awareness has to be built into the process rather than relied on as a personal quality.

### How awareness improves KPI interpretation

This is where the activity connects to the course, and each heuristic produces a specific practice:

| Heuristic | Its failure mode in KPI work | The practice that defeats it |
|---|---|---|
| **Availability** | Overreacting to recent trends; blaming the change everyone knows about | Ask what else changed in the window. Compare against normal variation, history, target and benchmark before naming a cause |
| **Representativeness** | Filing an anomaly under a familiar label and ceasing to examine it | Where a case does not fit, set a review date, not a verdict. Treat a flagged outlier as a request for investigation |
| **Anchoring** | Budgeting and targets built on a misleading initial figure | Date the anchor and record the conditions that produced it. Put review dates on thresholds |

The pattern across all three is the same, and it is the most useful thing in this activity: **none of them is defeated by trying harder to be rational.** Each is defeated by an **artefact** — a recorded baseline, a stated review date, a dated anchor with its conditions written next to it.

That reframes what documentation is for. Written definitions, version control and a documented method are not administrative tidiness. They exist because a written record is the only thing a cognitive shortcut cannot quietly rewrite. Awareness alone fades; a dated note does not.

---

## Step 5: Insights

1. **Every heuristic is a substitution.** Availability swaps "how common?" for "what comes to mind?". Representativeness swaps "how probable?" for "how similar?". Anchoring swaps "what is right?" for "how far from the first number?". Naming the substitution is the fastest way to identify which one is running.

2. **The everyday and business versions are the same mechanism at different stakes.** Avoiding a train after one delay and rolling back a redesign after one conversion drop are the same error. Only the cost differs — which is precisely why the conclusion "especially in crucial or high-stakes situations" is a decision rule and not a caveat.

3. **These shortcuts fail most where evaluation matters most.** All three break on the **unusual case**: the anomaly, the new pattern, the unrepresentative baseline. Routine cases are exactly where they work. Since evaluation work is disproportionately about anomalies — why did this move, is this result trustworthy, is this outlier an error — heuristics are least reliable in the situations this course is about.

4. **Beliefs can manufacture their own supporting data.** The B2B case is the sharpest example: classifying slow deals as lost removes them from the dataset, so the computed average sales cycle stays short, which confirms that six weeks is normal. A KPI computed on a filtered set can validate the filter. That is worth watching for anywhere a KPI and a classification rule touch each other.

5. **Awareness is necessary and insufficient.** Knowing about anchoring does not stop the launch month becoming the reference. Writing "40% promotional, not a baseline" next to the figure does.

### Optional: peer discussion

Comparing examples with others is worth doing for a specific reason rather than as a formality. Each of these heuristics is invisible from the inside and comparatively easy to see in someone else's reasoning. A colleague will spot your anchor faster than you will, because they did not see the first number. Building that into a process — a second person deriving a KPI independently, or reviewing a conclusion before it is circulated — is the practical version of the insight, and it is the same **ensembling** logic the course applies to data: several independent views cancel errors that any single view carries.

---

## Your turn: template for your own three examples

The activity asks for **your** scenarios. Fill this in with cases from your own decisions.

| | Everyday example | KPI-work example |
|---|---|---|
| **Availability** | | |
| **Representativeness** | | |
| **Anchoring** | | |

For each, answer:

1. **What made the shortcut attractive?** Time pressure, missing information, or an obvious available answer.
2. **How was it efficient?** State this honestly. If the heuristic had no advantage it would not be used.
3. **What did it get wrong, and how would you know?** Name the evidence that would have contradicted it.
4. **What were the consequences?** Include the ones that only appear later.
5. **Would more time and information have helped?** Sometimes the answer is no, and only a different default would have.
6. **What artefact would prevent a repeat?** A recorded baseline, a review date, a dated anchor. This is the question that turns the analysis into something usable.
