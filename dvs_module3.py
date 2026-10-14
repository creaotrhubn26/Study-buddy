"""Original English Module 3 study material and all numbered task/activity guides."""
from copy import deepcopy
from pathlib import Path

CONTENT_REVISION = "2026-10-14-dvs3-ready"
COURSE_CODE = "FI1BBDV75"
ROOT = Path(__file__).resolve().parent / "assets" / "dvs"
DATA_ROOT = ROOT / "datasets"
BOOK = "https://learning.noroff.no/mod/book/view.php?id=22906&chapterid="
MS_CHARTS = "https://support.microsoft.com/en-us/excel/get-started/create-a-chart-from-start-to-finish"
MS_TRENDS = "https://support.microsoft.com/en-us/office/trendline-options-in-office"
MS_HIST = "https://support.microsoft.com/en-us/excel/use-the-analysis-toolpak-to-perform-complex-data-analysis"
ONS_AXES = "https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines"
NIST_BOX = "https://www.itl.nist.gov/div898/handbook/eda/section3/boxplot.htm"

WORKBOOKS = [
    {"file":"C7M3_Data.xlsx", "title":"Lesson chart examples", "source":BOOK+"81610", "sha256":"d6f79e0c3f84eea06119d21b40ae308410691a3ec54c254cae4abc137767e882"},
    {"file":"C7M3LT_Data.xlsx", "title":"Tasks 3.2–3.4 source data L2 L3 L4", "source":BOOK+"81614", "sha256":"38fd26867f8586f8aeda6a143e0b1602bf67c5702bfe9d5477d9b32ece74dba0"},
    {"file":"C7M3L5_Data.xlsx", "title":"Activities 3.4.1 and 3.4.2 source data", "source":BOOK+"81625", "sha256":"d5ba74436d73e712e2c92425970523158c7c33fcc3d9003b860d0a1feca9ba73"},
]

ILLUSTRATIONS = {
"3.1": [{"file":"lesson-3-1-choose-visualisation-v2.png","title":"Choose a visualisation for the question","caption":"Compare categories with bars/columns, show ordered time with lines, inspect distributions with histograms/box plots, relationships with scatter plots and location with maps. Start with audience and data. A visible association does not establish causation."}],
"3.2": [{"file":"lesson-3-2-chart-anatomy-v2.png","title":"Bakery line chart and chart anatomy","caption":"Task 3.2 uses L2 B3:E10 with seven day labels and three product series. Add Bakery sales, primary major vertical gridlines and an outer shadow on the chart area. The illustration is a conceptual preview, not the plotted source values or an Excel screenshot."}],
"3.3": [{"file":"lesson-3-3-relationship-charts.png","title":"Scatter coordinates and an exponential trendline","caption":"Task 3.3 uses X = L3 C3:C15 employees and Y = D3:D15 revenue. Set X minimum 150 and Y minimum 20000 and add the required titles and exponential trendline. The poster geometry is illustrative; use the actual workbook values. Pie charts show composition; bubble charts add a size variable."}],
"3.4": [{"file":"lesson-3-4-bins-combo-pivot.png","title":"Bins combo charts and PivotCharts","caption":"Task 3.4 uses the supplied upper bin bounds and a ToolPak frequency chart with 0% gap width. Combo charts need clearly named measures and axes. PivotCharts summarise and filter grouped data. Unequal bin widths need care when interpreting area."}],
}

