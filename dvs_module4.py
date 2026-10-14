"""Original English explanations and guided tasks for DVS Presentation Tools."""
from copy import deepcopy
from pathlib import Path

CONTENT_REVISION = "2026-10-15-dvs4-media"
COURSE_CODE = "FI1BBDV75"
ROOT = Path(__file__).resolve().parent / "assets" / "dvs"
DATA_ROOT = ROOT / "datasets"
BOOK = "https://learning.noroff.no/mod/book/view.php?id=22907&chapterid="
KAGGLE = "https://www.kaggle.com/datasets/hunter0007/ecommerce-dataset-for-predictive-marketing-2023"
MS_DESIGN = "https://support.microsoft.com/en-us/powerpoint/training/design-in-powerpoint"
MS_TRANSITIONS = "https://support.microsoft.com/en-us/powerpoint/training/add-change-or-remove-transitions-between-slides"
MS_MORPH = "https://support.microsoft.com/en-us/powerpoint/morph-transition-tips-and-tricks"
MS_MODEL = "https://support.microsoft.com/en-us/excel/create-a-data-model-in-excel"
DATASETS = [
    {"file":"Chocolate bar ratings 2022.csv", "source":BOOK+"81662", "rows":2588,
     "sha256":"75d1a2ccb7235cb990f1f10de6d2186902d1ef232c077142923cb3c2d141ca0a"},
    {"file":"sf_clean.csv", "source":BOOK+"81660", "rows":989,
     "sha256":"640e3f83df157fa0d837dc78946f932c560a48c607645c3428657044c2074233"},
]
PRESENTATION_TEMPLATES = {
    "4.2-task":"DVS Task 4.2 Fruit Media Template.pptx",
    "4.3-task":"DVS Task 4.3 Fruit Media Template.pptx",
    "4.4-task":"DVS Task 4.4 Chocolate Media Template.pptx",
}
REVIEW_NOTE = "The brief says Review Transition. Its intended effect is not defined in the chapter, and a matching effect name was not verified. Check your English transition gallery and clarify the intended name with the lecturer if absent; do not silently substitute Reveal. Record this item as unresolved until confirmed."
FRUIT_NOTE = "Task 4.2 spells the lemon's Latin name Citrus lemon. Preserve the supplied exercise wording and distinguish it from independently verified botanical terminology. Annual consumption values are supplied exercise data: lemon 2.5 kg, banana 12 kg, pineapple 3.5 kg. No population, per-person denominator, location or reporting year is supplied."
ILLUSTRATIONS = {n:[{"file":f"lesson-4-{n[-1]}-{stem}.png","title":title,"caption":caption}] for n,stem,title,caption in [
    ("4.1","presentation-routes","Choose a presentation route","A planned slide sequence and canvas navigation organise the same ideas differently. Storytelling can use either approach. The 10–20–30 rule is a guideline, not a compulsory task limit."),
    ("4.2","fruit-slides","Build five fruit slides","Task 4.2 requires five slides: title, lemon, banana, pineapple and consumption. The supplied values are 2.5, 12 and 3.5 kg; no population or year is stated. This illustration is conceptual. Add actual PowerPoint media yourself."),
    ("4.3","transitions-animations","Distinguish transitions and animations","Morph is a transition between slides. Grow & Turn, Float Down and Fade are the required object animations. The timing diagram explains examples of triggers; the brief does not prescribe those trigger settings."),
    ("4.4","reviews-custom-shows","Group reviews and route custom shows","Apply cutoffs to the calculated average Rating of each group: company >3.5, bean origin >3.25, cocoa percentage >=3.0. Review Date stores years. Six slides are an optional structure, with three specified custom shows; no slide count is prescribed.")
]}

