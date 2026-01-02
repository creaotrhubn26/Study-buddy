import streamlit as st
import pandas as pd
from openai import OpenAI
import os
import json

st.set_page_config(
    page_title="Data Analyst Study App",
    page_icon="📊",
    layout="wide"
)

client = OpenAI(
    api_key=os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY"),
    base_url=os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL")
)

# Training modules with structured lessons
training_modules = {
    "Introduction to business intelligence and big data": {
        "course": "Data Analysis Fundamentals",
        "description": "Learn what Business Intelligence (BI) and Big Data mean, and how they help companies make better decisions.",
        "lessons": [
            {
                "title": "What is Business Intelligence?",
                "content": """
**Business Intelligence (BI)** is the process of collecting, analyzing, and presenting business data to help companies make better decisions.

**Key Components of BI:**
- **Data Collection**: Gathering data from various sources (sales, customers, operations)
- **Data Storage**: Storing data in databases or data warehouses
- **Data Analysis**: Using tools to find patterns and insights
- **Reporting**: Creating dashboards and reports to share findings

**Real-World Example:**
A retail store uses BI to analyze which products sell best during different seasons. They discover that winter jackets sell 300% more in November than in July, so they stock up accordingly.
                """,
                "key_points": ["BI helps companies make data-driven decisions", "It involves collecting, analyzing, and presenting data", "Dashboards and reports are key outputs"]
            },
            {
                "title": "What is Big Data?",
                "content": """
**Big Data** refers to extremely large datasets that are too complex for traditional data processing tools.

**The 3 V's of Big Data:**
- **Volume**: Massive amounts of data (terabytes, petabytes)
- **Velocity**: Data is generated very quickly (real-time)
- **Variety**: Different types of data (text, images, videos, sensors)

**Examples of Big Data Sources:**
- Social media posts (millions per minute)
- IoT sensors (temperature, location, movement)
- Online transactions
- Website clickstreams

**Real-World Example:**
Netflix analyzes viewing habits of 200+ million users to recommend shows. This involves processing billions of data points daily.
                """,
                "key_points": ["Big Data = Volume + Velocity + Variety", "Traditional tools cannot handle Big Data", "Companies like Netflix and Amazon rely on Big Data"]
            },
            {
                "title": "BI vs Big Data: Key Differences",
                "content": """
**Business Intelligence** and **Big Data** work together but serve different purposes:

| Aspect | Business Intelligence | Big Data |
|--------|----------------------|----------|
| **Focus** | Analyzing structured data | Processing all data types |
| **Data Size** | Gigabytes to Terabytes | Terabytes to Petabytes |
| **Questions** | "What happened?" | "What might happen?" |
| **Tools** | Tableau, Power BI, Excel | Hadoop, Spark, Python |
| **Users** | Business analysts | Data scientists |

**How They Work Together:**
1. Big Data systems collect and process massive datasets
2. BI tools visualize and report on the processed data
3. Decision-makers use BI dashboards to take action
                """,
                "key_points": ["BI focuses on structured data and reporting", "Big Data handles massive, varied datasets", "They complement each other in modern analytics"]
            }
        ],
        "exercises": [
            {
                "title": "Identify BI Use Cases",
                "type": "scenario",
                "question": "A coffee shop chain wants to know which menu items are most popular at each location. They have sales data from 50 stores over 2 years. Is this a BI or Big Data problem?",
                "answer": "This is a Business Intelligence problem. The data is structured (sales records), moderate in size (2 years × 50 stores), and the goal is to analyze 'what happened' to make business decisions. BI tools like Excel or Tableau would be appropriate.",
                "hint": "Think about the 3 V's - is this data extremely large, fast, or varied?"
            },
            {
                "title": "Big Data Scenario",
                "type": "scenario",
                "question": "A social media company needs to analyze 500 million posts per day, including text, images, and videos, to detect trending topics in real-time. Is this BI or Big Data?",
                "answer": "This is a Big Data problem. It involves massive Volume (500M posts/day), high Velocity (real-time), and Variety (text, images, videos). Big Data tools like Hadoop or Spark would be needed.",
                "hint": "Check all 3 V's: Volume, Velocity, and Variety"
            },
            {
                "title": "Calculate Data Volume",
                "type": "practical",
                "question": "A company stores 1,000 customer transactions per day. Each transaction record is 2 KB. How much data do they generate in one year?",
                "answer": "1,000 transactions × 2 KB × 365 days = 730,000 KB = 730 MB per year. This is manageable with traditional BI tools.",
                "hint": "Multiply daily transactions × size × days in a year"
            }
        ],
        "quiz": [
            {
                "question": "What does BI stand for?",
                "options": ["Big Information", "Business Intelligence", "Binary Integration", "Basic Insights"],
                "correct": 1,
                "explanation": "BI stands for Business Intelligence - the process of analyzing business data to make better decisions."
            },
            {
                "question": "Which is NOT one of the 3 V's of Big Data?",
                "options": ["Volume", "Velocity", "Value", "Variety"],
                "correct": 2,
                "explanation": "The 3 V's are Volume, Velocity, and Variety. Value is sometimes added as a 4th V, but it's not part of the original definition."
            },
            {
                "question": "Which tool is typically used for Business Intelligence?",
                "options": ["Hadoop", "Tableau", "Spark", "TensorFlow"],
                "correct": 1,
                "explanation": "Tableau is a BI visualization tool. Hadoop and Spark are Big Data processing tools, and TensorFlow is for machine learning."
            },
            {
                "question": "A dataset of 10 million social media posts updated every second is an example of:",
                "options": ["Business Intelligence", "Big Data", "Traditional database", "Spreadsheet data"],
                "correct": 1,
                "explanation": "This exhibits Big Data characteristics: high Volume (10M posts), high Velocity (every second), and likely Variety (text, images, etc.)."
            }
        ]
    },
    "Statistical methodologies to extract KPIs": {
        "course": "Statistical Tools",
        "description": "Learn how to use statistics to calculate and analyze Key Performance Indicators (KPIs).",
        "lessons": [
            {
                "title": "What are KPIs?",
                "content": """
**Key Performance Indicators (KPIs)** are measurable values that show how effectively a company is achieving its objectives.

**Characteristics of Good KPIs:**
- **Specific**: Clearly defined
- **Measurable**: Can be quantified
- **Achievable**: Realistic targets
- **Relevant**: Aligned with business goals
- **Time-bound**: Has a deadline

**Common Business KPIs:**
- Revenue growth rate
- Customer acquisition cost
- Employee turnover rate
- Net Promoter Score (NPS)
- Conversion rate
                """,
                "key_points": ["KPIs measure business performance", "Good KPIs are SMART", "Different industries have different KPIs"]
            },
            {
                "title": "Statistical Measures for KPIs",
                "content": """
**Basic Statistical Measures:**

**Mean (Average):**
Sum of all values ÷ Number of values
Example: Sales of 100, 150, 200 → Mean = 150

**Median:**
The middle value when sorted
Example: 100, 150, 200 → Median = 150

**Standard Deviation:**
Measures how spread out values are
Low SD = values close to mean
High SD = values spread out

**Percentage Change:**
((New - Old) / Old) × 100
Example: Sales went from 1000 to 1200
Change = ((1200-1000)/1000) × 100 = 20%
                """,
                "key_points": ["Mean shows the average", "Median is better when there are outliers", "Standard deviation shows variability"]
            },
            {
                "title": "Calculating KPIs in Practice",
                "content": """
**Example: Customer Retention Rate**

Formula: ((Customers at End - New Customers) / Customers at Start) × 100

**Scenario:**
- Start of month: 1000 customers
- New customers acquired: 200
- End of month: 1050 customers

Calculation:
((1050 - 200) / 1000) × 100 = 85%

**Interpretation:**
85% retention rate means 15% of customers left (churned).

**Example: Average Order Value (AOV)**

Formula: Total Revenue / Number of Orders

**Scenario:**
- Monthly revenue: $50,000
- Total orders: 1,000

AOV = $50,000 / 1,000 = $50

This means customers spend $50 on average per order.
                """,
                "key_points": ["KPIs use simple formulas", "Always compare KPIs over time", "Context matters for interpretation"]
            }
        ],
        "exercises": [
            {
                "title": "Calculate Mean Sales",
                "type": "practical",
                "question": "A store had daily sales of: $500, $750, $600, $800, $650. Calculate the mean (average) daily sales.",
                "answer": "Mean = (500 + 750 + 600 + 800 + 650) / 5 = 3300 / 5 = $660. The average daily sales is $660.",
                "hint": "Add all values and divide by the count"
            },
            {
                "title": "Calculate Percentage Change",
                "type": "practical",
                "question": "Website traffic was 10,000 visitors last month and 12,500 this month. What is the percentage change?",
                "answer": "Percentage Change = ((12,500 - 10,000) / 10,000) × 100 = (2,500 / 10,000) × 100 = 25%. Traffic increased by 25%.",
                "hint": "Use the formula: ((New - Old) / Old) × 100"
            },
            {
                "title": "Calculate Customer Retention",
                "type": "practical",
                "question": "A company started with 500 customers, gained 100 new customers, and ended with 480 customers. What is the retention rate?",
                "answer": "Retention Rate = ((480 - 100) / 500) × 100 = (380 / 500) × 100 = 76%. The company retained 76% of its original customers.",
                "hint": "Subtract new customers from ending total, then divide by starting customers"
            }
        ],
        "quiz": [
            {
                "question": "What does KPI stand for?",
                "options": ["Key Performance Index", "Key Performance Indicator", "Knowledge Process Integration", "Key Process Information"],
                "correct": 1,
                "explanation": "KPI stands for Key Performance Indicator - a measurable value that shows business performance."
            },
            {
                "question": "If sales were 100, 200, 300, 400, 500, what is the median?",
                "options": ["300", "280", "350", "250"],
                "correct": 0,
                "explanation": "The median is the middle value when sorted. In 100, 200, 300, 400, 500, the middle value is 300."
            },
            {
                "question": "Revenue went from $80,000 to $100,000. What is the percentage increase?",
                "options": ["20%", "25%", "15%", "30%"],
                "correct": 1,
                "explanation": "((100,000 - 80,000) / 80,000) × 100 = (20,000 / 80,000) × 100 = 25%"
            }
        ]
    },
    "Correlation, regression, ANOVA, histogram and covariance analysis": {
        "course": "Statistical Tools",
        "description": "Learn essential statistical analysis techniques used in data analysis.",
        "lessons": [
            {
                "title": "Understanding Correlation",
                "content": """
**Correlation** measures the relationship between two variables.

**Correlation Coefficient (r):**
- Ranges from -1 to +1
- **+1**: Perfect positive correlation (as X increases, Y increases)
- **0**: No correlation
- **-1**: Perfect negative correlation (as X increases, Y decreases)

**Interpreting Correlation:**
- 0.7 to 1.0: Strong positive
- 0.4 to 0.7: Moderate positive
- 0.0 to 0.4: Weak or no correlation

**Example:**
Ice cream sales and temperature have a positive correlation (r ≈ 0.8).
When temperature rises, ice cream sales rise too.

**Important:** Correlation ≠ Causation!
Just because two things correlate doesn't mean one causes the other.
                """,
                "key_points": ["Correlation ranges from -1 to +1", "Positive correlation = both increase together", "Correlation does not prove causation"]
            },
            {
                "title": "Introduction to Regression",
                "content": """
**Regression** predicts one variable based on another.

**Simple Linear Regression:**
y = mx + b
- y = predicted value
- m = slope (how much y changes for each unit of x)
- x = input value
- b = y-intercept (value of y when x = 0)

**Example:**
Predicting sales based on advertising spend:
Sales = 2.5 × Ad_Spend + 1000

If you spend $500 on ads:
Sales = 2.5 × 500 + 1000 = $2,250

**R-squared (R²):**
- Measures how well the regression fits the data
- Ranges from 0 to 1
- R² = 0.85 means 85% of variation is explained by the model
                """,
                "key_points": ["Regression predicts outcomes", "y = mx + b is the basic formula", "R² shows how good the prediction is"]
            },
            {
                "title": "Histograms and Data Distribution",
                "content": """
**Histogram** is a chart showing how data is distributed across ranges (bins).

**How to Read a Histogram:**
- X-axis: Value ranges (bins)
- Y-axis: Frequency (count)
- Tall bars = many values in that range

**Common Distribution Shapes:**
- **Normal (Bell Curve)**: Most values in the middle
- **Skewed Right**: Tail extends to the right
- **Skewed Left**: Tail extends to the left
- **Bimodal**: Two peaks

**Example:**
Employee salary histogram might show:
- Most employees earn $40,000-$60,000
- Few earn above $100,000
- This is right-skewed (long tail toward high salaries)
                """,
                "key_points": ["Histograms show data distribution", "Normal distribution is bell-shaped", "Skewness shows data is not symmetric"]
            },
            {
                "title": "ANOVA and Covariance Basics",
                "content": """
**ANOVA (Analysis of Variance)**
Compares means across multiple groups to see if differences are significant.

**When to Use ANOVA:**
- Comparing sales across 3+ regions
- Comparing test scores across different teaching methods
- Comparing customer satisfaction across product lines

**Example:**
Testing if coffee brand affects taste ratings:
- Brand A: average rating 4.2
- Brand B: average rating 3.8
- Brand C: average rating 4.5
ANOVA tells you if these differences are statistically significant.

**Covariance**
Measures how two variables change together.
- Positive covariance: both increase/decrease together
- Negative covariance: one increases as other decreases
- Similar to correlation but not standardized
                """,
                "key_points": ["ANOVA compares means across groups", "Use ANOVA for 3+ groups", "Covariance shows joint variability"]
            }
        ],
        "exercises": [
            {
                "title": "Interpret Correlation",
                "type": "scenario",
                "question": "A study finds correlation of r = 0.85 between study hours and exam scores. What does this mean?",
                "answer": "This is a strong positive correlation. Students who study more hours tend to score higher on exams. However, this doesn't prove that studying causes higher scores - there could be other factors.",
                "hint": "0.85 is close to 1, indicating a strong positive relationship"
            },
            {
                "title": "Use Regression Formula",
                "type": "practical",
                "question": "A regression model shows: Revenue = 3 × Marketing_Spend + 5000. If you spend $2000 on marketing, what is the predicted revenue?",
                "answer": "Revenue = 3 × 2000 + 5000 = 6000 + 5000 = $11,000. The predicted revenue is $11,000.",
                "hint": "Substitute the marketing spend value into the formula"
            },
            {
                "title": "Choose the Right Test",
                "type": "scenario",
                "question": "You want to compare customer satisfaction scores across 4 different store locations. Which statistical test should you use?",
                "answer": "Use ANOVA (Analysis of Variance). ANOVA is designed to compare means across 3 or more groups, making it perfect for comparing satisfaction across 4 store locations.",
                "hint": "You're comparing means across multiple groups"
            }
        ],
        "quiz": [
            {
                "question": "A correlation of r = -0.9 means:",
                "options": ["Strong positive relationship", "No relationship", "Strong negative relationship", "Weak relationship"],
                "correct": 2,
                "explanation": "-0.9 is close to -1, indicating a strong negative relationship. As one variable increases, the other decreases."
            },
            {
                "question": "In y = mx + b, what does 'm' represent?",
                "options": ["Y-intercept", "Slope", "Correlation", "Mean"],
                "correct": 1,
                "explanation": "In the linear equation, m is the slope - it shows how much y changes for each unit increase in x."
            },
            {
                "question": "When should you use ANOVA?",
                "options": ["Comparing 2 groups", "Comparing 3+ groups", "Finding correlation", "Creating histograms"],
                "correct": 1,
                "explanation": "ANOVA is used to compare means across 3 or more groups. For 2 groups, you would use a t-test."
            }
        ]
    },
    "Z-scores and z-testing for outlier reduction": {
        "course": "Statistical Tools",
        "description": "Learn how to identify and handle outliers using z-scores.",
        "lessons": [
            {
                "title": "What is a Z-Score?",
                "content": """
**Z-Score** measures how many standard deviations a value is from the mean.

**Formula:**
Z = (Value - Mean) / Standard Deviation

**Example:**
- Mean height = 170 cm
- Standard Deviation = 10 cm
- Your height = 190 cm

Z = (190 - 170) / 10 = 2

This means you are 2 standard deviations above the mean.

**Interpreting Z-Scores:**
- Z = 0: Value equals the mean
- Z = 1: Value is 1 SD above mean
- Z = -1: Value is 1 SD below mean
- Z > 3 or Z < -3: Likely an outlier
                """,
                "key_points": ["Z-score shows distance from mean in SDs", "Z = 0 means value equals the mean", "High absolute Z-scores indicate outliers"]
            },
            {
                "title": "Identifying Outliers with Z-Scores",
                "content": """
**Outliers** are data points that are significantly different from other values.

**Common Rule:**
- |Z| > 3 = Outlier (99.7% of data falls within ±3 SD)
- |Z| > 2 = Potential outlier (95% of data falls within ±2 SD)

**Example Dataset:** Sales: 100, 120, 110, 115, 105, 500
- Mean = 175
- SD = 150

Z-score for 500:
Z = (500 - 175) / 150 = 2.17

This is a potential outlier!

**Why Remove Outliers?**
- Outliers can skew averages
- They may indicate errors in data
- They can affect statistical models
                """,
                "key_points": ["Z > 3 or Z < -3 typically indicates outliers", "Outliers can distort analysis", "Always investigate why outliers exist"]
            },
            {
                "title": "Practical Outlier Handling",
                "content": """
**Steps to Handle Outliers:**

1. **Calculate Z-scores** for all data points
2. **Identify outliers** (|Z| > 3 or your chosen threshold)
3. **Investigate** why they exist:
   - Data entry error?
   - Measurement error?
   - Genuine unusual value?
4. **Decide action:**
   - Remove if error
   - Keep if genuine (but note it)
   - Transform data (e.g., use median instead of mean)

**Example in Excel/Sheets:**
```
=STANDARDIZE(A2, AVERAGE(A:A), STDEV(A:A))
```
This calculates the Z-score for cell A2.

**Best Practice:**
Always document which outliers were removed and why!
                """,
                "key_points": ["Calculate Z-scores for all values", "Investigate before removing", "Document your decisions"]
            }
        ],
        "exercises": [
            {
                "title": "Calculate Z-Score",
                "type": "practical",
                "question": "Mean = 50, Standard Deviation = 10. Calculate the Z-score for a value of 75.",
                "answer": "Z = (75 - 50) / 10 = 25 / 10 = 2.5. The value is 2.5 standard deviations above the mean.",
                "hint": "Use the formula: Z = (Value - Mean) / SD"
            },
            {
                "title": "Identify the Outlier",
                "type": "practical",
                "question": "Dataset: 20, 22, 21, 19, 23, 20, 85. Mean = 30, SD = 23. Which value is likely an outlier? Calculate its Z-score.",
                "answer": "The value 85 is the outlier. Z = (85 - 30) / 23 = 55 / 23 = 2.39. While not above 3, it's clearly different from the other values which all cluster around 20-23.",
                "hint": "The value that's very different from the others"
            },
            {
                "title": "Decision Making",
                "type": "scenario",
                "question": "Your sales data shows one transaction of $50,000 when average is $500 with SD of $200. Z-score is 247.5. Should you remove this value?",
                "answer": "You should investigate first! This extreme Z-score (247.5) suggests either: 1) Data entry error ($500 became $50,000), 2) A legitimate large order. Check the original records before removing.",
                "hint": "Don't automatically remove - investigate the cause"
            }
        ],
        "quiz": [
            {
                "question": "What does a Z-score of 0 mean?",
                "options": ["Value is missing", "Value equals the mean", "Value is an outlier", "Value is negative"],
                "correct": 1,
                "explanation": "A Z-score of 0 means the value is exactly at the mean (0 standard deviations away)."
            },
            {
                "question": "A value with Z-score of -2.5 is:",
                "options": ["2.5 SDs above the mean", "2.5 SDs below the mean", "Exactly at the mean", "Not calculable"],
                "correct": 1,
                "explanation": "A negative Z-score means the value is below the mean. -2.5 means 2.5 standard deviations below."
            },
            {
                "question": "Which Z-score most likely indicates an outlier?",
                "options": ["Z = 0.5", "Z = 1.2", "Z = 2.0", "Z = 3.5"],
                "correct": 3,
                "explanation": "Z = 3.5 is beyond the ±3 threshold commonly used to identify outliers. Only 0.3% of data falls beyond ±3 SDs."
            }
        ]
    },
    "Tool: Excel & Google Sheets": {
        "course": "Spreadsheet Fundamentals",
        "tool_type": "spreadsheet",
        "description": "Master spreadsheet tools for data analysis - learn formulas, pivot tables, data cleaning, and automation techniques.",
        "lessons": [
            {
                "title": "Essential Formulas for Data Analysis",
                "content": """
**Key Formulas Every Data Analyst Needs:**

**1. VLOOKUP / XLOOKUP (Finding Data)**
```
=VLOOKUP(lookup_value, table_array, col_index, FALSE)
=XLOOKUP(lookup_value, lookup_array, return_array)
```
*Use case:* Match customer IDs to their names across different sheets.

**2. SUMIF / COUNTIF (Conditional Calculations)**
```
=SUMIF(range, criteria, sum_range)
=COUNTIF(range, criteria)
```
*Use case:* Sum all sales for a specific product or count orders from a region.

**3. IF / IFS (Logic)**
```
=IF(condition, value_if_true, value_if_false)
=IFS(condition1, value1, condition2, value2, ...)
```
*Use case:* Categorize sales as "High", "Medium", or "Low" based on amount.

**4. INDEX/MATCH (Advanced Lookup)**
```
=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))
```
*Use case:* More flexible than VLOOKUP - can look left or right in a table.

**Real-World Scenario:**
You have a sales report with 10,000 rows. Your manager wants to know total sales by region. Instead of manually calculating, you use:
```
=SUMIF(B:B, "North", D:D)
```
This instantly sums all sales where region (column B) equals "North".
                """,
                "key_points": ["VLOOKUP finds data across sheets", "SUMIF/COUNTIF calculate with conditions", "INDEX/MATCH is more powerful than VLOOKUP"]
            },
            {
                "title": "Pivot Tables for Quick Analysis",
                "content": """
**Pivot Tables: Your Data Analysis Superpower**

Pivot tables summarize thousands of rows of data in seconds without writing formulas.

**Creating a Pivot Table (Excel):**
1. Select your data (including headers)
2. Insert → Pivot Table
3. Drag fields to Rows, Columns, Values, and Filters

**Example Scenario:**
You have a dataset of 50,000 sales transactions with columns:
- Date, Product, Region, Salesperson, Amount

**Analysis Tasks Made Easy:**

| Task | Pivot Table Setup |
|------|-------------------|
| Total sales by product | Rows: Product, Values: Sum of Amount |
| Sales by region and month | Rows: Region, Columns: Month, Values: Sum of Amount |
| Top salespeople | Rows: Salesperson, Values: Sum of Amount (sort descending) |
| Average order size by product | Rows: Product, Values: Average of Amount |

**Key Features:**
- **Filters**: Show only specific products or date ranges
- **Grouping**: Group dates by month/quarter/year
- **Calculated Fields**: Create new calculations within the pivot
- **Slicers**: Visual filters for easy data exploration

**Pro Tip:** Right-click on values → "Show Values As" → "% of Column Total" to see percentages instead of raw numbers.
                """,
                "key_points": ["Pivot tables summarize data without formulas", "Drag and drop fields to analyze different angles", "Use filters and slicers for interactive exploration"]
            },
            {
                "title": "Data Cleaning Techniques",
                "content": """
**Common Data Problems and Solutions:**

**1. Removing Duplicates**
- Excel: Data → Remove Duplicates
- Sheets: Data → Data Cleanup → Remove Duplicates
- Formula: `=UNIQUE(range)` to create a clean list

**2. Handling Blank Cells**
```
=IF(A1="", "Missing", A1)
```
Or use Find & Replace: Find blank cells → Replace with "N/A"

**3. Text Cleaning**
```
=TRIM(A1)           -- Remove extra spaces
=UPPER(A1)          -- Convert to uppercase
=PROPER(A1)         -- Capitalize first letters
=CLEAN(A1)          -- Remove non-printable characters
```

**4. Splitting Text**
```
=LEFT(A1, 5)        -- First 5 characters
=RIGHT(A1, 3)       -- Last 3 characters
=MID(A1, 2, 4)      -- 4 characters starting at position 2
=TEXTSPLIT(A1, ",") -- Split by delimiter (Excel 365)
```
Or: Data → Text to Columns

**5. Date Standardization**
```
=DATEVALUE("2024-01-15")  -- Convert text to date
=TEXT(A1, "YYYY-MM-DD")   -- Format date consistently
```

**Real-World Scenario:**
You receive customer data with:
- Names in all caps: "JOHN SMITH"
- Extra spaces: "  Chicago  "
- Inconsistent dates: "01/15/24", "2024-01-15", "Jan 15, 2024"

**Cleaning Process:**
```
=PROPER(TRIM(A2))           -- Clean names
=TRIM(B2)                   -- Clean cities
=DATEVALUE(C2)              -- Standardize dates
```
                """,
                "key_points": ["Remove duplicates before analysis", "TRIM removes extra spaces", "Use Text to Columns to split data"]
            },
            {
                "title": "Automation with Macros and Scripts",
                "content": """
**Automating Repetitive Tasks**

**Excel: Recording Macros**
1. View → Macros → Record Macro
2. Give it a name and shortcut key
3. Perform your actions
4. Stop recording
5. Run the macro anytime with your shortcut

**Example Macro Tasks:**
- Format all reports the same way
- Copy data from one sheet to another
- Apply consistent styling to tables

**Google Sheets: Apps Script**
Google Sheets uses JavaScript-based Apps Script for automation.

**Example Script (Auto-email report):**
```javascript
function sendWeeklyReport() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getRange("A1:D10").getValues();
  
  MailApp.sendEmail({
    to: "manager@company.com",
    subject: "Weekly Sales Report",
    body: "See attached data..."
  });
}
```

**Common Automation Use Cases:**
1. **Data Import**: Pull data from external sources automatically
2. **Report Generation**: Create formatted reports with one click
3. **Email Alerts**: Send notifications when thresholds are met
4. **Data Validation**: Automatically check for errors in new entries

**Power Query (Excel):**
- Connect to databases, websites, or other files
- Transform data with a visual interface
- Refresh data automatically

**Pro Tip:** Start with recording macros to learn the basics, then graduate to VBA (Excel) or Apps Script (Sheets) for more complex automation.
                """,
                "key_points": ["Macros record repetitive actions", "Google Sheets uses Apps Script for automation", "Power Query connects to external data sources"]
            }
        ],
        "exercises": [
            {
                "title": "Calculate Regional Sales",
                "type": "practical",
                "question": "You have sales data with columns: Region (A), Product (B), Amount (C). Write a formula to sum all sales for the 'East' region.",
                "answer": "=SUMIF(A:A, \"East\", C:C) - This formula checks column A for 'East' and sums the corresponding values in column C.",
                "hint": "Use SUMIF with the region column as the range and 'East' as the criteria"
            },
            {
                "title": "Create a Pivot Table Summary",
                "type": "scenario",
                "question": "Your manager wants a report showing total sales by month for each product category. Describe how you would set up a pivot table to show this.",
                "answer": "1. Select all data including headers. 2. Insert Pivot Table. 3. Drag 'Product Category' to Rows. 4. Drag 'Date' to Columns and group by Month. 5. Drag 'Sales Amount' to Values (set to SUM). This creates a matrix with products as rows, months as columns, and sales totals in each cell.",
                "hint": "Think about what goes in rows vs columns, and what value you're summarizing"
            },
            {
                "title": "Clean Messy Data",
                "type": "practical",
                "question": "Cell A1 contains '  JOHN DOE  ' (with extra spaces and all caps). Write a formula to clean this to 'John Doe'.",
                "answer": "=PROPER(TRIM(A1)) - TRIM removes the extra spaces, then PROPER capitalizes only the first letter of each word, resulting in 'John Doe'.",
                "hint": "Combine TRIM to remove spaces and PROPER for proper capitalization"
            }
        ],
        "quiz": [
            {
                "question": "Which formula finds a value in the first column and returns a value from another column?",
                "options": ["SUMIF", "VLOOKUP", "COUNTIF", "TRIM"],
                "correct": 1,
                "explanation": "VLOOKUP (Vertical Lookup) searches the first column of a range for a value and returns a value from a specified column."
            },
            {
                "question": "What does =SUMIF(A:A, \"North\", B:B) do?",
                "options": ["Counts cells containing 'North'", "Sums column B where column A equals 'North'", "Finds 'North' in column A", "Averages column B"],
                "correct": 1,
                "explanation": "SUMIF adds up values in the sum_range (B:B) where the corresponding cells in the criteria_range (A:A) match the criteria ('North')."
            },
            {
                "question": "Which feature summarizes large datasets without formulas?",
                "options": ["VLOOKUP", "Conditional Formatting", "Pivot Table", "Data Validation"],
                "correct": 2,
                "explanation": "Pivot Tables allow you to summarize, analyze, and explore large datasets by dragging and dropping fields - no formulas required."
            },
            {
                "question": "=PROPER(TRIM(\"  HELLO WORLD  \")) returns:",
                "options": ["HELLO WORLD", "hello world", "Hello World", "  Hello World  "],
                "correct": 2,
                "explanation": "TRIM removes extra spaces, then PROPER capitalizes the first letter of each word, resulting in 'Hello World'."
            }
        ]
    },
    "Tool: Python Programming": {
        "course": "Programming Fundamentals",
        "tool_type": "programming",
        "description": "Learn Python for data analysis - pandas for data manipulation, data cleaning scripts, and automated analysis pipelines.",
        "lessons": [
            {
                "title": "Introduction to Pandas DataFrames",
                "content": """
**Pandas: The Data Analyst's Best Friend**

Pandas is a Python library that makes working with data easy and intuitive.

**Creating a DataFrame:**
```python
import pandas as pd

# From a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# From a CSV file
df = pd.read_csv('sales_data.csv')

# From an Excel file
df = pd.read_excel('report.xlsx')
```

**Exploring Your Data:**
```python
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.info()           # Column types and non-null counts
df.describe()       # Statistical summary
df.shape            # (rows, columns)
df.columns          # List of column names
```

**Selecting Data:**
```python
df['Name']                    # Single column
df[['Name', 'Age']]          # Multiple columns
df.loc[0]                    # Row by label/index
df.iloc[0:5]                 # Rows by position
df[df['Age'] > 30]           # Filter rows by condition
```

**Real-World Example:**
```python
# Load sales data
sales = pd.read_csv('sales.csv')

# Quick exploration
print(f"Total records: {len(sales)}")
print(f"Columns: {sales.columns.tolist()}")
print(f"Date range: {sales['date'].min()} to {sales['date'].max()}")
```
                """,
                "key_points": ["pandas uses DataFrames to organize data in rows and columns", "read_csv() and read_excel() load external data", "Use head(), info(), describe() to explore data quickly"]
            },
            {
                "title": "Data Manipulation with Pandas",
                "content": """
**Common Data Operations:**

**1. Adding and Modifying Columns:**
```python
# New column from calculation
df['Bonus'] = df['Salary'] * 0.10

# New column from condition
df['Senior'] = df['Age'] > 30

# Modify existing column
df['Name'] = df['Name'].str.upper()
```

**2. Aggregations:**
```python
df['Salary'].sum()      # Total
df['Salary'].mean()     # Average
df['Age'].max()         # Maximum
df['Name'].count()      # Count

# Group by and aggregate
df.groupby('Department')['Salary'].mean()
df.groupby('Region').agg({
    'Sales': 'sum',
    'Orders': 'count',
    'Amount': 'mean'
})
```

**3. Sorting:**
```python
df.sort_values('Salary', ascending=False)  # Sort by column
df.sort_values(['Dept', 'Salary'])         # Sort by multiple columns
```

**4. Merging DataFrames:**
```python
# Like VLOOKUP in Excel
merged = pd.merge(orders, customers, on='customer_id', how='left')

# Combine datasets vertically
all_data = pd.concat([jan_data, feb_data, mar_data])
```

**Real-World Scenario:**
```python
# Calculate sales metrics by region
summary = sales.groupby('Region').agg({
    'Amount': ['sum', 'mean', 'count'],
    'Profit': 'sum'
}).round(2)

# Find top 10 customers
top_customers = sales.groupby('Customer')['Amount'].sum().nlargest(10)
```
                """,
                "key_points": ["groupby() aggregates data like pivot tables", "merge() combines DataFrames like VLOOKUP", "Method chaining allows multiple operations in one line"]
            },
            {
                "title": "Data Cleaning in Python",
                "content": """
**Handling Common Data Issues:**

**1. Missing Values:**
```python
# Find missing values
df.isnull().sum()                    # Count per column

# Handle missing values
df.dropna()                          # Remove rows with any missing
df.dropna(subset=['Name'])           # Remove if Name is missing
df.fillna(0)                         # Fill with 0
df['Age'].fillna(df['Age'].mean())   # Fill with mean
```

**2. Duplicates:**
```python
# Find duplicates
df.duplicated().sum()                # Count duplicates
df[df.duplicated()]                  # Show duplicate rows

# Remove duplicates
df.drop_duplicates()                 # Remove exact duplicates
df.drop_duplicates(subset=['Email']) # Remove based on column
```

**3. Data Type Conversion:**
```python
df['Date'] = pd.to_datetime(df['Date'])        # Convert to datetime
df['Price'] = df['Price'].astype(float)        # Convert to float
df['ID'] = df['ID'].astype(str)                # Convert to string
```

**4. Text Cleaning:**
```python
df['Name'] = df['Name'].str.strip()            # Remove whitespace
df['Name'] = df['Name'].str.lower()            # Lowercase
df['Name'] = df['Name'].str.title()            # Title Case
df['Code'] = df['Code'].str.replace('-', '')   # Remove characters
```

**5. Outlier Detection:**
```python
# Using Z-score
from scipy import stats
df['z_score'] = stats.zscore(df['Value'])
outliers = df[abs(df['z_score']) > 3]

# Using IQR
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Value'] < Q1 - 1.5*IQR) | (df['Value'] > Q3 + 1.5*IQR)]
```
                """,
                "key_points": ["isnull().sum() shows missing value counts", "drop_duplicates() removes duplicate rows", "to_datetime() converts text to proper dates"]
            },
            {
                "title": "Analysis Scripts and Automation",
                "content": """
**Creating Reusable Analysis Scripts:**

**Basic Analysis Template:**
```python
import pandas as pd

def analyze_sales(filepath):
    # Load data
    df = pd.read_csv(filepath)
    
    # Clean data
    df = df.dropna(subset=['Amount'])
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Calculate metrics
    results = {
        'total_sales': df['Amount'].sum(),
        'avg_order': df['Amount'].mean(),
        'num_orders': len(df),
        'top_product': df.groupby('Product')['Amount'].sum().idxmax()
    }
    
    return results

# Run analysis
metrics = analyze_sales('sales_2024.csv')
print(f"Total Sales: ${metrics['total_sales']:,.2f}")
```

**Scheduling Automated Reports:**
```python
import schedule
import time

def daily_report():
    data = pd.read_csv('daily_data.csv')
    summary = data.groupby('Category').sum()
    summary.to_csv(f'report_{date.today()}.csv')
    print("Report generated!")

# Run every day at 9 AM
schedule.every().day.at("09:00").do(daily_report)

while True:
    schedule.run_pending()
    time.sleep(60)
```

**Exporting Results:**
```python
# To CSV
df.to_csv('output.csv', index=False)

# To Excel with formatting
with pd.ExcelWriter('report.xlsx') as writer:
    summary.to_excel(writer, sheet_name='Summary')
    details.to_excel(writer, sheet_name='Details')

# To JSON
df.to_json('data.json', orient='records')
```
                """,
                "key_points": ["Functions make analysis reusable", "schedule library automates recurring tasks", "Export to CSV, Excel, or JSON formats"]
            }
        ],
        "exercises": [
            {
                "title": "Calculate Sales Summary",
                "type": "practical",
                "question": "Write Python code to load 'sales.csv' and calculate the total sales amount and number of unique customers.",
                "answer": "```python\nimport pandas as pd\ndf = pd.read_csv('sales.csv')\ntotal_sales = df['Amount'].sum()\nunique_customers = df['CustomerID'].nunique()\nprint(f'Total: ${total_sales:,.2f}')\nprint(f'Unique Customers: {unique_customers}')\n```\nThe .sum() method adds all values, and .nunique() counts unique values.",
                "hint": "Use pd.read_csv to load, .sum() for total, and .nunique() for unique count"
            },
            {
                "title": "Group By Analysis",
                "type": "practical",
                "question": "Write code to find the average order amount by product category from a DataFrame called 'orders'.",
                "answer": "```python\navg_by_category = orders.groupby('Category')['Amount'].mean()\nprint(avg_by_category.sort_values(ascending=False))\n```\nThis groups orders by Category, then calculates the mean Amount for each group.",
                "hint": "Use groupby('Category') followed by .mean() on the Amount column"
            },
            {
                "title": "Clean Missing Data",
                "type": "scenario",
                "question": "Your DataFrame 'customers' has missing values in the 'Email' column and duplicate rows. Describe the steps to clean this data.",
                "answer": "```python\n# Step 1: Check missing values\nprint(customers['Email'].isnull().sum())\n\n# Step 2: Remove rows with missing emails\ncustomers = customers.dropna(subset=['Email'])\n\n# Step 3: Remove duplicate rows\ncustomers = customers.drop_duplicates()\n\n# Step 4: Verify cleaning\nprint(f'Remaining rows: {len(customers)}')\n```",
                "hint": "Use dropna() for missing values and drop_duplicates() for duplicates"
            }
        ],
        "quiz": [
            {
                "question": "Which pandas function loads a CSV file?",
                "options": ["pd.load_csv()", "pd.read_csv()", "pd.import_csv()", "pd.open_csv()"],
                "correct": 1,
                "explanation": "pd.read_csv() is the standard function to load CSV files into a pandas DataFrame."
            },
            {
                "question": "df.groupby('Region')['Sales'].sum() does what?",
                "options": ["Counts rows by region", "Averages sales by region", "Sums sales by region", "Lists all regions"],
                "correct": 2,
                "explanation": "This groups data by Region, then sums the Sales column for each region - like a pivot table."
            },
            {
                "question": "How do you check for missing values in a DataFrame?",
                "options": ["df.missing()", "df.isnull().sum()", "df.check_null()", "df.find_empty()"],
                "correct": 1,
                "explanation": "df.isnull().sum() returns the count of missing (null) values for each column."
            },
            {
                "question": "What does df.drop_duplicates() do?",
                "options": ["Removes columns", "Removes null values", "Removes duplicate rows", "Removes the first row"],
                "correct": 2,
                "explanation": "drop_duplicates() removes rows that are exact copies of other rows in the DataFrame."
            }
        ]
    },
    "Tool: SQL & Databases": {
        "course": "Databases and Cloud Services",
        "tool_type": "database",
        "description": "Master SQL for querying databases - learn SELECT statements, JOINs, aggregations, and data extraction from relational databases.",
        "lessons": [
            {
                "title": "SQL Basics: SELECT Queries",
                "content": """
**SQL (Structured Query Language)** is the standard language for working with databases.

**Basic SELECT Statement:**
```sql
SELECT column1, column2
FROM table_name
WHERE condition
ORDER BY column1;
```

**Examples:**

**1. Select All Data:**
```sql
SELECT * FROM customers;
```

**2. Select Specific Columns:**
```sql
SELECT first_name, last_name, email
FROM customers;
```

**3. Filter with WHERE:**
```sql
SELECT * FROM orders
WHERE order_date > '2024-01-01';

SELECT * FROM products
WHERE price BETWEEN 10 AND 50;

SELECT * FROM customers
WHERE city IN ('New York', 'Los Angeles', 'Chicago');
```

**4. Sort Results:**
```sql
SELECT * FROM sales
ORDER BY amount DESC;  -- Highest first

SELECT * FROM employees
ORDER BY department, hire_date;
```

**5. Limit Results:**
```sql
SELECT * FROM products
ORDER BY sales DESC
LIMIT 10;  -- Top 10 best sellers
```

**Common WHERE Operators:**
| Operator | Example | Description |
|----------|---------|-------------|
| = | WHERE city = 'Oslo' | Exact match |
| > < >= <= | WHERE price > 100 | Comparisons |
| BETWEEN | WHERE age BETWEEN 20 AND 30 | Range |
| LIKE | WHERE name LIKE 'J%' | Pattern match |
| IN | WHERE status IN ('Active', 'Pending') | Multiple values |
| IS NULL | WHERE email IS NULL | Missing values |
                """,
                "key_points": ["SELECT retrieves data from tables", "WHERE filters rows based on conditions", "ORDER BY sorts results, LIMIT restricts row count"]
            },
            {
                "title": "JOINs: Combining Tables",
                "content": """
**JOINs connect data from multiple tables** based on related columns.

**Types of JOINs:**

**1. INNER JOIN (Most Common)**
Returns only matching rows from both tables.
```sql
SELECT orders.order_id, customers.name, orders.amount
FROM orders
INNER JOIN customers ON orders.customer_id = customers.id;
```

**2. LEFT JOIN**
Returns all rows from the left table, matched rows from the right.
```sql
SELECT customers.name, orders.order_id
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;
-- Shows all customers, even those without orders (NULL for orders)
```

**3. RIGHT JOIN**
Returns all rows from the right table, matched rows from the left.
```sql
SELECT customers.name, orders.order_id
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id;
```

**Visual Representation:**
```
INNER JOIN:     [A ∩ B]     - Only matching records
LEFT JOIN:      [A + (A∩B)] - All from left + matches
RIGHT JOIN:     [(A∩B) + B] - All from right + matches
FULL OUTER JOIN:[A + B]     - All records from both
```

**Real-World Example:**
You have three tables: `orders`, `customers`, `products`

```sql
SELECT 
    o.order_id,
    c.customer_name,
    p.product_name,
    o.quantity,
    o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN products p ON o.product_id = p.id
WHERE o.order_date >= '2024-01-01'
ORDER BY o.order_date DESC;
```
                """,
                "key_points": ["INNER JOIN returns only matching rows", "LEFT JOIN keeps all rows from the first table", "Use aliases (o, c, p) to simplify queries"]
            },
            {
                "title": "Aggregations and GROUP BY",
                "content": """
**Aggregate Functions** calculate values across multiple rows.

**Common Aggregate Functions:**
```sql
COUNT(*)        -- Number of rows
COUNT(column)   -- Non-null values in column
SUM(column)     -- Total
AVG(column)     -- Average
MIN(column)     -- Minimum value
MAX(column)     -- Maximum value
```

**GROUP BY: Aggregate by Category**
```sql
SELECT category, SUM(amount) as total_sales
FROM sales
GROUP BY category;
```

**Example Results:**
| category | total_sales |
|----------|-------------|
| Electronics | 150000 |
| Clothing | 85000 |
| Home | 62000 |

**HAVING: Filter Grouped Results**
```sql
SELECT customer_id, COUNT(*) as order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 5;  -- Only customers with 5+ orders
```

**Difference: WHERE vs HAVING**
- WHERE filters rows BEFORE grouping
- HAVING filters groups AFTER aggregation

**Complex Example:**
```sql
SELECT 
    region,
    COUNT(*) as num_orders,
    SUM(amount) as total_revenue,
    AVG(amount) as avg_order,
    MAX(amount) as largest_order
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY region
HAVING SUM(amount) > 10000
ORDER BY total_revenue DESC;
```
                """,
                "key_points": ["SUM, COUNT, AVG, MIN, MAX are aggregate functions", "GROUP BY creates groups for aggregation", "HAVING filters after grouping, WHERE filters before"]
            },
            {
                "title": "Subqueries and Advanced Techniques",
                "content": """
**Subqueries: Queries Within Queries**

**1. Subquery in WHERE:**
```sql
-- Find customers who spent above average
SELECT customer_name, total_spent
FROM customers
WHERE total_spent > (SELECT AVG(total_spent) FROM customers);
```

**2. Subquery in FROM:**
```sql
-- Calculate metrics on aggregated data
SELECT region, avg_order
FROM (
    SELECT region, AVG(amount) as avg_order
    FROM orders
    GROUP BY region
) as region_summary
WHERE avg_order > 100;
```

**Common Table Expressions (CTEs):**
```sql
WITH monthly_sales AS (
    SELECT 
        DATE_TRUNC('month', order_date) as month,
        SUM(amount) as revenue
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
)
SELECT month, revenue,
       revenue - LAG(revenue) OVER (ORDER BY month) as change
FROM monthly_sales;
```

**Window Functions:**
```sql
-- Rank salespeople by performance
SELECT 
    salesperson,
    total_sales,
    RANK() OVER (ORDER BY total_sales DESC) as rank
FROM sales_summary;

-- Running total
SELECT 
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) as running_total
FROM orders;
```

**CASE Statements:**
```sql
SELECT 
    product_name,
    price,
    CASE 
        WHEN price < 10 THEN 'Budget'
        WHEN price < 50 THEN 'Mid-range'
        ELSE 'Premium'
    END as category
FROM products;
```
                """,
                "key_points": ["Subqueries can be used in WHERE, FROM, or SELECT", "CTEs make complex queries more readable", "Window functions calculate across rows without grouping"]
            }
        ],
        "exercises": [
            {
                "title": "Basic Query",
                "type": "practical",
                "question": "Write a SQL query to find all orders over $500 from 2024, sorted by amount (highest first).",
                "answer": "```sql\nSELECT *\nFROM orders\nWHERE amount > 500\n  AND order_date >= '2024-01-01'\nORDER BY amount DESC;\n```\nThis filters orders by amount AND date, then sorts descending.",
                "hint": "Use WHERE with two conditions (AND), ORDER BY with DESC"
            },
            {
                "title": "JOIN Two Tables",
                "type": "practical",
                "question": "Write a query to show order_id, customer_name, and amount by joining 'orders' and 'customers' tables on customer_id.",
                "answer": "```sql\nSELECT o.order_id, c.customer_name, o.amount\nFROM orders o\nINNER JOIN customers c ON o.customer_id = c.id;\n```\nINNER JOIN connects the tables where customer_id matches.",
                "hint": "Use INNER JOIN with ON clause to specify the matching columns"
            },
            {
                "title": "Aggregation Challenge",
                "type": "practical",
                "question": "Write a query to find total sales by product category, but only show categories with total sales over $10,000.",
                "answer": "```sql\nSELECT category, SUM(amount) as total_sales\nFROM sales\nGROUP BY category\nHAVING SUM(amount) > 10000\nORDER BY total_sales DESC;\n```\nGROUP BY aggregates by category, HAVING filters the grouped results.",
                "hint": "Use GROUP BY for categories, HAVING (not WHERE) to filter after aggregation"
            }
        ],
        "quiz": [
            {
                "question": "Which SQL clause filters rows BEFORE grouping?",
                "options": ["HAVING", "WHERE", "GROUP BY", "ORDER BY"],
                "correct": 1,
                "explanation": "WHERE filters individual rows before any grouping. HAVING filters after grouping."
            },
            {
                "question": "What does LEFT JOIN do?",
                "options": ["Returns only matching rows", "Returns all rows from the left table plus matches", "Returns all rows from both tables", "Joins tables side by side"],
                "correct": 1,
                "explanation": "LEFT JOIN returns all rows from the left (first) table, and matching rows from the right table. Non-matches show NULL."
            },
            {
                "question": "SELECT COUNT(*) FROM orders returns:",
                "options": ["All order details", "Number of columns", "Total order amount", "Number of rows"],
                "correct": 3,
                "explanation": "COUNT(*) counts all rows in the table. COUNT(column) would count non-null values in that column."
            },
            {
                "question": "To show only top 5 results, use:",
                "options": ["TOP 5", "FIRST 5", "LIMIT 5", "MAX 5"],
                "correct": 2,
                "explanation": "LIMIT 5 restricts the result to 5 rows. (Note: TOP is used in SQL Server, LIMIT in MySQL/PostgreSQL)"
            }
        ]
    },
    "Tool: Tableau & Power BI": {
        "course": "Data Visualisation",
        "tool_type": "visualization",
        "description": "Learn to create professional dashboards and data visualizations using Business Intelligence tools like Tableau and Power BI.",
        "lessons": [
            {
                "title": "Dashboard Design Principles",
                "content": """
**Creating Effective Dashboards**

**The 5-Second Rule:**
Users should understand the main message within 5 seconds of viewing your dashboard.

**Key Design Principles:**

**1. Hierarchy: Most Important First**
- Place key metrics at the top-left (where eyes naturally start)
- Use size to indicate importance
- Group related information together

**2. Layout Patterns:**
```
┌─────────────────────────────────┐
│     KPI Cards (Top Metrics)     │
├───────────────┬─────────────────┤
│  Main Chart   │  Supporting     │
│  (Trend/Map)  │  Charts         │
├───────────────┴─────────────────┤
│     Detail Table / Filters      │
└─────────────────────────────────┘
```

**3. Color Best Practices:**
- Use a consistent color palette (3-5 colors max)
- Reserve red for negative/alerts
- Reserve green for positive/good
- Use gray for context/secondary info
- Ensure color-blind accessibility

**4. White Space:**
- Don't overcrowd - let visualizations breathe
- Group related elements with subtle borders or backgrounds
- Consistent margins and padding

**5. Interactivity:**
- Add filters for user exploration
- Use drill-down for details on demand
- Cross-filter charts when one is clicked
- Include tooltips for additional context

**Common Mistakes to Avoid:**
- Too many charts (aim for 4-6 per dashboard)
- 3D charts (distort perception)
- Pie charts with many slices (use bar charts instead)
- Inconsistent formatting across charts
                """,
                "key_points": ["Key metrics go top-left", "Limit to 3-5 colors", "Less is more - avoid clutter"]
            },
            {
                "title": "Choosing the Right Visualization",
                "content": """
**Match Your Chart to Your Data Story**

**1. Comparisons:**
| Chart Type | Best For |
|------------|----------|
| Bar Chart | Comparing categories |
| Column Chart | Comparing over time (few periods) |
| Bullet Chart | Comparing to a target |
| Lollipop Chart | Many categories, cleaner than bars |

**2. Trends Over Time:**
| Chart Type | Best For |
|------------|----------|
| Line Chart | Continuous time series |
| Area Chart | Showing volume over time |
| Sparklines | Compact trends in tables |

**3. Parts of a Whole:**
| Chart Type | Best For |
|------------|----------|
| Stacked Bar | Composition with few categories |
| Treemap | Hierarchical part-to-whole |
| Donut Chart | Simple 2-3 part breakdowns |

**4. Relationships:**
| Chart Type | Best For |
|------------|----------|
| Scatter Plot | Correlation between variables |
| Bubble Chart | Three variables (x, y, size) |
| Heat Map | Patterns across two dimensions |

**5. Geographic:**
| Chart Type | Best For |
|------------|----------|
| Choropleth Map | Values by region |
| Symbol Map | Point locations with values |

**Decision Framework:**
1. What question are you answering?
2. How many variables?
3. What type of data? (categories, time, geography)
4. Who is the audience?

**Example:**
"How have sales changed by region over the past year?"
- Time + Categories = Line chart with one line per region
- Or: Small multiples (one chart per region)
                """,
                "key_points": ["Bar charts for comparisons, line charts for trends", "Avoid pie charts with many slices", "Consider your audience when choosing complexity"]
            },
            {
                "title": "Building in Tableau",
                "content": """
**Tableau Workflow:**

**1. Connect to Data:**
- File → New → Connect to data source
- Supports: Excel, CSV, databases, cloud services
- Use "Data Interpreter" to clean messy files

**2. Understand the Interface:**
```
┌──────────────────────────────────────────┐
│ Data Pane │ Cards & Shelves  │ Worksheet │
│ (Fields)  │ (Rows, Columns,  │ (Canvas)  │
│           │  Filters, Marks) │           │
└──────────────────────────────────────────┘
```

**3. Building Visualizations:**
- Drag DIMENSIONS (categorical) to Rows/Columns
- Drag MEASURES (numerical) to create charts
- Tableau automatically suggests chart types

**4. Key Actions:**
```
Show Me Panel     → Quick chart suggestions
Marks Card        → Color, Size, Label, Tooltip
Filters Shelf     → Filter data
Pages Shelf       → Animation through data
```

**5. Calculated Fields:**
```
// Example: Profit Margin
[Profit] / [Sales]

// Example: Sales Category
IF [Sales] > 10000 THEN "High"
ELSEIF [Sales] > 5000 THEN "Medium"
ELSE "Low"
END
```

**6. Creating Dashboards:**
- New → Dashboard
- Drag worksheets onto the canvas
- Add filters, text boxes, images
- Set up actions (filter, highlight, URL)

**Pro Tips:**
- Use Ctrl+click to multi-select fields
- Right-click for format options
- Save as .twbx to include data with workbook
                """,
                "key_points": ["Dimensions are categories, Measures are numbers", "Drag fields to Rows/Columns to build charts", "Dashboards combine multiple worksheets"]
            },
            {
                "title": "Building in Power BI",
                "content": """
**Power BI Workflow:**

**1. Get Data:**
- Home → Get Data → Choose source
- Transform data in Power Query Editor
- Load to data model

**2. Interface Overview:**
```
┌────────────────────────────────────────────┐
│ Report View │ Data View │ Model View       │
├────────────────────────────────────────────┤
│ Fields │ Visualizations │ Report Canvas    │
│ Pane   │ Pane           │                  │
└────────────────────────────────────────────┘
```

**3. Creating Visuals:**
1. Click visual type in Visualizations pane
2. Drag fields to Values, Axis, Legend
3. Format in Format pane (paint roller icon)

**4. DAX Formulas:**
```
// Total Sales
Total Sales = SUM(Sales[Amount])

// Year-over-Year Growth
YoY Growth = 
DIVIDE(
    [Total Sales] - CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date])),
    CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
)

// Running Total
Running Total = 
CALCULATE(
    [Total Sales],
    FILTER(ALL('Date'), 'Date'[Date] <= MAX('Date'[Date]))
)
```

**5. Key Features:**
- **Slicers**: Interactive filters
- **Drill Through**: Right-click to see details
- **Bookmarks**: Save views/states
- **Q&A**: Natural language queries

**6. Publishing:**
- Publish → Select workspace
- Share dashboards with colleagues
- Schedule data refresh
- Set up alerts on metrics

**Tableau vs Power BI:**
| Feature | Tableau | Power BI |
|---------|---------|----------|
| Strengths | Visualization | Microsoft integration |
| Learning | Steeper curve | Easier for Excel users |
| Cost | Higher | Lower (included in Microsoft 365) |
                """,
                "key_points": ["Power BI uses DAX for calculations", "Slicers are interactive dashboard filters", "Publish to Power BI Service to share online"]
            }
        ],
        "exercises": [
            {
                "title": "Choose the Right Chart",
                "type": "scenario",
                "question": "You need to show how market share has changed over 5 years for 4 companies. What chart type would you use and why?",
                "answer": "A stacked area chart or 100% stacked area chart would work best. It shows: 1) Time progression (x-axis), 2) Each company's share (different colors), 3) How shares changed relative to each other. Alternative: Line chart if you want to emphasize individual company trends.",
                "hint": "You're showing parts of a whole (market share) over time"
            },
            {
                "title": "Dashboard Layout",
                "type": "scenario",
                "question": "Design a sales dashboard layout for a manager who needs to see: Total Revenue, Monthly Trend, Sales by Region, and Top Products. Describe where each element should go.",
                "answer": "Layout: 1) TOP: KPI cards for Total Revenue, Orders, Avg Order Value (most important, immediate visibility). 2) MIDDLE-LEFT: Line chart showing Monthly Sales Trend (main story, largest space). 3) MIDDLE-RIGHT: Map or bar chart for Sales by Region. 4) BOTTOM: Table or horizontal bar chart for Top 10 Products with details. Add date filter at top-right.",
                "hint": "Think about visual hierarchy - what's most important goes where the eye looks first"
            },
            {
                "title": "Create a DAX Measure",
                "type": "practical",
                "question": "Write a DAX formula to calculate the percentage of sales that came from the 'Online' channel (where Sales[Channel] = 'Online').",
                "answer": "```\nOnline % = \nDIVIDE(\n    CALCULATE(SUM(Sales[Amount]), Sales[Channel] = \"Online\"),\n    SUM(Sales[Amount])\n)\n```\nThis calculates Online sales divided by Total sales. CALCULATE applies the filter for Online channel.",
                "hint": "Use CALCULATE to filter for Online, then DIVIDE by total"
            }
        ],
        "quiz": [
            {
                "question": "What's the best chart for showing sales trends over 12 months?",
                "options": ["Pie chart", "Bar chart", "Line chart", "Scatter plot"],
                "correct": 2,
                "explanation": "Line charts are ideal for showing continuous trends over time. They clearly show patterns, increases, and decreases."
            },
            {
                "question": "In dashboard design, key metrics should be placed:",
                "options": ["At the bottom", "In the center", "At the top-left", "Hidden behind filters"],
                "correct": 2,
                "explanation": "Eyes naturally start at the top-left, so key metrics should be placed there for immediate visibility."
            },
            {
                "question": "In Tableau, what are DIMENSIONS?",
                "options": ["Numerical values for calculations", "Categorical fields for grouping", "Chart types", "Color settings"],
                "correct": 1,
                "explanation": "Dimensions are categorical fields (like Region, Product Name) used to group and categorize data. Measures are numerical values."
            },
            {
                "question": "In Power BI, DAX is used for:",
                "options": ["Connecting to databases", "Creating calculated measures and columns", "Designing visual layouts", "Sharing dashboards"],
                "correct": 1,
                "explanation": "DAX (Data Analysis Expressions) is Power BI's formula language for creating calculated columns, measures, and tables."
            }
        ]
    },
    "Tool: Statistical Analysis": {
        "course": "Statistical Tools",
        "tool_type": "statistics",
        "description": "Learn statistical analysis techniques including hypothesis testing, confidence intervals, and when to use different statistical methods.",
        "lessons": [
            {
                "title": "Descriptive Statistics Fundamentals",
                "content": """
**Summarizing Data with Numbers**

**Measures of Central Tendency:**

**1. Mean (Average)**
```
Mean = Sum of all values / Number of values

Example: 10, 20, 30, 40, 50
Mean = 150 / 5 = 30
```
Use when: Data is symmetric, no extreme outliers

**2. Median (Middle Value)**
```
Sort values, find the middle
Example: 10, 20, 30, 40, 100
Median = 30 (middle value)
```
Use when: Data has outliers (median is resistant to extremes)

**3. Mode (Most Frequent)**
```
Example: 10, 20, 20, 30, 20
Mode = 20 (appears most often)
```
Use when: Working with categorical data

**Measures of Spread:**

**1. Range**
```
Range = Maximum - Minimum
Example: Max=100, Min=10 → Range = 90
```

**2. Variance**
```
Average of squared deviations from mean
σ² = Σ(x - μ)² / n
```

**3. Standard Deviation**
```
Square root of variance
σ = √(Variance)

Interpretation:
- 68% of data within ±1 SD of mean
- 95% of data within ±2 SD of mean
- 99.7% of data within ±3 SD of mean
```

**4. Interquartile Range (IQR)**
```
IQR = Q3 - Q1 (75th percentile - 25th percentile)
Used for identifying outliers:
Outlier if value < Q1 - 1.5×IQR or > Q3 + 1.5×IQR
```

**Real-World Application:**
Salary data: [30K, 35K, 40K, 45K, 500K]
- Mean = 130K (misleading due to outlier)
- Median = 40K (more representative)
- Report BOTH with explanation of the outlier
                """,
                "key_points": ["Mean is affected by outliers, median is not", "Standard deviation shows data spread", "Always report both mean and median for skewed data"]
            },
            {
                "title": "Hypothesis Testing Basics",
                "content": """
**Making Data-Driven Decisions**

**What is Hypothesis Testing?**
A method to determine if observed results are statistically significant or due to chance.

**Key Concepts:**

**1. Null Hypothesis (H₀)**
The "nothing special" assumption
Example: "There is no difference in sales before and after the marketing campaign."

**2. Alternative Hypothesis (H₁)**
What you're trying to prove
Example: "The marketing campaign increased sales."

**3. P-value**
Probability of seeing your results if H₀ is true
- p < 0.05: Statistically significant (reject H₀)
- p ≥ 0.05: Not significant (fail to reject H₀)

**4. Significance Level (α)**
Usually set at 0.05 (5%)
- α = 0.05 means 5% chance of false positive

**Common Tests:**

| Test | When to Use |
|------|-------------|
| T-test | Compare means of 2 groups |
| ANOVA | Compare means of 3+ groups |
| Chi-square | Test categorical relationships |
| Correlation | Test relationship strength |

**Example Workflow:**
1. **Question**: Did the new website design increase conversions?
2. **H₀**: Conversion rate is the same (no effect)
3. **H₁**: New design has higher conversion rate
4. **Collect Data**: Old design: 3.2%, New design: 4.1%
5. **Run Test**: Calculate p-value
6. **Interpret**: p = 0.02 < 0.05 → Significant!
7. **Conclude**: New design significantly improved conversions

**Caution:**
- Statistical significance ≠ practical importance
- p = 0.04 is not "more significant" than p = 0.03
- Always consider effect size alongside p-value
                """,
                "key_points": ["p < 0.05 typically means statistically significant", "Null hypothesis assumes no effect", "Statistical significance doesn't guarantee practical importance"]
            },
            {
                "title": "Choosing the Right Statistical Test",
                "content": """
**Decision Framework for Statistical Tests**

**Step 1: What Type of Data?**
- Continuous (numbers): Age, Sales, Temperature
- Categorical (groups): Gender, Region, Product Type

**Step 2: How Many Groups/Variables?**

**Comparing Groups:**
```
Comparing 2 groups:
├── Continuous outcome → T-test
│   Example: Compare sales between Region A and B
│
└── Categorical outcome → Chi-square test
    Example: Compare click rates between 2 designs

Comparing 3+ groups:
├── Continuous outcome → ANOVA
│   Example: Compare satisfaction across 5 departments
│
└── Categorical outcome → Chi-square test
    Example: Compare preferences across age groups
```

**Analyzing Relationships:**
```
Two continuous variables → Correlation / Regression
Example: Relationship between ad spend and sales

One continuous + categories → T-test / ANOVA
Example: Effect of training (yes/no) on performance

Two categorical variables → Chi-square
Example: Relationship between gender and product preference
```

**Quick Reference Table:**

| Scenario | Test |
|----------|------|
| Compare 2 group means | Independent t-test |
| Compare same group before/after | Paired t-test |
| Compare 3+ group means | One-way ANOVA |
| Predict outcome from variables | Regression |
| Test category relationships | Chi-square |
| Measure relationship strength | Correlation |

**Sample Size Considerations:**
- Small samples (n < 30): Use non-parametric tests
- Large samples: Central Limit Theorem helps
- Rule of thumb: At least 30 per group for t-tests
                """,
                "key_points": ["T-test for 2 groups, ANOVA for 3+", "Chi-square for categorical data", "Always check sample size requirements"]
            },
            {
                "title": "Confidence Intervals and Effect Size",
                "content": """
**Beyond P-values: Practical Significance**

**Confidence Intervals:**
Range where the true value likely falls.

**Interpreting a 95% CI:**
```
Average order value: $45 (95% CI: $42 - $48)

Meaning: We're 95% confident the true average
is between $42 and $48.
```

**Key Insights from CIs:**
- Narrow CI = More precise estimate
- If CI includes 0 (for differences): Not significant
- CIs that don't overlap → Significantly different

**Example:**
```
Group A mean: 50 (95% CI: 45-55)
Group B mean: 60 (95% CI: 56-64)

CIs don't overlap → Significant difference!
```

**Effect Size:**
Measures the magnitude of an effect, independent of sample size.

**Common Effect Size Measures:**

**1. Cohen's d (for mean differences):**
```
d = (Mean1 - Mean2) / Pooled SD

Interpretation:
d = 0.2: Small effect
d = 0.5: Medium effect
d = 0.8: Large effect
```

**2. R-squared (for regression):**
```
R² = Proportion of variance explained

Example: R² = 0.64 means 64% of variation
in Y is explained by X
```

**3. Correlation Coefficient (r):**
```
r = 0.1-0.3: Weak
r = 0.3-0.5: Moderate
r = 0.5-0.7: Strong
r > 0.7: Very strong
```

**Real-World Example:**
"The new training program significantly improved test scores (p < 0.01), with a medium effect size (d = 0.52). Scores increased from 72 (±8) to 76 (±7)."

This tells the full story: significant, meaningful, and practical!
                """,
                "key_points": ["Confidence intervals show the range of plausible values", "Effect size shows practical importance", "Report both p-value AND effect size"]
            }
        ],
        "exercises": [
            {
                "title": "Choose Correct Test",
                "type": "scenario",
                "question": "You want to compare customer satisfaction scores (1-10) across 4 different store locations. Which statistical test should you use?",
                "answer": "Use One-Way ANOVA. Reasons: 1) You're comparing means (satisfaction scores are continuous), 2) You have more than 2 groups (4 stores), 3) Groups are independent. If ANOVA shows significance, follow up with post-hoc tests to see which specific stores differ.",
                "hint": "You have continuous data (scores) and 3+ independent groups"
            },
            {
                "title": "Interpret Results",
                "type": "practical",
                "question": "A study reports: 'Mean difference = 5 points, p = 0.03, 95% CI: [1.2, 8.8], Cohen's d = 0.45'. What does this tell you?",
                "answer": "This tells us: 1) The difference (5 points) is statistically significant (p < 0.05). 2) The true difference is likely between 1.2 and 8.8 points (CI doesn't include 0). 3) The effect size is 'small to medium' (d = 0.45). 4) The finding is statistically significant but the practical impact is moderate.",
                "hint": "Consider what each metric (p-value, CI, effect size) tells you about the finding"
            },
            {
                "title": "Descriptive Statistics",
                "type": "practical",
                "question": "Calculate the mean and median for this salary data (in thousands): 40, 45, 42, 48, 150, 44, 46. Which measure better represents the typical salary?",
                "answer": "Mean = (40+45+42+48+150+44+46)/7 = 415/7 = 59.3K. Median = 45K (middle value when sorted: 40,42,44,45,46,48,150). The MEDIAN (45K) better represents typical salary because the 150K outlier pulls the mean up significantly. Most employees earn around 45K, not 59K.",
                "hint": "Sort the values to find the median. Consider which measure is affected by the outlier"
            }
        ],
        "quiz": [
            {
                "question": "A p-value of 0.03 means:",
                "options": ["97% chance the result is true", "3% chance of seeing this result if null hypothesis is true", "The effect size is 0.03", "3% of data is significant"],
                "correct": 1,
                "explanation": "P-value is the probability of observing results at least as extreme as yours, assuming the null hypothesis is true. p=0.03 means 3% chance."
            },
            {
                "question": "To compare means across 5 different groups, use:",
                "options": ["T-test", "Chi-square", "ANOVA", "Correlation"],
                "correct": 2,
                "explanation": "ANOVA (Analysis of Variance) is designed to compare means across 3 or more groups. T-test is for 2 groups only."
            },
            {
                "question": "A 95% confidence interval of [2, 8] for a difference means:",
                "options": ["95% of data falls in this range", "We're 95% confident the true difference is between 2 and 8", "The p-value is 0.95", "The effect is 95% significant"],
                "correct": 1,
                "explanation": "A 95% CI means we're 95% confident the true population value falls within this range. Since it doesn't include 0, the difference is significant."
            },
            {
                "question": "Cohen's d = 0.8 indicates:",
                "options": ["Not significant", "Small effect", "Medium effect", "Large effect"],
                "correct": 3,
                "explanation": "Cohen's d of 0.8 or higher is considered a large effect size. Small=0.2, Medium=0.5, Large=0.8."
            }
        ]
    }
}