LESSON_TEXT = {
"3.1": """
### Lesson 3.1: choose a visualisation deliberately

Data visualisation represents data through positions, lengths, shapes, colour and supporting text. It helps people notice comparisons, patterns, unusual observations and uncertainty. Its value depends on the question, the audience and the data quality. A beautiful chart cannot repair a misleading dataset. Avoid repeating the lesson's unverified claim that images are processed “60,000 times faster” as an established fact.

#### 1. Define the question and audience

Ask what the reader needs to compare, understand or decide. Distinguish exploratory graphics, which help you investigate, from explanatory graphics, which communicate a supported finding. Record the intended audience, available time, technical familiarity and medium. A dashboard for recurring monitoring and a static report for one decision serve different needs.

#### 2. Identify and shape the data

Record what one row represents, the variables, units, time period, population and source. Check missing values, duplicates, impossible values and inconsistent category labels. Investigate unusual observations before removing them. Choose the relevant subset transparently and explain exclusions. Aggregate only when the aggregation answers the question: a total, average and rate communicate different things. Check denominators when comparing percentages or rates.

Keep original values separate from cleaned or summarised values. Numerical variables can be discrete counts or continuous measurements; categorical variables can be nominal or ordered. Categorical and discrete are not synonyms. A summary can lose detail, so decide whether that loss matters.

#### 3. Count the variables and choose the analysis

| Scope | Example | Suitable view |
|---|---|---|
| Univariate | Distribution of item prices | Histogram, density plot or box plot |
| Bivariate | Employees and revenue | XY scatter plot |
| Bivariate | Product category and sales amount | Bar or column chart |
| Multivariate | Employees, revenue and customers | Bubble chart or a scatter plot with another encoding |
| Multivariate | Pairwise relationships across several numeric variables | Correlation matrix |

Cluster analysis, PCA and regression are analytical methods. A visualisation can display their results; naming the method alone does not choose a chart.

#### 4. Recognise the presentation forms

A **chart** encodes data visually. A **dashboard** combines related metrics, charts and controls for a defined monitoring question; it need not be interactive or real time. **Graph** is a broad term: a network graph uses nodes and edges for entities and links, whereas an XY plot uses numerical coordinates. An **infographic** combines visuals and text to explain a topic and still needs trustworthy evidence. A **map** is useful when location or spatial structure matters; it is not automatically the clearest way to rank categories.

On a map, distinguish counts from population-adjusted rates and consider what an area or point represents. A hotspot shows a spatial pattern, not its cause. Provide scale, legend, dates and meaningful annotations.

#### 5. Read the common plot families

| Plot | What to read | Main limitation to check |
|---|---|---|
| Box and whisker | Median, Q1, Q3 and spread | It hides much of the distribution shape |
| Histogram | Counts in numerical intervals | Bin choice can alter the apparent shape |
| Density plot | A smoothed estimate of a numerical distribution | Bandwidth affects peaks; density is not a count |
| Heatmap | Cell values encoded through a labelled colour scale | Colour can hide small differences and missingness |
| Bar/column | Magnitudes for named categories | Length needs a zero baseline |
| Line | Change across an ordered X variable | Connections imply order; gaps and aspect ratio matter |
| Scatter | Numeric X/Y pairs, direction, form and unusual points | Association does not establish causation |
| Correlation matrix | Pairwise coefficients and their signs | A near-zero linear coefficient can miss nonlinear dependence |

A standard box spans **Q1 to Q3**, with the median inside. **IQR = Q3 − Q1**. A common convention flags points outside Q1 − 1.5×IQR and Q3 + 1.5×IQR; whiskers reach observed values inside the fences. Outliers require investigation, not automatic deletion. Quartiles are percentiles, not percentages of the median. [NIST explanation](https://www.itl.nist.gov/div898/handbook/eda/section3/boxplot.htm).

Histograms use numerical bins; ordinary bars use categories. With equal-width bins, heights can show frequencies; with unequal widths, area-faithful histograms use density. Density plots are affected by smoothing, while histograms are affected by bins, so neither is assumption-free. A right-skewed distribution has a longer right tail; a left-skewed distribution has a longer left tail. Several peaks may suggest groups, but they do not prove the explanation.

A heatmap can show an existing matrix or aggregated values; not every numerical heatmap requires histogram binning. Use ordered rows/columns, a suitable sequential or diverging scale, a visible legend and an equivalent table/text explanation. Distinguish missing cells from zero. A correlation matrix is symmetric for the same variables/method; its diagonal is usually 1 for nonconstant variables, but correlations involving constant variables are undefined.

#### 6. Design and review honestly

Use a meaningful title, readable labels, units, source and scope. Use colour together with labels or symbols. Avoid 3D perspective, selective periods, excessive series and unsupported precision. Bar and area charts need a zero baseline. A line or scatter plot can use a justified cropped axis, with clear bounds and context. Dual axes can create an apparent relationship through arbitrary scaling, so use them cautiously and explain each measure. [ONS axes guidance](https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines).

Ask another person what the chart tells them and compare their interpretation with the source data. Record actual feedback separately from planned checks. Include uncertainty and limitations instead of forcing a stronger story than the evidence supports.

#### 7. Choose a tool and complete the task

The lesson names Matplotlib, Seaborn, Plotnine and Plotly. Matplotlib provides plotting primitives; Seaborn supports statistical visualisation on Matplotlib; Plotnine uses a grammar-of-graphics approach; Plotly supports interactive graphics. Excel is the tool used in the next lessons. Tool choice follows the required output and workflow, not an unsupported popularity ranking.

**Task 3.1:** create a **3–4 page best-practice document** answering why visualisation matters, how to identify/shape data, which pitfalls to avoid and how to select/design an appropriate plot. The focus is the selection process; a catalogue of individual chart types is not required. Finish with a proper conclusion and acknowledge all sources. The template below is an original scaffold, not the official solution.

The twelve numbered activities are separately searchable: examples of visual forms; three additional benefits; three techniques for each analysis scope; three spatial cases; box-plot strengths/limits; histogram shapes; density shapes; a one-page heatmap guide; three additional bar variations; research on “cutting”; three suitable and three unsuitable scatter cases; and a one-page correlation-matrix interpretation.
""",
"3.2": """
### Lesson 3.2: create and customise column, bar and line charts

Start with the question and a clean table. Include the header row so Excel can name series correctly. Check whether rows or columns represent series before adding formatting. **Chart area** includes the whole chart; **plot area** is the region containing the plotted marks. Selecting the wrong element changes the wrong property.

#### 1. Compare categories with columns

In the lesson example workbook, the Column chart sheet contains quarterly country comparisons and monthly data. Select the relevant headers and values and use Insert → Column → Clustered Column. A clustered chart compares series side by side. A stacked chart shows contributions to a total; internal segments are harder to compare because they do not share a baseline. A 100% stacked chart compares proportions rather than absolute totals.

Use Chart Design → Add Chart Element for titles and labels. Name the variable and unit accurately, and keep the numerical baseline at zero when height encodes magnitude. The course's example title is Book sales; its formatting choices are practice examples rather than universal requirements.

#### 2. Use horizontal bars when labels need space

A bar chart puts categories vertically and magnitudes horizontally. Chart Design → Switch Row/Column changes which rows or columns form series and categories; it does not convert horizontal bars into vertical columns. Inspect the resulting names and values. Quick Layout is a starting arrangement, not a guarantee that the chart suits the reader.

#### 3. Show ordered change with lines

A line chart connects values across ordered categories such as days or months. In a multi-series chart, verify that each line corresponds to the intended variable. Markers identify individual observations; trendlines summarise fitted direction. They serve different purposes. A fitted line is not a new observation or proof of a cause.

#### 4. Add purposeful reference elements

Add gridlines sparingly so readers can locate values without clutter. Major vertical gridlines align with the horizontal axis categories or values; horizontal gridlines help read the Y scale. Move the legend only when it improves identification. For an area/stacked-area view, totals and contributions may be relevant, but filled areas invite magnitude comparisons and require careful baselines. Droplines connect a point to an axis; they are not trendlines.

#### 5. Format the correct object

Click the chart, then use Chart Design or Format. The formatting pane should name the object you intended to change. A title effect is different from a chart-area effect. An outer shadow is required by Task 3.2 but should not be treated as a default best practice for every professional chart. Microsoft menus and options may differ across desktop, Mac and web versions.

#### 6. Complete Task 3.2 using the actual task workbook

Open **C7M3LT_Data.xlsx → L2**. Select **B3:E10**: day plus muffins, cakes and biscuits. There are seven day rows and three product series. Insert a line chart and verify that Monday–Sunday are the category labels. Do not use the separate lesson example workbook for this task.

Add the exact title **Bakery sales**, **primary major vertical gridlines**, and an **outer shadow on the chart area**. The task does not specify markers, trendlines, a currency, a page count or a font. Optional refinements must preserve the requested chart and clear comparison.

#### 7. Reconcile and explain

Check a source row against all three lines; for Monday the source values are muffins 20, cakes 12 and biscuits 47. Explain which line represents which series, why the ordered days suit a line chart, and which elements satisfy the brief. Save and reopen the workbook to check the real chart. Exam Resolver reviews written reasoning and supplied data; it cannot certify native Excel styling from your notes alone.
""",
"3.3": """
### Lesson 3.3: distinguish composition from relationships

Pie, scatter and bubble charts answer different questions. Choose the data and series deliberately before editing labels or styling.

#### 1. Use a pie for a meaningful whole

A pie chart shows contributions to one whole. Confirm that the categories are mutually appropriate parts of the same total and that values are nonnegative. Keep the number of slices small and labels readable. A bar chart is often easier when exact category comparison matters. A doughnut chart can contain several rings, but comparing slices across rings can be difficult; it is not automatically clearer.

In the lesson Pie chart sheet, the Warsaw and London satisfaction data provide composition examples. Select both the category names and the corresponding values, then Insert → Pie. For nonadjacent ranges, use the appropriate multiple-selection modifier for your platform or explicitly set the categories and series through Select Data. Data Labels can show values or percentages; explain what the denominator represents. Doughnut Hole Size changes ring thickness, not the data.

#### 2. Use a scatter plot for paired numerical values

An XY scatter plot places each record at its numerical X and Y coordinates. Unlike a category line chart, spacing reflects the actual numeric X values. Choose one X variable and one Y variable for each series, keep matching rows aligned and avoid connecting independent observations simply because they appear in file order.

Read direction, form, strength and unusual observations. Strength concerns how closely points follow a relationship, not how physically close all points are to each other. A lack of an obvious straight-line pattern does not rule out a nonlinear relationship.

#### 3. Separate an index from a measured variable

The course also shows an example with a numeric month index and multiple series. Check Select Data rather than assuming Excel has assigned the intended axes. Changing major units and bounds changes displayed ticks; it does not redefine the observations. A scatter chart with a month index can show two Y series over time, which is different from plotting one measured variable directly against another.

#### 4. Add a third numeric dimension with bubbles

In a bubble chart, X and Y locate the point and a third value controls bubble size. Verify which column supplies each role, label the measures, and consider overlap and perceptual limits. Value From Cells can label points with city names; disable extra Y-value labels if they clutter the explanation. A text label adds identity, not another numeric coordinate.

#### 5. Complete Task 3.3 with L3

Open **C7M3LT_Data.xlsx → L3**. Use **X = C3:C15, Number of employees**, and **Y = D3:D15, Revenue**. Select C2:D15 or explicitly create one XY series. **Year is not the X variable** for this task. There are thirteen pairs; the first is employees 157 and revenue 23894. Use a scatter chart with separate markers.

Set the exact chart title **revenue vs. employees**. Set the vertical axis minimum to **20000** and the horizontal minimum to **150**. Add vertical title **revenue** and horizontal title **number of employees**. The source does not specify a currency, so do not invent one.

#### 6. Add the requested exponential trendline

Select the revenue series and choose Add Chart Element → Trendline → More Trendline Options → Exponential. All supplied revenue values are positive. Excel cannot fit its exponential trendline when the Y data include zero or negative values. The brief asks for the trendline, not a forecast, an equation or an R-squared label. A fitted curve summarises the association; it does not prove that hiring more employees causes revenue to rise. [Microsoft trendline options](https://support.microsoft.com/en-us/office/trendline-options-in-office).

#### 7. Verify the finished chart

Check series ranges, thirteen markers, both bounds, all three titles and the trendline type in Excel. The specified nonzero bounds are suitable for this scatter exercise because coordinates, not bar lengths, encode the data; make the scale clear and retain every point. Record your actual checks and interpretation separately from plans. Save, reopen and review the chart before submission.
""",
"3.4": """
### Lesson 3.4: build bins, combine measures and summarise groups

This lesson adds histograms, combo charts and PivotCharts. It also has two separate self-study activities. Each chart starts with a different data structure and needs its own checks.

#### 1. Understand bins before formatting a histogram

A histogram groups numerical observations into intervals. Bin choice affects the appearance. Excel's native histogram can choose bins automatically or accept a bin width, number of bins, and underflow/overflow settings. Automatic bins do not guarantee equal numbers of observations. Check the interval boundary conventions rather than deciding from the appearance of a screenshot.

The **Analysis ToolPak Histogram** produces a frequency table and an ordinary chart from the supplied upper bin bounds. Its bins include values greater than the previous bound and less than or equal to the current bound; the first bin includes values up to its bound. More contains values above the last bound. This output does not automatically recalculate its counts when the input data change: rerun the analysis after an edit. [Microsoft ToolPak](https://support.microsoft.com/en-us/excel/use-the-analysis-toolpak-to-perform-complex-data-analysis).

#### 2. Complete Task 3.4 with the supplied bins

Open **C7M3LT_Data.xlsx → L4**. Use prices **C4:C19** as Input Range and upper bounds **D4:D7 = 30, 50, 70, 100** as Bin Range. With ranges that exclude their headers, leave Labels unchecked. Use Data → Data Analysis → Histogram and enable Chart Output, choosing a blank output area. Enable the Analysis ToolPak through your platform's add-in controls if Data Analysis is missing.

The supplied sixteen prices give the following control counts:

| ToolPak interval | Frequency |
|---|---:|
| Price ≤ 30 | 5 |
| 30 < Price ≤ 50 | 6 |
| 50 < Price ≤ 70 | 1 |
| 70 < Price ≤ 100 | 4 |
| Price > 100 (More) | 0 |
| Total | 16 |

The value 50 belongs in the ≤50 bin. These are verified controls for the unchanged source data, not evidence that your own Excel chart has been inspected. No currency is supplied.

#### 3. Apply the full formatting checklist

Use **Item prices** for the chart title and **Price** for the horizontal axis title. Select the series and set **Gap Width = 0%**. Delete the chart legend. Under Chart Design, select **Colourful Palette 3** and **Style 6**. Add **Data Callout** labels, then use Format Data Labels to clear **Category Name** and retain the frequency value. Check the labels rather than removing their numeric values.

This ToolPak chart supports the ordinary column-chart controls used by the lesson. Native histogram controls may differ. Palette/style previews and spelling vary by Excel version or theme; use the displayed gallery name and record any unavailable option instead of claiming an exact match.

**Interpretation caveat:** the supplied upper bounds create unequal numerical interval widths. Equal-width frequency columns with zero gaps reproduce the course exercise but are not an area-faithful continuous histogram. For a genuine histogram with unequal-width intervals, density is frequency divided by interval width and area represents frequency. Keep the requested task output and explain this distinction when discussing the theory.

#### 4. Combine chart types only when it helps

A combo chart can put one series in columns and another in a line. If the measures share a unit, a common axis often suffices. If their units or scales differ, a secondary axis may help but can also suggest a relationship through arbitrary scaling. Label both axes and clearly map each series to its axis. A chart alone cannot establish correlation or causation. Keep a zero baseline for columns; avoid copying the lesson's cropped column-axis example as a general best practice.

#### 5. Choose PivotChart fields and aggregation

PivotCharts summarise source records through categories, series, filters and value aggregations. Start from a clean table with named columns; decide whether each value should be Sum, Count or Average. A total of customers and a total of revenue have different units, so a combined display needs clear scales or separate views. Refresh after changing the source. A PivotTable may be created alongside a PivotChart; an existing one is not always necessary to start. Chart options and their preservation on refresh differ from ordinary charts. [Microsoft PivotChart overview](https://support.microsoft.com/en-us/excel/overview-of-pivottables-and-pivotcharts).

#### 6. Keep both self-study activities separate

**Activity 3.4.1:** use **C7M3L5_Data.xlsx** for ABC Company's toy-product comparison. Create a column chart comparing the supplied **revenue** and **income** columns. Title it **Revenue vs income**, add a data table **with no legend keys**, and choose **Style 5**. The source's income values equal sold items × production cost; do not silently rename them profit or recalculate the course data. Record the definition issue when interpreting the measures.

**Activity 3.4.2:** use the same data to make a clustered column/line combo titled **sales vs. price**. Put sold-item counts on the primary axis titled **number of sold items**, and price on the secondary axis titled **price**. Choose **Colorful Palette 4**. Explain the two measures and the limits of a dual-axis comparison.

#### 7. Save and check the real output

For Task 3.4, reconcile the frequency total to sixteen and check every formatting requirement. For both activities, check category labels, source series and their axis assignments. Record the workbook/platform/version and real reopen checks. The walkthrough videos and official solutions are optional review resources; they were not used to claim that a student chart has been completed. Exam Resolver supports written reasoning and supplied data, while native Excel formatting must be checked in Excel.
""",
}