LESSON_TEXT = {
"4.1": """
### Lesson 4.1: presentation tools communicate the meaning of analysis

Analysis produces evidence; presentation helps an audience understand its relevance. State the audience's question, what the data can show and the action or understanding the presentation supports. Give enough context to interpret each chart: source, population, period, measure, units and limitations. An attractive slide does not repair incorrect analysis.

#### 1. Understand the two presentation approaches

A traditional slide deck uses a planned sequence. A useful flow is title → agenda → introduction → findings → conclusion → questions → contact/end. Adapt this to the audience and available time rather than adding empty sections. Findings should connect a claim to evidence and an explanation, and recommendations should follow from the findings.

A canvas presentation places related topics in a spatial arrangement and allows navigation or zooming between them. It can help explain how details fit a wider context. It can also disorient viewers if movement is excessive. **Storytelling is not the same as non-linear navigation**: a linear PowerPoint deck can tell a story, and a canvas can follow a planned route. Use evidence, context and a coherent argument in either format.

#### 2. Treat design rules as guidance

The course introduces the **10–20–30 rule**: no more than ten slides, up to twenty minutes and a minimum 30-point font. Treat this as a presentation heuristic, not a universal rule or a replacement for a task's explicit requirements. Task 4.2 requires exactly five slides. Font readability also depends on the room, display, contrast and content. Place supporting detail in speaker notes rather than filling slides with paragraphs.

#### 3. Compare tools using a shared question

Task 4.1 asks for at least four tools, including **PowerPoint and Prezi**. PowerPoint, Prezi, Keynote and Google Slides are an appropriate research set. For each, write a brief description covering history if available, vendor, and documented use in particular domains. Then create a table comparing meaningful features. Do not assert that one sector uses a tool most widely without evidence.

| Tool | Verified historical starting point | Vendor | Presentation approach to investigate |
|---|---|---|---|
| PowerPoint | Forethought released it in 1987; Microsoft acquired Forethought in July 1987 | Microsoft | Slide sequence, multimedia and presenter workflow |
| Prezi | Founded in 2009 | Prezi | Zoomable canvas and spatial navigation |
| Keynote | Apple announced it on 7 January 2003 | Apple | Slide design, media and Apple-device workflow |
| Google Slides | Google's presentation feature launched in September 2007 | Google | Browser-based shared presentation editing |

Research links: [Microsoft history](https://learn.microsoft.com/en-us/shows/history/history-of-microsoft-1987), [PowerPoint anniversary](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/happy-35th-anniversary-powerpoint/4214230), [Prezi company history](https://prezi.com/blog/prezis-journey-to-becoming-a-virtual-first-organization/), [Apple's Keynote launch](https://www.apple.com/newsroom/2003/01/07Apple-Unveils-Keynote/), [Google's presentation launch](https://cloud.googleblog.com/2007/09/we-are-pleased-to-present.html). Product capabilities and licence terms change: date your checks and cite the exact vendor edition/page, rather than copying old pricing or market-share claims.

#### 4. Understand PowerPoint's working areas

Use **Home** for slides, layouts and text; **Insert** for images, tables, charts and other media; **Design** for themes and variants; **Transitions** for movement between slides; **Animations** for objects within a slide; **Slide Show** for delivery and custom shows; **Review** for comments, spelling and accessibility; **View** for working views, notes and Slide Master. File operations include save, export and sharing. Tab names and available features depend on platform, version and licence; do not expect a fixed eleven-tab ribbon on every device.

**Exam pattern:** audience need → tool feature → benefit → limitation → evidence. For example, a shared editing feature may help a distributed team maintain one deck, while access, offline needs and export behaviour still need checking. A recommendation is optional; Task 4.1 chiefly asks for descriptions and a comparison table.
""",
"4.2": """
### Lesson 4.2: build slides with text, media, tables and charts

The lesson's practice deck is **Farm animals**. It demonstrates a title slide, three animal slides and an inventory slide. **Task 4.2 uses tropical fruits instead**. Keep the two briefs separate. Start with a blank presentation, add the title, then use Home → New Slide and Layout to select suitable placeholders. Duplicate a consistent content slide, then replace every copied heading, fact and media object.

#### 1. Organise and format content

The Home tab supports text size, alignment, bullets, Format Painter, shapes and slide organisation. A **layout** arranges placeholders on a slide; a **theme** defines coordinated fonts, colours and effects. Reset concerns layout/placeholder formatting; do not assume it undoes every custom change to every object. Check the slide after resetting or changing layouts.

#### 2. Insert and arrange media deliberately

Use Insert → Pictures for a photograph, Icons for a scalable illustration and 3D Models for a genuine model. A PNG drawing of a lemon is not a 3D model. The continuation task establishes these media roles: **lemon 3D model, banana photograph and pineapple icon**. Add appropriate media now so Task 4.3 can modify the intended object types. The stock catalogue varies; record unavailable assets rather than claiming a substitute fulfils an exact media requirement.

Objects have a stacking order. Send Backward moves an object one layer; Send to Back places it behind other objects. Put the title background behind text. Crop without distorting proportions, and make the background semi-transparent so the title remains legible. The source does not prescribe a transparency percentage for the fruit task. In the farm demonstration it uses 50%, which is an example. Review contrast on the actual picture; transparency alone does not guarantee legibility.

Tables communicate precise values. A chart helps compare them. PowerPoint charts have underlying editable data: replace all default categories and dummy series, check the selected range, and compare every chart value with the table. In Excel-style data editors, enter labels like '5-10 as text when automatic conversion would change the label; it is not universally treated as a formula.

#### 3. Build the five Task 4.2 slides

| Slide | Required content |
|---|---|
| 1 | Title and a semi-transparent background picture |
| 2 | Lemon: supplied Latin name Citrus lemon; size 5–8 cm; weight up to 60 g |
| 3 | Banana: Musa; length 15 cm; weight approximately 120 g |
| 4 | Pineapple: Ananas comosus; size approximately 30 cm; weight 900–1,100 g |
| 5 | Annual consumption table and bar chart: lemon 2.5 kg; banana 12 kg; pineapple 3.5 kg |

These are **supplied exercise values**, not independently established consumption statistics. No country, year, population or per-person denominator is given. Keep the kg unit and explain the scope limitation; do not add a year or per-capita label. Preserve the task's botanical wording while distinguishing it from independently researched nomenclature.

Use a zero baseline for the bar chart. A horizontal bar chart is a simple option. Keep fruit labels and numeric values readable. The lesson's farm example uses clustered columns, but the task explicitly asks for a bar chart. Do not confuse this example with the required fruit data.

#### 4. Save for the next task

Save the editable presentation and reopen it. Check all five slides, readability, media types, chart values and table agreement. Keep a copy before Task 4.3 so later formatting changes do not overwrite your only earlier version. The downloaded media template includes fruit images, a title background and an editable consumption table/bar chart. The lemon is a static illustration, not a native 3D model, and the pineapple is a raster icon picture. Add a genuine 3D lemon, set native title-background transparency and finish the required effects in PowerPoint. Generated media are educational illustrations, not sourced photographs of actual specimens.
""",
"4.3": """
### Lesson 4.3: design and rehearse the existing presentation

Continue from **your fruit deck from Task 4.2**, not the lesson's farm example. A consistent theme coordinates colours, fonts and effects. Applying a theme may change placeholder appearance or expose visual issues, so inspect all slides. It does not universally reverse every image flip; the source's farm demonstration describes what happened in that example.

#### 1. Apply the required theme and title colour

Select the slides and use Design → Themes → **Facet**. Change the title font to the theme colour named **Dark Green, Accent 2, Darker 50%**. This is a named theme swatch, not an arbitrary green RGB value; check the displayed name and review titles after changing the theme. The supplied scaffold has a neutral study layout. Apply Facet in PowerPoint before completing the task.

#### 2. Clean up the media

Select the **banana photograph** and use Picture Format → Remove Background. Inspect the automatic mask, mark areas to keep/remove and retain the complete banana before Keep Changes. Review the edges at a useful zoom and against the final background. Select the **pineapple icon** and resize proportionally so its apparent size is approximately the lemon's. Avoid stretching; visual size depends on the visible fruit, not just the object's bounding box.

#### 3. Distinguish transitions from object animations

| Feature | Acts on | Task 4.3 requirement |
|---|---|---|
| Transition | Arrival of a slide from the previous slide | Morph on all slides |
| Animation | An object within a slide | Grow & Turn on lemon 3D model; Float Down on banana photo; Fade on pineapple icon |

Use Transitions → Morph → Apply To All. Morph's motion depends on related objects across slides; applying the effect alone does not promise a particular movement. Microsoft documents that charts cross-fade rather than geometrically morph. [Morph guidance](https://support.microsoft.com/en-us/powerpoint/morph-transition-tips-and-tricks).

Select each required object, then choose its named animation. For Float Down, inspect the appropriate Float effect and direction option in your edition and confirm its displayed effect name. Preview the actual result rather than assuming an approximate effect is equivalent. Animations, 3D model support and catalogue names can vary across versions and devices.

#### 4. Understand the Animation Pane

**On Click** waits for the presenter's input; **With Previous** starts with the previous effect; **After Previous** starts after the previous effect ends. Duration controls playback length; delay postpones the start after its trigger. Add Animation preserves an existing effect when adding another, whereas choosing an effect in a gallery may replace it. Use the Animation Pane to check the selected object, order and timing. The fruit task does not prescribe specific trigger settings or additional effects.

#### 5. Use notes and delivery settings

Speaker notes explain content without filling the slide. Presenter View separates notes and controls from the audience's slide display when the setup supports it. Rehearse on the actual display arrangement; verify that notes appear on your screen and slides on the audience screen. Start from the beginning or current slide using Slide Show commands; keyboard shortcuts depend on platform and keyboard setup. Custom shows select a subset/order for a particular audience; hiding a slide or defining a custom show does not delete it from the deck.

**Task 4.3 final check:** Facet throughout; exact named title colour; banana background removed; pineapple resized; Morph throughout; all three required object animations; saved and reopened deck. Rehearsal and notes are useful lesson practice, not extra prescribed submission requirements. The media template includes a banana cutout and the fruit chart. Native themes, title-background transparency and animations still need to be applied and verified; the static lemon illustration must be replaced with a real 3D model.
""",
"4.4": """
### Lesson 4.4: move from a dataset to a presentation for a defined audience

The lesson's **e-commerce demonstration**, the **San Francisco self-study** and the **chocolate Task 4.4** use three separate datasets. Keep their fields, measures and findings separate. The common workflow is source → import and inspect → define measures → summarise → visualise → explain → rehearse.

#### 1. Follow the e-commerce demonstration without losing rows

The lesson links to a [Kaggle e-commerce dataset](https://www.kaggle.com/datasets/hunter0007/ecommerce-dataset-for-predictive-marketing-2023) and describes 2,019,501 rows. Check the actual downloaded version, licence, schema and row count. This external dataset is linked, not included in the app's source downloads. The lesson's claimed count is not a newly verified local import.

Excel worksheets have a 1,048,576-row limit, including any header row. A partially loaded table is not the whole dataset. The course demonstrates a **Data Model** and PivotTables from that full query. Use a supported edition/workflow and verify row coverage. If the full model workflow is unavailable on your platform, aggregate through a supported query/tool or use a supported environment and disclose the change; never silently label a truncated table as complete. Task 4.4's small chocolate CSV does not need this large-data workaround. [Microsoft Data Model guidance](https://support.microsoft.com/en-us/excel/create-a-data-model-in-excel).

The demonstration uses order_id, user_id, order_number, day/hour fields, product_id, department and other fields. Some header spellings in the prose differ: inspect the actual CSV rather than coding from a guessed spelling. One row is a product line, so **Count of product_id** counts nonblank lines, **Distinct Count of order_id** counts orders, and **Sum of order_id** has no useful order-count meaning. Product-line counts are not monetary revenue or necessarily unit quantities.

Create time_of_day from valid integer hours: Night 0–5; Morning 6–11; Afternoon 12–17; Evening 18–23. Reject/flag null or invalid hours rather than classifying them as Evening. Preserve this chronological order in summaries.

The course's department_manager mapping is:

| Manager | Departments |
|---|---|
| Stephen Smith | alcohol; bakery; breakfast; dairy eggs; pantry |
| Carl Whiley | meat seafood; missing; other; personal care; pets; snacks |
| John Snow | babies; bulk; frozen; household; international |
| Marty White | beverages; canned goods; deli; dry goods pasta; produce |

Match the actual category spelling, including punctuation, and flag unmatched categories. This is a supplied exercise mapping, not an inferred real organisation. The source demonstration gives **200,000 orders** in its PivotTable chapter but **2,000 orders** in its presentation chapter. It also varies the order of the second/third departments. Resolve these using your actual complete data and calculated summaries, not by copying the inconsistent prose.

#### 2. Present charts with their meaning intact

The demonstration creates category-count columns, a time-of-day line and a manager-share pie chart. Check the measure and whether counts are additive or distinct before comparing or summing categories. An order spanning departments can contribute to more than one department's distinct-order count. Use one coherent order-level classification for the time chart.

Use a title, key findings and chart slides with concise comments. Pasting an editable chart, embedding a workbook, linking to a file and pasting a picture have different consequences. Editable objects allow changes; links require a reachable source; pictures are static and must retain their aspect ratio. Check both editability and data disclosure when choosing a paste option. Remove redundant chart furniture only while preserving category/series meaning. Rehearse the custom show for each audience.

#### 3. Prepare the five Task 4.4 analyses

The included original chocolate CSV has **2,588 review rows**. Inspect numeric Rating, Company (Manufacturer), Country of Bean Origin, Cocoa Percent and Review Date. REF is not demonstrated to be a unique review identifier. Keep original values intact. Review Date contains **years**, not full calendar dates, so the guide interprets the task's phrase average rating based on review data as average Rating by Review Date/year. State this interpretation; clarify it if the lecturer intended another grouping.

| Required analysis | Rows/groups | Values | Filter after grouping |
|---|---|---|---|
| Company ratings | Company (Manufacturer) | Average of Rating | Greater than 3.5 |
| Bean-origin ratings | Country of Bean Origin | Average of Rating | Greater than 3.25 |
| Cocoa-percentage ranking | Cocoa Percent | Average of Rating | Greater than or equal to 3.0; descending average |
| Rating over review years | Review Date | Average of Rating | No stated cutoff; years ascending |
| Reviews per year | Review Date | Count of valid review records | No stated cutoff; years ascending |

Use PivotTable Value Field Settings → **Average** for the first four; count records for the fifth. Apply a **value filter to group averages**, not a row filter to individual ratings. Filtering out low-rated reviews before averaging changes the question and biases the result. Strict > excludes an equal value; >= includes it. Apply cutoffs to underlying averages before display rounding. Convert Cocoa Percent consistently for sorting while retaining its percent meaning; do not accidentally compare 70% with a rating cutoff of 3.0.

Bar charts can show all five required summaries. Put years in chronological order, keep a zero baseline for bars, label Rating versus Number of reviews, and report group sample sizes in comments or working notes. A highest mean based on one review is less stable than a mean based on many reviews. These are dataset reviewer assessments, not proof of universal product quality or population preferences.

#### 4. Create the presentation and three custom shows

Add each of the five charts with a comment grounded in your calculations. Choose **Wisp**, apply **Float In** to all visuals and address the source's **Review Transition** wording. The effect name is not defined in the chapter and was not verified; if absent from your gallery, clarify it with the lecturer instead of silently changing it to Reveal. [Microsoft transitions](https://support.microsoft.com/en-us/powerpoint/training/add-change-or-remove-transitions-between-slides).

A title plus five chart slides gives an optional **six-slide scaffold**; the task does not prescribe a total. Define three custom shows: all slides; title plus best producers, origins and cocoa percentage; only the rating-statistics slides. In the six-slide scaffold these are 1–6, 1–4 and 5–6 respectively. Custom shows reference slides in the same file; they need not be three separate decks. The grouping is a plan: configure and test the native shows in PowerPoint. The downloadable media template uses **nine slides** to keep every qualifying company/cocoa group legible. Its all-slides show order is **1, 2, 7, 8, 3, 4, 9, 5, 6**; best-groups order is **1, 2, 7, 8, 3, 4, 9**; rating statistics are **5, 6**. Charts contain computed literal data with embedded editable workbook snapshots, not live links or PivotTables. Refresh the summaries after a source change; chart labels are rounded after filtering, and per-group review counts are in speaker notes. Write your own finding comments and consider the limits of small samples.

#### 5. Complete the San Francisco self-study separately

Use the included original sf_clean CSV (**989 listings**). hood_district is a district code, not a researched neighbourhood name. Calculate average price by district, average sqft by district, a price-versus-area comparison, and listing count by district. For the relationship, an XY scatter of sqft versus price is a clear option; state that interpretation rather than claiming the source demands a specific scatter type. Count listings with an explicit record counter rather than Distinct Count of price. Investigate missing/nonpositive values before averaging or excluding rows, and disclose your chosen handling.

Use a San Francisco stock picture for the title and the **Ion** theme. Currency, exact listing date and district-name lookup are not provided in this CSV; label the available source units and avoid invented context. Asking prices do not establish completed rental transactions, current market prices, or why homelessness occurs. Verify the four views against the summaries and save/reopen the presentation.
"""
}