courses_data = [
    {
        "code": "FI1BBDF05", 
        "name": "Data Analysis Fundamentals", 
        "type": "Core Course", 
        "credits": 5, 
        "semester": "2025 Spring",
        "weeks": 3,
        "hours": 126,
        "description": "This course delivers an introductory overview of Data Analysis. It provides the foundational material required to build a strong theoretical understanding of why data analysis is required in industry and how using analytics tools can shape decision making in the real world.",
        "knowledge": [
            "History of data and data sources",
            "Significance of data in the real world",
            "Introduction to business intelligence and big data",
            "Data strategies: exploration, visualization, trends and estimates",
            "Data warehouses, data silos, and open data platforms"
        ],
        "skills": [
            "Apply problem division and solving into each stage in the data lifecycle",
            "Apply theoretical data analysis strategies into real world scenarios",
            "Find information relevant to problem scenarios and suggest solutions",
            "Identify where data can be collected first-hand and alternative sources",
            "Use online data collection tools such as Google Forms",
            "Identify and source data ethically with GDPR standards"
        ],
        "competence": [
            "Understand ethical principles for successful data analysis projects",
            "Understand ethical principles of collecting and maintaining data",
            "Carry out data strategies from real world scenarios",
            "Develop data analysis terminology"
        ]
    },
    {
        "code": "FI1BBSF05", 
        "name": "Spreadsheet Fundamentals", 
        "type": "Core Course", 
        "credits": 5, 
        "semester": "2025 Spring",
        "weeks": 3,
        "hours": 126,
        "description": "This course teaches a foundation level introduction to the spreadsheet work environment, specifically Microsoft Excel. Learn to gather, clean, manage, and organize data. Also covers Google Sheets for collaborative work.",
        "knowledge": [
            "Concepts and processes to gather, clean, manage, and organize data in spreadsheets",
            "Data management techniques: storing, sorting, and presenting data",
            "Cloud-based spreadsheet software (Google Sheets)",
            "Data flow pipelines to link spreadsheet software to external tools",
            "Why spreadsheets are useful in society and value-creation"
        ],
        "skills": [
            "Apply spreadsheet software to gather, sort, store, manage and organize data",
            "Use conditional formatting and pivot tables to summarize key data points",
            "Find information to develop transformative spreadsheet projects",
            "Master two spreadsheet software suites (offline and online)",
            "Master basic workbook manipulation tools",
            "Use basic field formulas to automate data tasks"
        ],
        "competence": [
            "Create workbooks to manage data from start to finish",
            "Build relations with clients using real world data sets",
            "Develop collaborative workbooks using cloud-based software"
        ]
    },
    {
        "code": "FI1BBDD75", 
        "name": "Data Driven Decision-Making", 
        "type": "Core Course", 
        "credits": 7.5, 
        "semester": "2025 Spring",
        "weeks": 4,
        "hours": 168,
        "description": "This course establishes core concepts of decision-making techniques applied to data models. Learn the data analysis lifecycle, techniques (Descriptive, Predictive, Prescriptive, Diagnostic), and qualitative vs quantitative data.",
        "knowledge": [
            "Data structure models and where to apply applicable data sets",
            "Concepts and processes for data cleaning using real world data",
            "Real-world use case stories and company impacts",
            "Key Performance Indicators (KPI) and data types",
            "Four data analysis philosophies: descriptive, diagnostic, predictive, prescriptive",
            "Error detection, elimination, and correction"
        ],
        "skills": [
            "Apply data driven decision making to problems like market price prediction",
            "Strategically select appropriate data models to solve scenarios",
            "Apply data lifecycle to create iterative solutions and analyze KPIs",
            "Identify erroneous data and eliminate/correct them",
            "Master theoretical models to real world data"
        ],
        "competence": [
            "Understand the fidelity of data within a project",
            "Develop work methods using KPIs to guide decision-making",
            "Deliver insights to gauge if models are accurate for intended use"
        ]
    },
    {
        "code": "FI1BBST05", 
        "name": "Statistical Tools", 
        "type": "Core Course", 
        "credits": 5, 
        "semester": "2025 Spring",
        "weeks": 3,
        "hours": 126,
        "description": "This course provides knowledge of using integrated spreadsheet tools and introductory statistical modelling software. Builds on Spreadsheet Fundamentals competence.",
        "knowledge": [
            "Spreadsheet data tools for statistical analysis using built-in functions",
            "Statistical methodologies to extract KPIs from numerical values",
            "Advanced data analytics tool packs in spreadsheet software",
            "Correlation, regression, ANOVA, histogram and covariance analysis",
            "Power Query for automation",
            "Z-scores and z-testing for outlier reduction"
        ],
        "skills": [
            "Perform statistical analysis on data sets using spreadsheet tools",
            "Install and use advanced data analysis suite",
            "Use Power Query to automate tasks",
            "Apply z-values to reduce errors and eliminate outliers"
        ],
        "competence": [
            "Carry out work using advanced spreadsheet tools",
            "Develop effective work methods for analysis within spreadsheets"
        ]
    },
    {
        "code": "FI1BBP175", 
        "name": "Semester Project 1", 
        "type": "Core Course", 
        "credits": 7.5, 
        "semester": "2025 Spring",
        "weeks": 4,
        "hours": 168,
        "description": "Apply first semester knowledge to a practical data analysis project. Demonstrate understanding of data fundamentals, spreadsheets, and decision-making.",
        "knowledge": [
            "Project planning and scope definition",
            "Data collection for real-world problems",
            "Applying analytical techniques learned",
            "Documentation and reporting standards",
            "Presentation skills for data findings"
        ],
        "skills": [
            "Execute a complete data analysis project",
            "Apply spreadsheet and statistical tools",
            "Present findings to an audience",
            "Document work professionally"
        ],
        "competence": [
            "Plan and execute data analysis tasks independently",
            "Work according to ethical requirements",
            "Deliver professional project documentation"
        ]
    },
    {
        "code": "FI1BBEO10", 
        "name": "Evaluation of Outcomes", 
        "type": "Core Course", 
        "credits": 10, 
        "semester": "2025 Fall",
        "weeks": 8,
        "hours": 336,
        "description": "Learn to review, assess, and appraise the results of analytical models. Covers statistical inferences, confidence levels, and iterative error elimination.",
        "knowledge": [
            "Key Performance Indicators (KPI) as heuristics in decision making",
            "Statistical inferences: sampled sets, linear regression, variance, five-point summaries, z-testing",
            "Confidence levels and multiple probability outcomes",
            "Iterative error elimination processes and tools",
            "Ensambling data techniques",
            "Version control for collaborative data work",
            "ETL systems in data analysis lifecycle"
        ],
        "skills": [
            "Apply statistical inferences to identify and solve problems",
            "Apply iterative error elimination to improve results",
            "Create multiple outcome scenarios with confidence levels",
            "Critically assess and analyse data models",
            "Improve reliability using ensambling techniques"
        ],
        "competence": [
            "Independently assess and critique analysis approaches",
            "Develop ethical approach to solving data problems",
            "Facilitate solution discussions among project members"
        ]
    },
    {
        "code": "FI1BBDV75", 
        "name": "Data Visualisation", 
        "type": "Core Course", 
        "credits": 7.5, 
        "semester": "2025 Fall",
        "weeks": 5,
        "hours": 210,
        "description": "Learn visualization and graphing techniques to represent data using graphical illustrations. Create intuitive graphs for professional settings and presentations.",
        "knowledge": [
            "Concepts, processes and tools for creating data visualizations",
            "Selecting correct visualization for problem domains",
            "Design principles for effective data visualizations",
            "User experience techniques for accessible visualizations"
        ],
        "skills": [
            "Select data subsets for visualization",
            "Communicate to non-technical audiences",
            "Master tools and techniques to visualize data",
            "Create slideshow presentations",
            "Identify problem areas and provide insights"
        ],
        "competence": [
            "Understand ethical requirements for data visualizations",
            "Develop ethical attitude in presentations and publications",
            "Apply visualization techniques based on audience",
            "Develop work methods to create graphics for clients"
        ]
    },
    {
        "code": "FI1BBAR05", 
        "name": "Analysis Reporting", 
        "type": "Core Course", 
        "credits": 5, 
        "semester": "2025 Fall",
        "weeks": 3,
        "hours": 126,
        "description": "Learn conclusive report writing methodologies to communicate results clearly and concisely. Cover technical vs non-technical reporting.",
        "knowledge": [
            "Report structure and organization",
            "Executive summaries writing",
            "Technical vs non-technical reporting",
            "Data documentation best practices",
            "Presenting findings to stakeholders"
        ],
        "skills": [
            "Write clear, concise analysis reports",
            "Structure reports for different audiences",
            "Document data analysis professionally",
            "Present findings effectively"
        ],
        "competence": [
            "Communicate results to various stakeholders",
            "Develop professional documentation standards",
            "Deliver insights in accessible formats"
        ]
    },
    {
        "code": "FI1BBP275", 
        "name": "Exam Project 1", 
        "type": "Core Course", 
        "credits": 7.5, 
        "semester": "2025 Fall",
        "weeks": 6,
        "hours": 252,
        "description": "Complete a comprehensive exam project demonstrating first-year competencies in data analysis, visualization, and reporting.",
        "knowledge": [
            "End-to-end data analysis workflow",
            "Professional presentation standards",
            "Portfolio development",
            "Self-assessment and reflection"
        ],
        "skills": [
            "Execute comprehensive data analysis project",
            "Present findings professionally",
            "Document work for portfolio",
            "Receive and apply peer feedback"
        ],
        "competence": [
            "Demonstrate first-year learning outcomes",
            "Work independently on complex projects",
            "Deliver professional-quality deliverables"
        ]
    },
    {
        "code": "FI2BCDC75", 
        "name": "Databases and Cloud Services", 
        "type": "Core Course", 
        "credits": 7.5, 
        "semester": "2026 Spring",
        "weeks": 4,
        "hours": 168,
        "description": "Learn core concepts of databases, SQL language, and cloud-based data services. Cover ETL practices, data warehouses, and on-premises vs cloud databases.",
        "knowledge": [
            "Data warehouses and ETL (Extract, Transform, Load) practices",
            "Database components for building and maintaining databases",
            "SQL data language for interfacing with databases",
            "On-premises vs cloud-based database decision-making",
            "History and traditions of databases and cloud services"
        ],
        "skills": [
            "Use cloud-based native tools to interact with databases",
            "Determine between on-premises and cloud-based solutions",
            "Apply ETL practices to stage data into access layers",
            "Use SQL to create, read, update and delete data",
            "Find and refer to database documentation"
        ],
        "competence": [
            "Plan and carry out database-related tasks independently or in groups",
            "Develop effective methods for database solutions",
            "Work according to ethical requirements and principles"
        ]
    },
    {
        "code": "FI2BCPP10", 
        "name": "Programming Fundamentals", 
        "type": "Core Course", 
        "credits": 10, 
        "semester": "2026 Spring",
        "weeks": 6,
        "hours": 252,
        "description": "Introduction to programming using Python 3.x. Learn data types, operators, collections, objects, file I/O, libraries, and APIs. Use Jupyter Notebook for documentation.",
        "knowledge": [
            "Computational thinking to solve data analysis problems",
            "Processes and techniques in Python programming",
            "Tools to export code examples to Markdown",
            "Data access layers and APIs",
            "History of programming languages"
        ],
        "skills": [
            "Use control structures and objects for iterative solutions",
            "Use APIs to access databases from programs",
            "Integrate databases with programming environment",
            "Use programming syntax and interactive interpreter",
            "Use alternative text editing syntax in coded reports",
            "Find materials about programming to develop robust programs"
        ],
        "competence": [
            "Create well-documented programs to solve real-world problems",
            "Write fast, powerful scripts ethically",
            "Collaborate with other analysts and programmers"
        ]
    },
    {
        "code": "FI2BCPA05", 
        "name": "Programmatic Data Analysis", 
        "type": "Core Course", 
        "credits": 5, 
        "semester": "2026 Spring",
        "weeks": 3,
        "hours": 126,
        "description": "Apply programming skills to automate and enhance data analysis workflows. Use pandas, numpy, and create reproducible analysis pipelines.",
        "knowledge": [
            "Data manipulation with pandas library",
            "Data cleaning with code",
            "Automated data pipelines",
            "Statistical analysis with Python",
            "Reproducible analysis workflows",
            "Version control basics (Git)"
        ],
        "skills": [
            "Manipulate data programmatically",
            "Clean and transform data with code",
            "Automate repetitive analysis tasks",
            "Perform statistical analysis with Python"
        ],
        "competence": [
            "Create reproducible analysis workflows",
            "Develop efficient data processing methods",
            "Collaborate using version control"
        ]
    },
    {
        "code": "FI2BCP175", 
        "name": "Semester Project 2", 
        "type": "Core Course", 
        "credits": 7.5, 
        "semester": "2026 Spring",
        "weeks": 4,
        "hours": 168,
        "description": "Apply second-year skills including databases, programming, and programmatic analysis to a comprehensive technical project.",
        "knowledge": [
            "Advanced project management",
            "Technical implementation standards",
            "Code documentation practices",
            "Testing and validation methods"
        ],
        "skills": [
            "Execute technical data analysis project",
            "Use databases and programming together",
            "Document code professionally",
            "Test and validate results"
        ],
        "competence": [
            "Work on complex technical projects",
            "Deliver professional technical deliverables",
            "Collaborate in development teams"
        ]
    },
    {
        "code": "FI2BCIT75", 
        "name": "Industry Tools", 
        "type": "Core Course", 
        "credits": 7.5, 
        "semester": "2026 Fall",
        "weeks": 5,
        "hours": 210,
        "description": "Learn industry-standard tools used by professional data analysts including Business Intelligence tools, ETL processes, and data warehousing.",
        "knowledge": [
            "Business Intelligence tools",
            "ETL processes and tools",
            "Data warehousing concepts",
            "Reporting automation",
            "Industry-standard software",
            "Tool selection criteria"
        ],
        "skills": [
            "Use BI tools for data analysis",
            "Implement ETL processes",
            "Work with data warehouses",
            "Automate reporting tasks"
        ],
        "competence": [
            "Select appropriate tools for projects",
            "Apply industry best practices",
            "Develop efficient work methods"
        ]
    },
    {
        "code": "FI2BCCT05", 
        "name": "Critical Data Thinking", 
        "type": "Core Course", 
        "credits": 5, 
        "semester": "2026 Fall",
        "weeks": 4,
        "hours": 168,
        "description": "Develop critical thinking skills for evaluating data and analysis quality. Cover data quality, bias, source credibility, and ethical data practices.",
        "knowledge": [
            "Data quality assessment methods",
            "Bias identification and mitigation",
            "Source credibility evaluation",
            "Logical reasoning with data",
            "Common data fallacies",
            "GDPR and ethical data practices"
        ],
        "skills": [
            "Assess data quality critically",
            "Identify and address bias in data",
            "Evaluate source credibility",
            "Apply logical reasoning to analysis"
        ],
        "competence": [
            "Think critically about data and results",
            "Maintain ethical standards in analysis",
            "Question assumptions and validate findings"
        ]
    },
    {
        "code": "FI2BCBD05", 
        "name": "Big Data and Advanced Topics", 
        "type": "Core Course", 
        "credits": 5, 
        "semester": "2026 Fall",
        "weeks": 4,
        "hours": 168,
        "description": "Explore big data technologies and advanced analytical concepts including distributed computing, data lakes, and machine learning basics.",
        "knowledge": [
            "Big data concepts and characteristics (Volume, Velocity, Variety)",
            "Introduction to distributed computing",
            "Data lakes vs data warehouses",
            "Machine learning basics",
            "Advanced analytics overview",
            "Future trends in data analysis"
        ],
        "skills": [
            "Work with big data concepts",
            "Understand distributed systems basics",
            "Apply basic machine learning concepts",
            "Evaluate advanced analytics solutions"
        ],
        "competence": [
            "Assess when big data solutions are needed",
            "Stay current with industry trends",
            "Apply advanced concepts appropriately"
        ]
    },
    {
        "code": "FI2BCID05", 
        "name": "Interactive Dashboards", 
        "type": "Core Course", 
        "credits": 5, 
        "semester": "2026 Fall",
        "weeks": 3,
        "hours": 126,
        "description": "Create interactive dashboards for data exploration. Cover dashboard design, universal design principles, real-time data integration, and tools like Tableau/Power BI.",
        "knowledge": [
            "Dashboard theory and design principles",
            "Universal design for accessibility",
            "Interactive elements and filters",
            "Real-time data integration",
            "Dashboard tools (Tableau, Power BI)",
            "Performance optimization"
        ],
        "skills": [
            "Design effective dashboards",
            "Create interactive data visualizations",
            "Integrate real-time data sources",
            "Optimize dashboard performance"
        ],
        "competence": [
            "Develop dashboards for various audiences",
            "Apply universal design principles",
            "Create accessible interactive experiences"
        ]
    },
    {
        "code": "FI2BCP275", 
        "name": "Exam Project 2", 
        "type": "Core Course", 
        "credits": 7.5, 
        "semester": "2026 Fall",
        "weeks": 6,
        "hours": 126,
        "description": "Complete a final capstone project demonstrating all program competencies. Full data analysis lifecycle from problem identification to stakeholder presentation.",
        "knowledge": [
            "Full data analysis lifecycle",
            "Professional documentation standards",
            "Stakeholder presentation techniques",
            "Portfolio finalization",
            "Career preparation"
        ],
        "skills": [
            "Execute end-to-end data analysis project",
            "Apply all learned techniques",
            "Present to stakeholders professionally",
            "Build professional portfolio"
        ],
        "competence": [
            "Demonstrate program competencies",
            "Work independently on complex projects",
            "Prepare for industry employment"
        ]
    },
]