TASK_STEPS = {
"3.1-task": [
("1. Turn the brief into an outline","Plan a 3–4 page best-practice document with four required questions, a proper conclusion and acknowledged sources. Focus on how to select and design a visualisation, not an encyclopaedia of chart types.","The source specifies length and references, but no mandatory font or citation style."),
("2. Explain why visualisation matters","Explain how well-chosen encodings support comparison, pattern detection and communication. Give a concrete applied example and a limitation.","Do not repeat the unsupported 60,000-times claim or assume every reader thinks identically."),
("3. Identify and shape the data","Describe the question, audience, row meaning, variables, units, period, source, cleaning and justified aggregation/subsetting. Preserve original values and document exclusions.","An unusual value requires investigation; it is not automatically an error to delete."),
("4. Explain pitfalls and corrections","Discuss misleading baselines, cherry-picking, missing context, excessive series, 3D distortion, inaccessible colour-only cues and overclaiming causation. Explain a practical correction for each.","Bars encode length and need zero; a justified cropped line or scatter axis is a different case."),
("5. Describe how to select and design","Match the reader's task and data type to the encoding. Explain labels, units, scales, scope, uncertainty and accessibility, then plan a reader check.","The task explicitly permits a process-focused explanation without discussing particular plot types."),
("6. Write the conclusion and acknowledge sources","Synthesize the workflow and its implications, without introducing unsupported new evidence. Add in-text acknowledgement and a consistent reference list.","Cite claims you actually researched; do not list papers you have not consulted as if you read them."),
("7. Review the finished document","Check all four questions, conclusion, references, coherence and the final 3–4 page length in your writing application. Record actual checks and remaining revisions.","The downloadable scaffold contains placeholders; filling it can change pagination. It is not a completed submission.")],
"3.2-task": [
("1. Open L2 and read the headers","Open C7M3LT_Data.xlsx and select L2. Identify day, muffins, cakes and biscuits in B3:E10.","Use the task workbook, not the lesson examples file. No currency is supplied."),
("2. Select the source and create a line chart","Select B3:E10 including headers. Insert a 2-D line chart, keeping the three product columns as separate series.","There should be three product series, not seven day-named series."),
("3. Check category and series assignments","Use Chart Design → Select Data if needed. Categories are B4:B10; values are C4:C10, D4:D10 and E4:E10, with names in row 3.","Keep Monday–Sunday in order. Do not transpose the comparison merely to change the look."),
("4. Add the exact title","Set the chart title to Bakery sales.","Retain the exact title required by the task."),
("5. Add vertical gridlines","Choose Chart Design → Add Chart Element → Gridlines → Primary Major Vertical.","Vertical gridlines are required; horizontal gridlines alone do not satisfy this item."),
("6. Apply an outer chart-area shadow","Select the whole chart area and open Format Chart Area → Effects → Shadow → an Outer preset.","A plot-area or title shadow is not the requested chart-area effect. The exact preset is not specified."),
("7. Reconcile and reopen","Check Monday values 20, 12 and 47 against the three series, all seven day labels, title, gridlines and chart-area shadow. Save and reopen.","Record checks you performed. The task does not require a trendline or additional report.")],
"3.3-task": [
("1. Open L3 and identify X and Y","Use C7M3LT_Data.xlsx L3. X is number of employees in C3:C15; Y is revenue in D3:D15.","Year in column B is not X for the requested relationship."),
("2. Insert one XY scatter series","Select C2:D15 or set one series explicitly, then insert a scatter plot with markers.","There are thirteen paired observations. First point: (157, 23894)."),
("3. Set the title","Change the chart title to revenue vs. employees.","The task gives no currency; do not infer one from the word revenue."),
("4. Set both minimum bounds","In Format Axis, set vertical Minimum to 20000 and horizontal Minimum to 150.","Use the correct axis and retain all observations; these are scatter bounds, not bar baselines."),
("5. Name both axes","Add vertical axis title revenue and horizontal axis title number of employees.","Employees must remain X and revenue Y after formatting."),
("6. Add the exponential trendline","Select the series and choose Exponential under More Trendline Options. The supplied revenue values are positive.","The required curve is exponential, not linear. A fit is neither causal evidence nor an actual future result."),
("7. Check the series and real chart","Verify ranges, thirteen points, title, two minimum bounds, two axis titles and trendline type. Save, reopen and explain the observed association cautiously.","An equation, R-squared and forecasts are optional extensions, not requirements.")],
"3.4-task": [
("1. Read L4 and the supplied bins","Use C7M3LT_Data.xlsx L4. Prices are C4:C19; upper bin bounds D4:D7 are 30, 50, 70 and 100.","There are sixteen prices. The bins are upper limits, not four raw price observations."),
("2. Generate the ToolPak frequency output","Choose Data → Data Analysis → Histogram. Input C4:C19, Bin D4:D7, Labels unchecked and Chart Output checked. Choose an empty output area.","If Data Analysis is missing, enable Analysis ToolPak. Rerun after changing prices; counts are not automatically live."),
("3. Check frequencies and boundaries","Confirm counts 5, 6, 1, 4 and More 0, summing to 16. Price 50 belongs in the ≤50 bin.","Keep the source intact. Unequal numerical bin widths make equal-width frequency columns different from an area-faithful histogram."),
("4. Set titles and remove the legend","Chart title Item prices, horizontal axis title Price; delete the chart legend.","No currency is specified. Removing the legend must not remove numeric labels."),
("5. Make the columns touch","Open Format Data Series and set Gap Width to 0%.","Use the ToolPak output's column-series controls; a native statistical histogram may expose different options."),
("6. Apply colour style and callout settings","Choose Colourful Palette 3 and Style 6. Add Data Callout labels, clear Category Name and retain Value.","Check the gallery names in your version; do not treat an arbitrary similar colour or style as a verified exact match."),
("7. Save and verify all requirements","Reconcile the total and check chart/axis titles, legend removal, 0% gap, palette, style, data callouts and category-name removal. Save and reopen.","Written notes support the actual chart; they do not replace it or prove Excel styling.")],
}