def _guide(number, lesson, chapter, title, deliverable, steps, dataset=""):
    return {"course_code":COURSE_CODE,"id":number,"uid":f"dvs-{number}-{chapter}","lesson_number":lesson,
        "title":title,"source_url":BOOK+str(chapter),"method":"presentation workflow","deliverable":deliverable,
        "steps":[s[1] for s in steps],"step_details":steps,
        "caution":"Follow the original brief, distinguish supplied values from researched findings and record actual checks separately from plans. The resolver reviews written evidence; check native PowerPoint and Excel output yourself.",
        "task_dataset":dataset,"template_file":PRESENTATION_TEMPLATES.get(number,"")}

GUIDES = [
_guide("4.1-task","4.1",81638,"Four presentation tools and feature comparison","Brief descriptions of at least four tools including PowerPoint and Prezi, covering history if available, vendor and documented domain use, plus a feature comparison table",[
("1. Define the four-tool research set","Include PowerPoint and Prezi, plus at least two other presentation tools. Keynote and Google Slides are optional examples.","The source sets no page count, font, required price analysis or ranking."),
("2. Research history and vendor","Record each vendor, relevant history and exact primary sources, with the date checked.","Keep original developer and current vendor distinct. Do not invent an unavailable founding date."),
("3. Investigate domain use","Look for documented use in education, business or another relevant field, and state what your source actually supports.","A vendor use case is not evidence of market dominance in that field."),
("4. Write brief descriptions","Write one original paragraph per tool covering the three requested areas, with citations.","Separate sourced facts from your evaluation and avoid copying promotional claims."),
("5. Choose comparison criteria","Use shared criteria such as sequence/canvas navigation, collaboration, media, presenter features, platform and export. Cite capabilities for the actual editions checked.","Product capabilities may change; do not compare unrelated editions without saying so."),
("6. Build the feature table","Put the same criteria in each column and tools in rows. Write specific contrasts and mark unknown items honestly.","A recommendation is optional; descriptions and the comparison table are required."),
("7. Review coverage and sources","Check four or more tools, PowerPoint and Prezi included, history where available, vendor, domain-use reasoning and a comparison table.","Do not present this research plan as completed feature testing.")]),
_guide("4.2-task","4.2",81645,"Five-slide tropical fruit presentation","Five slides with a semi-transparent title background, three fruit descriptions, and a consumption table and bar chart; save for Task 4.3",[
("1. Plan exactly five slides","Create title, Lemon, Banana, Pineapple and annual-consumption slides. Save an editable working deck.","The farm-animal deck is a lesson example, not this task."),
("2. Make the title background readable","Insert a suitable background picture, put it behind the title and make it semi-transparent. Review actual contrast.","No exact transparency percentage is prescribed for the task."),
("3. Add the lemon slide","Use supplied Citrus lemon, size 5–8 cm and weight up to 60 g. Insert a real lemon 3D model to support Task 4.3.","A generated lemon picture is not a native 3D model. "+FRUIT_NOTE),
("4. Add banana and pineapple","Banana: Musa, 15 cm, approximately 120 g, photograph. Pineapple: Ananas comosus, approximately 30 cm, 900–1,100 g, icon.","Use the specified media types established by the continuation task and preserve units."),
("5. Create the consumption table","Add fruit labels and supplied numeric kg values: Lemon 2.5, Banana 12, Pineapple 3.5.","No year, population or per-person denominator is supplied."),
("6. Create and check the bar chart","Insert a bar chart, replace dummy data, use the same three values and a zero baseline, and label the kg unit.","Compare the table and chart; do not leave additional default series."),
("7. Save and reopen for Task 4.3","Verify exactly five slides, background transparency, all supplied facts, media, table and bar chart. Reopen and retain an earlier-version copy.","The media template supplies images and a chart; replace the static lemon with a real 3D model and set native background transparency in PowerPoint.")]),
_guide("4.3-task","4.3",81652,"Fruit theme, media and motion","Continue Task 4.2: Facet, named title colour, banana background removal, pineapple sizing, Morph on all slides and three specified object animations",[
("1. Open your Task 4.2 fruit deck","Make a working copy of the five-slide presentation, retaining the earlier version.","Do not switch to the farm example or a completed official solution."),
("2. Apply Facet and the named title colour","Apply Facet throughout, then set title text to Dark Green, Accent 2, Darker 50%.","Choose the named theme swatch. The scaffold's neutral styling does not fulfil this requirement."),
("3. Remove the banana background","Select the banana photo, use Remove Background and refine areas to keep/remove. Inspect edges and preserve the fruit.","Actual picture editing is required; written notes alone do not verify the mask."),
("4. Resize the pineapple icon","Resize proportionally so the visible pineapple is approximately as large as the lemon.","Compare visible objects rather than assuming equal bounding boxes mean equal apparent sizes."),
("5. Apply Morph to all slides","Choose Morph in Transitions, Apply To All and preview the slide changes.","A transition affects slide arrival; it is different from an object animation."),
("6. Apply the three object animations","Lemon 3D model: Grow & Turn. Banana photo: Float Down. Pineapple icon: Fade. Inspect object, effect and direction in the Animation Pane.","No exact trigger or duration is specified. Verify edition support; do not silently substitute effects."),
("7. Rehearse, save and reopen","Verify all required effects and design settings in Slide Show, save and reopen. Record checks actually completed.","Speaker notes and rehearsal settings are useful lesson practice, not extra prescribed task items.")]),
_guide("4.4-task","4.4",81662,"Chocolate review analysis and three custom shows","Five required rating/count charts with comments, Wisp, Review Transition wording, Float In on visuals, and three custom shows",[
("1. Import and inspect the original chocolate CSV","Use the original 2,588-row file. Check Company (Manufacturer), Country of Bean Origin, Cocoa Percent, Rating and Review Date types; preserve the source.","Review Date stores years. Do not confuse bean origin with Company Location or REF with a unique review ID."),
("2. Average and filter company and origin groups","Calculate Average of Rating by company and keep group means >3.5. Calculate Average of Rating by bean origin and keep group means >3.25.","Value-filter the group averages. Filtering individual high-rating rows first changes the result."),
("3. Rank cocoa percentages and summarise years","Average Rating by Cocoa Percent, retain means >=3.0 and rank descending. Average Rating by Review Date/year; separately count review records per year.","The cocoa cutoff applies to average Rating, not Cocoa Percent. Apply cutoffs before rounding; record the review-year interpretation."),
("4. Create five labelled charts and evidence comments","Use bar charts for the five required summaries, label rating/count distinctly, order years chronologically and verify values against summaries.","Discuss group review counts and scope limitations. Do not invent conclusions or infer causation from rankings."),
("5. Build the Wisp presentation and effects","Insert charts and comments, apply Wisp and Float In on every visual. Address Review Transition as stated in the brief.",REVIEW_NOTE),
("6. Define the three custom shows","All slides; title plus best companies, bean origins and cocoa percentages; only rating-statistics slides. For the nine-slide media template use all: 1,2,7,8,3,4,9,5,6; best: 1,2,7,8,3,4,9; statistics: 5,6. The six-slide conceptual illustration instead shows 1–6, 1–4 and 5–6.","These are subsets in the same deck, not necessarily three separate files. Six slides is a scaffold choice, not a prescribed count."),
("7. Verify the analyses and real slide shows","Check average versus count, strict/inclusive cutoffs, source columns, all five charts/comments, Wisp, resolved transition name, Float In and all custom shows. Save/reopen and run each show.","The media template contains calculated charts and review counts in speaker notes. Add your own interpretations; native Wisp, Float In, resolved transition and custom shows still need configuring.")],"Chocolate bar ratings 2022.csv"),
_guide("4.4.1","4.4",81660,"San Francisco rental listings self-study","Four required rental views in a presentation with a San Francisco stock title picture and Ion theme",[
("1. Import and inspect the rental CSV","Use the original 989 listings. Inspect price, sqft and hood_district; record missing and invalid values and any exclusions.","Districts are codes. No currency, current market period or verified neighbourhood-name mapping is supplied."),
("2. Summarise price and area by district","Create separate Average of price and Average of sqft summaries by hood_district, with counts supporting each mean.","Do not silently treat missing area as zero or average district codes."),
("3. Compare price and apartment area","An XY scatter with sqft on X and price on Y is a clear interpretation of the relationship request. Label axes and units and inspect unusual points.","The source does not prescribe this chart type. Asking price and area do not prove causation."),
("4. Count offers by district","Use a record counter to count listing rows by hood_district and verify the total against included listings.","Distinct Count of price is not the number of offers."),
("5. Build and check the Ion presentation","Add a San Francisco stock title picture, Ion theme and all four required views with evidence-based comments. Save, reopen and review readability.","The CSV alone does not demonstrate causes of homelessness or current rental conditions.")],"sf_clean.csv"),
]