knowledge_outcomes = [
    "Concepts and theories used in data analysis",
    "Processes and tools used for data analysis",
    "Databases, cloud services and native cloud tools used in data analysis",
    "Programming and programmatic data analysis",
    "Processes and tools for data visualization",
    "Problem identification methodologies for problem solving and data error discovery",
    "Conclusive report writing methodologies for clear communication",
    "Real-world situations to guide decision-making in data analysis",
    "Industry-relevant tools used in field data analysis",
    "Essential concepts in data science and engineering related to Big Data",
    "Dashboard theory, universal design principles and interactive dashboards",
    "Regulations, data analysis lifecycle and quantitative vs qualitative data",
    "GDPR guidelines, data maintenance and critical data thinking",
    "History, traditions and distinctive nature of the data analysis discipline"
]

skills_outcomes = [
    "Apply knowledge of data model results to business problems",
    "Apply data collection and cleaning from various sources to secure storage",
    "Master relevant tools, techniques and material for data analysis and presentation",
    "Master tools and techniques to generate and visualise data through reports and infographics",
    "Apply knowledge of suitable data analysis use-cases to project problems",
    "Explain vocational choices of tools, methods and techniques for data analysis",
    "Reflect over own vocational practice and adjust under supervision",
    "Find information about data analysis techniques relevant to projects",
    "Study workplace environments and identify issues through data analysis",
    "Find and interact with data from large data sources and cloud-based systems",
    "Find applicable data models for data sets during project planning"
]