GUIDES=[]
TASK_INFO = {
"3.1-task": (81608,"Best-practice visualisation guidelines","3–4 page document answering all four process questions with a conclusion and acknowledged sources","visualisation best practices",""),
"3.2-task": (81614,"Bakery sales line chart","Line chart using L2, Bakery sales title, primary major vertical gridlines and outer chart-area shadow","Excel line chart","C7M3LT_Data.xlsx"),
"3.3-task": (81620,"Revenue and employees scatter plot","L3 XY scatter, revenue vs. employees title, Y minimum 20000, X minimum 150, both axis titles and exponential trendline","Excel scatter plot","C7M3LT_Data.xlsx"),
"3.4-task": (81627,"Item prices frequency chart","L4 histogram/frequency chart with Item prices and Price titles, 0% gap, no legend, Colourful Palette 3, Style 6 and value-only Data Callout labels","Excel histogram","C7M3LT_Data.xlsx"),
}

def make_guide(number,lesson,chapter,title,deliverable,steps,caution,method="visualisation research",dataset=""):
    return {"course_code":COURSE_CODE,"id":number,"uid":f"dvs-{number}-{chapter}","lesson_number":lesson,
        "title":title,"source_url":BOOK+str(chapter),"method":method,"deliverable":deliverable,
        "steps":[s[1] for s in steps],"step_details":steps,"caution":caution,"task_dataset":dataset,
        "template_file":"DVS Task 3.1 Best Practice Template.docx" if number=="3.1-task" else ""}