def get_template(guide):
    if guide["id"] == "4.1-task":
        return """# Task 4.1 Presentation tool research

Date checked: [...]
Tools: PowerPoint; Prezi; [third]; [fourth]

## Brief description for each tool
Tool and edition: [...]
History, if available: [...]
Original developer / current vendor: [...]
Documented fields or domains of use: [...]
What the evidence supports and does not establish: [...]
Primary sources actually consulted: [...]

## Feature comparison
| Tool / edition | Sequence or canvas | Collaboration | Media | Presenter features | Platforms / export | Source and date |
|---|---|---|---|---|---|---|
| PowerPoint | [...] | [...] | [...] | [...] | [...] | [...] |
| Prezi | [...] | [...] | [...] | [...] | [...] | [...] |
| [Third tool] | [...] | [...] | [...] | [...] | [...] | [...] |
| [Fourth tool] | [...] | [...] | [...] | [...] | [...] | [...] |

## Final check
[At least four tools; PowerPoint and Prezi included; required descriptions; comparison table; sources; remaining work.]
"""
    text=f"# {'Task' if guide['id'].endswith('-task') else 'Activity'} {guide['id'].replace('-task','')} Working notes\n\nRequired output: {guide['deliverable']}\nOriginal source: {guide['source_url']}\n\n"
    text+="\n\n".join(f"## {title}\nRequirement: {instruction}\nCheck: {caution}\nMy action or explanation: [...]\nActual evidence or source: [...]\nRemaining work: [...]" for title,instruction,caution in guide['step_details'])
    return text+"\n\n## Findings and limitations\n[Calculated result; supporting summary; interpretation; limitation.]\n\n## Final check\n[Native checks actually completed; saved output; unresolved requirements.]\n"