competence_outcomes = [
    "Understand the ethical principles for sourced, stored, and used data",
    "Develop an ethical attitude as a responsible data analyst",
    "Plan and carry out data analysis tasks according to GDPR principles and practices",
    "Exchange points of view with others in data analysis and discuss good practices",
    "Contribute to organisational quality assurance and optimisation through data analysis",
    "Contribute to solving practical problems through computational thinking techniques",
    "Contribute to data safety by considering security measures in each project phase",
    "Develop products of relevance to data analysis and optimize own work methods"
]

# Initialize session state
if 'completed_courses' not in st.session_state:
    st.session_state.completed_courses = []
if 'knowledge_progress' not in st.session_state:
    st.session_state.knowledge_progress = [False] * len(knowledge_outcomes)
if 'skills_progress' not in st.session_state:
    st.session_state.skills_progress = [False] * len(skills_outcomes)
if 'competence_progress' not in st.session_state:
    st.session_state.competence_progress = [False] * len(competence_outcomes)
if 'training_progress' not in st.session_state:
    st.session_state.training_progress = {}
if 'quiz_scores' not in st.session_state:
    st.session_state.quiz_scores = {}
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = 0
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
if 'show_exercise_answer' not in st.session_state:
    st.session_state.show_exercise_answer = {}