for number,(chapter,title,deliverable,method,dataset) in TASK_INFO.items():
    GUIDES.append(make_guide(number,number[:3],chapter,title,deliverable,TASK_STEPS[number],
        "Use the required source and output. Record actual checks separately from plans; the resolver does not operate Excel or certify native chart formatting.",method,dataset))

ACTIVITIES = [
("3.1.1",81588,"Recognise four visualisation forms","Document real examples of charts, graphs, maps and dashboards",[
"Find one referenced example of each of the four forms and record its URL, date and purpose.","Describe its encodings, audience and question, distinguishing a network graph from a numerical plot where relevant.","Compare what each form helps the reader do and a limitation; include the examples or properly acknowledged links."],"Research the actual examples; do not invent inspected pages or reproduce a chart without acknowledgement."),
("3.1.2",81589,"Three additional benefits","Describe at least three benefits beyond those listed in the lesson",[
"List the seven benefits already discussed so you avoid repeating them.","Research three additional examples, such as communicating uncertainty, comparing scenarios consistently and monitoring against explicit thresholds.","For each, explain the benefit, a concrete visualisation example, its conditions and a consulted source."],"The proposed examples are starting points to research, not measured productivity claims."),
("3.1.3",81590,"Techniques for three analysis scopes","Identify three univariate, three bivariate and three multivariate visualisation techniques",[
"For one variable, consider a histogram, density plot and box plot; state the variable and question for each.","For two variables, consider XY scatter, grouped box plots and category-value bars; identify both roles.","For several variables, consider bubbles, scatter with a group encoding and a correlation matrix; identify what each encoding represents and cite your research."],"Three per scope means nine examples. Analytical methods such as PCA are not automatically chart types."),
("3.1.4",81596,"Maps for three spatial cases","Choose suitable map types for traffic density, nightclub/mugging locations and a tracked stolen vehicle",[
"For traffic distribution/density, research a heat/density or appropriately aggregated choropleth map and define the measure.","For nightclub and incident locations, use distinguishable point layers or a spatial density view and explain the question and denominator.","For the tracking example, consider a current-location marker and a timestamped route. Document why each choice suits its case."],"Spatial proximity does not prove that the nightclub caused incidents. Use hypothetical data for the scenario, not invented real tracking evidence."),
("3.1.5",81597,"Box-plot strengths and limitations","Document contextual advantages and disadvantages of box and whisker plots",[
"Explain median, Q1, Q3, IQR and the selected whisker/outlier convention.","Describe useful comparisons of centre and spread and the advantage of compact summaries.","Explain lost distribution detail, hidden multiple modes and sample-size/context limits, with an example and sources."],"Outlier points are not necessarily errors. State the convention rather than claiming every box plot uses the same whiskers."),
("3.1.6",81598,"Histogram shapes","Document histogram shapes and explain what each suggests",[
"Find or create clearly labelled examples of symmetric, right-skewed, left-skewed and multiple-peaked shapes.","Identify tail direction, central concentration and unusual gaps or values using the plotted bins.","Explain how changing bin width/boundaries can change the visible shape and cite the examples."],"A peak pattern suggests possible structure, not its proven cause. Left skew means a longer left tail."),
("3.1.7",81599,"Density-plot shapes","Find examples of distribution/density shapes and explain them",[
"Find labelled density examples with symmetric, skewed and multiple-peaked shapes.","Explain where observations are concentrated and distinguish density height from frequency or probability at a point.","Compare smoothing/bandwidth settings and document interpretation limits and sources."],"The area under a properly normalised density curve is 1; changing bandwidth can create or hide peaks."),
("3.1.8",81600,"Heatmap best practices","One-page heatmap best-practice document",[
"Define the two axes, what each cell represents and the metric encoded by colour.","Choose logical ordering, a suitable labelled sequential/diverging scale and readable labels; distinguish missing values from zero.","Add an accessible table or text interpretation, sources and an example; check the final one-page length."],"Not all numeric heatmaps require binning. Warm/cool colours are a possible palette, not a universal rule."),
("3.1.9",81601,"Three additional bar-chart variations","One-page description of at least three variations beyond those covered",[
"Record the variations already mentioned in the course, then choose three additional ones with referenced examples.","Possible research topics include diverging bars, floating/range bars and lollipop charts; explain how each represents values.","State a suitable use, a limitation and the relevant baseline/encoding for each; keep the final write-up to one page."],"The suggested candidates require your own researched examples; a lollipop is a point-and-stem variation rather than an ordinary filled bar."),
("3.1.10",81602,"Research cutting in line plots","Research and document the term cutting in relation to line plots",[
"Find a reliable definition and record the exact term and source; the Noroff prompt does not supply a definition.","If discussing axis cropping/truncation, explain the displayed range and why a line can use a justified nonzero axis while a bar needs zero.","Show a labelled example and distinguish axis cropping, axis breaks and a gap for missing observations. State which interpretation your source supports."],"Do not claim that an assumed meaning is Noroff's official answer. Ask the tutor if the course uses the term differently."),
("3.1.11",81603,"When to use scatter plots","Three suitable and three unsuitable scatter-plot cases",[
"Give three paired-numeric cases, such as employees/revenue, salary/spending and advertising budget/sales, and identify X and Y.","Give three unsuitable direct uses, such as category labels versus one amount, parts of one total, and a network of named relationships; propose alternatives.","Explain pairing, numerical spacing, overplotting and causal limitations, with supporting research."],"Multiple numeric series against an ordered time index are possible, but that is a different question from one measure versus another."),
("3.1.12",81604,"Interpret a correlation matrix","One-page summary of correlation-matrix interpretation",[
"Explain row/column variables, coefficient sign and magnitude, symmetry and the main diagonal.","Locate a pair's row-column intersection and distinguish linear correlation from causation and nonlinear dependence.","Discuss method, missingness, constant variables and useful annotations, then write a one-page summary with references."],"Near zero does not prove independence; a constant variable's correlation is undefined."),
]
for number,chapter,title,deliverable,instructions,caution in ACTIVITIES:
    steps=[(f"{i}. "+["Identify the requirement","Develop the explanation","Review evidence and output"][i-1],s,caution) for i,s in enumerate(instructions,1)]
    GUIDES.append(make_guide(number,"3.1",chapter,title,deliverable,steps,caution))