def get_task_guide_markdown(guide):
    kind="Task" if guide['id'].endswith('-task') else "Activity"
    text=f"### DVS {kind} {guide['id'].replace('-task','')}: {guide['title']}\n\n**Deliverable:** {guide['deliverable']}\n\n"
    for title,instruction,caution in guide['step_details']:
        text+=f"#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n"
    return text+f"[Original source]({guide['source_url']}).\n\n{guide['caution']}\n\nOriginal study scaffold; official solutions were not opened."

def get_lessons():
    specs=[("4.1",81630,"Presentation Tools"),("4.2",81639,"Crafting Presentations with PowerPoint — Part 1"),
        ("4.3",81646,"Crafting Presentations with PowerPoint — Part 2"),("4.4",81653,"Crafting Presentations with PowerPoint — Part 3")]
    return [{"course_code":COURSE_CODE,"lesson_number":n,"title":title,"module_number":4,"module_title":"Presentation Tools",
        "source_url":BOOK+str(chapter),"source_checked_on":"2026-10-14","content":LESSON_TEXT[n].strip()+f"\n\n[Original lesson]({BOOK}{chapter}).",
        "illustration":None,"dvs_illustrations":deepcopy(ILLUSTRATIONS[n]),
        "key_points":["Match the presentation to audience and evidence","Keep supplied values, computed findings and assumptions distinct","Verify the required native output and actual show behaviour"],
        "visual_elements":{"diagrams":False,"tables":True,"highlighted_sections":True}} for n,chapter,title in specs]

def step_context(guide,base_key,state):
    i=state.get(f"{base_key}_dvs_step_{guide['uid']}",0)
    if not isinstance(i,int) or not 0<=i<len(guide['step_details']):i=0
    title,instruction,caution=guide['step_details'][i]
    return f"Current selected step: {title}\n{instruction}\nCheck: {caution}\n\n"