def generate_practice_question(course, question_type="general"):
    course_info = f"Course: {course['name']}\nDescription: {course['description']}\nKnowledge topics: {', '.join(course['knowledge'][:3])}\nSkills: {', '.join(course['skills'][:3])}"
    
    prompts = {
        "general": f"Generate one practice question for this data analysis course:\n{course_info}\n\nFormat: Start with the question, then on a new line write 'ANSWER:' followed by a clear answer (2-3 sentences). Make it practical and test real understanding.",
        "knowledge": f"Generate a knowledge-based question testing theoretical understanding:\n{course_info}\n\nFormat: Question first, then 'ANSWER:' on new line with explanation.",
        "skills": f"Generate a practical skills-based question:\n{course_info}\n\nFormat: Describe a scenario or task, then 'ANSWER:' with the expected approach or solution.",
        "case_study": f"Generate a mini case study question:\n{course_info}\n\nFormat: Present a brief business scenario (2-3 sentences), ask what the student should do, then 'ANSWER:' with the recommended approach."
    }
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an educational tutor for a Data Analyst vocational program. Generate clear, practical questions that test understanding of data analysis concepts."},
                {"role": "user", "content": prompts.get(question_type, prompts["general"])}
            ],
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating question: {str(e)}"

def evaluate_answer(question, correct_answer, user_answer):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a supportive educational tutor. Evaluate student answers and provide constructive feedback. Be encouraging but accurate."},
                {"role": "user", "content": f"Question: {question}\n\nCorrect answer concept: {correct_answer}\n\nStudent's answer: {user_answer}\n\nProvide brief feedback (2-3 sentences): Is the answer correct or partially correct? What did they get right? What could be improved?"}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error evaluating answer: {str(e)}"