for number,title,deliverable,steps in [
("3.4.1","Revenue and income product comparison","Column chart, Revenue vs income title, data table with no legend keys, Style 5",[
("1. Identify source fields","Use C7M3L5_Data.xlsx Sheet1 product names B3:B8, revenue F3:F8 and income G3:G8; include their row-2 headers when setting series.","The supplied income figures equal quantity × production cost. Use the provided label and flag its definition; do not silently rename it profit."),
("2. Create and label the columns","Insert a clustered column comparison with two series and title Revenue vs income.","Category labels are the six supplied products. Both series must retain their correct source values."),
("3. Add the required presentation elements","Choose Add Chart Element → Data Table → No Legend Keys, and set Style 5.","No Legend Keys is a data-table setting; check that the data table still shows values."),
("4. Check and reopen","Verify both series, six products, exact title, data table without keys and Style 5. Save and reopen.","This activity is separate from Task 3.4's price-bin histogram.")]),
("3.4.2","Sold items and price combo comparison","Clustered combo chart, sales vs. price title, two named axes and Colorful Palette 4",[
("1. Identify categories and measures","Use C7M3L5_Data.xlsx Sheet1 product names B3:B8, sold items C3:C8 and price E3:E8, with headers in row 2.","Counts and prices have different meanings and scales; no currency is specified."),
("2. Set the combo and axes","Choose a clustered column/line combo: sold items as columns on the primary axis, price as a line on the secondary axis.","A secondary scale can create visual alignments; it is not evidence of causation or a measured correlation."),
("3. Add exact titles and palette","Chart title sales vs. price, primary axis number of sold items, secondary axis price; choose Colorful Palette 4.","Keep counts and price mapped to their named axes."),
("4. Verify and reopen","Check the six products, source ranges, series types, axis assignments, all three titles and palette. Save and reopen.","The dataset's product sequence is categorical, not a time series.")])]:
    GUIDES.append(make_guide(number,"3.4",81625,title,deliverable,steps,"Follow this independent activity's requirements; record actual Excel checks rather than inferred completion.","Excel chart activity","C7M3L5_Data.xlsx"))