st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Select page:",
    ["Overview", "Course Plan", "Training Center", "Playground", "Learn & Practice", "Progress", "Learning Outcomes", "About"]
)

if page == "Overview":
    st.title("🎓 Data Analyst 2 - Study App")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_credits = sum(c["credits"] for c in courses_data)
    completed_credits = sum(c["credits"] for c in courses_data if c["code"] in st.session_state.completed_courses)
    
    with col1:
        st.metric("Total Credits", f"{int(total_credits)}")
    with col2:
        st.metric("Completed", f"{completed_credits:.1f}")
    with col3:
        st.metric("Remaining", f"{total_credits - completed_credits:.1f}")
    with col4:
        progress_pct = (completed_credits / total_credits * 100) if total_credits > 0 else 0
        st.metric("Progress", f"{progress_pct:.0f}%")
    
    st.markdown("---")
    st.subheader("📅 Study Path")
    
    semesters = ["2025 Spring", "2025 Fall", "2026 Spring", "2026 Fall"]
    
    cols = st.columns(4)
    for i, sem in enumerate(semesters):
        with cols[i]:
            st.markdown(f"**{sem}**")
            sem_courses = [c for c in courses_data if c["semester"] == sem]
            sem_credits = sum(c["credits"] for c in sem_courses)
            st.caption(f"{sem_credits:.0f} credits")
            
            for course in sem_courses:
                is_completed = course["code"] in st.session_state.completed_courses
                status = "✅" if is_completed else "📚"
                st.markdown(f"{status} {course['name']}")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Training Progress")
        if st.session_state.training_progress:
            for topic, data in st.session_state.training_progress.items():
                short_topic = topic[:40] + "..." if len(topic) > 40 else topic
                lessons_done = data.get('lessons_completed', 0)
                total_lessons = len(training_modules.get(topic, {}).get('lessons', []))
                st.progress(lessons_done / total_lessons if total_lessons > 0 else 0)
                st.caption(f"{short_topic}: {lessons_done}/{total_lessons} lessons")
        else:
            st.info("Start training in the Training Center!")
    
    with col2:
        st.subheader("🔗 Useful Links")
        st.markdown("[📖 Study Catalog](https://studiekatalog.edutorium.no/voc/en/programme/PDAN/2025-autumn)")