def get_template(guide):
    if guide["id"]=="3.1-task":
        return """# Task 3.1 Best practice guidelines

Purpose and audience: [state the decision and reader]
Final document target: 3–4 pages including a conclusion and acknowledged sources. Check pagination after writing.

## Why visualisation matters
[Explain the benefit, an applied example and a limitation. Cite researched claims.]

## How to identify and shape the data
[Question, row meaning, types, units, period, population, source, cleaning, exclusions and aggregation.]

## Pitfalls to avoid
[For each: misleading feature, consequence, correction and check.]

## How to select and design an appropriate plot
[Reader task, variable roles, encoding, scale, labels, units, uncertainty, accessibility and reader review. Focus on the process.]

## Conclusion
[Synthesize the workflow and its importance; introduce no unsupported new results.]

## References
[Record sources actually consulted, with consistent in-text acknowledgement and reference details.]

## Personal final check
[All four questions covered; conclusion present; sources acknowledged; actual length 3–4 pages; remaining revisions.]
"""
    return (f"# {'Task' if guide['id'].endswith('-task') else 'Activity'} {guide['id'].replace('-task','')} Working notes\n\n"
        f"Required output: {guide['deliverable']}\nOriginal source: {guide['source_url']}\n\n"
        "## My source and setup\n[Actual workbook/sheet/ranges or research sources; software/version; question and audience.]\n\n"
        + "\n\n".join(f"## {title}\nRequirement: {instruction}\nMy action or explanation: [...]\nActual evidence or source: [...]\nRemaining work: [...]" for title,instruction,_ in guide['step_details'])
        + "\n\n## My interpretation and limitations\n[Explain the result in context. Distinguish evidence from assumptions.]\n\n"
          "## Final review\n[Checks actually completed; references; saved output; unresolved items.]\n")