elif page == "Training Center":
    st.title("🎓 Training Center")
    st.markdown("*Hands-on learning with step-by-step lessons, exercises, and quizzes*")
    st.markdown("---")
    
    # Topic selection
    available_topics = list(training_modules.keys())
    selected_topic = st.selectbox(
        "Choose a topic to learn:",
        options=available_topics,
        index=0
    )
    
    module = training_modules[selected_topic]
    
    st.markdown(f"**Course:** {module['course']}")
    st.markdown(f"*{module['description']}*")
    
    # Initialize progress for this topic
    if selected_topic not in st.session_state.training_progress:
        st.session_state.training_progress[selected_topic] = {
            'lessons_completed': 0,
            'exercises_completed': [],
            'quiz_score': None
        }
    
    progress = st.session_state.training_progress[selected_topic]
    
    # Progress bar
    total_items = len(module['lessons']) + len(module['exercises']) + 1  # +1 for quiz
    completed_items = progress['lessons_completed'] + len(progress['exercises_completed']) + (1 if progress['quiz_score'] is not None else 0)
    st.progress(completed_items / total_items)
    st.caption(f"Progress: {completed_items}/{total_items} items completed")
    
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["📖 Lessons", "✏️ Exercises", "📝 Quiz"])
    
    with tab1:
        st.subheader("Step-by-Step Lessons")
        
        for i, lesson in enumerate(module['lessons']):
            with st.expander(f"Lesson {i+1}: {lesson['title']}", expanded=(i == 0)):
                st.markdown(lesson['content'])
                
                st.markdown("---")
                st.markdown("**Key Takeaways:**")
                for point in lesson['key_points']:
                    st.markdown(f"✓ {point}")
                
                if st.button(f"Mark Lesson {i+1} Complete", key=f"lesson_{selected_topic}_{i}"):
                    if progress['lessons_completed'] <= i:
                        st.session_state.training_progress[selected_topic]['lessons_completed'] = i + 1
                        st.success(f"Lesson {i+1} completed!")
                        st.rerun()
                
                if progress['lessons_completed'] > i:
                    st.success("✅ Completed")
    
    with tab2:
        st.subheader("Hands-On Exercises")
        
        for i, exercise in enumerate(module['exercises']):
            with st.expander(f"Exercise {i+1}: {exercise['title']}", expanded=False):
                st.markdown(f"**Type:** {exercise['type'].title()}")
                st.markdown("---")
                st.markdown(f"**{exercise['question']}**")
                
                # Hint button
                if st.button(f"Show Hint", key=f"hint_{selected_topic}_{i}"):
                    st.info(f"💡 Hint: {exercise['hint']}")
                
                # User answer input
                user_answer = st.text_area(
                    "Your answer:",
                    key=f"exercise_answer_{selected_topic}_{i}",
                    placeholder="Type your answer here..."
                )
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("Check Answer", key=f"check_{selected_topic}_{i}"):
                        if user_answer.strip():
                            with st.spinner("Evaluating..."):
                                feedback = evaluate_answer(exercise['question'], exercise['answer'], user_answer)
                                st.success(feedback)
                                if i not in progress['exercises_completed']:
                                    st.session_state.training_progress[selected_topic]['exercises_completed'].append(i)
                        else:
                            st.warning("Please enter an answer first.")
                
                with col2:
                    show_key = f"show_{selected_topic}_{i}"
                    if st.button("Show Answer", key=f"reveal_{selected_topic}_{i}"):
                        st.session_state.show_exercise_answer[show_key] = True
                
                if st.session_state.show_exercise_answer.get(f"show_{selected_topic}_{i}", False):
                    st.info(f"**Answer:** {exercise['answer']}")
                
                if i in progress['exercises_completed']:
                    st.success("✅ Attempted")
    
    with tab3:
        st.subheader("Knowledge Quiz")
        st.markdown("Test your understanding with this quiz!")
        
        quiz = module['quiz']
        
        if progress['quiz_score'] is not None:
            st.success(f"Quiz completed! Score: {progress['quiz_score']}/{len(quiz)}")
            if st.button("Retake Quiz"):
                st.session_state.training_progress[selected_topic]['quiz_score'] = None
                st.session_state.quiz_answers = {}
                st.rerun()
        else:
            for i, q in enumerate(quiz):
                st.markdown(f"**Q{i+1}: {q['question']}**")
                answer = st.radio(
                    "Select your answer:",
                    options=q['options'],
                    key=f"quiz_{selected_topic}_{i}",
                    index=None
                )
                st.session_state.quiz_answers[f"{selected_topic}_{i}"] = q['options'].index(answer) if answer else None
                st.markdown("---")
            
            if st.button("Submit Quiz", type="primary"):
                score = 0
                for i, q in enumerate(quiz):
                    user_ans = st.session_state.quiz_answers.get(f"{selected_topic}_{i}")
                    if user_ans == q['correct']:
                        score += 1
                
                st.session_state.training_progress[selected_topic]['quiz_score'] = score
                st.success(f"Quiz completed! Score: {score}/{len(quiz)}")
                
                # Show explanations
                st.markdown("### Results:")
                for i, q in enumerate(quiz):
                    user_ans = st.session_state.quiz_answers.get(f"{selected_topic}_{i}")
                    correct = user_ans == q['correct']
                    icon = "✅" if correct else "❌"
                    st.markdown(f"{icon} **Q{i+1}:** {q['question']}")
                    if not correct:
                        st.markdown(f"   Correct answer: {q['options'][q['correct']]}")
                    st.markdown(f"   *{q['explanation']}*")

elif page == "Course Plan":
    st.title("📚 Course Plan")
    st.markdown("---")
    
    df = pd.DataFrame([{
        "Code": c["code"],
        "Course": c["name"],
        "Credits": c["credits"],
        "Weeks": c["weeks"],
        "Hours": c["hours"],
        "Semester": c["semester"]
    } for c in courses_data])
    
    col1, col2 = st.columns(2)
    with col1:
        semester_filter = st.multiselect(
            "Filter by semester:",
            options=["2025 Spring", "2025 Fall", "2026 Spring", "2026 Fall"],
            default=[]
        )
    with col2:
        search = st.text_input("Search courses:", "")
    
    filtered_df = df.copy()
    if semester_filter:
        filtered_df = filtered_df[filtered_df["Semester"].isin(semester_filter)]
    if search:
        filtered_df = filtered_df[
            filtered_df["Course"].str.lower().str.contains(search.lower()) |
            filtered_df["Code"].str.lower().str.contains(search.lower())
        ]
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.subheader("📊 Credits per Semester")
    
    semester_credits = df.groupby("Semester")["Credits"].sum().reset_index()
    semester_order = ["2025 Spring", "2025 Fall", "2026 Spring", "2026 Fall"]
    semester_credits["Semester"] = pd.Categorical(semester_credits["Semester"], categories=semester_order, ordered=True)
    semester_credits = semester_credits.sort_values("Semester")
    
    st.bar_chart(semester_credits.set_index("Semester"))

elif page == "Learn & Practice":
    st.title("📖 Learn & Practice")
    st.markdown("---")
    
    selected_course = st.selectbox(
        "Select a course to study:",
        options=[f"{c['code']} - {c['name']}" for c in courses_data],
        index=0
    )
    
    course_code = selected_course.split(" - ")[0]
    course = next(c for c in courses_data if c["code"] == course_code)
    
    st.markdown("---")
    
    # Check if this course has training modules
    course_topics_with_training = []
    for topic in training_modules.keys():
        if training_modules[topic]['course'] == course['name']:
            course_topics_with_training.append(topic)
    
    if course_topics_with_training:
        st.info(f"💡 This course has {len(course_topics_with_training)} topic(s) with hands-on training available in the Training Center!")
    
    tab1, tab2 = st.tabs(["Course Content", "Practice Questions"])
    
    with tab1:
        st.subheader(f"📚 {course['name']}")
        st.markdown(f"**{course['credits']} credits** | {course['weeks']} weeks | {course['hours']} hours | {course['semester']}")
        st.markdown(f"*{course['description']}*")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📖 Knowledge")
            st.markdown("*After this course, you will have knowledge of:*")
            for item in course['knowledge']:
                # Check if topic has training
                has_training = item in training_modules
                training_badge = " 🎓" if has_training else ""
                st.markdown(f"- {item}{training_badge}")
        
        with col2:
            st.markdown("### 🛠️ Skills")
            st.markdown("*After this course, you will be able to:*")
            for item in course['skills']:
                st.markdown(f"- {item}")
        
        st.markdown("---")
        st.markdown("### 💡 General Competence")
        st.markdown("*After this course, you will:*")
        for item in course['competence']:
            st.markdown(f"- {item}")
    
    with tab2:
        st.subheader("🎯 Practice Questions")
        
        question_type = st.selectbox(
            "Question type:",
            options=["General", "Knowledge-based", "Skills-based", "Case Study"],
            index=0
        )
        
        type_map = {"General": "general", "Knowledge-based": "knowledge", "Skills-based": "skills", "Case Study": "case_study"}
        
        if 'current_question' not in st.session_state:
            st.session_state.current_question = None
        if 'show_answer' not in st.session_state:
            st.session_state.show_answer = False
        if 'user_answer' not in st.session_state:
            st.session_state.user_answer = ""
        if 'feedback' not in st.session_state:
            st.session_state.feedback = None
        
        if st.button("Generate New Question", type="primary"):
            with st.spinner("Generating question..."):
                st.session_state.current_question = generate_practice_question(course, type_map[question_type])
                st.session_state.show_answer = False
                st.session_state.user_answer = ""
                st.session_state.feedback = None
        
        if st.session_state.current_question:
            st.markdown("---")
            
            if "ANSWER:" in st.session_state.current_question:
                parts = st.session_state.current_question.split("ANSWER:")
                question_text = parts[0].strip()
                answer_text = parts[1].strip() if len(parts) > 1 else ""
            else:
                question_text = st.session_state.current_question
                answer_text = "Answer not available"
            
            st.markdown("### Question:")
            st.markdown(f"**{question_text}**")
            
            user_answer = st.text_area(
                "Your answer:",
                value=st.session_state.user_answer,
                height=100,
                placeholder="Type your answer here..."
            )
            st.session_state.user_answer = user_answer
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Check My Answer"):
                    if user_answer.strip():
                        with st.spinner("Evaluating..."):
                            st.session_state.feedback = evaluate_answer(question_text, answer_text, user_answer)
                    else:
                        st.warning("Please enter an answer first.")
            
            with col2:
                if st.button("Show Answer"):
                    st.session_state.show_answer = True
            
            if st.session_state.feedback:
                st.markdown("### Feedback:")
                st.success(st.session_state.feedback)
            
            if st.session_state.show_answer:
                st.markdown("### Correct Answer:")
                st.info(answer_text)

elif page == "Progress":
    st.title("📈 My Progress")
    st.markdown("---")
    
    st.subheader("Mark Completed Courses")
    
    semesters = ["2025 Spring", "2025 Fall", "2026 Spring", "2026 Fall"]
    
    for sem in semesters:
        st.markdown(f"**{sem}**")
        sem_courses = [c for c in courses_data if c["semester"] == sem]
        
        cols = st.columns(2)
        for i, course in enumerate(sem_courses):
            with cols[i % 2]:
                is_checked = st.checkbox(
                    f"{course['name']} ({course['credits']} cr)",
                    value=course["code"] in st.session_state.completed_courses,
                    key=f"course_{course['code']}"
                )
                if is_checked and course["code"] not in st.session_state.completed_courses:
                    st.session_state.completed_courses.append(course["code"])
                elif not is_checked and course["code"] in st.session_state.completed_courses:
                    st.session_state.completed_courses.remove(course["code"])
        
        st.markdown("---")
    
    total_credits = sum(c["credits"] for c in courses_data)
    completed_credits = sum(c["credits"] for c in courses_data if c["code"] in st.session_state.completed_courses)
    progress = completed_credits / total_credits if total_credits > 0 else 0
    
    st.subheader("Summary")
    st.progress(progress)
    st.write(f"**{completed_credits:.1f} / {total_credits:.0f} credits completed ({progress*100:.0f}%)**")

elif page == "Learning Outcomes":
    st.title("🎯 Program Learning Outcomes")
    st.markdown("*Based on the Norwegian Qualifications Framework (NQF)*")
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["Knowledge", "Skills", "General Competence"])
    
    with tab1:
        st.subheader("📖 Knowledge")
        st.markdown("*After graduation, the candidate has knowledge of:*")
        
        for i, outcome in enumerate(knowledge_outcomes):
            checked = st.checkbox(
                outcome,
                value=st.session_state.knowledge_progress[i],
                key=f"knowledge_{i}"
            )
            st.session_state.knowledge_progress[i] = checked
        
        completed = sum(st.session_state.knowledge_progress)
        st.progress(completed / len(knowledge_outcomes))
        st.caption(f"{completed} / {len(knowledge_outcomes)} learning goals achieved")
    
    with tab2:
        st.subheader("🛠️ Skills")
        st.markdown("*After graduation, the candidate can:*")
        
        for i, outcome in enumerate(skills_outcomes):
            checked = st.checkbox(
                outcome,
                value=st.session_state.skills_progress[i],
                key=f"skills_{i}"
            )
            st.session_state.skills_progress[i] = checked
        
        completed = sum(st.session_state.skills_progress)
        st.progress(completed / len(skills_outcomes))
        st.caption(f"{completed} / {len(skills_outcomes)} learning goals achieved")
    
    with tab3:
        st.subheader("💡 General Competence")
        st.markdown("*After graduation, the candidate:*")
        
        for i, outcome in enumerate(competence_outcomes):
            checked = st.checkbox(
                outcome,
                value=st.session_state.competence_progress[i],
                key=f"competence_{i}"
            )
            st.session_state.competence_progress[i] = checked
        
        completed = sum(st.session_state.competence_progress)
        st.progress(completed / len(competence_outcomes))
        st.caption(f"{completed} / {len(competence_outcomes)} learning goals achieved")

elif page == "Playground":
    st.title("🎮 Interactive Playground")
    st.markdown("*Practice with real tools - enter data, run code, and see results instantly*")
    st.markdown("---")
    
    playground_tab = st.selectbox(
        "Choose a tool:",
        ["Python Code Runner", "Excel Formula Simulator", "SQL Query Tester", "Chart Builder"]
    )
    
    if playground_tab == "Python Code Runner":
        st.subheader("🐍 Python Code Playground")
        st.markdown("Practice pandas operations on your own data! Edit the tables below, then run exercises.")
        
        # Initialize session state for editable data
        if 'python_sales_data' not in st.session_state:
            st.session_state.python_sales_data = pd.DataFrame({
                'Product': ['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones'],
                'Price': [999, 699, 449, 299, 149],
                'Units_Sold': [150, 300, 200, 400, 500],
                'Region': ['North', 'South', 'North', 'East', 'West']
            })
        
        if 'python_employee_data' not in st.session_state:
            st.session_state.python_employee_data = pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
                'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT'],
                'Salary': [55000, 72000, 48000, 61000, 68000],
                'Years': [3, 5, 2, 7, 4]
            })
        
        st.markdown("### Your Datasets (Edit to add your own data!)")
        data_tab1, data_tab2 = st.tabs(["sales_data", "employee_data"])
        with data_tab1:
            st.caption("Click any cell to edit. Use the + button to add rows.")
            st.session_state.python_sales_data = st.data_editor(
                st.session_state.python_sales_data,
                num_rows="dynamic",
                use_container_width=True,
                key="python_sales_editor"
            )
        with data_tab2:
            st.caption("Click any cell to edit. Use the + button to add rows.")
            st.session_state.python_employee_data = st.data_editor(
                st.session_state.python_employee_data,
                num_rows="dynamic",
                use_container_width=True,
                key="python_employee_editor"
            )
        
        # Use the session state data
        sales_data = st.session_state.python_sales_data
        employee_data = st.session_state.python_employee_data
        
        st.markdown("### Select an Exercise")
        
        exercises = {
            "View DataFrame": {
                "code": "# View the sales data\nprint(sales_data)",
                "description": "Display the entire DataFrame"
            },
            "Add calculated column": {
                "code": "# Add a Revenue column\nsales_data['Revenue'] = sales_data['Price'] * sales_data['Units_Sold']\nprint(sales_data)",
                "description": "Create new columns from calculations"
            },
            "Basic statistics": {
                "code": "# Get summary statistics\nprint(sales_data.describe())\n\n# Specific calculations\nprint(f\"Total Revenue: ${(sales_data['Price'] * sales_data['Units_Sold']).sum():,}\")\nprint(f\"Average Price: ${sales_data['Price'].mean():.2f}\")",
                "description": "Calculate mean, sum, and other statistics"
            },
            "Filter data": {
                "code": "# Filter products with price over $300\nexpensive = sales_data[sales_data['Price'] > 300]\nprint(expensive)",
                "description": "Select rows based on conditions"
            },
            "Group By aggregation": {
                "code": "# Total units sold by region\nby_region = sales_data.groupby('Region')['Units_Sold'].sum()\nprint(by_region)",
                "description": "Aggregate data by categories"
            },
            "Sort data": {
                "code": "# Sort by price (highest first)\nsorted_data = sales_data.sort_values('Price', ascending=False)\nprint(sorted_data)",
                "description": "Order rows by column values"
            },
            "Employee analysis": {
                "code": "# Average salary by department\navg_salary = employee_data.groupby('Department')['Salary'].mean()\nprint(avg_salary)\n\n# Highest paid employee\ntop_earner = employee_data.loc[employee_data['Salary'].idxmax()]\nprint(f\"\\nHighest paid: {top_earner['Name']} (${top_earner['Salary']:,})\")",
                "description": "Practice with employee dataset"
            }
        }
        
        selected_exercise = st.selectbox("Choose exercise:", list(exercises.keys()))
        
        st.markdown(f"*{exercises[selected_exercise]['description']}*")
        
        st.markdown("### Code")
        st.code(exercises[selected_exercise]['code'], language="python")
        
        if st.button("▶️ Run Code", type="primary"):
            st.markdown("### Output:")
            
            # Execute the selected exercise safely with pre-defined data
            import io
            import sys as _sys
            
            old_stdout = _sys.stdout
            _sys.stdout = buffer = io.StringIO()
            
            try:
                # Create a copy of the data for this execution
                local_sales = sales_data.copy()
                local_employee = employee_data.copy()
                
                # Execute based on selected exercise
                if selected_exercise == "View DataFrame":
                    print(local_sales)
                elif selected_exercise == "Add calculated column":
                    local_sales['Revenue'] = local_sales['Price'] * local_sales['Units_Sold']
                    print(local_sales)
                elif selected_exercise == "Basic statistics":
                    print(local_sales.describe())
                    print(f"\nTotal Revenue: ${(local_sales['Price'] * local_sales['Units_Sold']).sum():,}")
                    print(f"Average Price: ${local_sales['Price'].mean():.2f}")
                elif selected_exercise == "Filter data":
                    expensive = local_sales[local_sales['Price'] > 300]
                    print(expensive)
                elif selected_exercise == "Group By aggregation":
                    by_region = local_sales.groupby('Region')['Units_Sold'].sum()
                    print(by_region)
                elif selected_exercise == "Sort data":
                    sorted_data = local_sales.sort_values('Price', ascending=False)
                    print(sorted_data)
                elif selected_exercise == "Employee analysis":
                    avg_salary = local_employee.groupby('Department')['Salary'].mean()
                    print(avg_salary)
                    top_earner = local_employee.loc[local_employee['Salary'].idxmax()]
                    print(f"\nHighest paid: {top_earner['Name']} (${top_earner['Salary']:,})")
                
                output = buffer.getvalue()
                _sys.stdout = old_stdout
                
                st.code(output, language="text")
                
                # Show resulting DataFrame if applicable
                if selected_exercise == "Add calculated column":
                    st.markdown("**Result DataFrame:**")
                    st.dataframe(local_sales, use_container_width=True)
                elif selected_exercise == "Filter data":
                    expensive = local_sales[local_sales['Price'] > 300]
                    st.dataframe(expensive, use_container_width=True)
                elif selected_exercise == "Sort data":
                    sorted_data = local_sales.sort_values('Price', ascending=False)
                    st.dataframe(sorted_data, use_container_width=True)
                    
            except Exception as e:
                _sys.stdout = old_stdout
                st.error(f"Error: {str(e)}")
        
        st.markdown("---")
        st.markdown("**Key pandas methods demonstrated:**")
        st.markdown("- `df.describe()` - Summary statistics")
        st.markdown("- `df.groupby()` - Group and aggregate")
        st.markdown("- `df.sort_values()` - Sort rows")
        st.markdown("- `df[condition]` - Filter rows")
    
    elif playground_tab == "Excel Formula Simulator":
        st.subheader("📊 Excel Formula Simulator")
        st.markdown("Enter data and apply formulas to see the results - just like in Excel!")
        
        st.markdown("### Sample Data")
        
        # Editable sample data
        if 'excel_data' not in st.session_state:
            st.session_state.excel_data = pd.DataFrame({
                'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
                'Region': ['North', 'South', 'North', 'East', 'West'],
                'Sales': [15000, 22000, 18000, 12000, 25000],
                'Target': [14000, 20000, 17000, 15000, 22000]
            })
        
        edited_data = st.data_editor(
            st.session_state.excel_data,
            num_rows="dynamic",
            use_container_width=True,
            key="excel_editor"
        )
        st.session_state.excel_data = edited_data
        
        st.markdown("### Apply Formulas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            formula_type = st.selectbox(
                "Choose a formula:",
                ["SUM", "AVERAGE", "COUNT", "MAX", "MIN", "SUMIF", "Custom Calculation"]
            )
        
        with col2:
            if formula_type in ["SUM", "AVERAGE", "COUNT", "MAX", "MIN"]:
                column = st.selectbox("Select column:", edited_data.select_dtypes(include=['number']).columns.tolist())
            elif formula_type == "SUMIF":
                column = st.selectbox("Sum column:", edited_data.select_dtypes(include=['number']).columns.tolist())
        
        if formula_type == "SUMIF":
            crit_col = st.selectbox("Criteria column:", edited_data.columns.tolist())
            criteria = st.text_input("Criteria (e.g., 'North'):", "North")
        
        if st.button("Calculate", type="primary"):
            st.markdown("### Result:")
            
            try:
                if formula_type == "SUM":
                    result = edited_data[column].sum()
                    st.success(f"=SUM({column}) = **{result:,.2f}**")
                    st.code(f"Excel: =SUM({column}2:{column}{len(edited_data)+1})")
                    
                elif formula_type == "AVERAGE":
                    result = edited_data[column].mean()
                    st.success(f"=AVERAGE({column}) = **{result:,.2f}**")
                    st.code(f"Excel: =AVERAGE({column}2:{column}{len(edited_data)+1})")
                    
                elif formula_type == "COUNT":
                    result = edited_data[column].count()
                    st.success(f"=COUNT({column}) = **{result}**")
                    st.code(f"Excel: =COUNT({column}2:{column}{len(edited_data)+1})")
                    
                elif formula_type == "MAX":
                    result = edited_data[column].max()
                    st.success(f"=MAX({column}) = **{result:,.2f}**")
                    st.code(f"Excel: =MAX({column}2:{column}{len(edited_data)+1})")
                    
                elif formula_type == "MIN":
                    result = edited_data[column].min()
                    st.success(f"=MIN({column}) = **{result:,.2f}**")
                    st.code(f"Excel: =MIN({column}2:{column}{len(edited_data)+1})")
                    
                elif formula_type == "SUMIF":
                    mask = edited_data[crit_col].astype(str).str.contains(criteria, case=False, na=False)
                    result = edited_data.loc[mask, column].sum()
                    st.success(f"=SUMIF({crit_col}, \"{criteria}\", {column}) = **{result:,.2f}**")
                    st.code(f"Excel: =SUMIF({crit_col}:{crit_col}, \"{criteria}\", {column}:{column})")
                    
                elif formula_type == "Custom Calculation":
                    st.info("Add a new calculated column below:")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        if formula_type == "Custom Calculation":
            st.markdown("### Add Calculated Column")
            new_col_name = st.text_input("New column name:", "Performance")
            
            calc_options = ["Sales - Target (Variance)", "Sales / Target (% of Target)", "Sales * 0.1 (Commission)"]
            calc_type = st.selectbox("Calculation:", calc_options)
            
            if st.button("Add Column"):
                if calc_type == "Sales - Target (Variance)":
                    edited_data[new_col_name] = edited_data['Sales'] - edited_data['Target']
                elif calc_type == "Sales / Target (% of Target)":
                    edited_data[new_col_name] = (edited_data['Sales'] / edited_data['Target'] * 100).round(1)
                elif calc_type == "Sales * 0.1 (Commission)":
                    edited_data[new_col_name] = edited_data['Sales'] * 0.1
                
                st.session_state.excel_data = edited_data
                st.success(f"Added column: {new_col_name}")
                st.rerun()
    
    elif playground_tab == "SQL Query Tester":
        st.subheader("🗄️ SQL Query Tester")
        st.markdown("Write SQL queries against sample data and see the results!")
        
        # Create sample tables
        customers = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown', 'Diana Ross', 'Eve Wilson'],
            'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
            'joined_date': ['2023-01-15', '2023-03-22', '2023-02-10', '2023-04-05', '2023-01-30']
        })
        
        orders = pd.DataFrame({
            'order_id': [101, 102, 103, 104, 105, 106, 107, 108],
            'customer_id': [1, 2, 1, 3, 4, 2, 5, 1],
            'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Watch', 'Headphones', 'Phone'],
            'amount': [999, 699, 449, 999, 699, 299, 149, 699],
            'order_date': ['2024-01-10', '2024-01-12', '2024-01-15', '2024-02-01', '2024-02-05', '2024-02-10', '2024-02-15', '2024-03-01']
        })
        
        st.markdown("### Available Tables")
        
        tab1, tab2 = st.tabs(["customers", "orders"])
        with tab1:
            st.dataframe(customers, use_container_width=True)
        with tab2:
            st.dataframe(orders, use_container_width=True)
        
        st.markdown("### Write Your Query")
        
        example_queries = {
            "Select all customers": "SELECT * FROM customers",
            "Orders over $500": "SELECT * FROM orders WHERE amount > 500",
            "Total sales by product": "SELECT product, SUM(amount) as total FROM orders GROUP BY product",
            "Join customers and orders": "SELECT c.name, o.product, o.amount FROM orders o JOIN customers c ON o.customer_id = c.id",
            "Top customers by spend": "SELECT c.name, SUM(o.amount) as total_spent FROM orders o JOIN customers c ON o.customer_id = c.id GROUP BY c.name ORDER BY total_spent DESC"
        }
        
        selected_example = st.selectbox("Try an example:", ["Custom Query"] + list(example_queries.keys()))
        
        if selected_example == "Custom Query":
            default_query = "SELECT * FROM customers"
        else:
            default_query = example_queries[selected_example]
        
        query = st.text_area("SQL Query:", value=default_query, height=100)
        
        if st.button("▶️ Run Query", type="primary"):
            st.markdown("### Results:")
            
            try:
                import sqlite3
                
                # Create in-memory database
                conn = sqlite3.connect(':memory:')
                customers.to_sql('customers', conn, index=False, if_exists='replace')
                orders.to_sql('orders', conn, index=False, if_exists='replace')
                
                # Execute query
                result = pd.read_sql_query(query, conn)
                
                st.dataframe(result, use_container_width=True)
                st.caption(f"Returned {len(result)} row(s)")
                
                conn.close()
                
            except Exception as e:
                st.error(f"Query Error: {str(e)}")
        
        st.markdown("---")
        st.markdown("**Practice Exercises:**")
        st.markdown("1. Find all orders from customer_id 1")
        st.markdown("2. Calculate average order amount")
        st.markdown("3. List customers who have placed more than 1 order")
    
    elif playground_tab == "Chart Builder":
        st.subheader("📈 Chart Builder")
        st.markdown("Create visualizations from your data!")
        
        # Sample data options
        data_source = st.radio("Choose data:", ["Sample Sales Data", "Enter Custom Data"], horizontal=True)
        
        if data_source == "Sample Sales Data":
            chart_data = pd.DataFrame({
                'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                'Revenue': [45000, 52000, 48000, 61000, 55000, 67000],
                'Expenses': [32000, 35000, 33000, 38000, 36000, 40000],
                'Customers': [120, 145, 138, 162, 155, 178]
            })
        else:
            st.markdown("Enter your data (comma-separated):")
            labels = st.text_input("Labels:", "Product A, Product B, Product C, Product D")
            values = st.text_input("Values:", "25, 40, 30, 35")
            
            try:
                label_list = [l.strip() for l in labels.split(',')]
                value_list = [float(v.strip()) for v in values.split(',')]
                chart_data = pd.DataFrame({
                    'Category': label_list,
                    'Value': value_list
                })
            except:
                st.warning("Please enter valid data")
                chart_data = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Value': [10, 20, 30]})
        
        st.markdown("### Your Data")
        st.dataframe(chart_data, use_container_width=True)
        
        st.markdown("### Choose Chart Type")
        
        col1, col2 = st.columns(2)
        
        with col1:
            chart_type = st.selectbox(
                "Chart type:",
                ["Bar Chart", "Line Chart", "Area Chart", "Scatter Plot"]
            )
        
        with col2:
            if data_source == "Sample Sales Data":
                y_column = st.selectbox("Y-axis value:", ["Revenue", "Expenses", "Customers"])
                x_column = "Month"
            else:
                y_column = "Value"
                x_column = "Category"
        
        st.markdown("### Your Chart")
        
        if chart_type == "Bar Chart":
            st.bar_chart(chart_data.set_index(x_column)[y_column])
        elif chart_type == "Line Chart":
            st.line_chart(chart_data.set_index(x_column)[y_column])
        elif chart_type == "Area Chart":
            st.area_chart(chart_data.set_index(x_column)[y_column])
        elif chart_type == "Scatter Plot":
            if data_source == "Sample Sales Data":
                import altair as alt
                scatter = alt.Chart(chart_data).mark_circle(size=100).encode(
                    x='Revenue',
                    y='Expenses',
                    tooltip=['Month', 'Revenue', 'Expenses']
                ).properties(width=600, height=400)
                st.altair_chart(scatter, use_container_width=True)
            else:
                st.bar_chart(chart_data.set_index(x_column)[y_column])
        
        st.markdown("---")
        st.markdown("**Chart Best Practices:**")
        st.markdown("- **Bar charts**: Best for comparing categories")
        st.markdown("- **Line charts**: Best for showing trends over time")
        st.markdown("- **Area charts**: Good for showing volume/cumulative data")
        st.markdown("- **Scatter plots**: Best for showing relationships between two variables")

elif page == "About":
    st.title("ℹ️ About the Data Analyst Program")
    st.markdown("---")
    
    st.markdown("""
    ## About the Programme
    
    Data analysts have a quintessential portfolio in every modern company ecology. Their ability to guide 
    business leaders to make informed decisions using relevant and up-to-date information 
    based on real-world data makes them a highly desired addition to every managerial team.
    
    **Effective data analysis can:**
    - Isolate workflow bottlenecks
    - Reduce operational costs
    - Solve overarching problems
    - Identify inefficient processes
    
    ---
    
    ## Programme Content
    
    This programme incorporates:
    - 📚 **Theoretical knowledge**
    - 🛠️ **Practical skills**
    - 💻 **Technical competency**
    
    ### Tools and Technologies:
    - Microsoft Excel and Google Spreadsheets
    - Python programming (Python 3.x)
    - SQL and databases (on-premises and cloud)
    - Data visualization and dashboards (Tableau, Power BI)
    - Statistical analysis tools
    - Business Intelligence concepts
    
    ---
    
    ## Career Opportunities
    
    After graduation, you may qualify for work as:
    - Financial Analyst
    - Marketing Analyst
    - Logistics Analyst
    - General Data Analyst
    - Technical Analyst
    - Information Scientist
    - Operational Management
    
    ---
    
    ## Study Details
    
    | Detail | Value |
    |--------|-------|
    | Programme Code | PDAN |
    | NQF Level | 5.2 |
    | Total Credits | 120 |
    | Duration | 2 years (4 semesters) |
    | Study Start | Spring 2025 |
    | Total Hours | 3150 |
    | Study Mode | Full-time / Part-time |
    
    ---
    
    📖 [View full study catalog](https://studiekatalog.edutorium.no/voc/en/programme/PDAN/2025-autumn)
    """)