def get_task_guide_markdown(guide):
    kind="Task" if guide['id'].endswith('-task') else "Activity"
    text=f"### DVS {kind} {guide['id'].replace('-task','')}: {guide['title']}\n\n**Deliverable:** {guide['deliverable']}\n\n"
    for title,instruction,caution in guide['step_details']:
        text+=f"#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n"
    text+=f"[Original source]({guide['source_url']}).\n\n{guide['caution']}\n\nOriginal study scaffold; official solutions were not opened."
    return text

def get_lessons():
    specs=[("3.1",81587,"Visualisation Techniques"),("3.2",81609,"Visualising Data in Excel — Part 1"),
           ("3.3",81615,"Visualising Data in Excel — Part 2"),("3.4",81621,"Visualising Data in Excel — Part 3")]
    return [{"course_code":COURSE_CODE,"lesson_number":n,"title":title,"module_number":3,"module_title":"Visualisation Techniques",
        "source_url":BOOK+str(chapter),"source_checked_on":"2026-10-14","content":LESSON_TEXT[n].strip()+f"\n\n[Original lesson]({BOOK}{chapter}).",
        "illustration":None,"dvs_illustrations":deepcopy(ILLUSTRATIONS[n]),"key_points":["Match the question, audience and data to the visualisation","Keep source meaning and required output explicit","Check the real output and acknowledge limitations"],
        "visual_elements":{"diagrams":False,"tables":True,"highlighted_sections":True}} for n,chapter,title in specs]

def step_context(guide,base_key,state):
    i=state.get(f"{base_key}_dvs_step_{guide['uid']}",0)
    if not isinstance(i,int) or not 0<=i<len(guide['step_details']):i=0
    title,instruction,caution=guide['step_details'][i]
    return f"Current selected step: {title}\n{instruction}\nCheck: {caution}\n\n"
