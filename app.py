import streamlit as st
import pandas as pd
from openai import OpenAI
import os
import json
import time
import re
from datetime import datetime, timedelta
try:
    from spellchecker import SpellChecker
    SPELLCHECK_AVAILABLE = True
except ImportError:
    SPELLCHECK_AVAILABLE = False

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
    },
    "Four Data Analysis Philosophies": {
        "course": "Data Driven Decision-Making",
        "description": "Master the four fundamental approaches to data analysis: Descriptive, Diagnostic, Predictive, and Prescriptive analytics.",
        "lessons": [
            {
                "title": "Overview: The Analytics Continuum",
                "content": """
**The Four Types of Data Analytics**

Data analysis follows a continuum from understanding the past to shaping the future:

```
DESCRIPTIVE → DIAGNOSTIC → PREDICTIVE → PRESCRIPTIVE
"What happened?" → "Why?" → "What will happen?" → "What should we do?"
```

**Value and Complexity:**
| Type | Question | Complexity | Business Value |
|------|----------|------------|----------------|
| Descriptive | What happened? | Low | Foundation |
| Diagnostic | Why did it happen? | Medium | Understanding |
| Predictive | What will happen? | High | Foresight |
| Prescriptive | What should we do? | Highest | Optimization |

**Real-World Example - Retail Store:**
1. **Descriptive**: "Sales dropped 15% last month"
2. **Diagnostic**: "Sales dropped because competitor opened nearby"
3. **Predictive**: "Sales will drop another 10% next quarter"
4. **Prescriptive**: "Launch loyalty program and price match campaign"

Each level builds on the previous, creating a complete analytical picture.
                """,
                "key_points": ["Four types form a continuum of increasing value", "Each answers a different question", "Most organizations start with descriptive and mature toward prescriptive"]
            },
            {
                "title": "Descriptive Analytics: What Happened?",
                "content": """
**Descriptive Analytics** summarizes historical data to understand what has occurred.

**Key Characteristics:**
- Looks at **past data** only
- Provides **summaries and aggregations**
- Answers: "What happened?" and "How many?"
- Foundation for all other analytics types

**Common Techniques:**
- Calculating averages, totals, percentages
- Creating dashboards and reports
- Trend analysis over time
- Data visualization (charts, graphs)

**Tools Used:**
- Excel/Google Sheets
- Power BI / Tableau
- SQL queries (SELECT, GROUP BY, SUM)

**Business Examples:**

| Industry | Descriptive Question | Output |
|----------|---------------------|--------|
| Retail | "What were total sales last quarter?" | $2.5M revenue |
| Healthcare | "How many patients visited in 2024?" | 45,000 patients |
| Marketing | "What was our email open rate?" | 22% open rate |
| HR | "What is our employee turnover?" | 15% annual turnover |

**Sample Dashboard Metrics:**
- Total Revenue: $2.5M
- Orders: 12,500
- Average Order Value: $200
- Top Product: Widget A (3,000 units)

**Limitations:**
Descriptive analytics tells you WHAT happened but not WHY or what to do about it.
                """,
                "key_points": ["Summarizes historical data", "Foundation of all analytics", "Uses dashboards, reports, and KPIs", "Cannot explain causes or predict future"]
            },
            {
                "title": "Diagnostic Analytics: Why Did It Happen?",
                "content": """
**Diagnostic Analytics** examines data to understand the causes behind outcomes.

**Key Characteristics:**
- Investigates **root causes**
- Uses drill-down and data mining
- Answers: "Why did this happen?"
- Requires deeper analysis skills

**Common Techniques:**
- **Drill-down analysis**: Breaking data into smaller segments
- **Correlation analysis**: Finding relationships between variables
- **Root cause analysis (RCA)**: Systematic problem investigation
- **Data discovery**: Exploring data for unexpected patterns

**The 5 Whys Technique:**
1. Sales dropped 15% → Why?
2. Fewer customers visited → Why?
3. Negative reviews increased → Why?
4. Wait times were too long → Why?
5. Staff shortage due to turnover → **ROOT CAUSE**

**Business Examples:**

| Descriptive Finding | Diagnostic Investigation | Root Cause |
|--------------------|-------------------------|------------|
| Sales dropped 15% | Analyze by region, product, time | New competitor opened |
| Website bounce rate up 20% | Check page load times, device types | Mobile site broken |
| Customer complaints doubled | Categorize complaint types | Shipping delays |
| Employee productivity down | Compare teams, projects, tools | Outdated software |

**Correlation Example:**
"We noticed sales spike when temperature exceeds 30°C. Correlation analysis shows r=0.85 between temperature and ice cream sales."

**Tools Used:**
- Excel Pivot Tables (drill-down)
- SQL (JOINs, subqueries)
- Statistical software
- BI tools with drill-through
                """,
                "key_points": ["Investigates root causes", "Uses drill-down and correlation", "5 Whys technique is powerful", "Correlation ≠ Causation"]
            },
            {
                "title": "Predictive Analytics: What Will Happen?",
                "content": """
**Predictive Analytics** uses historical data and statistical models to forecast future outcomes.

**Key Characteristics:**
- Uses **statistical models and machine learning**
- Provides **probabilities**, not certainties
- Answers: "What is likely to happen?"
- Requires historical data patterns

**Common Techniques:**
- **Regression analysis**: Predict numeric outcomes
- **Classification**: Predict categories (yes/no, high/medium/low)
- **Time series forecasting**: Predict trends over time
- **Machine learning models**: More complex predictions

**Business Examples:**

| Industry | Predictive Question | Model Type |
|----------|-------------------|------------|
| Retail | "What will next month's sales be?" | Time series forecast |
| Banking | "Will this customer default on loan?" | Classification (Yes/No) |
| Marketing | "Which customers will churn?" | Churn prediction model |
| Healthcare | "What's the patient readmission risk?" | Risk scoring |

**Example: Sales Forecasting**
```
Historical Data: Jan=100K, Feb=110K, Mar=105K, Apr=115K, May=120K
Model identifies: 3% monthly growth trend
Prediction: June = 124K, July = 128K, August = 132K
Confidence interval: ±8%
```

**Key Concepts:**
- **Training Data**: Historical data used to build the model
- **Features**: Variables used to make predictions
- **Accuracy**: How often predictions are correct
- **Confidence Interval**: Range of likely outcomes

**Important Limitations:**
- Predictions are probabilistic, not certain
- Models are only as good as historical data
- Unexpected events (black swans) break predictions
- "Past performance doesn't guarantee future results"
                """,
                "key_points": ["Forecasts future using historical patterns", "Provides probabilities not certainties", "Requires quality historical data", "Common: regression, classification, time series"]
            },
            {
                "title": "Prescriptive Analytics: What Should We Do?",
                "content": """
**Prescriptive Analytics** recommends specific actions to achieve desired outcomes.

**Key Characteristics:**
- **Recommends actions**, not just predictions
- Uses optimization and simulation
- Answers: "What is the best course of action?"
- Most advanced and valuable analytics type

**Common Techniques:**
- **Optimization algorithms**: Find the best solution
- **Simulation**: Test scenarios without real-world risk
- **Decision trees**: Map out action paths
- **A/B testing**: Compare action effectiveness
- **What-if analysis**: Explore different scenarios

**Business Examples:**

| Predictive Insight | Prescriptive Recommendation |
|-------------------|----------------------------|
| "30% churn risk for customers" | "Offer 20% discount to high-risk customers; expected to reduce churn by 15% and save $50K" |
| "Demand will spike 40% in December" | "Increase inventory by 35%, hire 10 temporary staff, extend operating hours" |
| "Campaign A outperforms B by 25%" | "Reallocate 80% of budget to Campaign A, expected ROI increase of $120K" |
| "Equipment failure likely in 2 weeks" | "Schedule preventive maintenance on Day 10, estimated cost savings of $25K" |

**Real-World Scenario:**
A delivery company uses prescriptive analytics:

1. **Descriptive**: "We made 10,000 deliveries last week"
2. **Diagnostic**: "Late deliveries were 30% higher in Zone C due to traffic"
3. **Predictive**: "Tomorrow Zone C will have 45% late deliveries"
4. **Prescriptive**: "Route trucks through Highway 5 instead of Main Street. Start Zone C deliveries 1 hour earlier. Deploy 2 additional drivers. **Expected result: Reduce late deliveries to 10%**"

**Tools Used:**
- Optimization software (solver tools)
- Simulation platforms
- Decision support systems
- AI/ML recommendation engines
                """,
                "key_points": ["Recommends specific actions", "Uses optimization and simulation", "Highest value but most complex", "Combines prediction with decision-making"]
            }
        ],
        "exercises": [
            {
                "title": "Classify the Analytics Type",
                "type": "scenario",
                "question": "Your manager says: 'We need to know why customer satisfaction scores dropped from 85% to 72% last quarter.' Which type of analytics is needed?",
                "answer": "This requires DIAGNOSTIC analytics. The question 'why did it drop?' indicates root cause investigation. You would drill down by customer segment, product line, service channel, and time period to identify what changed and caused the decline.",
                "hint": "Which question is being asked: What happened? Why? What will happen? What should we do?"
            },
            {
                "title": "Match Insights to Actions",
                "type": "practical",
                "question": "Your predictive model shows that 200 customers (worth $500K annual revenue) have 80% probability of churning next month. Recommend specific prescriptive actions.",
                "answer": "Prescriptive recommendations: 1) Segment the 200 customers by value - focus on top 50 (80/20 rule), 2) Assign account managers to personally call top 20 customers, 3) Offer tailored retention discounts (15-25% based on customer lifetime value), 4) Send personalized email campaign highlighting new features, 5) Create loyalty rewards for continued subscription. Expected outcome: Reduce churn to 30%, save ~$250K in revenue.",
                "hint": "Think about specific actions with measurable expected outcomes"
            },
            {
                "title": "Complete Analytics Journey",
                "type": "scenario",
                "question": "A coffee shop chain notices sales are declining. Walk through all four analytics types to address this problem.",
                "answer": "DESCRIPTIVE: 'Sales are down 20% over 3 months. Morning sales stable, afternoon sales down 35%.' DIAGNOSTIC: 'New competitor (bubble tea shop) opened nearby targeting afternoon customers. Weather data shows no correlation.' PREDICTIVE: 'If trend continues, afternoon sales will drop another 25% next quarter, totaling $50K lost revenue.' PRESCRIPTIVE: 'Launch afternoon happy hour (buy-one-get-one from 2-5pm), introduce 3 new iced drinks, partner with local businesses for afternoon delivery. Expected to recover 60% of lost afternoon sales within 2 months.'",
                "hint": "Address each of the four questions in sequence: What? Why? What next? What to do?"
            }
        ],
        "quiz": [
            {
                "question": "Which analytics type answers 'What should we do?'",
                "options": ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
                "correct": 3,
                "explanation": "Prescriptive analytics recommends specific actions to achieve desired outcomes. It goes beyond prediction to optimization."
            },
            {
                "question": "'Our website had 50,000 visitors last month, with 2% conversion rate' is an example of:",
                "options": ["Descriptive analytics", "Diagnostic analytics", "Predictive analytics", "Prescriptive analytics"],
                "correct": 0,
                "explanation": "This is descriptive analytics - it summarizes what happened (visitors, conversion rate) without explaining why or predicting future."
            },
            {
                "question": "Using drill-down analysis to find why sales dropped in a specific region is:",
                "options": ["Descriptive analytics", "Diagnostic analytics", "Predictive analytics", "Prescriptive analytics"],
                "correct": 1,
                "explanation": "Diagnostic analytics investigates root causes using techniques like drill-down analysis to understand WHY something happened."
            },
            {
                "question": "A model that forecasts '85% probability this customer will churn' is:",
                "options": ["Descriptive analytics", "Diagnostic analytics", "Predictive analytics", "Prescriptive analytics"],
                "correct": 2,
                "explanation": "Predictive analytics uses statistical models to forecast future outcomes with probabilities."
            },
            {
                "question": "Which analytics type is the foundation for all others?",
                "options": ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"],
                "correct": 0,
                "explanation": "Descriptive analytics is the foundation - you must understand what happened before analyzing why, predicting future, or recommending actions."
            }
        ]
    },
    "Data Analysis Lifecycle": {
        "course": "Data Driven Decision-Making",
        "description": "Learn the complete data analysis lifecycle from data collection to actionable insights and continuous improvement.",
        "lessons": [
            {
                "title": "Overview: The Data Lifecycle",
                "content": """
**The Data Analysis Lifecycle**

The data analysis lifecycle is a structured process that transforms raw data into actionable insights.

**The 6 Stages:**
```
1. DEFINE → 2. COLLECT → 3. CLEAN → 4. ANALYZE → 5. INTERPRET → 6. ACT
     ↑                                                              |
     └──────────────────── ITERATE ←────────────────────────────────┘
```

**Stage Overview:**

| Stage | Question | Output |
|-------|----------|--------|
| 1. Define | What problem are we solving? | Clear objectives, KPIs |
| 2. Collect | Where is the data? | Raw datasets |
| 3. Clean | Is the data reliable? | Clean, validated data |
| 4. Analyze | What patterns exist? | Statistical findings |
| 5. Interpret | What does it mean? | Insights and recommendations |
| 6. Act | What do we do? | Decisions and actions |

**Key Principle: ITERATION**
The lifecycle is not linear - you often need to go back to previous stages:
- Analysis reveals data quality issues → Return to Clean
- Interpretation raises new questions → Return to Define
- Actions create new data → Restart the cycle

**Time Distribution (Typical):**
- Define: 10%
- Collect: 15%
- **Clean: 40-60%** ← Most time-consuming!
- Analyze: 15%
- Interpret: 10%
- Act: 5%
                """,
                "key_points": ["6 stages from Define to Act", "Cleaning takes most time (40-60%)", "Process is iterative, not linear", "Each stage has clear outputs"]
            },
            {
                "title": "Stage 1: Define the Problem",
                "content": """
**Define: Setting Clear Objectives**

The most critical stage - a poorly defined problem leads to useless analysis.

**Key Activities:**
1. **Identify the business problem**
2. **Define success metrics (KPIs)**
3. **Scope the project** (what's in/out)
4. **Identify stakeholders**
5. **Set timeline and resources**

**SMART Goals Framework:**
- **S**pecific: "Reduce customer churn" → "Reduce monthly churn rate"
- **M**easurable: "Reduce from 5% to 3%"
- **A**chievable: Based on benchmarks and resources
- **R**elevant: Aligned with business strategy
- **T**ime-bound: "Within Q2 2025"

**Questions to Ask:**
| Category | Questions |
|----------|-----------|
| Problem | What exactly are we trying to solve? |
| Impact | Why does this matter? What's the cost of not solving it? |
| Success | How will we measure success? What KPIs? |
| Scope | What's included? What's explicitly excluded? |
| Data | What data do we need? Do we have access? |
| Timeline | When are results needed? |

**Example - Well-Defined Problem:**

❌ **Vague**: "We need to understand our customers better"

✅ **Well-defined**: "Identify the top 3 factors that predict customer churn for our subscription service, measured by monthly churn rate reduction from 5% to 3%, to be completed by end of Q2 with findings presented to the retention team."

**Output of Define Stage:**
- Problem statement document
- Success metrics and KPIs
- Project scope and timeline
- Data requirements list
                """,
                "key_points": ["Clear problem definition is critical", "Use SMART goals framework", "Define specific KPIs for success", "Document scope and constraints"]
            },
            {
                "title": "Stage 2: Collect Data",
                "content": """
**Collect: Gathering the Right Data**

Finding and acquiring data from various sources to answer your questions.

**Data Source Types:**

| Source Type | Examples | Pros | Cons |
|-------------|----------|------|------|
| **Internal** | CRM, ERP, databases | Trusted, accessible | May be incomplete |
| **External** | Government data, APIs | Broader context | Quality varies |
| **Primary** | Surveys, experiments | Tailored to needs | Time-consuming, costly |
| **Secondary** | Reports, research | Already analyzed | May not fit exactly |

**Common Data Collection Methods:**
1. **Database queries** (SQL)
2. **API connections** (automated data pulls)
3. **Web scraping** (public websites)
4. **Surveys/forms** (Google Forms, SurveyMonkey)
5. **Manual data entry** (observations, logs)
6. **File imports** (CSV, Excel from partners)

**Data Quality Considerations:**
When collecting, evaluate:
- **Completeness**: Are there missing values?
- **Accuracy**: Is the data correct?
- **Timeliness**: How recent is it?
- **Relevance**: Does it answer our questions?
- **Consistency**: Same format across sources?

**Ethical Considerations (GDPR):**
- ✅ Only collect data you need (data minimization)
- ✅ Get consent for personal data
- ✅ Document data sources and permissions
- ✅ Secure sensitive information
- ❌ Don't collect data "just in case"

**Example - Data Collection Plan:**

| Data Needed | Source | Method | Owner | Timeline |
|-------------|--------|--------|-------|----------|
| Customer info | CRM | SQL query | Data team | Day 1-2 |
| Transactions | ERP | API | IT | Day 2-3 |
| Satisfaction | Survey | Google Forms | Marketing | Day 3-7 |
| Industry benchmarks | External | Web research | Analyst | Day 5-7 |
                """,
                "key_points": ["Multiple source types: internal, external, primary, secondary", "Evaluate quality before using", "Follow GDPR and ethical guidelines", "Document sources and permissions"]
            },
            {
                "title": "Stage 3: Clean the Data",
                "content": """
**Clean: Ensuring Data Quality**

The most time-consuming stage - "garbage in, garbage out."

**Common Data Quality Issues:**

| Issue | Example | Solution |
|-------|---------|----------|
| Missing values | Empty cells | Delete, impute, or flag |
| Duplicates | Same record twice | Remove duplicates |
| Inconsistent formats | "USA", "U.S.A.", "United States" | Standardize |
| Typos | "Jonh" instead of "John" | Correct or fuzzy match |
| Outliers | Age = 200 | Investigate, cap, or remove |
| Wrong data types | Numbers stored as text | Convert types |
| Invalid values | Date = "32/13/2025" | Validate and correct |

**Data Cleaning Steps:**
1. **Explore** - Get overview of data structure and values
2. **Validate** - Check for invalid or impossible values
3. **Standardize** - Consistent formats, units, naming
4. **Deduplicate** - Remove repeated records
5. **Handle missing** - Delete, impute, or flag
6. **Handle outliers** - Investigate before removing
7. **Document** - Record all changes made

**Handling Missing Data:**

| Strategy | When to Use |
|----------|-------------|
| **Delete rows** | Few missing values, large dataset |
| **Delete columns** | >50% missing in column |
| **Impute with mean/median** | Numeric data, random missing |
| **Impute with mode** | Categorical data |
| **Flag as "Unknown"** | Missing has meaning |

**Tools for Data Cleaning:**
- Excel: Find/Replace, Remove Duplicates, TRIM(), CLEAN()
- Power Query: Transform steps, replace values
- Python: pandas library (dropna, fillna, replace)
- SQL: UPDATE, CASE WHEN, string functions

**Best Practice: Document Everything!**
```
Data Cleaning Log - Customer Data
- Removed 145 duplicate records (same email)
- Standardized country names (15 variations → 3)
- Imputed 23 missing ages with median (34)
- Flagged 5 outliers (age > 100) for review
- Converted phone numbers to E.164 format
```
                """,
                "key_points": ["Cleaning takes 40-60% of project time", "Common issues: missing, duplicates, inconsistencies", "Document all cleaning decisions", "Never assume data is clean"]
            },
            {
                "title": "Stages 4-6: Analyze, Interpret, Act",
                "content": """
**Stage 4: ANALYZE - Finding Patterns**

Apply statistical and analytical techniques to discover insights.

**Analysis Techniques:**
| Technique | Purpose | Example |
|-----------|---------|---------|
| Descriptive stats | Summarize data | Mean order value = $85 |
| Correlation | Find relationships | Temperature ↔ Sales |
| Regression | Predict outcomes | Price impact on demand |
| Segmentation | Group similar items | Customer clusters |
| Trend analysis | Track over time | Monthly growth rate |

**Key Questions:**
- What patterns emerge from the data?
- Are there unexpected findings?
- Do the numbers support or contradict our hypothesis?

---

**Stage 5: INTERPRET - Understanding Meaning**

Translate analytical findings into business insights.

**From Analysis to Insight:**
| Analysis Finding | Business Interpretation |
|-----------------|------------------------|
| "r = 0.85 between ads and sales" | "Ad spending strongly drives sales; $1 spent returns ~$3.40" |
| "Churn highest in month 3" | "Customers decide to stay/leave early; focus onboarding on first 90 days" |
| "Segment A has 3x LTV of Segment B" | "Prioritize acquiring more Segment A customers in marketing" |

**Avoiding Misinterpretation:**
- ❌ Correlation ≠ Causation
- ❌ Cherry-picking data that supports your view
- ❌ Ignoring confidence intervals
- ✅ Consider alternative explanations
- ✅ Validate with domain experts

---

**Stage 6: ACT - Taking Action**

Convert insights into decisions and monitor results.

**Action Planning:**
| Insight | Recommended Action | Owner | Timeline | Success Metric |
|---------|-------------------|-------|----------|----------------|
| 3-month churn spike | Redesign onboarding | Product | Q2 | -30% month-3 churn |
| Segment A high value | Target ads to lookalikes | Marketing | Q2 | +20% Segment A acquisition |

**After Acting:**
1. Monitor KPIs for impact
2. Compare actual vs. expected results
3. Document learnings
4. Start next iteration of the lifecycle
                """,
                "key_points": ["Analyze: Find patterns with statistics", "Interpret: Translate to business meaning", "Act: Make decisions and monitor", "Always iterate based on results"]
            }
        ],
        "exercises": [
            {
                "title": "Identify the Stage",
                "type": "scenario",
                "question": "You discover that 15% of your customer records have the country field as blank, while others have variations like 'USA', 'United States', and 'U.S.' What stage are you in and what should you do?",
                "answer": "You are in the CLEAN stage. Actions: 1) Standardize country variations to one format (e.g., all 'USA'), 2) For blank countries, decide whether to impute based on other fields (phone area code, city) or flag as 'Unknown', 3) Document these decisions in your cleaning log, 4) Consider adding validation rules to prevent this in future data collection.",
                "hint": "This involves data quality issues - which stage handles those?"
            },
            {
                "title": "Write a Problem Statement",
                "type": "practical",
                "question": "A retail manager says: 'Our online sales seem low.' Transform this into a well-defined problem statement with SMART goals.",
                "answer": "SMART Problem Statement: 'Identify the top 3 factors causing low online conversion rates (currently 1.2%, industry benchmark 2.5%) by analyzing website analytics, customer journey data, and competitor benchmarks. Success metric: Actionable recommendations that can increase conversion rate to 2.0% within 6 months. Timeline: Analysis complete within 4 weeks, presented to e-commerce team by [date].'",
                "hint": "Use the SMART framework: Specific, Measurable, Achievable, Relevant, Time-bound"
            },
            {
                "title": "Plan Data Collection",
                "type": "practical",
                "question": "You need to analyze why customer support calls have increased 40% this quarter. Create a data collection plan listing at least 4 data sources.",
                "answer": "Data Collection Plan: 1) INTERNAL - Support ticket system: Extract all tickets from this quarter vs. previous (categories, resolution time, customer info), 2) INTERNAL - CRM: Customer details, product ownership, account history, 3) INTERNAL - Product/Engineering: Recent releases, known bugs, feature changes, 4) PRIMARY - Customer survey: Post-call satisfaction survey with open-ended feedback, 5) EXTERNAL - Social media: Mentions and complaints on Twitter/Facebook for sentiment analysis. Method: SQL queries for internal data, survey tool for primary, social listening tool for external.",
                "hint": "Think about internal vs. external sources and what data would explain increased calls"
            }
        ],
        "quiz": [
            {
                "question": "Which stage typically takes the most time in the data analysis lifecycle?",
                "options": ["Define", "Collect", "Clean", "Analyze"],
                "correct": 2,
                "explanation": "Data cleaning typically takes 40-60% of project time. Real-world data is messy and requires significant effort to prepare for analysis."
            },
            {
                "question": "Which SMART criterion is missing? 'Increase sales next year'",
                "options": ["Specific", "Measurable", "Achievable", "All of the above"],
                "correct": 3,
                "explanation": "This goal is vague. It should be: Specific (which product line?), Measurable (by how much?), Achievable (based on what?), and more Time-bound (Q1? Q4?)."
            },
            {
                "question": "You find that 'correlation between ice cream sales and drowning deaths is 0.95.' The correct interpretation is:",
                "options": ["Ice cream causes drowning", "We should ban ice cream sales", "Both are likely caused by a third factor (summer heat)", "This is statistically impossible"],
                "correct": 2,
                "explanation": "Correlation does not imply causation. Both ice cream sales and drowning increase in summer due to hot weather - a confounding variable."
            },
            {
                "question": "When should you return to an earlier stage in the lifecycle?",
                "options": ["Never - the lifecycle is strictly linear", "Only if the project fails", "Whenever new information suggests it's needed", "Only at management request"],
                "correct": 2,
                "explanation": "The lifecycle is iterative. You might return to Clean if analysis reveals data issues, or to Define if interpretation raises new questions."
            }
        ]
    },
    "Data-Driven Case Studies": {
        "course": "Data Driven Decision-Making",
        "description": "Apply data-driven decision-making through real-world case studies with before-and-after scenarios.",
        "lessons": [
            {
                "title": "Case Study: Retail Inventory Optimization",
                "content": """
**Company: MegaMart Retail Chain**
**Problem: Stockouts and Overstock**

**Before (Data-Free Decision Making):**
- Store managers ordered inventory based on "gut feeling"
- Frequent stockouts of popular items (lost sales)
- Overstock of slow items (tied-up capital, markdowns)
- Annual loss: $2.5M in stockouts + $1.8M in excess inventory

**Data Analysis Approach:**

**1. DEFINE:**
"Optimize inventory levels to reduce stockouts by 50% and excess inventory by 40% within 12 months."

**2. COLLECT:**
- 3 years of sales data by product, store, date
- Supplier lead times
- Promotional calendars
- Weather data
- Local event schedules

**3. ANALYZE:**
| Finding | Insight |
|---------|---------|
| 80% of revenue from 15% of products | Focus on top SKUs first |
| Sales spike 300% during local events | Align inventory with event calendar |
| Rain increases umbrella sales 500% | Weather-based ordering |
| Lead time varies 2-14 days by supplier | Buffer stock for slow suppliers |

**4. PRESCRIPTIVE ACTION:**
- Implemented automated reorder points based on demand forecasting
- Created event-triggered ordering rules
- Integrated weather forecast into daily orders

**After (Data-Driven Results):**
| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Stockout rate | 12% | 4% | -67% |
| Excess inventory | $1.8M | $950K | -47% |
| Lost sales | $2.5M | $800K | -68% |
| Inventory turnover | 4x/year | 7x/year | +75% |

**Total Annual Savings: $2.55M**
                """,
                "key_points": ["Data replaced gut-feeling decisions", "Combined multiple data sources", "Automated decision-making with rules", "Measurable ROI from analytics"]
            },
            {
                "title": "Case Study: Healthcare Readmission Reduction",
                "content": """
**Organization: Regional Hospital Network**
**Problem: High 30-Day Readmission Rates**

**Before:**
- 30-day readmission rate: 22% (national target: 15%)
- Medicare penalties: $3.2M annually
- Readmissions cost average $15,000 each
- No systematic way to identify at-risk patients

**Data Analysis Approach:**

**1. DEFINE:**
"Identify patients at high risk of 30-day readmission and create targeted interventions to reduce rate from 22% to 15% within 18 months."

**2. COLLECT:**
- 5 years of patient records (anonymized)
- Diagnosis codes, procedures, medications
- Length of stay, discharge disposition
- Social factors (living alone, transport access)
- Prior admissions history

**3. ANALYZE - Key Predictors Found:**

| Risk Factor | Impact on Readmission |
|-------------|----------------------|
| 3+ admissions in past year | 4.2x higher risk |
| Lives alone, age 75+ | 2.8x higher risk |
| Discharged Friday afternoon | 1.9x higher risk |
| Heart failure + diabetes combo | 2.5x higher risk |
| No follow-up scheduled | 2.1x higher risk |

**4. PREDICTIVE MODEL:**
Created a risk score (0-100) calculated at admission:
- Score 0-30: Low risk (standard care)
- Score 31-60: Medium risk (phone follow-up)
- Score 61-100: High risk (intensive interventions)

**5. PRESCRIPTIVE ACTIONS:**
For high-risk patients:
- Discharge planning starts Day 1
- Social worker consultation
- Schedule follow-up before discharge
- Home health visit within 48 hours
- Medication reconciliation call

**After (Data-Driven Results):**
| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| 30-day readmission | 22% | 14.5% | -34% |
| Medicare penalties | $3.2M | $0 | -100% |
| Readmission costs | $8.2M | $5.1M | -38% |
| Patient satisfaction | 72% | 84% | +12pts |

**ROI:** Invested $800K in analytics program, saved $6.3M annually.
                """,
                "key_points": ["Predictive model identified at-risk patients", "Targeted interventions based on risk level", "Combined clinical and social data", "Massive ROI from prevented readmissions"]
            },
            {
                "title": "Case Study: Marketing Campaign Optimization",
                "content": """
**Company: E-Commerce Fashion Retailer**
**Problem: Inefficient Marketing Spend**

**Before:**
- Annual marketing budget: $5M
- Spent equally across all channels
- No attribution modeling
- Overall ROAS (Return on Ad Spend): 2.5x
- Many campaigns ran without performance tracking

**Data Analysis Approach:**

**1. DEFINE:**
"Optimize marketing spend allocation to achieve ROAS of 4.0x while maintaining revenue, using data-driven attribution."

**2. COLLECT:**
- All ad platform data (Google, Meta, TikTok)
- Website analytics (Google Analytics)
- Customer purchase history
- Email campaign performance
- Customer surveys (how did you hear about us?)

**3. ANALYZE - Channel Performance:**

| Channel | Spend | Revenue | ROAS | Customer Type |
|---------|-------|---------|------|---------------|
| Google Search | $1M | $4.5M | 4.5x | High intent |
| Meta Ads | $1.5M | $3M | 2.0x | Discovery |
| TikTok | $800K | $1.2M | 1.5x | Young demo |
| Email | $200K | $2.4M | 12x | Existing customers |
| Display | $1M | $1.5M | 1.5x | Brand awareness |
| Influencer | $500K | $800K | 1.6x | Mixed |

**Key Insights:**
- Email had highest ROAS but was underfunded
- Display ads often credited with conversions actually started by search
- TikTok reached new demographic not accessible elsewhere
- Influencer ROI varied wildly (2 out of 20 drove 80% of results)

**4. PRESCRIPTIVE RECOMMENDATIONS:**

| Channel | Before | After | Rationale |
|---------|--------|-------|-----------|
| Email | $200K | $600K | Highest ROAS, expand segments |
| Google Search | $1M | $1.5M | Proven high-intent performer |
| Meta | $1.5M | $1.2M | Focus on lookalike audiences only |
| Display | $1M | $400K | Reduce, use for retargeting only |
| TikTok | $800K | $800K | Maintain for new customer acquisition |
| Influencer | $500K | $500K | Focus on top 2 performers only |

**After (Data-Driven Results):**
| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Total Spend | $5M | $5M | Same |
| Total Revenue | $12.5M | $19.8M | +58% |
| ROAS | 2.5x | 3.96x | +58% |
| New customers | 45K | 52K | +16% |
| Email subscribers | 80K | 145K | +81% |
                """,
                "key_points": ["Attribution modeling revealed true channel value", "Reallocated budget without increasing total spend", "58% revenue increase with same budget", "Focused influencer spend on top performers"]
            }
        ],
        "exercises": [
            {
                "title": "Analyze the Case",
                "type": "scenario",
                "question": "In the MegaMart case, the team discovered that 80% of revenue came from 15% of products. What is this principle called, and how should it influence their analysis priority?",
                "answer": "This is the Pareto Principle (80/20 rule). Influence on analysis: 1) Focus demand forecasting efforts on the top 15% of SKUs first - errors here have the biggest impact, 2) These products should have tighter safety stock and more frequent reorder monitoring, 3) The remaining 85% of products can use simpler forecasting methods, 4) When presenting to stakeholders, lead with insights about top products.",
                "hint": "Think about the famous 80/20 principle and how to prioritize limited analytical resources"
            },
            {
                "title": "Calculate ROI",
                "type": "practical",
                "question": "The hospital case invested $800K in their analytics program. They saved $6.3M annually. Calculate: 1) Simple ROI, 2) Payback period in months, 3) 3-year total value.",
                "answer": "1) Simple ROI = (Savings - Investment) / Investment = ($6.3M - $0.8M) / $0.8M = 687.5% ROI in year 1. 2) Payback period = $800K / ($6.3M/12 months) = $800K / $525K per month = 1.52 months (about 6-7 weeks). 3) 3-year value = ($6.3M × 3) - $0.8M = $18.1M net value. Note: This assumes the $800K is a one-time investment; if there are annual operating costs, subtract those.",
                "hint": "ROI = (Gain - Cost) / Cost. Payback = Investment / Monthly Savings."
            },
            {
                "title": "Design Your Own Intervention",
                "type": "practical",
                "question": "A streaming service sees that 35% of free trial users cancel before converting to paid. Design a data-driven approach to reduce cancellations.",
                "answer": "DEFINE: 'Increase free trial to paid conversion from 65% to 80% within 6 months.' COLLECT: User behavior logs (features used, videos watched, engagement time), demographics, signup source, device type, time to first content. ANALYZE: Look for patterns - maybe users who watch 5+ shows convert at 90% vs 40% for those watching 1-2. PREDICTIVE: Build model to identify users at risk of not converting by Day 7. PRESCRIPTIVE: For at-risk users: personalized content recommendations, mid-trial email highlighting popular shows, offer extended trial or discounted first month, in-app tips highlighting premium features. Monitor conversion rate and adjust interventions.",
                "hint": "Follow the lifecycle: Define the goal with KPIs, collect relevant behavioral data, analyze patterns, then prescribe actions"
            }
        ],
        "quiz": [
            {
                "question": "In the MegaMart case, what was the total annual savings achieved?",
                "options": ["$1.8M", "$2.5M", "$2.55M", "$4.3M"],
                "correct": 2,
                "explanation": "Total savings = Reduced lost sales ($2.5M - $0.8M = $1.7M) + Reduced excess inventory ($1.8M - $0.95M = $0.85M) = $2.55M"
            },
            {
                "question": "The hospital's risk score model is an example of which analytics type?",
                "options": ["Descriptive", "Diagnostic", "Predictive", "All of the above"],
                "correct": 2,
                "explanation": "The risk score (0-100) predicts which patients are likely to be readmitted. This is predictive analytics - forecasting future outcomes based on current data."
            },
            {
                "question": "In the marketing case, which channel had the highest ROAS?",
                "options": ["Google Search", "Meta Ads", "Email", "TikTok"],
                "correct": 2,
                "explanation": "Email had ROAS of 12x ($200K spend → $2.4M revenue), far exceeding other channels. This insight led to tripling the email budget."
            },
            {
                "question": "What common theme appears across all three case studies?",
                "options": ["They all used AI/machine learning", "They all measured ROI and documented improvements", "They all focused on customer acquisition", "They all had unlimited budgets"],
                "correct": 1,
                "explanation": "All cases defined clear metrics, measured before/after results, and documented improvements with specific numbers. This proves the value of data-driven approaches."
            }
        ]
    },
    "KPI Selection and Tracking": {
        "course": "Data Driven Decision-Making",
        "description": "Learn to select appropriate KPIs, set targets, and create tracking systems to guide decision-making.",
        "lessons": [
            {
                "title": "Choosing the Right KPIs",
                "content": """
**What Makes a Good KPI?**

Not all metrics are KPIs. Key Performance Indicators are the vital few metrics that truly matter for success.

**The SMART Framework for KPIs:**

| Criterion | Question | Example |
|-----------|----------|---------|
| **S**pecific | What exactly are we measuring? | "Monthly active users" not "engagement" |
| **M**easurable | Can we quantify it? | Number, percentage, ratio |
| **A**chievable | Is the target realistic? | Based on benchmarks and capability |
| **R**elevant | Does it connect to goals? | Aligned with business strategy |
| **T**ime-bound | What's the timeframe? | Monthly, quarterly, annually |

**Types of KPIs:**

| Type | Purpose | Examples |
|------|---------|----------|
| **Lagging** | Measure outcomes (past) | Revenue, profit, customer count |
| **Leading** | Predict outcomes (future) | Pipeline value, website traffic, leads |
| **Input** | Resources invested | Marketing spend, hiring, training hours |
| **Process** | Efficiency of activities | Cycle time, defect rate, response time |
| **Output** | Results produced | Units sold, tickets resolved, content published |

**KPI Selection Process:**
1. Start with strategic objectives
2. Ask: "What would tell us if we're succeeding?"
3. Limit to 5-7 KPIs per area (avoid dashboard overload)
4. Ensure a mix of leading and lagging indicators
5. Verify data is available and reliable

**Common Mistakes:**
- ❌ Too many KPIs (vanity metrics)
- ❌ Only lagging indicators (no early warning)
- ❌ KPIs that can't be influenced
- ❌ No clear connection to strategy
- ✅ Focus on 5-7 metrics that drive decisions
                """,
                "key_points": ["KPIs are vital few metrics, not all metrics", "Use SMART framework", "Balance leading and lagging indicators", "Limit to 5-7 KPIs to stay focused"]
            },
            {
                "title": "KPIs by Business Function",
                "content": """
**Industry-Standard KPIs by Department**

**SALES KPIs:**
| KPI | Formula | Target Example |
|-----|---------|----------------|
| Revenue | Sum of all sales | $1M/month |
| Conversion Rate | Deals Won / Deals Created | 25% |
| Average Deal Size | Revenue / # Deals | $10,000 |
| Sales Cycle Length | Avg days from lead to close | 45 days |
| Pipeline Coverage | Pipeline Value / Quota | 3x |

**MARKETING KPIs:**
| KPI | Formula | Target Example |
|-----|---------|----------------|
| Customer Acquisition Cost (CAC) | Marketing Spend / New Customers | $50 |
| Return on Ad Spend (ROAS) | Revenue from Ads / Ad Spend | 4x |
| Website Conversion Rate | Conversions / Visitors | 3% |
| Email Open Rate | Opens / Emails Sent | 25% |
| Lead-to-Customer Rate | Customers / Leads | 10% |

**CUSTOMER SUCCESS KPIs:**
| KPI | Formula | Target Example |
|-----|---------|----------------|
| Customer Churn Rate | Lost Customers / Total Customers | <5%/month |
| Net Promoter Score (NPS) | % Promoters - % Detractors | >50 |
| Customer Lifetime Value (CLV) | Avg Revenue × Avg Lifespan | $500 |
| First Response Time | Avg time to first reply | <2 hours |
| Customer Satisfaction (CSAT) | Satisfied / Total Responses | >90% |

**OPERATIONS KPIs:**
| KPI | Formula | Target Example |
|-----|---------|----------------|
| On-Time Delivery Rate | On-time / Total Deliveries | >98% |
| Defect Rate | Defective Units / Total Units | <1% |
| Inventory Turnover | Cost of Goods Sold / Avg Inventory | 6x/year |
| Employee Productivity | Output / Employee Hours | Varies |
| Equipment Uptime | Operating Hours / Total Hours | >99% |

**Pro Tip:** The most valuable insight often comes from ratios and comparisons, not absolute numbers. "$1M revenue" means little without context like "vs. $800K last year" or "vs. $1.2M target."
                """,
                "key_points": ["Different functions have different KPIs", "Formulas make KPIs actionable", "Include targets for context", "Ratios and comparisons add meaning"]
            },
            {
                "title": "Building a KPI Dashboard",
                "content": """
**Creating Effective KPI Dashboards**

A dashboard should enable quick decisions, not just display numbers.

**Dashboard Design Principles:**

| Principle | Description |
|-----------|-------------|
| **5-second rule** | Key insight visible in 5 seconds |
| **Information hierarchy** | Most important KPIs at top |
| **Context always** | Show vs. target, vs. last period |
| **Actionable** | Each KPI links to a decision |
| **Real-time when needed** | Update frequency matches decision speed |

**Dashboard Layout Template:**
```
┌─────────────────────────────────────────────────────────────┐
│  EXECUTIVE DASHBOARD - [Month/Year]     [Last Updated: Now] │
├─────────────────────────────────────────────────────────────┤
│  [KPI Card 1]    [KPI Card 2]    [KPI Card 3]   [KPI Card 4]│
│   Revenue         New Users      Churn Rate     NPS Score   │
│   $1.2M ↑12%     5,240 ↑8%      3.2% ↓0.5%     72 ↑5       │
├─────────────────────────────────────────────────────────────┤
│                    [Main Trend Chart]                       │
│        Monthly Revenue Trend with Target Line               │
├─────────────────┬───────────────────────────────────────────┤
│ [Secondary      │  [Supporting Detail Table]                │
│  Chart 1]       │   Product    Revenue    Growth            │
│  Revenue by     │   Product A  $500K      +15%              │
│  Region         │   Product B  $400K      +8%               │
│                 │   Product C  $300K      -3%               │
└─────────────────┴───────────────────────────────────────────┘
```

**KPI Card Components:**
- Metric name
- Current value
- Comparison (↑↓ vs target or previous)
- Color coding (Green/Yellow/Red)
- Sparkline trend (optional)

**Effective Visualizations by KPI Type:**

| KPI Type | Best Visualization |
|----------|-------------------|
| Single metric | Big number card |
| Trend over time | Line chart |
| Part of whole | Pie/donut chart |
| Comparison | Bar chart |
| Geographic | Map |
| Progress to goal | Gauge / progress bar |
| Multiple dimensions | Table with conditional formatting |
                """,
                "key_points": ["5-second rule - key insight immediately visible", "Always show context (vs target, vs previous)", "Use color coding for status", "Match visualization to KPI type"]
            },
            {
                "title": "Setting Targets and Monitoring",
                "content": """
**Setting Meaningful KPI Targets**

A KPI without a target is just a number. Targets make KPIs actionable.

**Methods for Setting Targets:**

| Method | Description | When to Use |
|--------|-------------|-------------|
| **Historical** | Based on past performance | Stable, mature processes |
| **Benchmark** | Based on industry standards | New metrics, competitive pressure |
| **Aspirational** | Stretch goals beyond current | Growth mode, transformation |
| **Bottoms-up** | Calculated from team capacity | Resource-constrained |
| **Negotiated** | Agreed with stakeholders | Political environments |

**Target-Setting Formula (Historical + Growth):**
```
Target = Last Year's Actual × (1 + Growth Rate)

Example:
Last year revenue: $10M
Target growth: 20%
This year target: $10M × 1.20 = $12M
```

**RAG Status (Red/Amber/Green):**

| Status | Definition | Action |
|--------|------------|--------|
| 🟢 Green | On track (≥95% of target) | Continue current approach |
| 🟡 Amber | At risk (80-95% of target) | Investigate, adjust plans |
| 🔴 Red | Off track (<80% of target) | Immediate intervention required |

**Monitoring Cadence:**

| KPI Type | Review Frequency | Action Threshold |
|----------|-----------------|------------------|
| Strategic (Revenue, Customers) | Weekly/Monthly | Amber for 2+ weeks |
| Operational (Efficiency, Quality) | Daily/Weekly | Red for 1 day |
| Leading (Pipeline, Traffic) | Daily | Any negative trend |
| Lagging (NPS, Retention) | Monthly/Quarterly | Compare to target |

**KPI Review Meeting Agenda:**
1. **Current Status** - Dashboard walkthrough (5 min)
2. **Reds and Ambers** - What's off track? (10 min)
3. **Root Cause** - Why? (10 min)
4. **Action Items** - What are we doing about it? (10 min)
5. **Greens at Risk** - Early warnings? (5 min)

**Document Decisions:**
Every KPI review should end with:
- What we learned
- Decisions made
- Action items with owners and deadlines
                """,
                "key_points": ["Use multiple methods to set targets", "RAG status enables quick decisions", "Review frequency matches KPI type", "Document decisions and actions from reviews"]
            }
        ],
        "exercises": [
            {
                "title": "Select KPIs for a Scenario",
                "type": "practical",
                "question": "You're the new data analyst at a subscription meal kit company. The CEO wants to 'grow the business.' Select 5 KPIs you would recommend tracking and explain why.",
                "answer": "Recommended KPIs: 1) Monthly Recurring Revenue (MRR) - Primary growth indicator, directly measures business size. 2) Customer Acquisition Cost (CAC) - Ensures growth is sustainable and profitable. 3) Monthly Churn Rate - Critical for subscription businesses; growth is pointless if customers leave faster than they join. 4) Customer Lifetime Value (CLV) - Combined with CAC, shows if unit economics work (CLV should be 3x+ CAC). 5) Active Subscriber Count - Simple, easy to communicate growth metric. BONUS LEADING: Website conversion rate - Predicts future subscriber growth.",
                "hint": "Think about what metrics truly indicate a subscription business is growing sustainably"
            },
            {
                "title": "Calculate Target",
                "type": "practical",
                "question": "Last year's quarterly revenue was: Q1=$2M, Q2=$2.3M, Q3=$2.1M, Q4=$2.8M. Calculate the targets for next year if the goal is 25% annual growth, distributed proportionally by quarter.",
                "answer": "Step 1: Last year's total = $2M + $2.3M + $2.1M + $2.8M = $9.2M. Step 2: Next year's total with 25% growth = $9.2M × 1.25 = $11.5M. Step 3: Calculate each quarter's proportion of annual revenue: Q1=21.7%, Q2=25%, Q3=22.8%, Q4=30.4%. Step 4: Apply proportions to new total: Q1=$2.5M, Q2=$2.88M, Q3=$2.63M, Q4=$3.5M. These targets maintain the seasonal pattern (Q4 is peak) while achieving 25% growth.",
                "hint": "Calculate each quarter as a percentage of the year, then apply those percentages to the new annual target"
            },
            {
                "title": "Design a Dashboard",
                "type": "practical",
                "question": "An e-commerce manager wants a dashboard to monitor their holiday sales campaign (Nov-Dec). What KPIs would you include and how would you arrange them?",
                "answer": "Holiday Sales Dashboard: TOP ROW (Big Number Cards): 1) Daily Revenue vs Target (with ↑↓ and % of goal), 2) Conversion Rate (vs. campaign avg), 3) Average Order Value, 4) Cart Abandonment Rate. MIDDLE: Main line chart showing Daily Revenue with Target Line and Last Year comparison. Split into: LEFT - Revenue by Channel (pie or bar: Direct, Paid Search, Social, Email), RIGHT - Top Selling Products (table with stock status). BOTTOM: Hourly traffic heatmap to optimize staffing, and Promotional Code usage (which discounts are working). Update frequency: Real-time for revenue/traffic, hourly for others. Alert if daily revenue falls below 80% of target by 3pm.",
                "hint": "Think about what decisions need to be made during a high-stakes campaign period"
            }
        ],
        "quiz": [
            {
                "question": "Which of these is a LEADING indicator?",
                "options": ["Last month's revenue", "Customer satisfaction score", "Sales pipeline value", "Annual profit"],
                "correct": 2,
                "explanation": "Sales pipeline value is a leading indicator - it predicts future revenue. Revenue, satisfaction, and profit are lagging indicators that measure past outcomes."
            },
            {
                "question": "A KPI is at 87% of target. What RAG status should it show?",
                "options": ["Green - on track", "Amber - at risk", "Red - off track", "Depends on the KPI"],
                "correct": 1,
                "explanation": "87% falls in the Amber zone (80-95% of target), indicating the KPI is at risk and requires attention and possible plan adjustment."
            },
            {
                "question": "How many KPIs should each business function typically track?",
                "options": ["1-2", "5-7", "15-20", "As many as possible"],
                "correct": 1,
                "explanation": "Best practice is 5-7 KPIs per function. Too few miss important aspects; too many cause 'dashboard overload' and dilute focus."
            },
            {
                "question": "CLV/CAC ratio of 4:1 means:",
                "options": ["Company is losing money on each customer", "Each customer is worth 4× what it costs to acquire them", "4% of customers are profitable", "Acquisition takes 4 months"],
                "correct": 1,
                "explanation": "CLV/CAC of 4:1 means Customer Lifetime Value is 4× Customer Acquisition Cost. This is excellent - typically 3:1 or higher is considered healthy."
            },
            {
                "question": "For strategic KPIs like annual revenue, the typical review frequency is:",
                "options": ["Hourly", "Daily", "Weekly/Monthly", "Annually"],
                "correct": 2,
                "explanation": "Strategic KPIs are typically reviewed weekly or monthly. Daily is for operational metrics, and annual-only reviews don't allow time to course-correct."
            }
        ]
    },
    "Project Planning & Execution": {
        "course": "Semester Project 1",
        "description": "Learn to plan, scope, and execute data analysis projects from start to finish with professional standards.",
        "lessons": [
            {
                "title": "Defining Project Scope",
                "content": """
**Starting Your Data Analysis Project**

Every successful project begins with clear scope definition. Without it, projects fail or never end.

**Key Questions to Answer:**

| Question | Purpose |
|----------|---------|
| What problem are we solving? | Focus and direction |
| Who are the stakeholders? | Know your audience |
| What data do we need? | Resource planning |
| What are the deliverables? | Clear expectations |
| What's out of scope? | Prevent scope creep |
| When is it due? | Timeline planning |

**Project Scope Template:**
```
PROJECT: [Name]
PROBLEM STATEMENT: [1-2 sentences describing what you're solving]

OBJECTIVES:
1. [Specific goal 1]
2. [Specific goal 2]

IN SCOPE:
- [What's included]
- [Data sources to use]
- [Analysis methods]

OUT OF SCOPE:
- [What's NOT included]
- [Future phases]

DELIVERABLES:
- [ ] Data analysis report
- [ ] Cleaned dataset
- [ ] Visualization dashboard
- [ ] Presentation

TIMELINE: [Start] to [End]
STAKEHOLDERS: [Who needs to see results]
```

**Common Scope Mistakes:**
- ❌ "Analyze all the data" - Too vague
- ❌ No defined deliverables
- ❌ Unrealistic timeline
- ❌ Scope changes without documentation
- ✅ Specific, measurable objectives
- ✅ Clear list of what's IN and OUT
                """,
                "key_points": ["Define scope before starting work", "Use a scope template", "Document what's OUT of scope", "Get stakeholder agreement upfront"]
            },
            {
                "title": "Creating a Project Timeline",
                "content": """
**Building Your Project Schedule**

A timeline keeps you on track and helps manage stakeholder expectations.

**Data Analysis Project Phases:**

| Phase | % of Time | Activities |
|-------|-----------|------------|
| 1. Planning | 10% | Scope, data needs, approach |
| 2. Data Collection | 15% | Gather, access, import data |
| 3. Data Cleaning | 30-40% | Quality checks, standardization |
| 4. Analysis | 20% | Statistics, modeling, findings |
| 5. Documentation | 10% | Report writing, visualizations |
| 6. Presentation | 5% | Final delivery, Q&A |

**Sample 4-Week Project Timeline:**

```
WEEK 1: Foundation
├── Day 1-2: Define scope, identify data sources
├── Day 3-4: Collect and import data
└── Day 5: Initial data exploration

WEEK 2: Data Preparation
├── Day 1-2: Data cleaning and validation
├── Day 3-4: Continue cleaning, handle missing values
└── Day 5: Document data quality issues

WEEK 3: Analysis
├── Day 1-2: Perform main analysis
├── Day 3: Validate findings
├── Day 4-5: Create visualizations
└── Buffer day for unexpected issues

WEEK 4: Delivery
├── Day 1-2: Write report/documentation
├── Day 3: Create presentation
├── Day 4: Review and refine
└── Day 5: Final presentation
```

**Milestone Checkpoints:**
- ✅ Week 1: Data collected and accessible
- ✅ Week 2: Clean dataset ready for analysis
- ✅ Week 3: Key findings identified
- ✅ Week 4: Deliverables complete

**Buffer Time:**
Always add 20% buffer for unexpected issues:
- Data quality worse than expected
- New questions from stakeholders
- Technical problems
- Illness or other interruptions
                """,
                "key_points": ["Data cleaning takes most time (30-40%)", "Break project into weekly milestones", "Add 20% buffer for unexpected issues", "Track progress against timeline"]
            },
            {
                "title": "Managing Deliverables",
                "content": """
**Project Deliverables for Data Analysis**

Deliverables are the tangible outputs that prove your work is complete.

**Common Data Project Deliverables:**

| Deliverable | Purpose | Format |
|-------------|---------|--------|
| **Analysis Report** | Main findings and recommendations | PDF, Word doc |
| **Clean Dataset** | Prepared data for future use | CSV, Excel |
| **Dashboard** | Interactive visualization | Power BI, Tableau |
| **Presentation** | Summary for stakeholders | PowerPoint, Slides |
| **Code/Scripts** | Reproducible analysis | Python, SQL files |
| **Data Dictionary** | Explain data fields | Excel, PDF |

**Quality Checklist for Each Deliverable:**

**📊 Analysis Report:**
- [ ] Executive summary (1 page)
- [ ] Clear problem statement
- [ ] Methodology explained
- [ ] Key findings with evidence
- [ ] Visualizations to support points
- [ ] Recommendations with rationale
- [ ] Limitations and next steps
- [ ] Proofread for errors

**📁 Clean Dataset:**
- [ ] All values validated
- [ ] Consistent formatting
- [ ] Missing values handled
- [ ] Outliers addressed
- [ ] Column names clear
- [ ] Data dictionary included

**📈 Dashboard/Visualizations:**
- [ ] Clear titles and labels
- [ ] Appropriate chart types
- [ ] Consistent colors and fonts
- [ ] Interactive filters work
- [ ] Data source documented

**🎤 Presentation:**
- [ ] 10-15 slides maximum
- [ ] One key message per slide
- [ ] Visual-heavy, text-light
- [ ] Practiced timing (aim for 15-20 min)
- [ ] Prepared for Q&A
                """,
                "key_points": ["Define deliverables at project start", "Use checklists for quality", "Each deliverable serves a purpose", "Document everything for reproducibility"]
            },
            {
                "title": "Working Independently and in Teams",
                "content": """
**Project Execution: Solo and Team Work**

Data projects can be individual or collaborative - each requires different skills.

**Individual Project Best Practices:**

| Practice | Why It Matters |
|----------|---------------|
| **Daily progress log** | Track what you did, decisions made |
| **Version control** | Save versions (v1, v2, v3 or use Git) |
| **Regular breaks** | Avoid burnout, fresh eyes catch errors |
| **Self-review** | Check your own work before submission |
| **Ask for feedback** | Don't wait until the end |

**Sample Daily Log Entry:**
```
Date: 2025-02-15
Hours worked: 4

COMPLETED:
- Cleaned customer dataset (removed 145 duplicates)
- Created pivot table for sales by region
- Identified outlier in March data

BLOCKED:
- Need access to inventory data (emailed IT)

NEXT:
- Follow up on data access
- Start correlation analysis

DECISIONS MADE:
- Used median imputation for 23 missing ages
- Excluded records before 2023 (incomplete)
```

**Team Project Best Practices:**

| Practice | How to Do It |
|----------|-------------|
| **Clear role division** | Who does what (data, analysis, report) |
| **Regular check-ins** | Daily standup or weekly sync |
| **Shared workspace** | Cloud storage, shared drives |
| **Communication channel** | Slack, Teams, email thread |
| **Integration points** | When to merge work together |

**Team Role Examples:**
- **Data Lead**: Collection, cleaning, validation
- **Analysis Lead**: Statistics, modeling, insights
- **Visualization Lead**: Charts, dashboards
- **Documentation Lead**: Report, presentation

**Conflict Resolution:**
1. Discuss disagreements early, not at deadline
2. Focus on the project goal, not personal preferences
3. Use data to settle debates when possible
4. Escalate to mentor/supervisor if stuck
                """,
                "key_points": ["Keep a daily progress log", "Use version control for all files", "In teams: define clear roles", "Communicate early about problems"]
            }
        ],
        "exercises": [
            {
                "title": "Write a Scope Statement",
                "type": "practical",
                "question": "Your manager asks you to 'look into why sales are down.' Write a proper scope statement with objectives, in-scope, out-of-scope, and deliverables.",
                "answer": "PROJECT: Q1 2025 Sales Decline Analysis. PROBLEM: Identify root causes for 15% sales decline in Q1 2025 vs Q1 2024. OBJECTIVES: 1) Quantify decline by product category and region, 2) Identify top 3 contributing factors, 3) Recommend corrective actions. IN SCOPE: Sales data 2024-2025, customer feedback Q1 2025, competitor pricing data. OUT OF SCOPE: Marketing campaign effectiveness (separate project), international markets, product development recommendations. DELIVERABLES: Analysis report with findings and recommendations, executive presentation (10 slides), cleaned sales dataset. TIMELINE: 3 weeks. STAKEHOLDERS: Sales VP, Regional Managers.",
                "hint": "Transform the vague request into specific, measurable objectives with clear boundaries"
            },
            {
                "title": "Create a Project Timeline",
                "type": "practical",
                "question": "You have 2 weeks to analyze customer churn data and present findings. Create a day-by-day timeline with milestones.",
                "answer": "WEEK 1 - Data & Cleaning: Day 1: Define scope, success metrics, stakeholder alignment. Day 2: Collect customer data, subscription history, support tickets. Day 3-4: Data cleaning (expect 2 days - data quality usually worse than expected). Day 5: Exploratory analysis, initial patterns. MILESTONE: Clean dataset ready, initial insights documented. WEEK 2 - Analysis & Delivery: Day 1-2: Deep analysis (churn predictors, segment analysis, correlation). Day 3: Create visualizations, validate findings. Day 4: Write report, build presentation. Day 5: Review, practice presentation, buffer for refinements. MILESTONE: Final deliverables complete. BUFFER: Day 5 of each week reserved for overruns.",
                "hint": "Remember: cleaning takes 30-40% of time, always add buffer"
            },
            {
                "title": "Deliverable Checklist",
                "type": "scenario",
                "question": "You've finished your analysis and are about to submit. Your report shows that Product A has declining sales. What 5 things should you verify before submitting?",
                "answer": "Before submitting, verify: 1) DATA ACCURACY: Double-check the numbers - did you filter correctly? Are calculations right? Run the analysis again to confirm. 2) EVIDENCE: Does your visualization clearly show the decline? Are axes labeled correctly? Is the time period clear? 3) CONTEXT: Did you compare to benchmarks or previous periods? Is the decline significant or normal variation? 4) RECOMMENDATIONS: Are your suggestions actionable and tied to findings? 5) PROOFREADING: Check for typos, formatting issues, missing sections. Have someone else review if possible. BONUS: Check that your data source is documented so findings can be reproduced.",
                "hint": "Think about what would embarrass you if it were wrong in front of stakeholders"
            }
        ],
        "quiz": [
            {
                "question": "What percentage of a data project is typically spent on data cleaning?",
                "options": ["5-10%", "15-20%", "30-40%", "60-70%"],
                "correct": 2,
                "explanation": "Data cleaning typically takes 30-40% of project time. Real-world data is messy, and underestimating cleaning time is a common mistake."
            },
            {
                "question": "What is 'scope creep'?",
                "options": ["When the project finishes early", "When requirements keep expanding beyond original plan", "When team members leave", "When data is insufficient"],
                "correct": 1,
                "explanation": "Scope creep occurs when project requirements continuously expand beyond the original plan, often causing delays and budget overruns."
            },
            {
                "question": "Which deliverable provides explanations of data fields and their meanings?",
                "options": ["Executive Summary", "Data Dictionary", "Dashboard", "Analysis Report"],
                "correct": 1,
                "explanation": "A Data Dictionary documents what each field means, its data type, allowed values, and any transformations applied."
            },
            {
                "question": "When should you document decisions made during data cleaning?",
                "options": ["At the end of the project", "During the cleaning process", "Only if asked", "Never - it's not important"],
                "correct": 1,
                "explanation": "Document decisions as you make them. This ensures reproducibility, helps explain your methodology, and protects you if questions arise later."
            }
        ]
    },
    "Data Ethics & GDPR": {
        "course": "Semester Project 1",
        "description": "Understand ethical principles for data collection, storage, and use, including GDPR compliance.",
        "lessons": [
            {
                "title": "Why Data Ethics Matters",
                "content": """
**The Importance of Ethical Data Practice**

As a data analyst, you have access to sensitive information. With this access comes responsibility.

**Real-World Consequences of Poor Data Ethics:**

| Incident | What Happened | Consequence |
|----------|--------------|-------------|
| Cambridge Analytica | Used Facebook data without consent for political targeting | $5 billion fine, company dissolved |
| Equifax Breach | Poor security exposed 147 million people's data | $700 million settlement, reputation destroyed |
| Target Pregnancy | Predicted pregnancy from purchase data, exposed to family | Public backlash, privacy concerns |

**Core Ethical Principles:**

1. **Transparency**: Be honest about what data you collect and why
2. **Consent**: Get permission before collecting personal data
3. **Purpose Limitation**: Only use data for stated purposes
4. **Data Minimization**: Collect only what you need
5. **Accuracy**: Keep data correct and up-to-date
6. **Security**: Protect data from unauthorized access
7. **Accountability**: Take responsibility for data handling

**Questions to Ask Yourself:**
- Would I be comfortable if my data was used this way?
- Would this be acceptable if it became public?
- Am I respecting people's privacy and autonomy?
- Could this analysis harm individuals or groups?
- Is this use of data legal and compliant?

**The "Front Page Test":**
Before doing something with data, ask: "Would I be comfortable if this appeared on the front page of a newspaper?"
                """,
                "key_points": ["Data access comes with responsibility", "Poor ethics has real consequences", "Always consider the human impact", "Use the 'front page test'"]
            },
            {
                "title": "GDPR Fundamentals",
                "content": """
**Understanding GDPR (General Data Protection Regulation)**

GDPR is EU law that protects personal data. It applies to ANY organization handling EU residents' data.

**Key GDPR Principles:**

| Principle | Meaning | Your Action |
|-----------|---------|-------------|
| **Lawfulness** | Must have legal basis to process data | Document your legal basis |
| **Purpose Limitation** | Only use for specified purposes | State purpose before collecting |
| **Data Minimization** | Collect only what's necessary | Remove unnecessary fields |
| **Accuracy** | Data must be correct | Validate and update regularly |
| **Storage Limitation** | Don't keep longer than needed | Define retention periods |
| **Security** | Protect against unauthorized access | Encrypt, secure access |
| **Accountability** | Must prove compliance | Document everything |

**What is Personal Data?**
Any information relating to an identified or identifiable person:
- ✅ Name, email, phone number
- ✅ ID numbers (SSN, passport)
- ✅ Location data
- ✅ IP address
- ✅ Photos, videos
- ✅ Health, financial, genetic data (SPECIAL category - extra protection)

**Legal Bases for Processing:**
1. **Consent**: Person explicitly agrees
2. **Contract**: Necessary to fulfill a contract
3. **Legal Obligation**: Required by law
4. **Vital Interests**: To protect someone's life
5. **Public Task**: Official authority function
6. **Legitimate Interest**: Balanced business need (most complex)

**Individual Rights Under GDPR:**
- Right to be informed (what data, why, how long)
- Right of access (get copy of their data)
- Right to rectification (correct errors)
- Right to erasure ("right to be forgotten")
- Right to restrict processing
- Right to data portability
- Right to object
                """,
                "key_points": ["GDPR applies to EU resident data globally", "Need legal basis to process personal data", "Individuals have strong rights over their data", "Document your compliance"]
            },
            {
                "title": "Ethical Data Collection",
                "content": """
**Collecting Data the Right Way**

Before collecting any data, follow these guidelines:

**Before Collection Checklist:**
- [ ] Do I have a clear, specific purpose?
- [ ] Am I collecting only what I need? (minimization)
- [ ] Do I have legal basis/consent?
- [ ] Have I informed people about the collection?
- [ ] Is my collection method secure?
- [ ] Have I documented my approach?

**Sources and Their Ethical Considerations:**

| Source | Ethical Concerns | Best Practice |
|--------|-----------------|---------------|
| **Company databases** | Access rights, purpose limitation | Only access what you need for the task |
| **Surveys** | Informed consent, voluntary participation | Clear purpose statement, opt-out option |
| **Web scraping** | Terms of service, robots.txt | Check legality, respect restrictions |
| **Social media** | Public vs private, context collapse | Consider user expectations |
| **Third-party data** | Original consent, data quality | Verify source legitimacy and consent |
| **Public datasets** | Anonymization, re-identification risk | Check license and privacy safeguards |

**Informed Consent Essentials:**
When collecting directly from people:
1. Who you are (organization)
2. What data you're collecting
3. Why you need it (purpose)
4. How long you'll keep it
5. Who you'll share it with
6. Their rights (access, delete, etc.)
7. How to withdraw consent

**Red Flags - When to Stop and Ask:**
🚩 You don't have explicit permission
🚩 Data seems too personal for the purpose
🚩 You're not sure about the legal basis
🚩 The collection method feels sneaky
🚩 You can't explain why you need it
                """,
                "key_points": ["Always have a clear purpose before collecting", "Collect minimum necessary data", "Informed consent is essential", "When in doubt, stop and ask"]
            },
            {
                "title": "Handling Sensitive Data",
                "content": """
**Working with Sensitive Information**

Some data requires extra care due to potential for discrimination or harm.

**Special Category Data (GDPR):**
Requires explicit consent or special legal basis:
- Racial or ethnic origin
- Political opinions
- Religious beliefs
- Trade union membership
- Genetic data
- Biometric data
- Health data
- Sexual orientation

**Sensitive Data Best Practices:**

| Practice | How to Implement |
|----------|-----------------|
| **Anonymization** | Remove all identifying information |
| **Pseudonymization** | Replace IDs with codes (can be reversed with key) |
| **Encryption** | Encrypt data at rest and in transit |
| **Access Control** | Limit who can see sensitive fields |
| **Audit Logging** | Track who accessed what and when |
| **Secure Deletion** | Properly destroy when no longer needed |

**Anonymization Techniques:**
- **Data masking**: Replace with fake but realistic values
- **Generalization**: Use ranges instead of exact values (Age: 30-35)
- **Suppression**: Remove fields entirely
- **Noise addition**: Add random variation to values
- **Aggregation**: Only report group-level statistics

**Re-identification Risk:**
Even "anonymized" data can sometimes identify individuals:
- Netflix dataset + IMDB = identified users
- Zip code + birth date + gender = 87% of US uniquely identified

**Questions to Ask:**
- Can this data identify anyone if combined with other sources?
- Would individuals be surprised by this use of their data?
- Could this analysis enable discrimination?
- Is the minimum necessary data being used?
                """,
                "key_points": ["Special category data needs extra protection", "Anonymization is not always enough", "Consider re-identification risk", "Use encryption and access controls"]
            }
        ],
        "exercises": [
            {
                "title": "Identify Ethical Issues",
                "type": "scenario",
                "question": "Your company wants to analyze employee emails to predict which employees might quit. What ethical concerns should you raise?",
                "answer": "Ethical concerns: 1) PRIVACY: Employees may not know their emails are monitored for this purpose - lack of transparency. 2) CONSENT: Did employees consent to this specific use? Agreeing to email monitoring for security is different from predictive analysis. 3) DISCRIMINATION: Model might unfairly flag people based on protected characteristics (parental status, health discussions). 4) TRUST: Even if legal, this erodes employee trust and workplace culture. 5) PURPOSE LIMITATION: Email data collected for communication, not retention prediction. RECOMMENDATION: If proceeding, use voluntary surveys with clear consent, aggregate data only, and involve HR/legal. Consider the 'front page test' - how would this look publicly?",
                "hint": "Consider privacy, consent, potential for harm, and how employees would feel if they knew"
            },
            {
                "title": "GDPR Compliance Check",
                "type": "practical",
                "question": "You're building a customer survey for a European company. List 5 things you must include to comply with GDPR.",
                "answer": "GDPR compliance for survey: 1) IDENTITY: State who is collecting the data (company name and contact). 2) PURPOSE: Clearly explain why you're collecting responses and how they'll be used. 3) LEGAL BASIS: State your legal basis (likely consent for a survey). 4) RETENTION: Specify how long responses will be kept. 5) RIGHTS: Inform respondents of their rights (access, deletion, withdrawal). 6) CONSENT MECHANISM: Clear opt-in (no pre-ticked boxes), separate consent for different uses. 7) CONTACT: Provide way to contact data protection officer or make requests. 8) THIRD PARTIES: Disclose if data will be shared (analytics tools, etc.).",
                "hint": "Think about what individuals need to know to make an informed choice about participating"
            },
            {
                "title": "Anonymization Decision",
                "type": "scenario",
                "question": "You have customer data with: Name, Email, Age, City, Purchase History. You need to share analysis with a partner company. How would you anonymize it?",
                "answer": "Anonymization approach: 1) REMOVE: Name and Email (direct identifiers) - delete entirely. 2) GENERALIZE: Age → Age bands (18-25, 26-35, etc.) to prevent exact matching. City → Region level if small city populations. 3) AGGREGATE: Purchase history → Categories and totals, not individual transactions. 4) ASSESS: Can someone re-identify with remaining data? If city is small and age range narrow, might need to generalize further. 5) TEST: Try to identify yourself in the anonymized data - if you can, others might too. 6) DOCUMENT: Record what was removed/changed and why. Consider if pseudonymization (using a code that maps back) is sufficient instead, with the mapping kept secure.",
                "hint": "Consider both direct identifiers and combinations of fields that could identify someone"
            }
        ],
        "quiz": [
            {
                "question": "Which is NOT a GDPR principle?",
                "options": ["Data minimization", "Purpose limitation", "Maximum data collection", "Storage limitation"],
                "correct": 2,
                "explanation": "GDPR requires data MINIMIZATION - collecting only what's necessary. Maximum data collection is the opposite of what GDPR requires."
            },
            {
                "question": "Under GDPR, health data is classified as:",
                "options": ["Standard personal data", "Special category data requiring extra protection", "Public data", "Not regulated"],
                "correct": 1,
                "explanation": "Health data is 'special category data' under GDPR, requiring explicit consent and additional protections due to its sensitive nature."
            },
            {
                "question": "The 'right to be forgotten' means:",
                "options": ["Forgetting user passwords", "Individuals can request deletion of their data", "Companies can forget compliance", "Data expires automatically"],
                "correct": 1,
                "explanation": "Under GDPR, individuals have the right to request erasure of their personal data ('right to be forgotten') when certain conditions apply."
            },
            {
                "question": "Which technique replaces identifiers with codes that can be reversed with a key?",
                "options": ["Anonymization", "Pseudonymization", "Encryption", "Aggregation"],
                "correct": 1,
                "explanation": "Pseudonymization replaces identifiers with artificial identifiers (codes). Unlike anonymization, the link can be restored with the key, so it's still personal data under GDPR."
            }
        ]
    },
    "Documentation & Presentation": {
        "course": "Semester Project 1",
        "description": "Master professional documentation and presentation skills for data analysis projects.",
        "lessons": [
            {
                "title": "Writing the Analysis Report",
                "content": """
**Structure of a Professional Data Analysis Report**

Your report tells the story of your analysis and provides a record for future reference.

**Standard Report Structure:**

```
1. EXECUTIVE SUMMARY (1 page max)
   - Key findings in bullet points
   - Main recommendations
   - Bottom line impact

2. INTRODUCTION
   - Problem statement
   - Objectives
   - Scope and limitations

3. METHODOLOGY
   - Data sources
   - Cleaning steps taken
   - Analysis techniques used

4. FINDINGS
   - Results with visualizations
   - Key insights
   - Statistical evidence

5. RECOMMENDATIONS
   - Actions to take
   - Expected outcomes
   - Implementation considerations

6. APPENDIX
   - Technical details
   - Additional charts
   - Data dictionary
```

**Writing Tips:**

| Do | Don't |
|----|-------|
| Lead with the conclusion | Bury insights at the end |
| Use bullet points for lists | Write long paragraphs |
| Support claims with data | Make unsupported assertions |
| Explain technical terms | Assume reader expertise |
| Include visualizations | Use only text and tables |
| Acknowledge limitations | Overstate certainty |

**Executive Summary Formula:**
1. **Situation**: What was the problem/question?
2. **Findings**: What did we discover? (2-3 key points)
3. **Implications**: Why does it matter?
4. **Recommendations**: What should we do?

**Example Executive Summary:**
"This analysis investigated the 15% sales decline in Q1 2025. **Key findings:** (1) 80% of decline concentrated in the North region, (2) main driver was lost accounts to new competitor, (3) remaining customers are spending more per order. **Recommendation:** Launch targeted retention campaign in North region with estimated $200K recovery potential."
                """,
                "key_points": ["Lead with conclusions, not process", "Executive summary is most-read section", "Support every claim with evidence", "Keep it concise - respect reader's time"]
            },
            {
                "title": "Creating Effective Visualizations",
                "content": """
**Visualization Best Practices for Reports**

Charts should clarify, not confuse. Choose the right type for your message.

**Chart Selection Guide:**

| Message | Best Chart Type |
|---------|-----------------|
| Comparison across categories | Bar chart (horizontal for many categories) |
| Trend over time | Line chart |
| Part of whole | Pie chart (max 5-6 segments) or stacked bar |
| Relationship between variables | Scatter plot |
| Distribution | Histogram |
| Geographic data | Map |
| Multiple dimensions | Combo chart, small multiples |

**Visual Design Rules:**

**1. Declutter:**
- Remove gridlines or make very light
- Eliminate unnecessary borders
- Don't use 3D effects (ever!)
- Remove chart junk and decorations

**2. Focus Attention:**
- Highlight the key data point
- Use color purposefully (gray for context, color for focus)
- Add clear titles that state the insight

**3. Make It Readable:**
- Label axes clearly with units
- Font size minimum 10pt for print, 18pt for presentations
- Legend close to data (or label directly)
- Sort bars by value (usually largest to smallest)

**Title Examples:**

❌ **Bad**: "Sales by Region"
✅ **Good**: "North Region Sales Declined 20% While Others Grew"

❌ **Bad**: "Customer Satisfaction Survey Results"
✅ **Good**: "85% of Customers Rate Service 'Good' or 'Excellent'"

**Color Guidelines:**
- Use color consistently (same meaning throughout)
- Avoid red/green only (colorblind accessibility)
- Gray for context, 1-2 accent colors for key data
- Match company brand colors when appropriate
                """,
                "key_points": ["Choose chart type based on message", "Declutter ruthlessly", "Title should state the insight", "Use color with purpose"]
            },
            {
                "title": "Building Your Presentation",
                "content": """
**Presenting Data Findings to Stakeholders**

Your presentation is often the only thing stakeholders see. Make it count.

**Presentation Structure (15-20 minutes):**

```
1. OPENING (2 min)
   - The question we answered
   - Why it matters
   
2. KEY FINDINGS (8-10 min)
   - Finding 1 + supporting visual
   - Finding 2 + supporting visual
   - Finding 3 + supporting visual
   
3. RECOMMENDATIONS (3-4 min)
   - What should we do?
   - Expected impact
   
4. NEXT STEPS (2 min)
   - Immediate actions
   - Open questions for discussion
```

**Slide Design Rules:**

| Rule | Why |
|------|-----|
| One idea per slide | Prevents overwhelm |
| Maximum 5 bullet points | Easy to scan |
| Maximum 5 words per bullet | Prevents reading slides |
| Large font (24pt minimum) | Readability from back of room |
| High contrast | Visibility on projectors |
| Image/chart > text | Visual memory is stronger |

**Handling Data in Presentations:**

**❌ Don't:**
- Show complex tables with many rows
- Include all the data
- Use tiny fonts to fit everything
- Read numbers aloud from slides

**✅ Do:**
- Highlight key numbers in large font
- Round numbers (say "about 85%" not "84.7%")
- Use visuals to show patterns
- Provide detailed tables in appendix/handout

**Preparing for Q&A:**
1. Anticipate questions (especially "why?" and "how confident?")
2. Prepare backup slides with details
3. Know your data source and methodology
4. It's OK to say "I'll follow up on that"
5. Listen fully before answering
                """,
                "key_points": ["Structure: Opening, Findings, Recommendations, Next Steps", "One idea per slide", "Round numbers for speaking", "Prepare for likely questions"]
            },
            {
                "title": "The Reflection Report",
                "content": """
**Writing Your Individual Reflection**

A reflection report documents your learning journey and personal growth during the project.

**Purpose of Reflection:**
- Consolidate what you learned
- Identify areas for improvement
- Demonstrate critical thinking
- Build portfolio of experiences

**Reflection Structure:**

```
1. PROJECT OVERVIEW
   - Brief description of what you did
   - Your role and responsibilities

2. WHAT WENT WELL
   - Successful approaches
   - Skills you applied effectively
   - Challenges you overcame

3. WHAT COULD BE IMPROVED
   - Difficulties encountered
   - Mistakes made and lessons learned
   - What you would do differently

4. SKILLS DEVELOPED
   - Technical skills gained
   - Soft skills practiced
   - Knowledge areas expanded

5. FUTURE APPLICATION
   - How you'll apply learnings
   - Goals for continued development
```

**Reflection Prompts:**

| Area | Questions to Consider |
|------|----------------------|
| Process | What worked? What didn't? Why? |
| Technical | What new tools/techniques did you learn? |
| Collaboration | How did you work with others? |
| Time Management | Did you meet deadlines? Why/why not? |
| Problem-Solving | What unexpected issues arose? How did you handle them? |
| Growth | How have you improved from the start? |

**Writing Tips:**
- Be honest about challenges (this shows maturity)
- Give specific examples, not vague statements
- Connect learning to future goals
- Show self-awareness and critical thinking

**Example Excerpt:**
"I initially underestimated data cleaning time, allocating only 2 days when it ultimately took 5. This compressed my analysis phase and forced me to simplify my approach. In future projects, I'll add 50% buffer to cleaning estimates and do a quick data quality assessment before planning the timeline."
                """,
                "key_points": ["Reflection shows learning and maturity", "Be honest about challenges", "Give specific examples", "Connect to future improvement"]
            }
        ],
        "exercises": [
            {
                "title": "Write an Executive Summary",
                "type": "practical",
                "question": "Your analysis found: 1) Customer churn increased from 5% to 8% this quarter, 2) Main cause is price increase, 3) Competitor is offering 15% lower prices, 4) Loyal customers (2+ years) churned less. Write a 4-sentence executive summary.",
                "answer": "This analysis investigated the 60% increase in customer churn (5% to 8%) this quarter. Key findings: (1) Price-sensitive customers are leaving for a competitor offering 15% lower rates, while (2) long-term customers (2+ years) remain loyal with only 3% churn. The estimated revenue impact is $120K annually if trends continue. Recommendation: Implement tiered pricing with loyalty discounts for customers approaching the 2-year mark, and consider a targeted win-back campaign for recently churned price-sensitive segments.",
                "hint": "Follow: Situation → Findings → Implication → Recommendation"
            },
            {
                "title": "Fix the Slide",
                "type": "scenario",
                "question": "A slide has: Title 'Q1 Results', 12 bullet points of text in 10pt font, a complex table with 15 rows and 8 columns, and no visualization. What's wrong and how would you fix it?",
                "answer": "Problems: 1) Vague title that doesn't state insight, 2) Too many bullets (max 5), 3) Font too small (need 24pt+), 4) Complex table unreadable in presentation, 5) No visualization to tell the story. Fixes: 1) Retitle to the main finding: 'Q1 Revenue Up 12%, Driven by New Product Line', 2) Keep only 3-4 key bullet points, 3) Increase font to minimum 24pt, 4) Replace table with a bar or line chart showing the key comparison, 5) Move detailed table to appendix or handout, 6) Add one clear visualization that supports the title claim.",
                "hint": "Think about what someone can actually read and absorb during a presentation"
            },
            {
                "title": "Reflect on a Challenge",
                "type": "practical",
                "question": "Write a reflection paragraph about a time you struggled with messy data. Include: what happened, how you felt, what you did, and what you learned.",
                "answer": "Sample reflection: During my sales analysis project, I received customer data with over 40% missing values in key fields. Initially, I felt frustrated and considered asking for better data, which would have delayed the project by weeks. Instead, I researched imputation techniques and decided to use median imputation for numeric fields and 'Unknown' categories for text fields, documenting each decision. I learned that perfect data rarely exists in the real world, and developing strategies to work with imperfect data is a core analyst skill. I also learned to do a data quality assessment at the project start so I can plan appropriately. Going forward, I'll always request a sample of data before committing to timelines.",
                "hint": "Be specific about the situation, your response, and the concrete lesson learned"
            }
        ],
        "quiz": [
            {
                "question": "What should the first page of an analysis report typically be?",
                "options": ["Methodology", "Data sources", "Executive summary", "Table of contents"],
                "correct": 2,
                "explanation": "The executive summary should be first - it's the most-read section and gives busy stakeholders the key takeaways immediately."
            },
            {
                "question": "A good chart title should:",
                "options": ["Describe the chart type", "State the key insight", "List the data source", "Be as short as possible"],
                "correct": 1,
                "explanation": "A good chart title states the insight ('Sales Grew 20% in Q4') rather than just describing what the chart shows ('Quarterly Sales')."
            },
            {
                "question": "What is the maximum recommended number of bullet points per slide?",
                "options": ["3", "5", "8", "10"],
                "correct": 1,
                "explanation": "Maximum 5 bullet points per slide keeps content scannable. More than that overwhelms the audience."
            },
            {
                "question": "In a reflection report, you should:",
                "options": ["Only discuss successes", "Be honest about challenges and mistakes", "Blame external factors for problems", "Keep it as short as possible"],
                "correct": 1,
                "explanation": "Being honest about challenges and mistakes shows maturity and self-awareness. The goal is to demonstrate learning, not perfection."
            }
        ]
    },
    "Soft Skills for Data Analysts": {
        "course": "Semester Project 1",
        "description": "Develop essential soft skills for working effectively with stakeholders and team members.",
        "lessons": [
            {
                "title": "Communicating with Non-Technical Stakeholders",
                "content": """
**Translating Data Into Business Language**

Your analysis is only valuable if stakeholders understand and act on it.

**Common Communication Gaps:**

| Analyst Says | Stakeholder Hears |
|-------------|-------------------|
| "R-squared is 0.85" | "...what?" |
| "Statistically significant" | "Must be important" (not always true) |
| "Correlation of 0.7" | "Something about numbers" |
| "We need more data" | "They're stalling" |

**Translation Guide:**

| Technical Term | Plain Language |
|---------------|----------------|
| Correlation | "These things tend to move together" |
| Statistical significance | "This pattern is unlikely to be random chance" |
| Regression | "A formula to predict one thing from another" |
| Outlier | "An unusual value that doesn't fit the pattern" |
| Confidence interval | "We're 95% sure the true number is in this range" |
| P-value < 0.05 | "Less than 5% chance this is random luck" |

**The "So What?" Test:**
After every finding, ask yourself: "So what? Why should they care?"

❌ "Average order value increased by $12"
✅ "Average order value increased by $12, which means $2M additional annual revenue"

**Storytelling Framework:**
1. **Hook**: Start with the business problem
2. **Context**: What did we look at?
3. **Findings**: What did we discover?
4. **Impact**: What does it mean for the business?
5. **Action**: What should we do?

**Tips for Non-Technical Audiences:**
- Lead with the business impact, not the methodology
- Use analogies they understand
- Show, don't tell (visualizations > statistics)
- Avoid acronyms and jargon
- Check for understanding ("Does that make sense?")
                """,
                "key_points": ["Translate technical terms to plain language", "Always answer 'So what?' ", "Lead with business impact", "Use the storytelling framework"]
            },
            {
                "title": "Active Listening & Asking Questions",
                "content": """
**Understanding What Stakeholders Really Need**

Often what stakeholders ask for isn't what they actually need. Listening helps you find the real problem.

**Levels of Listening:**

| Level | Description | You're Doing This When... |
|-------|-------------|--------------------------|
| 1. Not listening | Waiting for your turn to speak | Formulating response while they talk |
| 2. Selective | Hearing only what you expect | Missing context and nuance |
| 3. Active | Fully focused, seeking to understand | Asking clarifying questions |
| 4. Empathic | Understanding feelings and perspective | Recognizing underlying concerns |

**Active Listening Techniques:**

1. **Paraphrase**: "So what I'm hearing is..."
2. **Clarify**: "When you say X, do you mean...?"
3. **Summarize**: "Let me make sure I understand..."
4. **Probe**: "Can you tell me more about...?"
5. **Reflect**: "It sounds like you're concerned about..."

**Powerful Questions to Ask:**

| Situation | Question |
|-----------|----------|
| Vague request | "What decision will this analysis support?" |
| Understanding goals | "What does success look like for this project?" |
| Finding constraints | "Are there any limitations I should know about?" |
| Clarifying priority | "If you could only know one thing, what would it be?" |
| Understanding context | "What have you already tried?" |
| Timeline | "When do you need this, and why that date?" |

**The "5 Whys" for Requirements:**
When someone asks for something, dig deeper:
- "I need sales data" → Why?
- "To see performance" → Why performance?
- "We're missing targets" → Why do you think?
- "Certain products are down" → Which ones? Why those?
- "New competitor in that segment" → So you need competitive analysis?

**Discovered Real Need**: Compare your products to competitor in that segment, not just "sales data"
                """,
                "key_points": ["Active listening finds the real problem", "Paraphrase to confirm understanding", "Ask 'why' to get to root needs", "What they ask for ≠ what they need"]
            },
            {
                "title": "Working with Different Roles",
                "content": """
**Collaborating Across Data and Business Teams**

Data analysts work with many different roles. Understanding their perspectives helps collaboration.

**Common Collaborators:**

| Role | Their Priority | What They Need From You |
|------|---------------|------------------------|
| **Executives** | Strategic decisions, ROI | High-level insights, recommendations |
| **Marketing** | Customer behavior, campaign performance | Segmentation, conversion metrics |
| **Sales** | Revenue, targets, forecasts | Pipeline analysis, trends |
| **Operations** | Efficiency, cost reduction | Process metrics, bottlenecks |
| **Product** | User experience, feature usage | Usage data, feedback analysis |
| **Finance** | Profitability, budgets | Cost analysis, forecasting |
| **IT/Engineering** | Data infrastructure, security | Data requirements, quality issues |

**Adapting Your Communication:**

**To Executives:**
- Bottom line first
- Focus on decisions, not details
- Quantify business impact
- 1-page max, with backup available

**To Technical Teams:**
- Can go deeper on methodology
- Discuss data quality openly
- Collaborate on implementation
- Share code/queries if helpful

**To Business Teams:**
- Focus on actionability
- Use their terminology
- Show how data supports their goals
- Be available for questions

**Building Relationships:**

1. **Understand their world**: Ask about their challenges and goals
2. **Speak their language**: Learn their terminology and metrics
3. **Be reliable**: Deliver on time, follow up promptly
4. **Educate gently**: Help them understand data without condescension
5. **Celebrate together**: Share wins as team achievements
6. **Accept feedback**: Be open to their domain expertise
                """,
                "key_points": ["Different roles have different priorities", "Adapt communication to audience", "Build relationships proactively", "Learn their terminology and goals"]
            },
            {
                "title": "Handling Feedback and Conflict",
                "content": """
**Receiving Feedback Professionally**

Feedback helps you grow. How you receive it matters as much as the feedback itself.

**Receiving Critical Feedback:**

| Step | Action |
|------|--------|
| 1. Listen | Let them finish without interrupting |
| 2. Clarify | Ask questions to understand fully |
| 3. Acknowledge | Thank them for the feedback |
| 4. Reflect | Consider it honestly before reacting |
| 5. Act | Make changes or explain your reasoning |

**What NOT to Do:**
- ❌ Get defensive ("But I...")
- ❌ Make excuses ("I didn't have time")
- ❌ Dismiss it ("They don't understand")
- ❌ Take it personally
- ❌ Argue immediately

**What TO Do:**
- ✅ "Thank you for pointing that out"
- ✅ "I hadn't considered that perspective"
- ✅ "Can you help me understand what you expected?"
- ✅ "I'll revisit that section and update it"

**Handling Disagreements:**

When someone disagrees with your analysis:

1. **Stay calm**: Take a breath, don't react emotionally
2. **Seek to understand**: "Can you tell me more about your concern?"
3. **Find common ground**: "We both want the best decision..."
4. **Use data**: Offer to investigate their hypothesis
5. **Know when to yield**: You might be wrong!
6. **Escalate thoughtfully**: If stuck, involve a neutral third party

**Common Conflict Scenarios:**

| Situation | Response |
|-----------|----------|
| "Your numbers are wrong" | "Let me verify the source and methodology" |
| "This isn't what I asked for" | "Help me understand what you were expecting" |
| "I don't believe this finding" | "What would convince you? Let me investigate" |
| "This analysis is useless" | "What would make it useful? Let's discuss" |

**Growth Mindset:**
Every piece of feedback is an opportunity to improve. Even harsh feedback usually contains some truth worth considering.
                """,
                "key_points": ["Listen fully before responding", "Thank people for feedback, even negative", "Stay calm in disagreements", "Use data to resolve conflicts"]
            }
        ],
        "exercises": [
            {
                "title": "Translate Technical to Plain Language",
                "type": "practical",
                "question": "Translate this to non-technical language: 'The regression analysis shows a statistically significant positive correlation (r=0.72, p<0.01) between marketing spend and customer acquisition.'",
                "answer": "Plain language: 'When we spend more on marketing, we get more customers - and this pattern is very consistent. For every $1 extra we spend on marketing, we typically gain [X] new customers. We're confident this is a real relationship, not just coincidence.' Note: Would be even better to add the actual business impact, e.g., 'Based on this, if we increased marketing budget by $50K, we'd expect to gain approximately 500 new customers.'",
                "hint": "Avoid statistical terms, focus on what it means for the business, and quantify the impact"
            },
            {
                "title": "Uncover the Real Need",
                "type": "scenario",
                "question": "A sales manager says: 'I need a report of all our customers sorted by revenue.' What questions would you ask to understand what they really need?",
                "answer": "Questions to ask: 1) 'What decision will this report help you make?' (Might reveal: identify at-risk accounts, find upsell opportunities, allocate account manager time). 2) 'What will you do with the top customers on this list?' (Reveals intended action). 3) 'Are you looking at a specific time period or trend?' (They might actually need trend data). 4) 'Should I include any other information like last contact date or satisfaction score?' (Might need a more complete view). 5) 'Is this a one-time analysis or something you'd need regularly?' (Informs automation). The real need might be: 'Help me identify my top 20 accounts at risk of churning so I can prioritize retention calls this week.'",
                "hint": "Focus on the decision they're trying to make and what action they'll take with the information"
            },
            {
                "title": "Handle Negative Feedback",
                "type": "scenario",
                "question": "Your stakeholder says: 'This analysis doesn't make sense. The conclusions don't match what we see on the ground.' How do you respond?",
                "answer": "Response approach: 1) STAY CALM - Don't get defensive. 2) ACKNOWLEDGE: 'I appreciate you sharing that concern. It's important that the analysis reflects reality.' 3) SEEK TO UNDERSTAND: 'Can you help me understand what you're seeing on the ground that doesn't match?' 4) COLLABORATE: 'Let's look at the data together - you might spot something I missed, or there might be context I need to understand.' 5) INVESTIGATE: 'Would it help if I checked [specific aspect they mention] to see if something was filtered incorrectly?' 6) COMMIT: 'I'll review the analysis with your feedback in mind and get back to you by [date].' Never say: 'You don't understand the data' or 'The numbers are correct, so you must be wrong.'",
                "hint": "Their ground-level experience is valuable data too - don't dismiss it"
            }
        ],
        "quiz": [
            {
                "question": "When a stakeholder asks for 'sales data,' you should:",
                "options": ["Send them the raw sales database", "Ask what decision they're trying to make", "Create every possible sales report", "Tell them to be more specific"],
                "correct": 1,
                "explanation": "Asking what decision they're trying to make helps uncover the real need. 'Sales data' could mean many things - understanding the purpose ensures you deliver what's actually useful."
            },
            {
                "question": "When translating 'statistically significant' for non-technical audiences, say:",
                "options": ["The p-value is below 0.05", "This is very important", "This pattern is unlikely to be random chance", "The correlation is strong"],
                "correct": 2,
                "explanation": "'Unlikely to be random chance' captures the meaning without jargon. 'Very important' is a common misunderstanding - statistical significance doesn't mean practical importance."
            },
            {
                "question": "When someone disagrees with your analysis, the first thing to do is:",
                "options": ["Defend your methodology", "Seek to understand their perspective", "Escalate to management", "Redo the entire analysis"],
                "correct": 1,
                "explanation": "First seek to understand their perspective - they may have valid information you don't have, or there may be a miscommunication you can resolve."
            },
            {
                "question": "Active listening involves:",
                "options": ["Waiting for your turn to speak", "Formulating your response while they talk", "Paraphrasing and asking clarifying questions", "Taking detailed notes"],
                "correct": 2,
                "explanation": "Active listening means fully focusing on understanding, demonstrated through paraphrasing ('So you're saying...') and asking clarifying questions."
            }
        ]
    },
    "KPIs & Decision Heuristics": {
        "course": "Evaluation of Outcomes",
        "description": "Learn to use Key Performance Indicators as heuristics for evaluating model outcomes and guiding decision-making.",
        "lessons": [
            {
                "title": "KPIs as Evaluation Heuristics",
                "content": """
**Using KPIs to Evaluate Model Outcomes**

KPIs serve as heuristics - mental shortcuts that help us quickly assess whether our analysis and models are performing well.

**What is a Heuristic?**
A heuristic is a practical rule of thumb that helps make decisions without analyzing every detail.

| Traditional Analysis | Heuristic Approach |
|---------------------|-------------------|
| Examine all metrics in detail | Focus on 3-5 key indicators |
| Time-consuming deep dives | Quick assessments |
| Risk of analysis paralysis | Faster decisions |
| Complete picture | "Good enough" picture |

**KPIs as Evaluation Heuristics:**

When evaluating model outcomes, KPIs help answer:
- Is the model working as expected?
- Are we achieving our objectives?
- Do we need to intervene?

**Example: Sales Forecasting Model**

| KPI Heuristic | Threshold | Action |
|---------------|-----------|--------|
| Forecast Error (MAPE) | < 10% = Good | > 15% = Investigate |
| Directional Accuracy | > 80% = Good | < 70% = Retrain model |
| Bias | ±5% = Acceptable | > 10% = Check data sources |

**Building Your KPI Dashboard:**

```
MODEL HEALTH DASHBOARD
─────────────────────────
✅ Accuracy: 92% (target: >85%)
⚠️  False Positives: 12% (target: <10%)
✅ Processing Time: 2.3s (target: <5s)
❌ Data Freshness: 48h (target: <24h)

Overall Status: ATTENTION NEEDED
Priority Action: Update data pipeline
```

**The 80/20 Rule for KPIs:**
Focus on the vital few metrics that indicate 80% of the outcomes:
- Don't track 50 metrics - track 5-7 that matter most
- Each KPI should drive a specific action
- If a KPI doesn't change decisions, remove it
                """,
                "key_points": ["KPIs are heuristics for quick assessment", "Focus on 5-7 key metrics", "Each KPI should drive an action", "Use thresholds to trigger interventions"]
            },
            {
                "title": "Selecting KPIs for Model Evaluation",
                "content": """
**Choosing the Right KPIs for Your Models**

Different models require different evaluation KPIs.

**Model Types and Their Primary KPIs:**

| Model Type | Primary KPIs | Why These Matter |
|------------|--------------|------------------|
| **Classification** | Accuracy, Precision, Recall, F1 | Balance of correct predictions |
| **Regression** | MAE, RMSE, R-squared, MAPE | Prediction error magnitude |
| **Clustering** | Silhouette Score, Inertia | Cluster quality |
| **Time Series** | MAPE, Directional Accuracy | Forecast reliability |
| **Recommendation** | Hit Rate, Coverage, Diversity | User satisfaction |

**Classification KPIs Explained:**

```
CONFUSION MATRIX
                 Predicted
                 Pos    Neg
Actual  Pos     [TP]   [FN]
        Neg     [FP]   [TN]

Accuracy = (TP + TN) / Total
Precision = TP / (TP + FP)  ← "Of predicted positives, how many correct?"
Recall = TP / (TP + FN)     ← "Of actual positives, how many found?"
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

**Which KPI to Prioritize?**

| Scenario | Priority KPI | Reasoning |
|----------|-------------|-----------|
| Medical diagnosis | Recall | Don't miss sick patients |
| Spam detection | Precision | Don't block legitimate emails |
| Fraud detection | F1 Score | Balance both errors |
| Customer churn | Recall | Catch at-risk customers |

**Regression KPIs Explained:**

```
MAE (Mean Absolute Error):
Average of |actual - predicted|
Interpretation: "On average, off by X units"

RMSE (Root Mean Square Error):
√(average of (actual - predicted)²)
Interpretation: Penalizes large errors more

MAPE (Mean Absolute Percentage Error):
Average of |actual - predicted| / actual × 100
Interpretation: "On average, off by X%"

R-squared:
1 - (Sum of squared errors / Total variance)
Interpretation: "Model explains X% of variance"
```

**Setting Realistic Targets:**
- Benchmark against industry standards
- Compare to baseline (naive) models
- Consider business impact of errors
                """,
                "key_points": ["Match KPIs to model type", "Prioritize based on business impact", "Understand precision vs recall tradeoff", "Set targets based on benchmarks"]
            },
            {
                "title": "KPI Thresholds and Alert Systems",
                "content": """
**Setting Thresholds and Automated Alerts**

Thresholds transform KPIs into actionable signals.

**Threshold Types:**

| Type | Example | Use Case |
|------|---------|----------|
| **Absolute** | Error rate < 5% | Fixed performance standard |
| **Relative** | 10% better than baseline | Improvement tracking |
| **Statistical** | ±2 standard deviations | Anomaly detection |
| **Time-based** | Same as last quarter | Trend maintenance |

**RAG Status System:**

```
🟢 GREEN: On target, no action needed
🟡 AMBER: At risk, monitor closely
🔴 RED: Off target, immediate action required

Example Thresholds:
┌─────────────────┬────────┬────────┬────────┐
│ KPI             │ Green  │ Amber  │ Red    │
├─────────────────┼────────┼────────┼────────┤
│ Accuracy        │ >90%   │ 80-90% │ <80%   │
│ Processing Time │ <2s    │ 2-5s   │ >5s    │
│ Data Freshness  │ <1hr   │ 1-4hr  │ >4hr   │
│ Error Rate      │ <2%    │ 2-5%   │ >5%    │
└─────────────────┴────────┴────────┴────────┘
```

**Alert Escalation Pyramid:**

```
         ┌─────────────┐
         │  CRITICAL   │ → Immediate escalation
         │   (Red)     │   Page on-call team
         ├─────────────┤
         │   WARNING   │ → Review within hours
         │  (Amber)    │   Email notification
         ├─────────────┤
         │    INFO     │ → Review in daily standup
         │  (Green)    │   Dashboard only
         └─────────────┘
```

**Avoiding Alert Fatigue:**

| Problem | Solution |
|---------|----------|
| Too many alerts | Prioritize by impact |
| False positives | Tune thresholds over time |
| Ignored alerts | Track response metrics |
| Duplicate alerts | Group related issues |

**Best Practices:**
1. Start with conservative thresholds, adjust over time
2. Every alert should have a clear response action
3. Review and refine thresholds quarterly
4. Include context in alerts (trend, comparison)
                """,
                "key_points": ["Use RAG status for quick assessment", "Every alert needs a response action", "Avoid alert fatigue with prioritization", "Review thresholds quarterly"]
            },
            {
                "title": "From KPIs to Decisions",
                "content": """
**Translating KPI Results into Business Decisions**

KPIs are only valuable if they drive decisions.

**Decision Framework:**

```
KPI RESULT → INTERPRETATION → OPTIONS → DECISION → ACTION
     ↓              ↓            ↓          ↓          ↓
  "What?"       "So what?"    "Now what?"  "Which?"   "How?"
```

**Example Decision Flow:**

| Stage | Example |
|-------|---------|
| **KPI Result** | Model accuracy dropped from 92% to 84% |
| **Interpretation** | 8% drop over 2 weeks, below 85% target |
| **Options** | 1) Retrain model 2) Check data quality 3) Accept degradation |
| **Decision** | Investigate data quality first (lowest cost) |
| **Action** | Run data validation checks by Friday |

**Decision Matrix for Model Issues:**

| Symptom | Possible Causes | First Action |
|---------|-----------------|--------------|
| Sudden accuracy drop | Data pipeline issue | Check data freshness/quality |
| Gradual accuracy decline | Concept drift | Evaluate retraining |
| High variance in predictions | Model instability | Review feature inputs |
| Consistent bias | Systematic error | Audit training data |

**Communicating Decisions:**

When presenting KPI-driven decisions:

1. **State the KPI**: "Customer churn prediction accuracy is at 78%"
2. **Provide context**: "Down from 85% last month, below our 80% threshold"
3. **Explain impact**: "We're missing 22% of at-risk customers"
4. **Propose action**: "Recommend retraining with Q4 data"
5. **Quantify benefit**: "Expected to recover 5% accuracy, saving ~$50K"

**Document Your Decisions:**
Keep a decision log linking KPIs to actions for:
- Learning from past decisions
- Justifying future investments
- Building institutional knowledge
                """,
                "key_points": ["KPIs must drive decisions, not just reports", "Use decision framework: What → So What → Now What", "Always quantify business impact", "Document decisions for future learning"]
            }
        ],
        "exercises": [
            {
                "title": "Design a KPI Dashboard",
                "type": "practical",
                "question": "You've built a customer churn prediction model. Design a KPI dashboard with 5 metrics, thresholds, and what action to take when each threshold is breached.",
                "answer": "Churn Model KPI Dashboard: 1) RECALL: Target >80%, Amber 70-80%, Red <70%. Action if Red: Review false negatives, possibly lower prediction threshold. 2) PRECISION: Target >60%, Amber 50-60%, Red <50%. Action if Red: Check for data quality issues causing false positives. 3) AUC-ROC: Target >0.75, Amber 0.65-0.75, Red <0.65. Action if Red: Retrain model with updated features. 4) PREDICTION TIMELINESS: Target <24hr before churn, Amber 24-48hr, Red >48hr. Action if Red: Increase scoring frequency. 5) INTERVENTION SUCCESS RATE: Target >30% saved, Amber 20-30%, Red <20%. Action if Red: Review intervention strategy, not just model.",
                "hint": "Include both model performance metrics and business outcome metrics"
            },
            {
                "title": "Interpret KPI Changes",
                "type": "scenario",
                "question": "Your sales forecast model shows: MAPE increased from 8% to 14%, but R-squared remained at 0.85. What does this combination tell you, and what should you investigate?",
                "answer": "Interpretation: MAPE measures average percentage error while R-squared measures explained variance. If R-squared stayed high but MAPE increased significantly, this suggests: 1) The model still captures the overall pattern (explains variance), 2) BUT individual predictions have larger errors (higher MAPE), 3) Likely cause: OUTLIERS or unusual data points are affecting predictions without distorting overall correlation. Investigation steps: 1) Check for outliers in recent data, 2) Look for specific segments with high errors, 3) Compare prediction errors by product/region/time, 4) Check if data distribution has shifted. This pattern often indicates concept drift in specific segments while overall relationships hold.",
                "hint": "Think about what each metric measures differently and what could affect one but not the other"
            }
        ],
        "quiz": [
            {
                "question": "A heuristic in decision-making is:",
                "options": ["A perfect algorithm", "A mental shortcut for quick decisions", "A detailed analysis method", "A type of database"],
                "correct": 1,
                "explanation": "A heuristic is a mental shortcut or rule of thumb that allows for quick decisions without analyzing every detail."
            },
            {
                "question": "For a medical diagnosis model, which KPI should be prioritized?",
                "options": ["Precision", "Recall", "Accuracy", "F1 Score"],
                "correct": 1,
                "explanation": "Recall is prioritized in medical diagnosis because missing a sick patient (false negative) is more dangerous than a false alarm (false positive)."
            },
            {
                "question": "What color in RAG status indicates 'at risk, monitor closely'?",
                "options": ["Red", "Amber", "Green", "Blue"],
                "correct": 1,
                "explanation": "Amber indicates 'at risk' status - not critical yet, but needs monitoring and may require action soon."
            },
            {
                "question": "When MAPE increases but R-squared stays the same, this likely indicates:",
                "options": ["Model is perfect", "Outliers affecting predictions", "Data is missing", "Model needs no changes"],
                "correct": 1,
                "explanation": "This pattern suggests outliers are causing larger individual prediction errors (MAPE) while overall patterns remain captured (R-squared)."
            }
        ]
    },
    "Statistical Result Analysis": {
        "course": "Evaluation of Outcomes",
        "description": "Master statistical inference techniques to evaluate and interpret model results including regression, variance, and z-testing.",
        "lessons": [
            {
                "title": "Interpreting Regression Results",
                "content": """
**Evaluating Linear Regression Outcomes**

Linear regression is fundamental for understanding relationships and making predictions.

**Key Regression Output Components:**

```
REGRESSION SUMMARY
─────────────────────────────────────
Dependent Variable: Sales
R-squared: 0.847
Adjusted R-squared: 0.831

Coefficients:
                  Estimate    Std Error   t-value   p-value
─────────────────────────────────────────────────────────────
(Intercept)       1250.00      125.50      9.96    <0.001 ***
Marketing_Spend      2.35        0.42      5.60    <0.001 ***
Price              -15.80        3.25     -4.86    <0.001 ***
Seasonality         45.20       12.30      3.67     0.002 **
```

**Interpreting Each Component:**

| Component | What It Tells You |
|-----------|------------------|
| **R-squared** | % of variance explained (0.847 = 84.7%) |
| **Adjusted R²** | R² adjusted for number of predictors |
| **Coefficient** | Change in Y for 1-unit change in X |
| **Std Error** | Uncertainty in coefficient estimate |
| **t-value** | Coefficient / Std Error (larger = more significant) |
| **p-value** | Probability result is due to chance |

**Reading the Example:**
- Marketing: $1 more spend → $2.35 more sales
- Price: $1 higher price → $15.80 less sales
- Model explains 84.7% of sales variation

**Common Interpretation Mistakes:**

| Mistake | Reality |
|---------|---------|
| High R² = good model | Could be overfit |
| Low p-value = important | Statistical ≠ practical significance |
| Coefficient shows causation | Correlation only without experiments |
| Larger coefficient = more important | Depends on scale of variables |

**Practical Significance vs Statistical Significance:**

```
Example:
Coefficient = 0.002, p-value = 0.001

Statistically significant? YES (p < 0.05)
Practically significant? Maybe not - 
  $1000 increase in marketing → only $2 more sales
```
                """,
                "key_points": ["R-squared shows variance explained", "Coefficients show relationship magnitude", "Low p-value ≠ practical importance", "Watch for overfitting with high R²"]
            },
            {
                "title": "Analyzing Variance and Spread",
                "content": """
**Understanding Data Variance in Model Evaluation**

Variance tells you how spread out your data and predictions are.

**Measures of Variance:**

```
VARIANCE (σ²)
Average of squared deviations from mean

Standard Deviation (σ)
Square root of variance - same units as data

Coefficient of Variation (CV)
Standard deviation / Mean × 100%
Use when comparing different scales
```

**Five-Point Summary (Box Plot Values):**

```
┌─────────────────────────────────────────┐
│  Min   Q1   Median   Q3   Max           │
│   ↓     ↓      ↓      ↓    ↓            │
│  10    25     35     45   90            │
│                                          │
│  ├──────┤      ├──────┤                 │
│     IQR = Q3 - Q1 = 20                   │
│                                          │
│  Outlier threshold:                      │
│  < Q1 - 1.5×IQR = 25 - 30 = -5          │
│  > Q3 + 1.5×IQR = 45 + 30 = 75          │
│  → 90 is an outlier!                     │
└─────────────────────────────────────────┘
```

**Using Variance in Model Evaluation:**

| High Variance | Low Variance |
|---------------|--------------|
| Predictions spread widely | Predictions clustered |
| Model may be unreliable | Model more consistent |
| Check for missing features | May be too conservative |
| Could indicate concept drift | Good for stable domains |

**Variance in Prediction Errors:**

```
RESIDUAL ANALYSIS
─────────────────────────
Mean Residual: -0.5 (bias)
Std Dev Residuals: 12.3
Min: -45.2
Max: +38.7

Check:
✓ Mean near 0? (no systematic bias)
✓ Constant variance? (homoscedasticity)
✓ Normally distributed? (valid confidence intervals)
```

**ANOVA for Comparing Groups:**

When comparing model performance across groups:
- H₀: All group means are equal
- H₁: At least one group differs
- Use F-statistic and p-value to decide
                """,
                "key_points": ["Five-point summary identifies outliers", "High variance may indicate model issues", "Residual variance should be constant", "Use ANOVA to compare group performance"]
            },
            {
                "title": "Z-Testing for Outcome Evaluation",
                "content": """
**Using Z-Tests to Evaluate Outcomes**

Z-tests help determine if observed results are statistically significant.

**When to Use Z-Test:**
- Large sample size (n > 30)
- Population standard deviation known
- Comparing sample mean to population mean
- Comparing two sample proportions

**Z-Test Formula:**

```
          Sample Mean - Population Mean
Z = ─────────────────────────────────────
         Population SD / √(Sample Size)

          x̄ - μ
Z = ─────────────
       σ / √n
```

**Interpreting Z-Scores:**

```
Z-Score Distribution:
─────────────────────────────────────
         │                    │
    -3   -2   -1   0   +1   +2   +3
         │                    │
    ─────┴────────────────────┴─────
         2.5%              97.5%
         
Common thresholds:
|Z| > 1.96 → p < 0.05 (95% confidence)
|Z| > 2.58 → p < 0.01 (99% confidence)
|Z| > 3.29 → p < 0.001 (99.9% confidence)
```

**Example: Evaluating Model Performance**

```
Question: Is our new model significantly better?

Old model accuracy: 85% (population mean μ)
New model accuracy: 88% (sample mean x̄)
Standard deviation: 3%
Sample size: 100 tests

Z = (88 - 85) / (3 / √100)
Z = 3 / 0.3
Z = 10

Interpretation:
Z = 10 >> 1.96
p << 0.001
Conclusion: New model is significantly better
```

**Two-Sample Z-Test for Proportions:**

Comparing conversion rates:
```
Group A: 250/1000 = 25% converted
Group B: 280/1000 = 28% converted

Pooled proportion p = 530/2000 = 26.5%
Standard Error = √[p(1-p)(1/n₁ + 1/n₂)]
               = √[0.265 × 0.735 × 0.002]
               = 0.0197

Z = (0.28 - 0.25) / 0.0197 = 1.52

|Z| < 1.96 → NOT statistically significant
```
                """,
                "key_points": ["Z > 1.96 indicates statistical significance at 95%", "Use for large samples (n > 30)", "Compare means or proportions", "Statistical significance ≠ practical importance"]
            },
            {
                "title": "Sampled Sets and Inference",
                "content": """
**Drawing Conclusions from Sample Data**

In practice, we evaluate models on sample data and infer population performance.

**Key Sampling Concepts:**

| Term | Meaning |
|------|---------|
| **Population** | The entire group you want to understand |
| **Sample** | Subset you actually measure |
| **Sampling Error** | Difference between sample and population |
| **Confidence Interval** | Range likely containing true value |

**Sample Size and Reliability:**

```
MARGIN OF ERROR
─────────────────
           z × σ
MOE = ───────────
          √n

For 95% confidence (z = 1.96):
n = 100  → MOE = 0.196σ
n = 400  → MOE = 0.098σ
n = 1000 → MOE = 0.062σ

Quadrupling sample size halves the margin of error!
```

**Confidence Intervals:**

```
INTERPRETING CONFIDENCE INTERVALS

Model accuracy: 87% ± 3% (95% CI)

This means:
✓ Sample accuracy is 87%
✓ 95% confident true accuracy is between 84-90%
✗ Does NOT mean 95% probability the true value is in range
   (it either is or isn't!)
```

**Comparing Two Models with Confidence Intervals:**

```
Model A: 85% (82-88)
Model B: 88% (84-92)
                    ←──────────→
                 ←────────────────→
         80  82  84  86  88  90  92

Intervals overlap!
→ Cannot conclude B is significantly better
→ Need more data or different test
```

**Cross-Validation for Robust Estimates:**

```
K-FOLD CROSS-VALIDATION
────────────────────────
Split data into K folds (e.g., K=5)

Fold 1: [Test] [Train] [Train] [Train] [Train] → Acc: 86%
Fold 2: [Train] [Test] [Train] [Train] [Train] → Acc: 88%
Fold 3: [Train] [Train] [Test] [Train] [Train] → Acc: 84%
Fold 4: [Train] [Train] [Train] [Test] [Train] → Acc: 87%
Fold 5: [Train] [Train] [Train] [Train] [Test] → Acc: 85%

Mean Accuracy: 86%
Std Dev: 1.6%
CI: 86% ± 1.4% (based on std error)
```

**Avoiding Sampling Bias:**
- Random sampling for representative data
- Stratified sampling for balanced groups
- Time-based splits for time series
- Never test on training data!
                """,
                "key_points": ["Larger samples reduce margin of error", "Confidence intervals show uncertainty", "Overlapping CIs suggest no significant difference", "Use cross-validation for robust estimates"]
            }
        ],
        "exercises": [
            {
                "title": "Interpret Regression Output",
                "type": "practical",
                "question": "A regression shows: R² = 0.72, Marketing coefficient = 1.8 (p=0.003), Price coefficient = -12.5 (p=0.41). What can you conclude about each variable's impact on sales?",
                "answer": "Interpretation: 1) R² = 0.72: The model explains 72% of sales variation - reasonably good but 28% unexplained. 2) Marketing (coef=1.8, p=0.003): Statistically significant (p<0.05). Each $1 in marketing increases sales by $1.80. Strong evidence of positive relationship. 3) Price (coef=-12.5, p=0.41): NOT statistically significant (p>0.05). We cannot confidently say price affects sales based on this data. The negative coefficient suggests higher price = lower sales, but the relationship could be due to chance. Recommendation: Keep marketing in model, consider removing price or collecting more data to detect effect.",
                "hint": "Look at both coefficient direction/magnitude AND statistical significance (p-value)"
            },
            {
                "title": "Calculate and Interpret Z-Score",
                "type": "practical",
                "question": "Your A/B test shows: Control group 1000 users, 12% conversion. Test group 1000 users, 15% conversion. Is the difference statistically significant at 95% confidence?",
                "answer": "Calculation: Pooled proportion p = (120 + 150) / 2000 = 0.135. Standard Error SE = √[0.135 × 0.865 × (1/1000 + 1/1000)] = √[0.1167 × 0.002] = √0.000234 = 0.0153. Z = (0.15 - 0.12) / 0.0153 = 0.03 / 0.0153 = 1.96. Interpretation: Z = 1.96 is exactly at the 95% confidence threshold. This is borderline significant. Technically, |Z| ≥ 1.96 means p ≤ 0.05, so this JUST reaches significance. However, I would recommend: 1) Running the test longer for more certainty, 2) Calculating exact p-value (it's about 0.05), 3) Considering practical significance: 3% lift = 30 extra conversions per 1000 users.",
                "hint": "Use the two-proportion z-test formula with pooled proportion"
            }
        ],
        "quiz": [
            {
                "question": "In regression, a high R-squared value means:",
                "options": ["The model is perfect", "The model explains most of the variance", "All coefficients are significant", "The model cannot be overfit"],
                "correct": 1,
                "explanation": "R-squared indicates the percentage of variance explained by the model. High R² means the model captures most of the variation, but doesn't guarantee it's not overfit."
            },
            {
                "question": "A coefficient is statistically significant when:",
                "options": ["It is large", "The p-value is less than 0.05", "R-squared is high", "The t-value is less than 1"],
                "correct": 1,
                "explanation": "Statistical significance is determined by p-value. P < 0.05 (at 95% confidence) means the relationship is unlikely due to chance."
            },
            {
                "question": "The IQR in a five-point summary is:",
                "options": ["Maximum minus minimum", "Q3 minus Q1", "Mean minus median", "Standard deviation times 2"],
                "correct": 1,
                "explanation": "IQR (Interquartile Range) = Q3 - Q1. It represents the middle 50% of the data and is used to identify outliers."
            },
            {
                "question": "What does |Z| > 1.96 indicate at 95% confidence?",
                "options": ["Result is not significant", "Result is statistically significant", "Sample is too small", "Data is normally distributed"],
                "correct": 1,
                "explanation": "Z-score magnitude greater than 1.96 indicates statistical significance at the 95% confidence level (p < 0.05)."
            }
        ]
    },
    "Confidence Levels & Scenarios": {
        "course": "Evaluation of Outcomes",
        "description": "Learn to work with confidence levels and create multiple outcome scenarios for data-driven decision making.",
        "lessons": [
            {
                "title": "Understanding Confidence Levels",
                "content": """
**Confidence Levels in Statistical Analysis**

Confidence levels quantify our certainty about results and predictions.

**What is a Confidence Level?**

The probability that a confidence interval contains the true population value.

| Confidence Level | Z-Score | Interpretation |
|-----------------|---------|----------------|
| 90% | 1.645 | 90% of similar intervals contain true value |
| 95% | 1.960 | 95% of similar intervals contain true value |
| 99% | 2.576 | 99% of similar intervals contain true value |

**The Tradeoff:**

```
HIGHER CONFIDENCE
─────────────────────────────────────
           Certainty
              ↑
           99%|  ████████████████████  Wide interval
              |                        (less precise)
           95%|  ████████████████
              |
           90%|  ██████████████        Narrow interval
              |                        (more precise)
              └───────────────────→
                      Width
```

**Calculating Confidence Intervals:**

```
CI = Point Estimate ± (Z × Standard Error)

Example: Survey results
Sample mean: 72%
Standard error: 2%

90% CI: 72% ± (1.645 × 2%) = 68.7% to 75.3%
95% CI: 72% ± (1.960 × 2%) = 68.1% to 75.9%
99% CI: 72% ± (2.576 × 2%) = 66.8% to 77.2%
```

**Choosing the Right Confidence Level:**

| Situation | Recommended Level | Why |
|-----------|------------------|-----|
| **High-stakes decisions** | 99% | Minimize risk of wrong conclusion |
| **Standard analysis** | 95% | Industry convention, good balance |
| **Exploratory research** | 90% | Acceptable for initial findings |
| **Life-critical** | 99.9%+ | Medical, safety applications |

**Common Misinterpretation:**

❌ "There's a 95% chance the true value is in this range"
✅ "If we repeated this study 100 times, ~95 intervals would contain the true value"
                """,
                "key_points": ["Higher confidence = wider intervals", "95% is the standard convention", "Choose level based on decision stakes", "CI interpretation is about the method, not this specific interval"]
            },
            {
                "title": "Building Probability Scenarios",
                "content": """
**Creating Multiple Outcome Scenarios**

Scenarios help decision-makers understand the range of possible outcomes.

**Scenario Framework:**

| Scenario | Probability | Characteristics |
|----------|-------------|-----------------|
| **Best Case** | 10-15% | Everything goes right |
| **Optimistic** | 20-25% | Most things go well |
| **Base Case** | 50% | Expected outcome |
| **Pessimistic** | 20-25% | Some challenges |
| **Worst Case** | 10-15% | Major problems |

**Building Scenarios from Data:**

```
REVENUE FORECAST SCENARIOS
──────────────────────────────────────
Based on historical data and model predictions:

                    Revenue    Probability
────────────────────────────────────────
Worst Case          $800K        10%
Pessimistic         $950K        20%
Base Case         $1,100K        40%
Optimistic        $1,250K        20%
Best Case         $1,400K        10%
────────────────────────────────────────
Expected Value = Σ(Probability × Outcome)
             = (0.1×800) + (0.2×950) + (0.4×1100) + (0.2×1250) + (0.1×1400)
             = $1,090K
```

**Monte Carlo Simulation:**

For complex scenarios with many variables:

```
STEPS:
1. Define probability distributions for each variable
2. Randomly sample from each distribution
3. Calculate outcome for this combination
4. Repeat 1000+ times
5. Analyze distribution of outcomes

Example: Profit Forecast
├── Sales: Normal(1000, 100)
├── Cost: Uniform(400, 500)
└── Price: Triangular(45, 50, 60)

After 10,000 simulations:
Mean Profit: $52,000
5th percentile: $38,000 (95% confidence lower bound)
95th percentile: $67,000 (95% confidence upper bound)
```

**Sensitivity Analysis:**

Which variables most impact outcomes?

```
TORNADO DIAGRAM
─────────────────────────────────────
Variable        Impact on Profit
─────────────────────────────────────
Sales Volume    ████████████████████  ±$25K
Price           ██████████████        ±$18K
Material Cost   █████████             ±$12K
Labor Cost      ███████               ±$9K
Marketing       ████                  ±$5K
─────────────────────────────────────
Focus on: Sales Volume and Price
```
                """,
                "key_points": ["Use scenarios to show range of possibilities", "Expected value weights outcomes by probability", "Monte Carlo handles complex uncertainty", "Sensitivity analysis identifies key variables"]
            },
            {
                "title": "Decision Making Under Uncertainty",
                "content": """
**Making Decisions with Incomplete Information**

Most business decisions involve uncertainty. Here's how to navigate it.

**Decision Framework with Confidence:**

```
1. IDENTIFY OPTIONS
   What actions can we take?

2. ESTIMATE OUTCOMES
   What might happen with each option?
   What's the confidence level?

3. ASSESS PROBABILITIES
   How likely is each outcome?

4. EVALUATE EXPECTED VALUES
   Expected Value = Σ(Probability × Outcome)

5. CONSIDER RISK TOLERANCE
   Can we afford the worst case?

6. DECIDE AND DOCUMENT
   Make choice, record reasoning
```

**Expected Value vs Risk Tolerance:**

```
Option A: 100% chance of $50,000
Option B: 50% chance of $120,000, 50% chance of $0

Expected Values:
A: $50,000
B: 0.5 × $120,000 + 0.5 × $0 = $60,000

B has higher expected value, BUT:
- If you can't afford to lose, choose A
- If you can absorb the loss, B might be better
```

**Decision Trees with Probabilities:**

```
                    ┌── Success (70%): +$100K
Launch New Model ───┤
        │           └── Failure (30%): -$40K
        │           EV = 0.7×100 + 0.3×(-40) = $58K
        │
        │           ┌── Market Grows (40%): +$30K
Wait and See ───────┤
                    └── Market Flat (60%): +$10K
                    EV = 0.4×30 + 0.6×10 = $18K

Decision: Launch (higher expected value)
```

**Communicating Uncertainty:**

| Bad Communication | Better Communication |
|------------------|---------------------|
| "Revenue will be $1M" | "Revenue expected $900K-1.1M (95% CI)" |
| "The model is accurate" | "Model accuracy: 87% ± 3%" |
| "This will definitely work" | "70% confidence in success" |
| "We'll probably hit target" | "65% probability of hitting Q4 target" |

**Document Your Assumptions:**
Always record:
- What confidence level you used
- What scenarios you considered
- What you assumed about probabilities
- What would change your decision
                """,
                "key_points": ["Expected value helps compare options", "Consider risk tolerance, not just expected value", "Decision trees visualize choices and outcomes", "Communicate uncertainty explicitly"]
            },
            {
                "title": "Probability Bounds and Ranges",
                "content": """
**Setting Probability Bounds for Model Outcomes**

Providing ranges instead of point estimates improves decision quality.

**Types of Uncertainty Bounds:**

| Type | Use Case | Example |
|------|----------|---------|
| **Confidence Interval** | Statistical uncertainty | Mean ± margin of error |
| **Prediction Interval** | Individual prediction | Wider than CI |
| **Credible Interval** | Bayesian analysis | Probability of parameter |
| **Tolerance Interval** | Process variation | Captures X% of population |

**Confidence vs Prediction Intervals:**

```
REGRESSION EXAMPLE
─────────────────────────────────────
Data: Marketing spend vs Sales

Confidence Interval (95%):
"Average sales at $50K marketing = $120K ± $8K"
→ Uncertainty about the MEAN

Prediction Interval (95%):
"A specific company spending $50K = $120K ± $25K"
→ Uncertainty about INDIVIDUAL outcome

Prediction intervals are ALWAYS wider!
```

**Percentile Ranges:**

```
SALES FORECAST DISTRIBUTION
─────────────────────────────────────
    P10     P25    P50    P75    P90
   (10%)   (25%)  (50%)  (75%)  (90%)
     │       │      │      │      │
    $80K   $95K  $110K  $125K  $140K
     
"50% chance sales between $95K-$125K (P25-P75)"
"90% chance sales between $80K-$140K (P10-P90)"
```

**Communicating Ranges to Stakeholders:**

**For Executives:**
"We expect Q4 revenue of $2.1M, with 80% confidence between $1.9M and $2.3M"

**For Operations:**
"Daily transactions: expect 450, plan capacity for up to 600 (95th percentile)"

**For Risk Management:**
"Value at Risk (95%): Maximum single-day loss of $125K"

**When to Use Each:**

| Audience Needs | Provide |
|---------------|---------|
| Planning for average | Point estimate + confidence interval |
| Planning for specific case | Prediction interval |
| Capacity planning | Upper percentile (90th, 95th) |
| Risk management | Lower percentile for upside, VaR for downside |
| Scenario planning | Multiple percentile ranges |
                """,
                "key_points": ["Prediction intervals are wider than confidence intervals", "Use percentiles for capacity and risk planning", "Match the bound type to the decision need", "Always communicate the confidence level"]
            }
        ],
        "exercises": [
            {
                "title": "Create Outcome Scenarios",
                "type": "practical",
                "question": "Your sales forecast model predicts $500K revenue with standard error of $50K. Create 5 scenarios with probabilities and calculate expected value.",
                "answer": "Using normal distribution principles: Worst Case ($350K, -3σ): 2% probability. Pessimistic ($400K, -2σ): 13% probability. Base Case ($500K, mean): 50% probability. Optimistic ($600K, +2σ): 13% probability. Best Case ($650K, +3σ): 2% probability. Note: Remaining 20% distributed around other outcomes. Expected Value calculation: (0.02 × 350) + (0.13 × 400) + (0.50 × 500) + (0.13 × 600) + (0.02 × 650) + (0.20 × 500) = 7 + 52 + 250 + 78 + 13 + 100 = $500K. The expected value equals the mean, as expected for a symmetric distribution. For planning, budget conservatively at $400K (pessimistic) while targeting $600K (optimistic).",
                "hint": "Use standard deviations to define scenarios and normal distribution probabilities"
            },
            {
                "title": "Choose Confidence Level",
                "type": "scenario",
                "question": "You're recommending a drug dosage algorithm for a hospital. What confidence level should you use and why? What if you were recommending a marketing email subject line instead?",
                "answer": "Drug Dosage Algorithm: Use 99.9% or higher confidence level. Reasoning: 1) Patient safety is paramount - wrong dosage could be fatal. 2) False positives/negatives have severe consequences. 3) Medical standards require extremely high certainty. 4) Would need extensive clinical validation. 5) Consider prediction intervals, not just confidence intervals. Marketing Email Subject Line: 90-95% confidence is appropriate. Reasoning: 1) Low-stakes decision - worst case is slightly lower open rate. 2) Can easily A/B test and iterate. 3) Cost of being wrong is minimal. 4) Speed of decision may be more valuable than precision. 5) 90% allows faster conclusions with smaller sample sizes. The key principle: match confidence level to the consequences of being wrong.",
                "hint": "Consider the consequences of being wrong in each situation"
            }
        ],
        "quiz": [
            {
                "question": "A 99% confidence interval is wider than a 95% interval because:",
                "options": ["It uses more data", "Higher certainty requires more range", "The sample is larger", "The calculation is different"],
                "correct": 1,
                "explanation": "To be more confident that the true value is captured, the interval must be wider. There's a tradeoff between precision and confidence."
            },
            {
                "question": "Expected value is calculated by:",
                "options": ["Taking the average outcome", "Multiplying each outcome by its probability and summing", "Choosing the most likely outcome", "Subtracting worst from best case"],
                "correct": 1,
                "explanation": "Expected Value = Σ(Probability × Outcome). It weights each possible outcome by its likelihood."
            },
            {
                "question": "A prediction interval is wider than a confidence interval because:",
                "options": ["It uses less data", "It accounts for individual variation, not just mean uncertainty", "The formula is different", "It has lower confidence"],
                "correct": 1,
                "explanation": "Prediction intervals account for both uncertainty about the mean AND variation of individual observations around that mean."
            },
            {
                "question": "For a life-critical medical decision, you should use:",
                "options": ["90% confidence", "95% confidence", "99%+ confidence", "No confidence interval needed"],
                "correct": 2,
                "explanation": "Life-critical decisions require very high confidence levels (99% or higher) because the cost of being wrong is extremely high."
            }
        ]
    },
    "Iterative Error Elimination": {
        "course": "Evaluation of Outcomes",
        "description": "Master systematic approaches to identify, debug, and eliminate errors in data models and analysis results.",
        "lessons": [
            {
                "title": "The Error Elimination Process",
                "content": """
**Systematic Debugging of Data Models**

Iterative error elimination is a structured approach to finding and fixing problems.

**The Debugging Cycle:**

```
    ┌─────────────────────────────────────┐
    │                                      │
    ↓                                      │
DETECT → DIAGNOSE → FIX → VERIFY → PREVENT
   │                                   │
   │   ←──── If new errors ────────────┘
   │
   └→ Document and close
```

**Step 1: DETECT - Finding Errors**

| Detection Method | What It Catches |
|-----------------|-----------------|
| **Automated tests** | Known failure patterns |
| **Monitoring/alerts** | Performance degradation |
| **Manual review** | Logic and interpretation errors |
| **User feedback** | Real-world failures |
| **Comparison to baseline** | Unexpected deviations |

**Step 2: DIAGNOSE - Root Cause Analysis**

**The 5 Whys Technique:**
```
Problem: Model accuracy dropped 10%

Why #1: Predictions are wrong for new customers
Why #2: New customer features have missing values
Why #3: Data pipeline doesn't handle new data source
Why #4: New data source format wasn't documented
Why #5: No validation check for source changes

Root Cause: Missing data validation in pipeline
```

**Step 3: FIX - Implementing Solutions**

| Fix Type | When to Use | Risk Level |
|----------|-------------|------------|
| **Hotfix** | Critical production issue | High - test quickly |
| **Standard fix** | Normal bugs | Medium - full testing |
| **Refactor** | Systemic issues | Low - plan carefully |

**Step 4: VERIFY - Confirming the Fix**

```
VERIFICATION CHECKLIST
☑ Error no longer occurs
☑ Related functionality still works
☑ Performance not degraded
☑ Edge cases tested
☑ Rollback plan ready
```

**Step 5: PREVENT - Stopping Recurrence**

- Add automated test for this error
- Update documentation
- Share learnings with team
- Consider systemic improvements
                """,
                "key_points": ["Follow systematic cycle: Detect → Diagnose → Fix → Verify → Prevent", "Use 5 Whys to find root cause", "Always verify fix and add prevention", "Document for future reference"]
            },
            {
                "title": "Common Error Types in Data Models",
                "content": """
**Recognizing and Fixing Model Errors**

Understanding error types helps you diagnose problems faster.

**Data Errors:**

| Error Type | Symptoms | Fix |
|-----------|----------|-----|
| **Missing values** | NaN in predictions | Imputation or filtering |
| **Outliers** | Extreme predictions | Detection and handling |
| **Data leakage** | Too-good validation scores | Review feature engineering |
| **Stale data** | Accuracy degradation | Update data pipeline |
| **Labeling errors** | Inconsistent patterns | Audit training labels |

**Model Errors:**

| Error Type | Symptoms | Fix |
|-----------|----------|-----|
| **Overfitting** | High train, low test accuracy | Regularization, more data |
| **Underfitting** | Low accuracy everywhere | More features, complex model |
| **Bias** | Systematic over/under prediction | Calibration, balanced training |
| **Concept drift** | Accuracy drops over time | Retrain, monitor distributions |
| **Feature importance shift** | Unexpected predictions | Review feature correlations |

**Process Errors:**

```
COMMON PROCESS MISTAKES
─────────────────────────────────────
1. Training on test data (data leakage)
   → Use proper train/test splits

2. Not versioning data and models
   → Implement version control

3. Ignoring edge cases
   → Add boundary testing

4. Hardcoding thresholds
   → Make configurable

5. No monitoring in production
   → Set up alerts and dashboards
```

**Error Severity Classification:**

| Severity | Impact | Response Time | Example |
|----------|--------|---------------|---------|
| **Critical** | System down | < 1 hour | Model returns no predictions |
| **High** | Major incorrect results | < 4 hours | 50% accuracy drop |
| **Medium** | Partial degradation | < 1 day | Some features not working |
| **Low** | Minor issues | < 1 week | Cosmetic or edge cases |

**Building Error Intuition:**
- Most errors are in data, not code
- Recent changes are usually the cause
- Simple errors are most common
- Edge cases reveal hidden bugs
                """,
                "key_points": ["Data errors are most common", "Overfitting = high train, low test accuracy", "Concept drift causes gradual degradation", "Classify severity to prioritize fixes"]
            },
            {
                "title": "Debugging Techniques for Analysts",
                "content": """
**Practical Debugging Methods**

When your model isn't working, use these techniques to find the problem.

**Technique 1: Sanity Checks**

```
SANITY CHECK SEQUENCE
─────────────────────────────────────
1. Check data shapes and types
   - Expected rows/columns?
   - Data types correct?

2. Check for nulls and infinities
   - df.isnull().sum()
   - np.isinf(values).sum()

3. Check value ranges
   - Are values within expected bounds?
   - Any impossible values?

4. Check distributions
   - Did the distribution change?
   - Compare to historical data

5. Check predictions
   - Are predictions in valid range?
   - Do they pass business logic?
```

**Technique 2: Bisection (Divide and Conquer)**

```
If the problem is somewhere in your pipeline:

1. Test at midpoint
   Data → [Process A] → [Process B] → [Model] → Output
                          ↑
                     Check here first

2. If good at midpoint, problem is in second half
   If bad at midpoint, problem is in first half

3. Repeat until you find the exact step
```

**Technique 3: Minimal Reproducible Example**

```
Reduce the problem to its smallest form:

Instead of:
"The model doesn't work on the full dataset"

Create:
"Row 47 with these exact values produces error X"

Steps:
1. Start with the failing case
2. Remove data/features one by one
3. Find the minimal set that still fails
4. Debug that specific case
```

**Technique 4: Comparison Testing**

| Compare | To Find |
|---------|---------|
| Current vs previous version | What changed |
| Production vs development | Environment issues |
| Sample vs full data | Data-specific bugs |
| Simple vs complex model | Model-related issues |

**Technique 5: Logging and Tracing**

```
Add strategic logging:

def predict(data):
    log("Input shape: " + str(data.shape))
    log("Input sample: " + str(data.head()))
    
    processed = preprocess(data)
    log("After preprocessing: " + str(processed.shape))
    
    result = model.predict(processed)
    log("Output range: " + str(result.min(), result.max()))
    
    return result
```
                """,
                "key_points": ["Start with sanity checks on data", "Use bisection to narrow down the problem", "Create minimal reproducible examples", "Add logging to trace issues"]
            },
            {
                "title": "Building Robust Error Prevention",
                "content": """
**Preventing Errors Before They Happen**

The best error is one that never reaches production.

**Defensive Programming Principles:**

| Principle | Implementation |
|-----------|---------------|
| **Validate inputs** | Check all data before processing |
| **Fail fast** | Error early rather than propagate |
| **Explicit defaults** | Don't rely on implicit behavior |
| **Boundary testing** | Test edge cases explicitly |
| **Assertion checks** | Verify assumptions in code |

**Data Validation Framework:**

```
INPUT VALIDATION CHECKLIST
─────────────────────────────────────
☐ Schema validation (correct columns/types)
☐ Value range checks (min/max bounds)
☐ Null/missing checks (acceptable levels)
☐ Uniqueness checks (duplicate handling)
☐ Referential integrity (foreign keys valid)
☐ Business logic (domain-specific rules)

Example checks:
assert df['age'].between(0, 120).all()
assert df['email'].str.contains('@').all()
assert df['revenue'] >= 0
```

**Automated Testing Layers:**

```
TEST PYRAMID
─────────────────────────────────────
          /\\
         /  \\     E2E Tests
        /    \\    (few, slow, expensive)
       /──────\\
      /        \\  Integration Tests
     /          \\ (some, medium speed)
    /────────────\\
   /              \\ Unit Tests
  /                \\ (many, fast, cheap)
 /──────────────────\\
```

**Continuous Monitoring:**

```
PRODUCTION MONITORING DASHBOARD
─────────────────────────────────────
📊 Model Performance
   └── Accuracy: 87% ✓ (threshold: >85%)
   └── Latency: 120ms ✓ (threshold: <200ms)
   └── Error Rate: 0.1% ✓ (threshold: <1%)

📈 Data Quality
   └── Null Rate: 0.5% ✓ (threshold: <2%)
   └── Distribution Drift: 0.02 ✓ (threshold: <0.05)
   └── Volume: 10,234 records ✓ (expected: 8K-12K)

🚨 Alerts (last 24h)
   └── No critical alerts
   └── 1 warning: Latency spike at 14:00
```

**Post-Mortem Process:**

After any significant error:
1. **Timeline**: What happened when?
2. **Root cause**: Why did it happen?
3. **Impact**: Who/what was affected?
4. **Resolution**: How was it fixed?
5. **Prevention**: How do we prevent recurrence?
6. **Action items**: Specific tasks with owners
                """,
                "key_points": ["Validate inputs before processing", "Build automated testing pyramid", "Monitor continuously in production", "Conduct post-mortems to learn and prevent"]
            },
            {
                "title": "Ethical Model Evaluation",
                "content": """
**Responsible Assessment and Ethical Critique of Models**

Evaluating outcomes isn't just technical - it requires ethical judgment and responsibility.

**Ethical Evaluation Framework:**

| Dimension | Questions to Ask |
|-----------|-----------------|
| **Fairness** | Does the model treat all groups equitably? |
| **Transparency** | Can we explain how decisions are made? |
| **Accountability** | Who is responsible for outcomes? |
| **Privacy** | Is personal data protected appropriately? |
| **Harm** | Could this model cause harm to individuals? |

**Bias Detection in Model Outcomes:**

```
BIAS AUDIT CHECKLIST
─────────────────────────────────────
☐ Performance by demographic group
   └── Accuracy, precision, recall by age, gender, location

☐ Outcome distribution fairness
   └── Are approval/rejection rates proportional?

☐ Feature importance review
   └── Are protected characteristics influencing decisions?

☐ Historical bias in training data
   └── Does past data encode unfair practices?

☐ Proxy variable detection
   └── Do features correlate with protected groups?
```

**Types of Algorithmic Bias:**

| Bias Type | Example | Detection |
|-----------|---------|-----------|
| **Selection bias** | Training data not representative | Compare data vs population |
| **Historical bias** | Past discrimination encoded | Audit historical decisions |
| **Measurement bias** | Errors differ by group | Error analysis by segment |
| **Aggregation bias** | One model for diverse groups | Subgroup performance testing |

**Ethical Decision-Making Process:**

```
1. ASSESS THE IMPACT
   Who is affected by this model's decisions?
   What are the consequences of errors?

2. CHECK FOR FAIRNESS
   Analyze performance across demographic groups
   Identify any disparate impact

3. ENSURE TRANSPARENCY
   Can we explain decisions to affected individuals?
   Is the logic understandable?

4. CONSIDER ALTERNATIVES
   If the model has issues, what are the options?
   Is using a model appropriate for this decision?

5. DOCUMENT AND COMMUNICATE
   Record ethical considerations
   Share concerns with stakeholders
```

**Presenting Outcomes Responsibly:**

| Bad Practice | Ethical Practice |
|-------------|------------------|
| Hide limitations | Acknowledge model limitations clearly |
| Ignore edge cases | Report performance on minority groups |
| Overstate confidence | Present uncertainty honestly |
| Blame the data | Take responsibility for model choices |
| Rush to production | Allow time for ethical review |

**When to Raise Concerns:**

You have a professional obligation to speak up when:
- Model could cause significant harm
- Bias is detected but not addressed
- Stakeholders ignore ethical risks
- Regulations or policies are violated
- You're asked to suppress unfavorable findings

**Escalation Path:**
1. Raise with immediate team/manager
2. Document concerns in writing
3. Escalate to ethics/compliance if unresolved
4. Consider professional obligations (varies by industry)
                """,
                "key_points": ["Evaluate models for fairness across groups", "Check for bias in training data and outcomes", "Present limitations and uncertainties honestly", "Raise ethical concerns when you see them"]
            }
        ],
        "exercises": [
            {
                "title": "Apply 5 Whys Analysis",
                "type": "practical",
                "question": "Your customer churn model suddenly started predicting everyone as 'will churn.' Apply the 5 Whys technique to find the root cause.",
                "answer": "5 Whys Analysis: Why #1: Model predicts 'churn' for all customers → Because all prediction probabilities are above threshold. Why #2: Why are all probabilities high? → Because one feature has extreme values for all records. Why #3: Why does that feature have extreme values? → The feature is customer tenure, and all values show 0 days. Why #4: Why is tenure showing 0 for everyone? → The data pipeline is calculating tenure from an empty 'signup_date' field. Why #5: Why is signup_date empty? → A recent database migration removed the date format, and the ETL couldn't parse it. ROOT CAUSE: Database migration broke date parsing in ETL pipeline. FIX: 1) Immediate: Restore from backup or fix date format. 2) Prevention: Add data validation to check for reasonable tenure values before model runs.",
                "hint": "Start with what's directly wrong, then ask 'why' at each level until you reach a systemic cause"
            },
            {
                "title": "Design Validation Checks",
                "type": "practical",
                "question": "Design 5 validation checks for a model that predicts loan approval (features: income, credit_score, debt_ratio, employment_years, loan_amount).",
                "answer": "Validation checks: 1) INCOME: Assert income >= 0 and income < 10,000,000 (reasonable bounds). Flag if null or negative. 2) CREDIT_SCORE: Assert credit_score between 300 and 850 (valid FICO range). Reject if outside range - this is a data error. 3) DEBT_RATIO: Assert debt_ratio between 0 and 1 (or 0-100%). If > 1, check if percentage vs decimal format. 4) EMPLOYMENT_YEARS: Assert employment_years >= 0 and < 60. If > person's age minus 16, flag as likely error. 5) LOAN_AMOUNT: Assert loan_amount > 0 and < 10 × income (reasonable debt-to-income). Also check loan_amount / income ratio is within lending policy limits. ADDITIONAL: Check for nulls in any required field. Validate referential integrity of customer_id. Log any records that fail validation for review.",
                "hint": "Consider valid ranges, business logic rules, and relationships between fields"
            },
            {
                "title": "Ethical Bias Assessment",
                "type": "scenario",
                "question": "Your hiring recommendation model has 85% overall accuracy, but you discover it rejects 60% of applicants from one demographic group compared to 30% for others. What ethical issues does this raise and how should you proceed?",
                "answer": "Ethical Issues: 1) DISPARATE IMPACT: The 2x rejection rate for one group (60% vs 30%) suggests unfair treatment, even if unintentional. 2) HISTORICAL BIAS: Training data may encode past hiring discrimination. 3) PROXY DISCRIMINATION: Features like zip code, school, or name may correlate with protected characteristics. 4) HARM POTENTIAL: Affected candidates lose job opportunities unfairly. Proceed: 1) PAUSE DEPLOYMENT: Do not use this model for decisions until resolved. 2) ANALYZE: Investigate which features drive the disparity. 3) AUDIT: Check if model relies on proxies for protected groups. 4) REPORT: Escalate to management/HR/legal with findings. 5) REMEDIATE: Consider removing biased features, retraining with balanced data, or applying fairness constraints. 6) DOCUMENT: Record findings and decisions made. The 85% accuracy is irrelevant if the model discriminates - fairness is a separate, critical requirement.",
                "hint": "Consider the impact on affected individuals and your professional responsibility to address bias"
            }
        ],
        "quiz": [
            {
                "question": "The 5 Whys technique is used to:",
                "options": ["Count errors", "Find root causes", "Measure accuracy", "Test performance"],
                "correct": 1,
                "explanation": "The 5 Whys is a root cause analysis technique that repeatedly asks 'why' to drill down from symptoms to underlying causes."
            },
            {
                "question": "If your model has high training accuracy but low test accuracy, the problem is likely:",
                "options": ["Underfitting", "Overfitting", "Data leakage", "Concept drift"],
                "correct": 1,
                "explanation": "High train/low test accuracy is the classic sign of overfitting - the model memorized training data but doesn't generalize."
            },
            {
                "question": "The bisection debugging technique works by:",
                "options": ["Testing random points", "Dividing the problem in half repeatedly", "Testing all points", "Skipping to the end"],
                "correct": 1,
                "explanation": "Bisection (divide and conquer) tests at midpoints to efficiently narrow down where the problem occurs in a pipeline."
            },
            {
                "question": "In the test pyramid, which tests are at the bottom (most numerous)?",
                "options": ["End-to-end tests", "Integration tests", "Unit tests", "Manual tests"],
                "correct": 2,
                "explanation": "Unit tests form the base of the pyramid - they're fast, cheap, and you should have many of them testing individual components."
            },
            {
                "question": "When you discover your model has significantly different error rates for different demographic groups, you should:",
                "options": ["Ignore it if overall accuracy is good", "Investigate for bias and consider pausing deployment", "Report only the overall accuracy", "Assume the difference is natural"],
                "correct": 1,
                "explanation": "Significant performance differences across demographic groups may indicate bias. You have an ethical obligation to investigate and address this before deployment, even if overall metrics look good."
            }
        ]
    },
    "Data Ensembling & Reliability": {
        "course": "Evaluation of Outcomes",
        "description": "Learn ensemble techniques to improve model reliability and result consistency.",
        "lessons": [
            {
                "title": "Introduction to Ensemble Methods",
                "content": """
**Combining Models for Better Results**

Ensemble methods combine multiple models to produce better predictions than any single model.

**Why Ensembles Work:**

| Problem | How Ensembles Help |
|---------|-------------------|
| Single model overfits | Different models overfit differently, averaging reduces it |
| High variance | Averaging reduces variance |
| Model uncertainty | Multiple models provide confidence bounds |
| Missing patterns | Different models capture different patterns |

**Main Ensemble Strategies:**

```
1. BAGGING (Bootstrap Aggregating)
   ─────────────────────────────────────
   Train multiple models on random subsets
   Combine by averaging (regression) or voting (classification)
   
   Example: Random Forest
   
   Data → [Subset 1] → Model 1 ─┐
       → [Subset 2] → Model 2 ──┼→ Average/Vote → Prediction
       → [Subset 3] → Model 3 ─┘


2. BOOSTING
   ─────────────────────────────────────
   Train models sequentially, each fixing previous errors
   
   Example: XGBoost, AdaBoost
   
   Data → Model 1 → Errors → Model 2 → Errors → Model 3
                                                    ↓
                                        Combined Prediction


3. STACKING
   ─────────────────────────────────────
   Train diverse base models, then train a meta-model on their predictions
   
   Data → [Model A] → Pred A ─┐
       → [Model B] → Pred B ──┼→ Meta-Model → Final Prediction
       → [Model C] → Pred C ─┘
```

**When to Use Each:**

| Method | Best For | Caution |
|--------|----------|---------|
| **Bagging** | High-variance models (decision trees) | Less effective for biased models |
| **Boosting** | Weak learners, tabular data | Can overfit, slower training |
| **Stacking** | Diverse model types | Complexity, risk of overfitting |
                """,
                "key_points": ["Ensembles combine multiple models for better results", "Bagging reduces variance through averaging", "Boosting reduces bias by focusing on errors", "Stacking uses a meta-model on base predictions"]
            },
            {
                "title": "Improving Reliability with Ensembles",
                "content": """
**Using Ensembles for More Reliable Predictions**

Beyond accuracy, ensembles improve prediction reliability and confidence.

**Reliability Metrics:**

| Metric | What It Measures |
|--------|-----------------|
| **Prediction variance** | How much predictions vary across models |
| **Calibration** | Do probabilities match actual frequencies? |
| **Consistency** | Same input → similar outputs over time |
| **Robustness** | Performance on noisy or adversarial data |

**Measuring Prediction Confidence:**

```
ENSEMBLE CONFIDENCE ESTIMATION
─────────────────────────────────────
For a single prediction, get outputs from all models:

Model 1: 0.82  ─┐
Model 2: 0.78   ├→ Mean: 0.81, Std: 0.04
Model 3: 0.85  ─┘

High agreement (low std) = High confidence
Low agreement (high std) = Low confidence, flag for review
```

**Confidence-Based Actions:**

| Prediction Std | Confidence | Action |
|---------------|------------|--------|
| < 0.05 | High | Automate decision |
| 0.05 - 0.15 | Medium | Apply with monitoring |
| > 0.15 | Low | Human review required |

**Calibration Improvement:**

```
BEFORE CALIBRATION:
Model says 70% → Actually 85% of the time
Model says 90% → Actually 75% of the time

CALIBRATION TECHNIQUES:
1. Platt Scaling: Fit logistic regression on probabilities
2. Isotonic Regression: Non-parametric calibration
3. Temperature Scaling: Scale logits by learned temperature

AFTER CALIBRATION:
Model says 70% → Actually ~70% of the time
Model says 90% → Actually ~90% of the time
```

**Reliability vs Accuracy Tradeoff:**

Sometimes you can increase reliability by:
- Abstaining on uncertain predictions
- Using simpler, more stable models
- Accepting slightly lower accuracy for more consistent results

```
ABSTENTION STRATEGY:
If prediction confidence < threshold:
    Return "Uncertain - requires human review"
Else:
    Return prediction

This improves reliability of accepted predictions
but reduces coverage (some cases not automated)
```
                """,
                "key_points": ["Ensemble variance indicates prediction confidence", "Calibration aligns probabilities with reality", "Consider abstaining on low-confidence predictions", "Reliability sometimes trades off with accuracy"]
            },
            {
                "title": "Practical Ensemble Implementation",
                "content": """
**Building Ensembles in Practice**

Step-by-step approach to implementing ensemble methods.

**Step 1: Select Diverse Base Models**

```
GOOD DIVERSITY (different error patterns):
├── Linear model (captures linear relationships)
├── Decision tree (captures non-linear, rules)
├── Neural network (captures complex patterns)
└── Nearest neighbors (captures local patterns)

BAD DIVERSITY (similar errors):
├── Random Forest
├── Extra Trees
├── Another Random Forest variant
└── Decision Tree
(All tree-based, similar biases)
```

**Step 2: Train Base Models**

```
# Pseudocode for bagging
base_models = []
for i in range(n_models):
    sample = bootstrap_sample(training_data)
    model = train_model(sample)
    base_models.append(model)
```

**Step 3: Combine Predictions**

| Task Type | Combination Method |
|-----------|-------------------|
| **Regression** | Mean, median, or weighted average |
| **Classification** | Majority vote or average probabilities |
| **Ranking** | Rank averaging or Borda count |

```
WEIGHTED AVERAGING
─────────────────────────────────────
Weight models by their validation performance:

Model 1: Accuracy 0.85 → Weight 0.85/2.45 = 0.35
Model 2: Accuracy 0.80 → Weight 0.80/2.45 = 0.33
Model 3: Accuracy 0.80 → Weight 0.80/2.45 = 0.33

Final = 0.35×Pred₁ + 0.33×Pred₂ + 0.33×Pred₃
```

**Step 4: Validate the Ensemble**

```
VALIDATION CHECKLIST
☐ Ensemble beats best single model?
☐ Ensemble variance is lower than individual?
☐ Ensemble is well-calibrated?
☐ Performance consistent across data splits?
☐ Computational cost acceptable?
```

**Step 5: Monitor in Production**

```
ENSEMBLE MONITORING DASHBOARD
─────────────────────────────────────
Base Model Agreement:
└── High agreement (>80%): 92% of predictions ✓
└── Low agreement (<50%): 3% of predictions (flagged)

Individual Model Health:
├── Model 1: Active, 86% accuracy ✓
├── Model 2: Active, 84% accuracy ✓
└── Model 3: Degraded, 78% accuracy ⚠ (investigate)

Ensemble Performance:
└── Combined: 89% accuracy ✓
```
                """,
                "key_points": ["Choose diverse model types for best ensembles", "Weight models by performance", "Validate ensemble against single models", "Monitor individual model health"]
            },
            {
                "title": "Ensemble Techniques for Data Quality",
                "content": """
**Using Ensembles to Detect and Handle Data Issues**

Ensembles can improve data reliability, not just model predictions.

**Data Ensembling for Quality:**

| Technique | Purpose |
|-----------|---------|
| **Multiple sources** | Cross-validate information |
| **Imputation ensemble** | Better missing value estimates |
| **Anomaly consensus** | More reliable outlier detection |
| **Label aggregation** | Handle noisy labels |

**Multi-Source Data Fusion:**

```
DATA SOURCE AGREEMENT
─────────────────────────────────────
Customer revenue from 3 sources:

CRM: $125,000
ERP: $127,500
Reports: $124,800

Agreement score: High (within 2%)
→ Use average: $125,767

If sources disagreed significantly:
→ Flag for manual review
→ Apply business rules to resolve
```

**Ensemble Imputation:**

```
MISSING VALUE: Customer age

Method 1 (Mean): 42
Method 2 (Median): 39
Method 3 (KNN): 44
Method 4 (Regression): 41

Ensemble estimate: 41.5 (average)
Uncertainty: ±2.2 (std dev)

Flag if uncertainty > threshold
```

**Consensus Outlier Detection:**

```
OUTLIER DETECTION ENSEMBLE
─────────────────────────────────────
For each data point, run multiple detectors:

Point X:
├── Z-score: Normal
├── IQR method: Normal
├── Isolation Forest: Outlier
└── LOF: Normal

Consensus: 1/4 flagged → Likely normal

Point Y:
├── Z-score: Outlier
├── IQR method: Outlier
├── Isolation Forest: Outlier
└── LOF: Normal

Consensus: 3/4 flagged → Likely outlier, investigate
```

**Label Aggregation (Crowdsourcing):**

When multiple labelers annotate data:

```
Sample #42 labels:
├── Labeler A: Positive
├── Labeler B: Positive
├── Labeler C: Negative
├── Labeler D: Positive
└── Labeler E: Positive

Majority vote: Positive (4/5)
Agreement: 80% → High confidence

Methods:
1. Simple majority vote
2. Weighted by labeler quality
3. Dawid-Skene model (accounts for labeler bias)
```
                """,
                "key_points": ["Combine multiple data sources for reliability", "Ensemble imputation provides uncertainty estimates", "Consensus improves outlier detection", "Aggregate labels from multiple annotators"]
            }
        ],
        "exercises": [
            {
                "title": "Design an Ensemble Strategy",
                "type": "practical",
                "question": "You're predicting customer lifetime value (CLV). Design an ensemble with 3 diverse models and explain how you'd combine them.",
                "answer": "Ensemble Design: BASE MODELS: 1) Linear Regression - Captures linear relationships between features (recency, frequency, monetary) and CLV. Simple, interpretable baseline. 2) XGBoost - Captures non-linear relationships and feature interactions. Good for tabular data, handles missing values. 3) Neural Network (MLP) - Captures complex patterns, can learn from large datasets. Different optimization approach. COMBINATION: Use weighted averaging based on validation RMSE. Calculate weights as inverse of error: Weight_i = (1/RMSE_i) / Σ(1/RMSE_j). Example: If RMSE = [1000, 800, 900], weights ≈ [0.28, 0.35, 0.31]. CONFIDENCE: Report prediction ± (std across models). If std > 20% of prediction, flag for review. VALIDATION: Verify ensemble RMSE < best individual model RMSE.",
                "hint": "Choose models that make different types of errors and decide how to weight their predictions"
            },
            {
                "title": "Implement Consensus Outlier Detection",
                "type": "scenario",
                "question": "You have sales data and want to detect anomalies. Three methods flag the following records: Z-score flags: [5, 23, 47]. IQR flags: [5, 23, 89]. Isolation Forest flags: [5, 47, 102]. Which records should be investigated?",
                "answer": "Consensus Analysis: Record 5: Flagged by ALL 3 methods (3/3) → HIGH PRIORITY. Definitely investigate - multiple independent methods agree. Record 23: Flagged by Z-score and IQR (2/3) → MEDIUM PRIORITY. Likely anomaly, worth investigating. Record 47: Flagged by Z-score and Isolation Forest (2/3) → MEDIUM PRIORITY. Worth investigating. Record 89: Flagged by IQR only (1/3) → LOW PRIORITY. Might be edge case for IQR method, less likely true anomaly. Record 102: Flagged by Isolation Forest only (1/3) → LOW PRIORITY. Single method disagreement. Investigation order: 5 → 23 → 47 → 89 → 102. Also consider: the methods that flagged it (Z-score sensitive to extremes, IQR to distribution, IF to isolation) give clues about the nature of the anomaly.",
                "hint": "Count how many methods flagged each record and prioritize by consensus"
            }
        ],
        "quiz": [
            {
                "question": "Bagging improves model performance primarily by:",
                "options": ["Increasing bias", "Reducing variance", "Adding more features", "Using more data"],
                "correct": 1,
                "explanation": "Bagging (Bootstrap Aggregating) reduces variance by training on random subsets and averaging predictions, which smooths out overfitting."
            },
            {
                "question": "In an ensemble, high prediction variance across models indicates:",
                "options": ["The ensemble is working well", "Low confidence in the prediction", "The models are identical", "Perfect accuracy"],
                "correct": 1,
                "explanation": "High variance means the models disagree, indicating uncertainty. This is actually useful information for flagging cases needing review."
            },
            {
                "question": "When building an ensemble, you should select models that are:",
                "options": ["All the same type", "Diverse with different error patterns", "Only the most accurate", "Random selections"],
                "correct": 1,
                "explanation": "Diverse models that make different types of errors complement each other, so their combination performs better than any individual."
            },
            {
                "question": "Boosting differs from bagging because it:",
                "options": ["Uses random subsets", "Trains models sequentially to fix errors", "Only uses one model", "Ignores training data"],
                "correct": 1,
                "explanation": "Boosting trains models sequentially, with each new model focusing on the errors of previous models. Bagging trains in parallel on random subsets."
            }
        ]
    },
    "ETL & Version Control": {
        "course": "Evaluation of Outcomes",
        "description": "Understand ETL systems and version control practices for collaborative data analysis.",
        "lessons": [
            {
                "title": "ETL in the Data Lifecycle",
                "content": """
**Understanding Extract, Transform, Load (ETL)**

ETL is the backbone of data analysis, moving data from sources to analysis-ready formats.

**ETL Components:**

```
┌──────────┐    ┌──────────────┐    ┌──────────┐
│ EXTRACT  │ →  │  TRANSFORM   │ →  │   LOAD   │
│          │    │              │    │          │
│ Sources: │    │ Clean        │    │ Targets: │
│ -Database│    │ Validate     │    │ -DW      │
│ -API     │    │ Aggregate    │    │ -Lake    │
│ -Files   │    │ Join         │    │ -Mart    │
│ -Streams │    │ Calculate    │    │ -Cache   │
└──────────┘    └──────────────┘    └──────────┘
```

**Extract Phase:**

| Source Type | Considerations |
|-------------|---------------|
| **Databases** | Query optimization, connection limits |
| **APIs** | Rate limits, authentication, pagination |
| **Files** | Format parsing, encoding issues |
| **Streams** | Real-time vs batch, ordering |

**Transform Phase:**

```
COMMON TRANSFORMATIONS
─────────────────────────────────────
1. Cleaning
   └── Handle nulls, fix formats, remove duplicates

2. Standardization
   └── Consistent naming, units, date formats

3. Validation
   └── Check ranges, business rules, integrity

4. Aggregation
   └── Sum, count, average by dimensions

5. Enrichment
   └── Add calculated fields, join reference data

6. Type Conversion
   └── Cast strings to dates, numbers, etc.
```

**Load Phase:**

| Load Type | Use Case | Frequency |
|-----------|----------|-----------|
| **Full load** | Initial load, small datasets | Daily/weekly |
| **Incremental** | Large datasets, frequent updates | Hourly/daily |
| **Streaming** | Real-time requirements | Continuous |
| **Merge (upsert)** | Update existing + insert new | As needed |

**ETL vs ELT:**

```
ETL (Traditional):
Source → Transform → Load to Target
- Transform before loading
- Good for structured data
- Transform logic in ETL tool

ELT (Modern):
Source → Load to Target → Transform
- Load raw data first
- Transform in the data warehouse
- Uses DW computing power
- Good for big data
```
                """,
                "key_points": ["ETL: Extract, Transform, Load", "Transform includes cleaning, validation, aggregation", "Choose load strategy based on data size and frequency", "ELT loads first, transforms in the warehouse"]
            },
            {
                "title": "Data Pipeline Design",
                "content": """
**Building Reliable Data Pipelines**

A well-designed pipeline ensures consistent, reliable data for analysis.

**Pipeline Architecture:**

```
MODERN DATA PIPELINE
─────────────────────────────────────
                                 ┌──→ Analytics
Sources                          │
   ↓                             │
[Ingestion] → [Storage] → [Processing] → Dashboards
                                 │
Raw Zone    Staging    Transform └──→ ML Models
   ↓           ↓          ↓
Landing    Cleaned    Aggregated
```

**Pipeline Components:**

| Component | Purpose | Tools |
|-----------|---------|-------|
| **Scheduler** | Trigger jobs at right time | Airflow, Cron |
| **Orchestrator** | Manage job dependencies | Airflow, Prefect |
| **Queue** | Handle async processing | Kafka, RabbitMQ |
| **Monitoring** | Track health and failures | Grafana, DataDog |
| **Alerting** | Notify on issues | PagerDuty, Slack |

**Pipeline Patterns:**

```
1. BATCH PROCESSING
   ─────────────────────────────
   Run at scheduled intervals
   Process all data since last run
   Good for: Daily reports, aggregations
   
   [Schedule: Daily 2am] → Process yesterday's data

2. MICRO-BATCH
   ─────────────────────────────
   Small batches every few minutes
   Balance latency and efficiency
   Good for: Near-real-time dashboards
   
   [Schedule: Every 5 min] → Process latest chunk

3. STREAMING
   ─────────────────────────────
   Continuous processing
   Event-driven
   Good for: Real-time analytics, alerts
   
   [Event arrives] → Process immediately
```

**Error Handling:**

```
PIPELINE ERROR STRATEGY
─────────────────────────────────────
1. Retry with backoff
   Try again after: 1min, 5min, 30min

2. Dead letter queue
   Failed records go to separate queue for review

3. Partial success
   Continue with valid data, log failures

4. Circuit breaker
   Stop processing if failure rate too high

5. Alerting
   Notify team of critical failures
```

**Pipeline Best Practices:**
- Idempotent operations (re-running produces same result)
- Checkpointing (save progress, resume on failure)
- Data lineage tracking (know where data came from)
- Quality checks at each stage
                """,
                "key_points": ["Design for reliability with retry and error handling", "Choose batch vs streaming based on latency needs", "Make pipelines idempotent for safe reruns", "Track data lineage for debugging"]
            },
            {
                "title": "Version Control for Data Projects",
                "content": """
**Managing Changes in Collaborative Data Work**

Version control tracks changes, enables collaboration, and provides rollback capability.

**What to Version Control:**

| Asset | Version Control? | How |
|-------|-----------------|-----|
| **Code** | Yes | Git |
| **Model files** | Yes | Git LFS, DVC |
| **Configurations** | Yes | Git |
| **Small datasets** | Maybe | Git (if < 100MB) |
| **Large datasets** | Track separately | DVC, data catalogs |
| **Documentation** | Yes | Git |
| **Results/outputs** | Maybe | Depends on reproducibility |

**Git Basics for Data Projects:**

```
ESSENTIAL GIT WORKFLOW
─────────────────────────────────────
1. Clone repository
   git clone <repo-url>

2. Create feature branch
   git checkout -b feature/new-model

3. Make changes and commit
   git add .
   git commit -m "Add churn prediction model v2"

4. Push to remote
   git push origin feature/new-model

5. Create pull request for review

6. Merge after approval
   git checkout main
   git merge feature/new-model
```

**Commit Message Best Practices:**

```
GOOD COMMIT MESSAGES
─────────────────────────────────────
Format: <type>: <subject>

feat: Add customer segmentation model
fix: Correct date parsing in ETL pipeline
docs: Update model documentation
refactor: Simplify feature engineering code
test: Add unit tests for data validation
data: Update training dataset to Q4 2025

Include:
- What changed
- Why it changed
- Any breaking changes
```

**Branching Strategy:**

```
GITFLOW FOR DATA PROJECTS
─────────────────────────────────────
main ──────────────────────────────→
       ↑         ↑
develop ─────────────────────────→
       ↑    ↑    ↑
      feature  feature
      /model   /pipeline
       
- main: Production-ready code
- develop: Integration branch
- feature/*: Individual work items
```

**Handling Large Files:**

```
GIT LFS (Large File Storage)
─────────────────────────────────────
Track model files:
git lfs track "*.pkl"
git lfs track "*.h5"

.gitattributes will include:
*.pkl filter=lfs diff=lfs merge=lfs -text
*.h5 filter=lfs diff=lfs merge=lfs -text

DVC (Data Version Control)
─────────────────────────────────────
Track datasets:
dvc add data/training.csv
git add data/training.csv.dvc

Data stored externally (S3, GCS)
Git tracks metadata only
```
                """,
                "key_points": ["Version control code, configs, and documentation", "Use Git LFS or DVC for large files", "Follow branching strategy for collaboration", "Write clear commit messages"]
            },
            {
                "title": "Collaborative Data Workflows",
                "content": """
**Working Together on Data Projects**

Effective collaboration requires clear processes and communication.

**Collaboration Framework:**

```
COLLABORATIVE WORKFLOW
─────────────────────────────────────
1. PLAN
   └── Define scope, assign roles, set timeline

2. DEVELOP
   └── Work on branches, commit frequently

3. REVIEW
   └── Code review, testing, documentation

4. INTEGRATE
   └── Merge to main, deploy to staging

5. VALIDATE
   └── Test in staging, verify results

6. DEPLOY
   └── Release to production, monitor
```

**Code Review for Data Projects:**

```
DATA PROJECT CODE REVIEW CHECKLIST
─────────────────────────────────────
☐ Does the code run without errors?
☐ Is the logic correct?
☐ Are there appropriate tests?
☐ Is the code documented?
☐ Does it follow coding standards?
☐ Are data validations in place?
☐ Is performance acceptable?
☐ Are secrets/credentials secure?
☐ Is the commit message clear?
```

**Handling Merge Conflicts:**

| Conflict Type | Resolution Approach |
|--------------|---------------------|
| **Code conflicts** | Discuss with other author, merge carefully |
| **Configuration conflicts** | Document environment differences |
| **Data conflicts** | Typically use latest version or merge rules |
| **Model conflicts** | May need to retrain on combined changes |

**Communication Best Practices:**

```
ASYNC COMMUNICATION (preferred)
─────────────────────────────────────
- Pull request descriptions
- Code comments
- Documentation updates
- Slack/Teams for quick questions

SYNC COMMUNICATION (when needed)
─────────────────────────────────────
- Standup meetings (brief, focused)
- Design discussions
- Conflict resolution
- Pair programming on complex issues
```

**Change Documentation:**

```
CHANGELOG ENTRY
─────────────────────────────────────
## [1.2.0] - 2025-10-15

### Added
- New feature importance calculation
- Automated data quality checks

### Changed
- Updated training data to include Q3 2025
- Improved model accuracy from 85% to 88%

### Fixed
- Fixed timezone handling in date features
- Corrected null handling in customer age

### Deprecated
- Old scoring endpoint (use /v2/score)
```

**Documentation Locations:**

| Type | Where to Document |
|------|------------------|
| **Code logic** | Inline comments, docstrings |
| **API/interfaces** | README, API docs |
| **Decisions** | ADRs (Architecture Decision Records) |
| **Changes** | CHANGELOG |
| **Processes** | Wiki/Confluence |
                """,
                "key_points": ["Follow structured development workflow", "Conduct code reviews for quality", "Document changes in changelog", "Communicate async when possible"]
            }
        ],
        "exercises": [
            {
                "title": "Design an ETL Pipeline",
                "type": "practical",
                "question": "Design an ETL pipeline to load daily sales data from 3 sources (POS system, e-commerce API, returns database) into a data warehouse for analysis. Include error handling.",
                "answer": "ETL Pipeline Design: EXTRACT: 1) POS: Query database for yesterday's transactions at 2am (incremental by date). 2) E-commerce: API call with pagination, handle rate limits with backoff. 3) Returns: Query returns database, join with original transaction IDs. TRANSFORM: 1) Standardize date formats (all to ISO 8601). 2) Normalize product codes across systems. 3) Calculate net sales (gross - returns). 4) Validate: sales > 0, dates within range, required fields present. 5) Handle nulls: impute missing store_id from product mapping, flag records with critical nulls. LOAD: 1) Upsert to staging table (update if exists, insert if new). 2) Run quality checks on staging. 3) If checks pass, merge to production fact table. ERROR HANDLING: 1) Retry failed extracts 3 times with exponential backoff. 2) Dead letter queue for records failing validation. 3) Alert if >5% records fail. 4) Checkpoint after each source extraction. 5) Full pipeline idempotent (re-run safe).",
                "hint": "Consider each phase (Extract, Transform, Load) and what happens when something fails"
            },
            {
                "title": "Create Git Workflow",
                "type": "practical",
                "question": "Your team has 3 data scientists working on the same model. One is improving features, one is tuning hyperparameters, one is adding new data. Design a Git workflow to avoid conflicts.",
                "answer": "Git Workflow: BRANCH STRUCTURE: main (production) → develop (integration) → feature branches. FEATURE BRANCHES: 1) feature/improved-features (feature engineering changes). 2) feature/hyperparameter-tuning (model config changes). 3) feature/new-data-source (data pipeline changes). WORKFLOW: 1) Each person works on their branch, commits frequently. 2) Daily: pull latest develop, merge into feature branch, resolve conflicts early. 3) When ready: create PR to develop, request review from one other team member. 4) Code review checklist: tests pass, documentation updated, no hardcoded paths. 5) Weekly: merge all approved PRs to develop, run integration tests. 6) Monthly: merge develop to main, tag release version. CONFLICT PREVENTION: 1) Separate concerns: features.py (person 1), config.yaml (person 2), pipeline.py (person 3). 2) Communicate in daily standup about overlapping files. 3) Use feature flags for experimental code. 4) Model files tracked with DVC, not Git.",
                "hint": "Separate work by file/component and establish clear merge cadence"
            }
        ],
        "quiz": [
            {
                "question": "In ETL, the 'Transform' step includes:",
                "options": ["Only extracting data", "Cleaning, validating, and aggregating data", "Just loading to database", "Deleting old data"],
                "correct": 1,
                "explanation": "The Transform step processes raw data: cleaning, validating, standardizing, aggregating, and enriching before loading."
            },
            {
                "question": "Git LFS is used for:",
                "options": ["Small text files", "Large binary files like models", "Deleted files", "Branch management"],
                "correct": 1,
                "explanation": "Git LFS (Large File Storage) handles large binary files like trained models, storing them separately while Git tracks metadata."
            },
            {
                "question": "An idempotent pipeline means:",
                "options": ["It runs once and stops", "Re-running it produces the same result", "It cannot be modified", "It runs faster each time"],
                "correct": 1,
                "explanation": "Idempotent pipelines produce the same result whether run once or multiple times, which is important for safe retries and reruns."
            },
            {
                "question": "ELT differs from ETL because:",
                "options": ["It doesn't transform data", "It loads raw data first, then transforms in the warehouse", "It only works with streaming", "It requires no configuration"],
                "correct": 1,
                "explanation": "ELT loads raw data to the data warehouse first, then uses the warehouse's computing power to transform it. ETL transforms before loading."
            }
        ]
    },
    "Data Visualization Fundamentals": {
        "course": "Data Visualisation",
        "description": "Learn visualization techniques to present data findings effectively to both technical and non-technical audiences.",
        "lessons": [
            {
                "title": "Introduction to Data Visualization",
                "content": """
**Why Data Visualization Matters**

Data visualization transforms complex data into visual representations that are easy to understand at a glance.

**Key Benefits:**
- **Clarity**: Complex patterns become visible
- **Speed**: Faster comprehension than reading tables
- **Engagement**: Visual stories capture attention
- **Accessibility**: Non-technical audiences can understand

**The Visualization Process:**

```
1. UNDERSTAND the data and audience
2. SELECT the right chart type
3. DESIGN with clarity in mind
4. REFINE based on feedback
5. PRESENT with context
```

**Real-World Example:**
A hospital reduced patient wait times by 30% after visualizing patient flow patterns on a dashboard. Staff could instantly see bottlenecks that were invisible in spreadsheets.

**Types of Visualizations:**

| Type | Purpose | Example |
|------|---------|---------|
| **Bar Chart** | Compare categories | Sales by product |
| **Line Chart** | Show trends over time | Revenue growth |
| **Pie Chart** | Show proportions | Market share |
| **Scatter Plot** | Show relationships | Price vs. demand |
| **Heatmap** | Show patterns in matrices | Website clicks |
                """,
                "key_points": ["Visualization makes data accessible", "Choose charts based on purpose", "Design for your audience", "Visual stories are more engaging"]
            },
            {
                "title": "Choosing the Right Chart Type",
                "content": """
**Chart Selection Guide**

The most common mistake in visualization is choosing the wrong chart type for your data and message.

**Decision Framework:**

**What are you trying to show?**

| Goal | Best Charts |
|------|-------------|
| **Compare values** | Bar chart, Column chart |
| **Show change over time** | Line chart, Area chart |
| **Show parts of a whole** | Pie chart, Stacked bar |
| **Show relationships** | Scatter plot, Bubble chart |
| **Show distribution** | Histogram, Box plot |
| **Show geographic data** | Map, Choropleth |

**Common Mistakes:**

❌ **Pie charts with too many slices** (max 5-7)
❌ **3D charts** (distort perception)
❌ **Dual y-axes** (confusing)
❌ **Truncated axes** (misleading)
❌ **Too many colors** (distracting)

**Chart Selection Examples:**

**Scenario 1:** "Compare Q1 revenue across 5 regions"
→ Use: Horizontal bar chart (easy to read labels)

**Scenario 2:** "Show website traffic trend over 12 months"
→ Use: Line chart (shows continuous change)

**Scenario 3:** "Show how budget is divided across departments"
→ Use: Pie chart (if ≤5 categories) or stacked bar

**Scenario 4:** "Explore relationship between ad spend and conversions"
→ Use: Scatter plot (shows correlation)
                """,
                "key_points": ["Match chart type to your goal", "Avoid 3D and excessive decoration", "Limit pie charts to 5-7 slices", "Consider your audience's familiarity"]
            },
            {
                "title": "Design Principles for Effective Visualizations",
                "content": """
**Universal Design Principles**

Good visualization design follows principles that make information clear and accessible.

**1. Simplicity (Data-Ink Ratio)**
Maximize the data shown, minimize unnecessary decoration.

| Good | Bad |
|------|-----|
| Clean gridlines | Heavy borders |
| Direct labels | Legends requiring lookup |
| White space | Crowded elements |
| Essential data only | Decorative graphics |

**2. Color Usage**

**Do:**
- Use color purposefully (highlight key data)
- Maintain contrast for readability
- Use colorblind-friendly palettes
- Keep consistent meaning (red = bad, green = good)

**Don't:**
- Use more than 5-7 colors
- Rely only on color to convey meaning
- Use red/green as only differentiator

**Colorblind-Safe Palettes:**
- Blue and Orange
- Blue and Yellow
- Purple and Green

**3. Typography**
- Use readable fonts (sans-serif for screens)
- Size hierarchy: Title > Subtitle > Labels > Annotations
- Left-align text for readability

**4. Layout and Hierarchy**
- Place the most important information prominently
- Use consistent alignment
- Group related elements
- Leave white space for breathing room

**5. Accessibility Checklist:**
- ✓ Sufficient color contrast
- ✓ Text alternatives for complex charts
- ✓ Clear titles and labels
- ✓ Logical reading order
                """,
                "key_points": ["Simplicity beats decoration", "Use color purposefully and accessibly", "Maintain consistent design language", "Design for accessibility from the start"]
            },
            {
                "title": "Telling Stories with Data",
                "content": """
**Data Storytelling**

The best visualizations tell a story that leads to action.

**Story Structure:**

```
SETUP      →  INSIGHT    →  ACTION
What is?      What matters?  What now?
```

**Components of a Data Story:**

1. **Context**: Why should the audience care?
2. **Conflict/Tension**: What's the problem or opportunity?
3. **Resolution**: What does the data reveal?
4. **Call to Action**: What should happen next?

**Example Data Story:**

**Context:** "Our customer satisfaction scores have been declining."

**Conflict:** "We analyzed 10,000 support tickets and found 60% mention 'wait time.'"

**Resolution:** [Show chart] "Wait times over 5 minutes correlate with 3x more negative reviews."

**Action:** "Investing in chat support could reduce wait times by 70% and recover our satisfaction scores."

**Presentation Tips:**

| Do | Don't |
|-----|--------|
| Start with the headline | Start with methodology |
| Build to the insight | Show all data at once |
| Use animation purposefully | Animate everything |
| Pause for questions | Rush through slides |
| Provide takeaway summary | End abruptly |

**Slideshow Best Practices:**
- One message per slide
- Maximum 6 data points per chart
- Include source citations
- Number slides for reference
- Provide handout with details
                """,
                "key_points": ["Lead with the insight, not the methodology", "Structure as setup → insight → action", "One message per visualization", "Always end with clear recommendations"]
            },
            {
                "title": "Visualization Tools and Software",
                "content": """
**Common Visualization Tools**

Different tools serve different purposes and skill levels.

**Tool Comparison:**

| Tool | Best For | Skill Level |
|------|----------|-------------|
| **Excel/Sheets** | Quick charts, basic dashboards | Beginner |
| **Tableau** | Interactive dashboards, exploration | Intermediate |
| **Power BI** | Microsoft integration, business dashboards | Intermediate |
| **Python (matplotlib, seaborn)** | Custom visualizations, automation | Advanced |
| **R (ggplot2)** | Statistical visualizations | Advanced |
| **D3.js** | Web-based custom visualizations | Expert |

**Excel/Google Sheets:**
- Quick and accessible
- Good for simple charts
- Limited interactivity
- Best for: Internal reports, quick analysis

**Tableau:**
- Drag-and-drop interface
- Excellent for exploration
- Interactive dashboards
- Best for: Business analytics, presentations

**Power BI:**
- Strong Microsoft 365 integration
- AI-powered insights
- Good for enterprise
- Best for: Corporate reporting, KPI dashboards

**Python Libraries:**
- matplotlib: Basic plotting
- seaborn: Statistical visualizations
- plotly: Interactive charts
- Best for: Reproducible analysis, automation

**Choosing Your Tool:**

Ask yourself:
1. What's my skill level?
2. What's my audience expecting?
3. Does it need to be interactive?
4. Will I need to update it regularly?
5. What tools does my organization use?
                """,
                "key_points": ["Match tool to skill level and need", "Excel works for quick, simple charts", "Tableau/Power BI for interactive dashboards", "Python for automation and reproducibility"]
            },
            {
                "title": "Ethics in Data Visualization",
                "content": """
**Ethical Visualization Practices**

Visualizations can mislead as easily as they inform. Ethical practice is essential.

**Common Manipulation Techniques (To Avoid):**

**1. Truncated Axes**
Starting a y-axis at a non-zero value exaggerates differences.

Example:
- Misleading: Bar chart showing 98% vs 100% with y-axis starting at 95%
- Honest: Same data with y-axis starting at 0%

**2. Cherry-Picking Time Frames**
Selecting dates that support your narrative.

Example:
- Misleading: "Sales doubled!" (comparing best month to worst)
- Honest: Show full year with context

**3. Missing Context**
Omitting comparison data or baselines.

Example:
- Misleading: "Crime up 50%!" (without population growth context)
- Honest: Show per-capita rates

**4. Aspect Ratio Manipulation**
Stretching charts to exaggerate or minimize trends.

**Ethical Guidelines:**

✓ Always start quantitative axes at zero (for bar charts)
✓ Include data sources
✓ Show uncertainty when relevant
✓ Provide appropriate time context
✓ Use consistent scales when comparing
✓ Acknowledge limitations
✓ Consider colorblind accessibility

**Questions to Ask Before Publishing:**

1. Does this accurately represent the data?
2. Could someone reasonably misinterpret this?
3. Am I being fair to all perspectives?
4. Would I be comfortable if this were fact-checked?
5. Does this serve the audience or my agenda?

**Your Responsibility:**
As a data analyst, you have power to influence decisions. Use visualization ethically to inform, not manipulate.
                """,
                "key_points": ["Avoid truncated axes and cherry-picked data", "Always provide context and sources", "Design for accurate interpretation", "Consider how visualizations might be misused"]
            }
        ],
        "exercises": [
            {
                "title": "Choose the Right Chart",
                "type": "scenario",
                "question": "You need to show how your company's market share has changed compared to 3 competitors over the past 5 years. What chart type would you use and why?",
                "answer": "Best choice: Stacked area chart or multiple line chart. The stacked area shows how the whole market (100%) is divided among competitors over time, making it easy to see both individual changes and relative positions. Alternatively, a multi-line chart works if you want to emphasize individual company trajectories. Avoid: Pie charts (only show one point in time), bar charts (harder to see trends), 3D charts (distort perception).",
                "hint": "Think about what you're showing: parts of a whole AND change over time"
            },
            {
                "title": "Identify Visualization Problems",
                "type": "practical",
                "question": "A chart shows monthly revenue with a y-axis starting at $950,000 instead of $0. The bars show $950K, $975K, and $1M for three months. What's wrong with this visualization?",
                "answer": "The truncated y-axis is misleading. By starting at $950K, the visual difference between bars is exaggerated. The $975K bar appears 50% taller than the $950K bar, when the actual difference is only 2.6% ($25K/$950K). The viewer's eye perceives much larger differences than exist in the data. Fix: Start the y-axis at $0, or use a different chart type (like a table with percentage change) if the small differences are truly significant.",
                "hint": "Calculate the actual percentage difference vs. how different the bars appear"
            },
            {
                "title": "Design for Accessibility",
                "type": "practical",
                "question": "Your dashboard uses red and green colors to show negative and positive values. A colleague mentions they're colorblind. How would you redesign this?",
                "answer": "Redesign solutions: 1) Use colorblind-friendly palette: Blue for negative, Orange for positive (distinguishable by most colorblind people). 2) Add icons/symbols: ▼ for negative, ▲ for positive (not relying on color alone). 3) Use patterns: Solid fill for positive, hatched/striped for negative. 4) Add text labels: Include actual values and +/- signs. 5) Use saturation: Keep same hue but vary brightness. Best practice: Combine color WITH another indicator (shape, pattern, or label) so information isn't conveyed by color alone.",
                "hint": "Don't rely solely on color to convey meaning - add redundant cues"
            }
        ],
        "quiz": [
            {
                "question": "Which chart is best for showing how a budget is divided among 5 departments?",
                "options": ["Line chart", "Scatter plot", "Pie chart", "Histogram"],
                "correct": 2,
                "explanation": "A pie chart shows parts of a whole, perfect for showing how a budget is divided. With only 5 categories, it remains readable. For more categories, consider a bar chart."
            },
            {
                "question": "What is wrong with starting a bar chart's y-axis at a non-zero value?",
                "options": ["It saves space", "It exaggerates visual differences", "It's standard practice", "It helps with small values"],
                "correct": 1,
                "explanation": "Starting at non-zero exaggerates differences, making small changes look dramatic. This can mislead viewers about the magnitude of differences."
            },
            {
                "question": "When presenting to executives, you should:",
                "options": ["Show all your data and methodology first", "Lead with the key insight and recommendation", "Use as many charts as possible", "Avoid simplifying complex data"],
                "correct": 1,
                "explanation": "Executives want the bottom line first. Lead with the insight and recommendation, then provide supporting data if asked. Don't make them wait for the conclusion."
            },
            {
                "question": "A colorblind-friendly visualization should:",
                "options": ["Only use shades of gray", "Rely solely on red and green", "Use color AND another indicator like shapes", "Avoid all color"],
                "correct": 2,
                "explanation": "Best practice is to use color AND another indicator (shapes, patterns, labels) so meaning isn't conveyed by color alone. This helps everyone, not just colorblind users."
            },
            {
                "question": "The 'data-ink ratio' principle suggests:",
                "options": ["Use more ink for important data", "Maximize decoration to engage viewers", "Remove unnecessary visual elements", "Add borders around all elements"],
                "correct": 2,
                "explanation": "Data-ink ratio (from Edward Tufte) means maximizing the data shown while minimizing non-essential 'ink' (decorations, heavy gridlines, unnecessary borders)."
            }
        ]
    },
    "Analysis Reporting Fundamentals": {
        "course": "Analysis Reporting",
        "description": "Learn report writing skills to present analytical work in professional documents for technical and non-technical audiences.",
        "lessons": [
            {
                "title": "Introduction to Analysis Reporting",
                "content": """
**Why Analysis Reports Matter**

A brilliant analysis is worthless if it can't be communicated effectively. Reports transform your findings into actionable documents.

**Key Purpose of Reports:**
- **Document findings**: Create permanent record of analysis
- **Enable decisions**: Provide information for stakeholders to act
- **Share knowledge**: Transfer insights across teams/organizations
- **Build credibility**: Establish you as a trusted analyst

**Report vs. Presentation:**

| Report | Presentation |
|--------|--------------|
| Comprehensive | Highlights only |
| Self-contained | Requires speaker |
| Reference document | One-time event |
| Detailed methodology | High-level overview |
| Read at reader's pace | Controlled timing |

**Types of Analysis Reports:**

| Type | Purpose | Audience | Length |
|------|---------|----------|--------|
| **Executive Summary** | Quick overview | Executives | 1-2 pages |
| **Technical Report** | Full methodology | Analysts | 10-30 pages |
| **Client Report** | Findings + recommendations | Clients | 5-15 pages |
| **Dashboard Report** | Ongoing metrics | Operations | 1-3 pages |
| **Ad-hoc Analysis** | Specific question | Requestor | 2-5 pages |

**The Report Writing Process:**

```
1. UNDERSTAND the audience and purpose
2. STRUCTURE the document logically
3. WRITE clearly and concisely
4. VISUALIZE data effectively
5. REVIEW and refine
6. DELIVER in appropriate format
```
                """,
                "key_points": ["Reports document and communicate findings", "Different report types serve different audiences", "Reports must be self-contained and actionable", "Writing process follows clear stages"]
            },
            {
                "title": "Report Structure and Organization",
                "content": """
**Standard Report Structure**

A well-organized report guides readers through your analysis logically.

**Essential Sections:**

**1. Executive Summary** (Write Last)
- Key findings in 1-2 paragraphs
- Main recommendations
- Critical numbers/metrics
- *Tip: Busy readers may only read this*

**2. Introduction/Background**
- Business context and problem statement
- Scope of analysis
- Data sources used
- Time period covered

**3. Methodology**
- How data was collected/cleaned
- Analysis techniques used
- Assumptions and limitations
- *Adjust detail level for audience*

**4. Findings**
- Present results clearly
- Use visualizations
- Organize by theme or priority
- Include supporting data

**5. Conclusions & Recommendations**
- What the findings mean
- Specific actions to take
- Expected impact of recommendations
- Next steps

**6. Appendix** (Optional)
- Detailed data tables
- Technical methodology
- Supplementary charts
- Glossary of terms

**Organization Tips:**

| Do | Don't |
|-----|--------|
| Use numbered sections | Use vague headings |
| Include table of contents (>5 pages) | Bury key findings |
| Put most important info first | Make readers hunt for answers |
| Use consistent formatting | Change styles mid-document |
                """,
                "key_points": ["Follow standard report structure", "Write executive summary last", "Adjust detail level for audience", "Put most important information first"]
            },
            {
                "title": "Academic Writing for Reports",
                "content": """
**Professional Writing Style**

Analysis reports require clear, professional language that builds credibility.

**Key Principles:**

**1. Clarity Over Complexity**
- Use simple words when possible
- Short sentences (15-20 words average)
- One idea per paragraph
- Active voice preferred

**Bad:** "The utilization of advanced analytical methodologies facilitated the identification of correlational patterns."
**Good:** "Our analysis found a strong link between marketing spend and sales."

**2. Be Precise and Specific**

| Vague | Precise |
|-------|---------|
| "Sales increased significantly" | "Sales increased 23% ($1.2M)" |
| "Most customers prefer..." | "67% of customers prefer..." |
| "Recently" | "In Q3 2025" |
| "Some improvement" | "15% improvement" |

**3. Objective Tone**
- State facts, not opinions
- Support claims with data
- Acknowledge limitations
- Avoid emotional language

**Bad:** "Clearly, the amazing results prove our strategy works perfectly."
**Good:** "Results show a 23% increase, suggesting the strategy is effective. Further testing is recommended."

**4. Consistent Terminology**
- Define terms on first use
- Use same word for same concept
- Create glossary if needed
- Avoid jargon with non-technical audiences

**5. Hedging Appropriately**
When certainty is limited, use appropriate hedging:
- "The data suggests..." (not "proves")
- "This may indicate..."
- "Based on available data..."
- "Further analysis would be needed to confirm..."

**Common Phrases for Reports:**

| Purpose | Phrases |
|---------|---------|
| Introducing findings | "The analysis reveals...", "Data indicates..." |
| Comparing | "In contrast...", "Similarly...", "However..." |
| Recommending | "We recommend...", "Consider...", "The next step is..." |
| Concluding | "In summary...", "The key takeaway is..." |
                """,
                "key_points": ["Clarity and precision over complexity", "Use specific numbers, not vague terms", "Maintain objective, professional tone", "Define terms and be consistent"]
            },
            {
                "title": "Integrating Visualizations in Reports",
                "content": """
**Using Graphics Effectively in Reports**

Static visualizations in reports differ from interactive dashboards - they must stand alone on paper.

**Principles for Report Graphics:**

**1. Every Chart Needs Context**
- Descriptive title (not just "Figure 1")
- Axis labels and units
- Source citation
- Brief caption explaining the insight

**Example:**
✅ "Figure 3: Monthly Revenue Growth (2024-2025). Revenue increased 45% year-over-year, with Q4 showing the strongest growth."

❌ "Figure 3: Revenue"

**2. Design for Print**
- High resolution (300 DPI minimum)
- Readable when printed in grayscale
- Sufficient font size (10pt minimum)
- No interactive elements (obviously!)

**3. Placement Guidelines**

| Rule | Reason |
|------|--------|
| Place near related text | Easy reference |
| Don't split across pages | Visual integrity |
| Consistent sizing | Professional appearance |
| White space around graphics | Readability |

**4. Reference Charts in Text**
Always mention figures in your narrative:
- "As shown in Figure 2, sales peaked in December..."
- "The correlation (see Figure 4) suggests..."

**5. Chart Selection for Static Reports**

| Works Well in Reports | Avoid in Reports |
|----------------------|------------------|
| Bar charts | Complex interactive charts |
| Line charts | Animations |
| Pie charts (limited) | Overly detailed maps |
| Tables | Charts requiring zoom |
| Simple scatter plots | 3D charts |

**Caption Writing:**

A good caption includes:
1. Figure number
2. Descriptive title
3. Key insight or takeaway
4. Data source (if not stated elsewhere)

**Example:**
"Figure 5: Customer Satisfaction Scores by Region (Q4 2025). The North region scored 15% higher than the company average, while the South region needs attention. Source: Customer Survey, n=2,500."
                """,
                "key_points": ["Every visualization needs context and caption", "Design for print (high resolution, grayscale-friendly)", "Reference all figures in the text", "Place visuals near related content"]
            },
            {
                "title": "Universal Design and Accessibility",
                "content": """
**Creating Accessible Reports**

Reports should be usable by everyone, including people with disabilities.

**Universal Design Principles:**

**1. Visual Accessibility**

**Color:**
- Don't rely solely on color to convey meaning
- Ensure sufficient contrast (4.5:1 ratio)
- Use colorblind-friendly palettes
- Provide text alternatives

**Fonts:**
- Sans-serif fonts for screens (Arial, Calibri)
- Minimum 11pt body text, 10pt for tables
- Avoid all-caps for long text
- Adequate line spacing (1.15-1.5)

**2. Document Structure**
- Use heading styles (not just bold text)
- Logical heading hierarchy (H1 → H2 → H3)
- Include table of contents for long documents
- Number sections consistently

**3. Table Accessibility**

| Accessible | Not Accessible |
|-----------|----------------|
| Header row identified | No headers |
| Simple structure | Merged cells |
| Reading order clear | Complex nesting |
| Alt text for table | No description |

**4. Alternative Text for Images**
- Describe what the image shows
- Include key data points
- Explain the insight
- Keep under 125 characters

**Good Alt Text:**
"Bar chart showing Q4 sales by region: North $2.3M, South $1.8M, East $2.1M, West $1.5M. North leads by 28%."

**5. Document Format**
- Use accessible PDF settings
- Include bookmarks for navigation
- Tag document structure
- Test with screen reader

**Accessibility Checklist:**
- ✓ Color contrast meets standards
- ✓ All images have alt text
- ✓ Tables have headers identified
- ✓ Document uses heading styles
- ✓ Links have descriptive text
- ✓ Font size is readable
- ✓ Content order is logical
                """,
                "key_points": ["Design for all users, including those with disabilities", "Use proper heading structure and document tags", "Provide alt text for all visuals", "Test accessibility before distribution"]
            },
            {
                "title": "Report Tools and Distribution",
                "content": """
**Tools for Creating Reports**

Different tools suit different needs and organizational contexts.

**Common Report Tools:**

| Tool | Best For | Pros | Cons |
|------|----------|------|------|
| **Microsoft Word** | Traditional reports | Universal, familiar | Manual formatting |
| **Google Docs** | Collaborative work | Real-time collaboration | Limited offline |
| **LaTeX** | Technical/academic | Professional typography | Steep learning curve |
| **Jupyter/RMarkdown** | Reproducible reports | Code + narrative | Technical audience |
| **Power BI/Tableau** | Dashboard reports | Interactive | Export limitations |

**Word/Google Docs Tips:**
- Use styles for consistency
- Set up templates for repeated reports
- Use section breaks for different headers/footers
- Enable track changes for review

**Distribution Formats:**

| Format | When to Use |
|--------|-------------|
| **PDF** | Final distribution, archival |
| **Word/Doc** | Collaborative editing |
| **HTML** | Web publishing |
| **Print** | Formal presentations |

**Version Control:**
- Include version number in filename
- Date all versions: "Report_v2_2025-01-02.pdf"
- Keep track of what changed
- Archive final versions

**Review Process:**

Before distributing:
1. **Self-review**: Read aloud, check for errors
2. **Peer review**: Fresh eyes catch mistakes
3. **Stakeholder preview**: Ensure alignment
4. **Final proofread**: Spelling, formatting, links

**Quality Checklist:**
- ✓ Spelling and grammar checked
- ✓ All figures numbered and referenced
- ✓ Page numbers included
- ✓ Headers/footers consistent
- ✓ Links working
- ✓ Data is current
- ✓ Recommendations are clear
- ✓ Executive summary matches content
                """,
                "key_points": ["Choose tools based on audience and collaboration needs", "Use templates for consistency", "Follow clear version control practices", "Always review before distribution"]
            },
            {
                "title": "Ethical Report Writing",
                "content": """
**Ethics in Analysis Reporting**

As a report writer, you have responsibility for how information is presented and interpreted.

**Core Ethical Principles:**

**1. Accuracy**
- Report data truthfully
- Don't cherry-pick favorable results
- Acknowledge limitations and uncertainties
- Correct errors promptly

**2. Transparency**
- Disclose methodology
- Note data sources
- Explain assumptions
- Reveal conflicts of interest

**3. Fairness**
- Present balanced findings
- Include context that might change interpretation
- Consider multiple stakeholder perspectives
- Don't misrepresent others' views

**Common Ethical Pitfalls:**

| Pitfall | Example | How to Avoid |
|---------|---------|--------------|
| Cherry-picking | Only showing favorable quarters | Show full time period |
| Misleading visuals | Truncated axes | Follow visualization ethics |
| Omitting context | "Sales up 50%!" (from very low base) | Provide absolute numbers too |
| Overstating certainty | "This proves..." | Use appropriate hedging |
| Burying bad news | Hiding problems in appendix | Address issues directly |

**Client vs. Truth:**

What if findings are unfavorable to the client?

**Ethical approach:**
1. Present findings accurately
2. Provide context and explanation
3. Suggest constructive next steps
4. Never falsify or hide data

**Handling Pressure:**
- "Can you make these numbers look better?"
- "Can we leave out this part?"
- "The client won't like this finding"

**Response:**
- Explain why accuracy matters
- Offer alternative framing (not falsification)
- Escalate if pressured to be unethical
- Document requests in writing

**Attribution and Sources:**
- Cite data sources properly
- Credit others' work
- Respect data privacy
- Follow licensing requirements

**The Golden Rule:**
Would you be comfortable if your methodology and decisions were reviewed by a neutral third party? If not, reconsider your approach.
                """,
                "key_points": ["Report data accurately, even unfavorable findings", "Be transparent about methodology and limitations", "Don't mislead through omission or framing", "Maintain professional integrity under pressure"]
            }
        ],
        "exercises": [
            {
                "title": "Rewrite for Clarity",
                "type": "practical",
                "question": "Rewrite this sentence for a non-technical audience: 'The multivariate regression analysis yielded a statistically significant coefficient (β=0.43, p<0.01) for the marketing expenditure variable, indicating a positive relationship with sales outcomes.'",
                "answer": "Clear version: 'Our analysis found that marketing spending has a strong positive effect on sales. For every additional $1,000 spent on marketing, sales increased by approximately $430. This relationship is statistically reliable.' Key improvements: 1) Removed jargon (multivariate regression, coefficient, β, p-value). 2) Explained what the numbers mean practically. 3) Used plain language. 4) Kept the essential insight while making it accessible.",
                "hint": "Replace technical terms with plain language, and explain what the finding means for the business"
            },
            {
                "title": "Structure an Executive Summary",
                "type": "scenario",
                "question": "You've completed an analysis showing that customer churn increased 25% last quarter, mainly due to slow support response times (average 4 hours vs. competitor's 30 minutes). You recommend investing $50K in a chat support system. Write bullet points for the executive summary.",
                "answer": "Executive Summary bullet points: KEY FINDING: Customer churn increased 25% last quarter, costing an estimated $200K in lost annual revenue. ROOT CAUSE: Support response time (4 hours) is 8x slower than industry average (30 minutes). Analysis of 500 exit surveys found 'slow support' cited as primary reason by 67% of churned customers. RECOMMENDATION: Implement chat support system ($50K investment). Expected outcomes: Reduce response time to under 30 minutes, reduce churn by 15-20%, ROI within 4 months based on reduced customer loss. NEXT STEPS: Vendor selection and pilot program in Q2. Note: This structure gives busy executives: the problem, the cause, the solution, and expected results in under 100 words.",
                "hint": "Include: the problem, the cause, the recommended solution, and expected outcomes"
            },
            {
                "title": "Write Alt Text for a Chart",
                "type": "practical",
                "question": "Write appropriate alt text for a bar chart showing quarterly revenue: Q1 $1.2M, Q2 $1.4M, Q3 $1.8M, Q4 $2.1M. The chart highlights that Q4 was the highest.",
                "answer": "Good alt text options: Option 1 (brief): 'Bar chart showing quarterly revenue growth: Q1 $1.2M, Q2 $1.4M, Q3 $1.8M, Q4 $2.1M. Q4 represents 75% growth from Q1.' Option 2 (detailed): 'Vertical bar chart displaying 2025 quarterly revenue. Revenue grew each quarter: Q1 at $1.2M, Q2 at $1.4M (17% increase), Q3 at $1.8M (29% increase), and Q4 reaching $2.1M (17% increase). Q4 is highlighted as the highest quarter, representing total annual growth of 75% from Q1 to Q4.' Key elements: Describes chart type, provides all data values, explains the key insight, quantifies the main finding.",
                "hint": "Include the chart type, the data values, and the key insight someone should take away"
            }
        ],
        "quiz": [
            {
                "question": "Which section should you write LAST in a report?",
                "options": ["Introduction", "Methodology", "Executive Summary", "Appendix"],
                "correct": 2,
                "explanation": "The Executive Summary should be written last because it summarizes the entire report. You can't summarize what you haven't written yet."
            },
            {
                "question": "When writing for non-technical audiences, you should:",
                "options": ["Use technical terms to show expertise", "Replace jargon with plain language", "Include all statistical details", "Avoid numbers entirely"],
                "correct": 1,
                "explanation": "Replace jargon with plain language. Technical terms create barriers. You can still include important numbers, but explain what they mean practically."
            },
            {
                "question": "Alt text for images in reports should:",
                "options": ["Just say 'Figure 1'", "Describe the visual and key insight", "Only be used for decorative images", "Repeat the caption exactly"],
                "correct": 1,
                "explanation": "Alt text should describe what the image shows and convey the key insight, making the content accessible to screen reader users and providing value if images don't load."
            },
            {
                "question": "If your analysis findings are unfavorable to the client, you should:",
                "options": ["Hide them in the appendix", "Present them accurately with context", "Change the numbers to be more positive", "Leave them out entirely"],
                "correct": 1,
                "explanation": "Present findings accurately with appropriate context. Hiding or falsifying results is unethical. You can frame findings constructively and suggest solutions."
            },
            {
                "question": "The minimum font size recommended for body text in reports is:",
                "options": ["8pt", "11pt", "14pt", "18pt"],
                "correct": 1,
                "explanation": "11pt is the recommended minimum for body text to ensure readability. Tables can go to 10pt, but anything smaller becomes difficult to read."
            }
        ]
    },
    "Exam Project 1 - Professional Data Analysis": {
        "course": "Exam Project 1",
        "description": "Develop skills to execute a comprehensive data analysis project from start to finish with professional standards, including project planning, execution, documentation, and presentation.",
        "lessons": [
            {
                "title": "Understanding the Exam Project",
                "content": """
**What is Exam Project 1?**

This is a major project that demonstrates all the competencies you've acquired during your first academic year. It reflects your ability to independently execute a complete data analysis project.

**Project Options:**
- **Individual Project**: Work independently on a self-chosen or assigned problem
- **Group Project**: Collaborate in a team (2-4 members)
- **Internship Project**: Work with a real company on an actual business problem (encouraged!)

**Project Scope:**
Your project must include:
1. **Problem Definition**: Clear statement of what you're solving
2. **Data Collection**: Ethically sourced, relevant data
3. **Analysis**: Using tools and techniques from Semester 1-2
4. **Visualization**: Clear, accessible charts and reports
5. **Recommendations**: Actionable insights for stakeholders

**Industry Standards:**
- Professional documentation
- Deadline compliance
- Efficient workflows
- Clear communication
- Quality deliverables

**Key Success Factors:**
- Plan thoroughly before starting
- Manage time effectively
- Document all decisions
- Communicate regularly with supervisors
- Focus on quality over quantity
                """,
                "key_points": ["Major project demonstrating all first-year skills", "Can be individual, group, or internship-based", "Must follow professional standards", "Documentation and communication are critical"]
            },
            {
                "title": "Project Planning & Scoping",
                "content": """
**Effective Project Planning**

Good planning is the foundation of successful project execution.

**1. Defining Your Problem**

Ask these questions:
- What business question am I answering?
- Who will use my findings?
- What decisions will this support?
- What does success look like?

**Problem Statement Template:**
"[Organization] needs to understand [topic] in order to [action]. This analysis will examine [data] to provide [deliverable] by [deadline]."

**Example:**
"TechCorp needs to understand customer churn patterns in order to improve retention strategies. This analysis will examine 2 years of customer data to provide a retention recommendation report by March 15."

**2. Scoping Your Project**

**In Scope vs. Out of Scope:**

| In Scope | Out of Scope |
|----------|--------------|
| Questions you WILL answer | Questions for future work |
| Data sources you WILL use | Data you won't access |
| Tools you WILL apply | Tools beyond your skills |
| Time period covered | Historical extensions |

**3. Timeline Planning**

Recommended time allocation:
- **Planning & Research**: 15-20%
- **Data Collection & Cleaning**: 20-25%
- **Analysis & Exploration**: 25-30%
- **Reporting & Visualization**: 20-25%
- **Review & Finalization**: 10-15%

**4. Milestone Setting**

Create checkpoints:
- Week 2: Problem defined, data sources identified
- Week 4: Data collected and cleaned
- Week 6: Initial analysis complete
- Week 8: Draft report ready
- Week 10: Final submission

**Risk Planning:**
- What could go wrong?
- What's your backup plan?
- Who can help if you're stuck?
                """,
                "key_points": ["Define clear problem statements", "Explicitly scope what's in and out", "Allocate time realistically", "Set milestones and prepare for risks"]
            },
            {
                "title": "Working with Real-World Data",
                "content": """
**Finding and Using Real Data**

For your exam project, you'll work with real-world data—either from an internship partner or publicly available sources.

**Internship Projects (Recommended)**

Benefits:
- Real business problems
- Mentorship from professionals
- Industry experience for your CV
- Networking opportunities

Finding internship projects:
- Approach local businesses
- Use school connections
- Check company internship programs
- Reach out to alumni

**Public Data Sources**

If not doing an internship:
- **Statistics Norway (SSB)**: Norwegian economic/demographic data
- **Kaggle**: Curated datasets for analysis
- **EU Open Data Portal**: European datasets
- **World Bank**: Global development data
- **Government Open Data**: Many countries publish data

**Ethical Data Sourcing**

Remember your GDPR and ethics training:
- ✓ Ensure you have permission to use the data
- ✓ Anonymize personal information
- ✓ Document data sources properly
- ✓ Check licensing requirements
- ✗ Don't scrape data without permission
- ✗ Don't use data for unintended purposes

**Data Quality Assessment**

Before starting analysis:
1. How complete is the data?
2. What's the time period covered?
3. Are there obvious errors or outliers?
4. Is the sample representative?
5. What transformations are needed?

**Documenting Your Data**

Create a data dictionary:
| Field | Type | Description | Source | Notes |
|-------|------|-------------|--------|-------|
| customer_id | Integer | Unique identifier | CRM | Primary key |
| revenue | Decimal | Monthly revenue | Finance DB | In NOK |
                """,
                "key_points": ["Internship projects provide valuable real-world experience", "Many public data sources are available", "Always source data ethically and legally", "Document data thoroughly"]
            },
            {
                "title": "Executing Your Analysis",
                "content": """
**Applying Your Skills**

Your exam project is where you demonstrate mastery of all first-year skills.

**Tools & Techniques to Apply:**

**From Spreadsheet Fundamentals:**
- Data cleaning in Excel/Sheets
- Pivot tables for summarization
- Formulas for calculations
- Charts for visualization

**From Statistical Tools:**
- Descriptive statistics
- Correlation analysis
- Z-scores for outlier detection
- Hypothesis testing (if applicable)

**From Programming Fundamentals:**
- Python for data manipulation
- pandas for DataFrames
- Automated data cleaning
- Reproducible analysis scripts

**From Databases:**
- SQL queries for data extraction
- Joining multiple data sources
- Aggregations and groupings

**From Data Visualization:**
- Choosing appropriate chart types
- Following design principles
- Creating accessible visualizations
- Building dashboards

**Analysis Workflow:**

1. **Explore**: Understand your data
   - Summary statistics
   - Initial visualizations
   - Pattern identification

2. **Clean**: Prepare for analysis
   - Handle missing values
   - Fix errors
   - Standardize formats

3. **Analyze**: Answer your questions
   - Apply appropriate methods
   - Document your approach
   - Validate findings

4. **Interpret**: Extract meaning
   - What do the results mean?
   - What's actionable?
   - What are the limitations?

**Common Pitfalls:**
- Starting analysis before understanding the data
- Skipping data cleaning
- Not documenting your process
- Overcomplicating the analysis
- Ignoring limitations
                """,
                "key_points": ["Apply all tools learned in Semester 1-2", "Follow a systematic analysis workflow", "Document your process thoroughly", "Avoid common analysis pitfalls"]
            },
            {
                "title": "Professional Documentation",
                "content": """
**Documentation Standards**

Professional documentation distinguishes student work from industry-ready deliverables.

**What to Document:**

**1. Project Documentation**
- Project plan and timeline
- Scope and objectives
- Stakeholder requirements
- Risk assessment

**2. Technical Documentation**
- Data dictionary
- Methodology description
- Code comments
- Version history

**3. Analysis Documentation**
- Decisions made and why
- Assumptions stated
- Limitations acknowledged
- Findings validated

**Report Structure (from Analysis Reporting course):**

1. **Executive Summary**: Key findings for decision-makers
2. **Introduction**: Problem context and objectives
3. **Methodology**: How you approached the analysis
4. **Data Description**: Sources, preparation, limitations
5. **Findings**: Results with visualizations
6. **Recommendations**: Actionable next steps
7. **Appendix**: Technical details, additional charts

**Professional Writing Tips:**

- Write for your audience (technical vs. non-technical)
- Use clear, concise language
- Support claims with evidence
- Include visualizations effectively
- Proofread carefully

**Version Control:**

Even for solo projects:
- Use meaningful file names
- Track major changes
- Keep backups
- Document what changed

**Example naming:**
`project_report_v1.0_2025-03-10.docx`
`analysis_script_v2_cleaned_data.py`
                """,
                "key_points": ["Document project, technical, and analysis aspects", "Follow professional report structure", "Write clearly for your audience", "Maintain version control"]
            },
            {
                "title": "Presentation & Defense",
                "content": """
**Presenting Your Project**

Your exam includes presenting your work to evaluators. This is your chance to demonstrate both technical competence and communication skills.

**Presentation Structure:**

**1. Opening (2 minutes)**
- Introduce yourself and project
- State the problem you solved
- Hook the audience with a key finding

**2. Context (3 minutes)**
- Business background
- Why this matters
- Your objectives

**3. Methodology (3 minutes)**
- Data sources used
- Tools and techniques applied
- Key decisions made

**4. Findings (5 minutes)**
- Main results with visuals
- Insights discovered
- Patterns identified

**5. Recommendations (3 minutes)**
- Actionable suggestions
- Expected impact
- Next steps

**6. Conclusion (2 minutes)**
- Summary of key points
- Lessons learned
- Questions invitation

**Presentation Tips:**

**Visual Design:**
- One key message per slide
- Minimal text, maximum visuals
- Consistent formatting
- Readable fonts (18pt minimum)

**Delivery:**
- Practice out loud multiple times
- Time yourself
- Prepare for questions
- Speak to the audience, not slides

**Handling Questions:**

Common question types:
- "Why did you choose this approach?"
- "What were the limitations?"
- "What would you do differently?"
- "How confident are you in these findings?"

Answering strategies:
- Pause before answering
- Be honest about limitations
- Refer to your documentation
- Say "I don't know" if needed, then explain how you'd find out

**Professional Terminology:**

Use appropriate industry language:
- "The analysis revealed..." (not "I found...")
- "The data suggests..." (not "It's obvious that...")
- "I recommend..." (not "You should...")
- "Within the scope of this project..." (acknowledging limits)
                """,
                "key_points": ["Structure presentation logically", "Practice delivery multiple times", "Prepare for tough questions", "Use professional terminology"]
            },
            {
                "title": "Quality & Self-Assessment",
                "content": """
**Ensuring Quality**

Before submission, critically assess your own work against professional standards.

**Quality Checklist:**

**Project Execution:**
- ☐ Problem clearly defined and scoped
- ☐ Data sourced ethically
- ☐ Methodology appropriate for the problem
- ☐ Analysis thorough and documented
- ☐ Findings validated

**Technical Quality:**
- ☐ Data cleaned properly
- ☐ Calculations verified
- ☐ Code/formulas documented
- ☐ No obvious errors
- ☐ Reproducible process

**Report Quality:**
- ☐ Clear executive summary
- ☐ Logical structure
- ☐ Visualizations accessible
- ☐ Recommendations actionable
- ☐ Proofread for errors

**Presentation Quality:**
- ☐ Within time limit
- ☐ Key points clear
- ☐ Visuals readable
- ☐ Prepared for questions

**Self-Reflection Questions:**

Ask yourself:
1. Did I answer the original question?
2. Would a stakeholder find this useful?
3. Are my conclusions supported by evidence?
4. Did I acknowledge limitations honestly?
5. What would I do differently next time?

**Common Issues to Check:**

| Issue | How to Check |
|-------|--------------|
| Missing data handling | Document all decisions |
| Overclaiming | Review language for hedging |
| Unclear visuals | Show to someone unfamiliar |
| Weak recommendations | Are they specific and actionable? |
| Poor time management | Compare to original plan |

**Getting Feedback:**

Before submission:
- Have a peer review your work
- Ask your supervisor for input
- Read your report from the audience's perspective
- Practice your presentation with feedback

**After Submission:**

Document lessons learned:
- What went well?
- What was challenging?
- What skills do you need to develop?
- How will you apply this experience?
                """,
                "key_points": ["Use quality checklists before submission", "Self-assess honestly against standards", "Get feedback from peers and supervisors", "Document lessons learned for future projects"]
            }
        ],
        "exercises": [
            {
                "title": "Write a Problem Statement",
                "type": "practical",
                "question": "A local restaurant chain (5 locations) has noticed declining customer visits over the past 6 months. They have data on daily sales, customer reviews, and competitor activity. Write a clear problem statement for a data analysis project.",
                "answer": "Strong problem statement: 'Restaurant Group Oslo needs to understand the drivers of declining customer visits over the past 6 months in order to develop strategies to reverse the trend. This analysis will examine daily sales data, customer review sentiment, and competitor activity across all 5 locations to identify patterns and provide actionable recommendations by [deadline]. The project will focus on identifying which locations are most affected, what time periods show the greatest decline, and whether customer feedback reveals specific issues.' This statement includes: who needs the analysis, what question needs answering, what data will be used, what the deliverable is, and the scope boundaries.",
                "hint": "Include: who, what problem, what data, what deliverable, and any scope boundaries"
            },
            {
                "title": "Create a Project Timeline",
                "type": "scenario",
                "question": "You have 8 weeks to complete your exam project analyzing e-commerce sales data. Create a timeline with phases and milestones, allocating appropriate percentages of time.",
                "answer": "8-Week Project Timeline: WEEK 1-2 (25%): Planning & Data Collection - Week 1: Define problem, identify stakeholders, scope project, create project plan. Week 2: Obtain data access, initial data exploration, create data dictionary. Milestone: Project plan approved, data ready. WEEK 3-4 (25%): Data Cleaning & Preparation - Week 3: Clean data, handle missing values, fix errors. Week 4: Transform data for analysis, validate quality. Milestone: Clean dataset documented. WEEK 5-6 (25%): Analysis & Visualization - Week 5: Exploratory analysis, identify patterns. Week 6: Deep analysis, create visualizations. Milestone: Key findings identified. WEEK 7 (12.5%): Reporting - Draft report, integrate visualizations, write recommendations. Milestone: Draft report for review. WEEK 8 (12.5%): Review & Finalize - Peer review, revisions, finalize presentation, submit. Milestone: Final submission. Buffer: Built into each phase for unexpected issues.",
                "hint": "Consider the recommended percentages: Planning 15-20%, Data prep 20-25%, Analysis 25-30%, Reporting 20-25%, Review 10-15%"
            },
            {
                "title": "Prepare for Tough Questions",
                "type": "scenario",
                "question": "During your project presentation, an evaluator asks: 'Your sample size is only 500 customers out of 10,000. How confident can we be in your findings?' How would you respond professionally?",
                "answer": "Professional response: 'That's an important consideration. Our sample of 500 customers represents 5% of the total customer base, which provides a statistically meaningful sample with approximately a 4% margin of error at 95% confidence. The sample was selected randomly to ensure representativeness. I verified the sample demographics matched the overall customer base in terms of age distribution, location, and purchase history. While a larger sample would increase precision, the patterns we identified—particularly the 25% difference in satisfaction between segments—are well above the margin of error, giving us confidence in the directional findings. In the recommendations section, I've noted that implementing changes with a pilot group would allow validation before full rollout.' Key elements: 1) Acknowledge the valid concern, 2) Explain your methodology, 3) Quantify the confidence level, 4) Note limitations, 5) Suggest mitigation.",
                "hint": "Acknowledge the concern, explain your reasoning, quantify confidence, note limitations, suggest mitigation"
            }
        ],
        "quiz": [
            {
                "question": "What percentage of project time should typically be allocated to planning and research?",
                "options": ["5-10%", "15-20%", "40-50%", "60-70%"],
                "correct": 1,
                "explanation": "15-20% is the recommended allocation for planning and research. Rushing into analysis without proper planning often leads to wasted effort later."
            },
            {
                "question": "What type of project is encouraged for Exam Project 1?",
                "options": ["Theoretical research", "Internship with a real company", "Simulation exercise", "Literature review"],
                "correct": 1,
                "explanation": "Internship projects are encouraged as they provide real-world experience, professional mentorship, and practical skills that enhance your employability."
            },
            {
                "question": "When presenting findings, you should:",
                "options": ["Use as much technical jargon as possible", "Lead with the most important finding", "Save conclusions for the very end", "Avoid mentioning limitations"],
                "correct": 1,
                "explanation": "Lead with the most important finding to immediately engage your audience. Technical jargon should be minimized, conclusions should be clear throughout, and limitations should be acknowledged honestly."
            },
            {
                "question": "A good problem statement should include:",
                "options": ["Only the data sources available", "The organization, question, and deliverable", "Just the deadline", "Technical methodology details"],
                "correct": 1,
                "explanation": "A good problem statement includes who needs the analysis (organization), what question needs answering, and what the deliverable will be. Methodology comes later in planning."
            },
            {
                "question": "Before submitting your project, you should:",
                "options": ["Skip peer review to save time", "Only check for spelling errors", "Use a quality checklist and get feedback", "Assume everything is correct"],
                "correct": 2,
                "explanation": "Using a quality checklist and getting feedback from peers helps catch errors and improve your work. Never skip the review phase—fresh eyes often spot issues you've missed."
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

# Initialize new features session state
if 'study_notes' not in st.session_state:
    st.session_state.study_notes = {}
if 'flashcards' not in st.session_state:
    st.session_state.flashcards = {}
if 'flashcard_stats' not in st.session_state:
    st.session_state.flashcard_stats = {"total_cards": 0, "cards_reviewed": 0, "cards_mastered": 0}
if 'exam_mode' not in st.session_state:
    st.session_state.exam_mode = False
if 'exam_questions' not in st.session_state:
    st.session_state.exam_questions = []
if 'exam_answers' not in st.session_state:
    st.session_state.exam_answers = {}
if 'exam_start_time' not in st.session_state:
    st.session_state.exam_start_time = None
if 'code_snippets' not in st.session_state:
    st.session_state.code_snippets = {}
if 'study_timer_active' not in st.session_state:
    st.session_state.study_timer_active = False
if 'study_timer_start' not in st.session_state:
    st.session_state.study_timer_start = None
if 'study_timer_duration' not in st.session_state:
    st.session_state.study_timer_duration = 0
if 'study_sessions' not in st.session_state:
    st.session_state.study_sessions = []
if 'study_time_by_course' not in st.session_state:
    st.session_state.study_time_by_course = {}

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
    ["Overview", "Course Plan", "Training Center", "Playground", "Learn & Practice", 
     "Study Notes", "Flashcards", "Exam Simulator", "Code Library", "Formula Reference", 
     "Study Timer", "Progress", "Learning Outcomes", "About"]
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
    
    # Organize topics by semester and course (with official course codes)
    course_to_semester = {
        "Data Analysis Fundamentals": ("Semester 1", "FI1BBDF05"),
        "Spreadsheet Fundamentals": ("Semester 1", "FI1BBSF05"),
        "Statistical Tools": ("Semester 1", "FI1BBST05"),
        "Programming Fundamentals": ("Semester 1", "FI1BBPF20"),
        "Databases and Cloud Services": ("Semester 2", "FI1BBDC20"),
        "Data Visualisation": ("Semester 2", "FI1BBDV15"),
        "Data Driven Decision-Making": ("Semester 2", "FI1BBDD75"),
        "Semester Project 1": ("Semester 2", "FI1BBP175"),
        "Evaluation of Outcomes": ("Semester 3", "FI1BBEO10")
    }
    
    # Group topics by semester and course
    organized_topics = {}
    for topic, module_data in training_modules.items():
        course = module_data['course']
        if course in course_to_semester:
            semester, code = course_to_semester[course]
        else:
            semester, code = "Other", ""
        
        if semester not in organized_topics:
            organized_topics[semester] = {}
        if course not in organized_topics[semester]:
            organized_topics[semester][course] = {"code": code, "topics": []}
        organized_topics[semester][course]["topics"].append(topic)
    
    # Create formatted options with grouping
    st.markdown("### Choose a Topic to Learn")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Semester filter
        available_semesters = sorted(organized_topics.keys())
        selected_semester = st.selectbox(
            "📅 Semester:",
            options=["All Semesters"] + available_semesters
        )
    
    with col2:
        # Course filter based on semester (with course codes)
        if selected_semester == "All Semesters":
            all_courses = []
            for sem in available_semesters:
                for course in organized_topics[sem].keys():
                    if course not in all_courses:
                        all_courses.append(course)
            available_courses = all_courses
        else:
            available_courses = list(organized_topics[selected_semester].keys())
        
        # Create display names with course codes
        course_display_map = {}
        for course in available_courses:
            if course in course_to_semester:
                code = course_to_semester[course][1]
                display = f"{code} - {course}"
            else:
                display = course
            course_display_map[display] = course
        
        course_options = ["All Courses"] + list(course_display_map.keys())
        selected_course_display = st.selectbox(
            "📚 Course:",
            options=course_options
        )
        
        # Map back to actual course name
        if selected_course_display == "All Courses":
            selected_course = "All Courses"
        else:
            selected_course = course_display_map[selected_course_display]
    
    # Get filtered topics
    filtered_topics = []
    for semester, courses in organized_topics.items():
        if selected_semester != "All Semesters" and semester != selected_semester:
            continue
        for course, data in courses.items():
            if selected_course != "All Courses" and course != selected_course:
                continue
            for topic in data["topics"]:
                # Format: "Topic Name (Course - Semester)"
                display_name = f"{topic}"
                filtered_topics.append((display_name, topic, course, semester))
    
    # Sort by semester, then course, then topic
    semester_order = {"Semester 1": 1, "Semester 2": 2, "Semester 3": 3, "Semester 4": 4, "Other": 5}
    filtered_topics.sort(key=lambda x: (semester_order.get(x[3], 99), x[2], x[0]))
    
    if not filtered_topics:
        st.warning("No topics found for the selected filters.")
        st.stop()
    
    # Create display options with context
    topic_options = []
    for display, topic, course, semester in filtered_topics:
        topic_options.append(f"{topic}")
    
    # Show topic count
    st.caption(f"📖 {len(filtered_topics)} topics available")
    
    selected_display = st.selectbox(
        "🎯 Select Topic:",
        options=topic_options,
        format_func=lambda x: x
    )
    
    # Find the actual topic
    selected_topic = selected_display
    
    # Find course and semester for display
    topic_course = None
    topic_semester = None
    for display, topic, course, semester in filtered_topics:
        if topic == selected_topic:
            topic_course = course
            topic_semester = semester
            break
    
    module = training_modules[selected_topic]
    
    # Get course code for display
    topic_code = ""
    if topic_course and topic_course in course_to_semester:
        topic_code = course_to_semester[topic_course][1]
    
    # Show context with course code
    st.markdown(f"**📅 {topic_semester}** | **📚 {topic_code} - {topic_course}**")
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

elif page == "Study Notes":
    st.markdown("""
    <style>
    .word-toolbar {
        background: linear-gradient(180deg, #f3f3f3 0%, #e8e8e8 100%);
        border: 1px solid #d0d0d0;
        border-radius: 4px;
        padding: 8px 12px;
        margin-bottom: 10px;
    }
    .toolbar-group {
        display: inline-flex;
        gap: 4px;
        padding: 0 8px;
        border-right: 1px solid #ccc;
    }
    .doc-container {
        background: white;
        border: 1px solid #d0d0d0;
        border-radius: 4px;
        padding: 20px;
        min-height: 400px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .note-card {
        background: #fafafa;
        border-left: 4px solid #4A90D9;
        padding: 12px;
        margin: 8px 0;
        border-radius: 0 4px 4px 0;
    }
    .note-card.important { border-left-color: #FFD700; }
    .note-card.critical { border-left-color: #FF6B6B; }
    .sidebar-item {
        padding: 8px 12px;
        border-radius: 4px;
        cursor: pointer;
        margin: 2px 0;
    }
    .sidebar-item:hover { background: #e8f4fd; }
    .status-bar {
        background: #f0f0f0;
        padding: 4px 12px;
        font-size: 12px;
        color: #666;
        border-top: 1px solid #d0d0d0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    NOTE_CATEGORIES = {
        "lecture": {"icon": "📚", "label": "Lecture Notes", "color": "#4A90D9"},
        "exercise": {"icon": "✏️", "label": "Exercise Notes", "color": "#50C878"},
        "exam": {"icon": "📋", "label": "Exam Prep", "color": "#FF6B6B"},
        "tips": {"icon": "💡", "label": "Tips & Tricks", "color": "#FFD700"},
        "summary": {"icon": "📄", "label": "Summary", "color": "#9B59B6"}
    }
    
    IMPORTANCE_LEVELS = {
        "normal": {"icon": "○", "label": "Normal", "color": "#888"},
        "important": {"icon": "⭐", "label": "Important", "color": "#FFD700"},
        "critical": {"icon": "🔥", "label": "Exam Critical", "color": "#FF6B6B"}
    }
    
    QUICK_INSERTS = {
        "heading": "## ",
        "subheading": "### ",
        "bullet": "- ",
        "numbered": "1. ",
        "bold": "**text**",
        "italic": "*text*",
        "table": "| Col1 | Col2 | Col3 |\n|------|------|------|\n| | | |",
        "checklist": "- [ ] Task item",
        "quote": "> Quote text",
        "code": "```\ncode here\n```",
        "divider": "\n---\n",
        "link": "[text](url)"
    }
    
    NOTE_TEMPLATES = {
        "blank": {"name": "📄 Blank Document", "icon": "📄", "content": ""},
        "concept": {"name": "💡 Concept Summary", "icon": "💡", "content": """## Concept Name

**Definition:**
[Write the definition here]

**Key Points:**
- Point 1
- Point 2
- Point 3

**Examples:**
1. Example 1
2. Example 2

**Common Mistakes:**
- Mistake to avoid

**Related Concepts:**
- Related concept 1
- Related concept 2
"""},
        "case_study": {"name": "📊 Case Study", "icon": "📊", "content": """## Case Study: [Title]

### Background
[Describe the business context]

### Problem Statement
[What problem needs to be solved?]

### Data Available
- Data source 1
- Data source 2

### Analysis Approach
1. Step 1
2. Step 2
3. Step 3

### Findings
[Key insights from the analysis]

### Recommendations
1. Recommendation 1
2. Recommendation 2

### Lessons Learned
- Lesson 1
- Lesson 2
"""},
        "formula": {"name": "🔢 Formula Sheet", "icon": "🔢", "content": """## Formula Reference: [Topic]

### Basic Formulas
| Formula | Description | When to Use |
|---------|-------------|-------------|
| Formula 1 | Description | Use case |
| Formula 2 | Description | Use case |

### Key Variables
- **Variable 1**: Definition
- **Variable 2**: Definition

### Worked Example
**Problem:** [Describe the problem]

**Solution:**
1. Step 1
2. Step 2
3. Result

### Quick Reference
- Remember: [Key tip]
- Common error: [What to avoid]
"""},
        "comparison": {"name": "⚖️ Comparison Chart", "icon": "⚖️", "content": """## Comparison: [Topic A] vs [Topic B]

| Aspect | Topic A | Topic B |
|--------|---------|---------|
| Definition | | |
| Use Case | | |
| Advantages | | |
| Disadvantages | | |
| Example | | |

### When to Choose Topic A
- Situation 1
- Situation 2

### When to Choose Topic B
- Situation 1
- Situation 2

### Key Takeaway
[Main insight from comparison]
"""},
        "meeting": {"name": "📝 Meeting Notes", "icon": "📝", "content": """## Meeting Notes: [Date]

**Attendees:** [Names]
**Topic:** [Meeting topic]

### Key Discussion Points
1. Point 1
2. Point 2
3. Point 3

### Decisions Made
- Decision 1
- Decision 2

### Action Items
- [ ] Task 1 - Owner: [Name] - Due: [Date]
- [ ] Task 2 - Owner: [Name] - Due: [Date]

### Next Steps
[What happens next]
"""},
        "exam_prep": {"name": "📋 Exam Prep", "icon": "📋", "content": """## Exam Preparation: [Subject]

### Key Topics to Review
- [ ] Topic 1
- [ ] Topic 2
- [ ] Topic 3

### Important Definitions
| Term | Definition |
|------|------------|
| Term 1 | Definition |
| Term 2 | Definition |

### Practice Questions
1. Question 1?
   - Answer: 

2. Question 2?
   - Answer: 

### Quick Memory Aids
> Mnemonic or memory trick here

### Common Exam Mistakes
- Mistake to avoid 1
- Mistake to avoid 2
"""}
    }
    
    course_options = {f"{c['code']} - {c['name']}": c['code'] for c in courses_data}
    
    if 'current_note_content' not in st.session_state:
        st.session_state.current_note_content = ""
    if 'word_view_mode' not in st.session_state:
        st.session_state.word_view_mode = "edit"
    
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown("## 📝 Study Notes")
    with header_col2:
        view_mode = st.radio("View:", ["Edit", "Preview", "Split"], horizontal=True, key="word_view", label_visibility="collapsed")
    
    menu_col1, menu_col2, menu_col3, menu_col4, menu_col5 = st.columns([1, 1, 1, 1, 1])
    with menu_col1:
        if st.button("📄 New", key="word_new", use_container_width=True):
            st.session_state.current_note_content = ""
            st.session_state.pop('editing_note_idx', None)
            st.session_state.pop('current_note_title', None)
    with menu_col2:
        if st.button("💾 Save", key="word_save_top", use_container_width=True):
            st.session_state.trigger_save = True
    with menu_col3:
        if st.button("📥 Export", key="word_export", use_container_width=True):
            st.session_state.show_export = True
    with menu_col4:
        if st.button("🤖 AI Help", key="word_ai", use_container_width=True):
            st.session_state.show_ai_panel = not st.session_state.get('show_ai_panel', False)
    with menu_col5:
        if st.button("📊 Stats", key="word_stats", use_container_width=True):
            st.session_state.show_stats = not st.session_state.get('show_stats', False)
    
    st.markdown("---")
    
    sidebar_col, main_col = st.columns([1, 3])
    
    with sidebar_col:
        st.markdown("##### 📁 Documents")
        
        selected_course_label = st.selectbox(
            "Course:",
            options=list(course_options.keys()),
            key="word_course_select",
            label_visibility="collapsed"
        )
        selected_course_code = course_options[selected_course_label]
        
        if selected_course_code not in st.session_state.study_notes:
            st.session_state.study_notes[selected_course_code] = []
        
        course_notes = st.session_state.study_notes[selected_course_code]
        
        cat_filter = st.selectbox(
            "Filter:",
            ["All"] + [f"{v['icon']} {v['label']}" for v in NOTE_CATEGORIES.values()],
            key="word_cat_filter",
            label_visibility="collapsed"
        )
        
        search_term = st.text_input("🔍", placeholder="Search...", key="word_search", label_visibility="collapsed")
        
        filtered_notes = course_notes.copy()
        if cat_filter != "All":
            cat_key = [k for k, v in NOTE_CATEGORIES.items() if f"{v['icon']} {v['label']}" == cat_filter]
            if cat_key:
                filtered_notes = [n for n in filtered_notes if n.get('category') == cat_key[0]]
        if search_term:
            filtered_notes = [n for n in filtered_notes if search_term.lower() in n.get('title', '').lower() or search_term.lower() in n.get('content', '').lower()]
        
        st.markdown(f"**{len(filtered_notes)} notes**")
        
        for idx, note in enumerate(filtered_notes):
            orig_idx = course_notes.index(note) if note in course_notes else idx
            cat = note.get('category', 'lecture')
            cat_info = NOTE_CATEGORIES.get(cat, NOTE_CATEGORIES['lecture'])
            imp = note.get('importance', 'normal')
            imp_icon = IMPORTANCE_LEVELS.get(imp, {}).get('icon', '')
            
            btn_label = f"{cat_info['icon']} {imp_icon} {note.get('title', 'Untitled')[:20]}"
            if st.button(btn_label, key=f"open_{selected_course_code}_{orig_idx}", use_container_width=True):
                st.session_state.current_note_content = note.get('content', '')
                st.session_state.current_note_title = note.get('title', '')
                st.session_state.current_note_category = note.get('category', 'lecture')
                st.session_state.current_note_importance = note.get('importance', 'normal')
                st.session_state.current_note_tags = ', '.join(note.get('tags', []))
                st.session_state.current_note_outcome = note.get('learning_outcome', '')
                st.session_state.editing_note_idx = orig_idx
                st.rerun()
    
    with main_col:
        st.markdown("##### ✏️ Editor Toolbar")
        tool_cols = st.columns(12)
        
        insert_text = ""
        with tool_cols[0]:
            if st.button("H1", key="tb_h1", help="Heading 1"):
                insert_text = "## "
        with tool_cols[1]:
            if st.button("H2", key="tb_h2", help="Heading 2"):
                insert_text = "### "
        with tool_cols[2]:
            if st.button("B", key="tb_bold", help="Bold"):
                insert_text = "**bold**"
        with tool_cols[3]:
            if st.button("I", key="tb_italic", help="Italic"):
                insert_text = "*italic*"
        with tool_cols[4]:
            if st.button("•", key="tb_bullet", help="Bullet list"):
                insert_text = "- "
        with tool_cols[5]:
            if st.button("1.", key="tb_num", help="Numbered list"):
                insert_text = "1. "
        with tool_cols[6]:
            if st.button("☐", key="tb_check", help="Checklist"):
                insert_text = "- [ ] "
        with tool_cols[7]:
            if st.button("⊞", key="tb_table", help="Table"):
                insert_text = "\n| Col1 | Col2 | Col3 |\n|------|------|------|\n| | | |\n"
        with tool_cols[8]:
            if st.button("❝", key="tb_quote", help="Quote"):
                insert_text = "> "
        with tool_cols[9]:
            if st.button("</>", key="tb_code", help="Code block"):
                insert_text = "```\ncode\n```"
        with tool_cols[10]:
            if st.button("—", key="tb_div", help="Divider"):
                insert_text = "\n---\n"
        with tool_cols[11]:
            if st.button("🔗", key="tb_link", help="Link"):
                insert_text = "[text](url)"
        
        if insert_text:
            st.session_state.current_note_content = st.session_state.get('current_note_content', '') + insert_text
            st.rerun()
        
        prop_col1, prop_col2, prop_col3, prop_col4 = st.columns(4)
        with prop_col1:
            note_title = st.text_input("Title:", value=st.session_state.get('current_note_title', ''), key="word_title", placeholder="Document title...")
        with prop_col2:
            note_category = st.selectbox(
                "Category:",
                options=list(NOTE_CATEGORIES.keys()),
                format_func=lambda x: f"{NOTE_CATEGORIES[x]['icon']} {NOTE_CATEGORIES[x]['label']}",
                index=list(NOTE_CATEGORIES.keys()).index(st.session_state.get('current_note_category', 'lecture')),
                key="word_category"
            )
        with prop_col3:
            note_importance = st.selectbox(
                "Importance:",
                options=list(IMPORTANCE_LEVELS.keys()),
                format_func=lambda x: f"{IMPORTANCE_LEVELS[x]['icon']} {IMPORTANCE_LEVELS[x]['label']}",
                index=list(IMPORTANCE_LEVELS.keys()).index(st.session_state.get('current_note_importance', 'normal')),
                key="word_importance"
            )
        with prop_col4:
            template_choice = st.selectbox(
                "Template:",
                options=["(None)"] + [t['name'] for t in NOTE_TEMPLATES.values()],
                key="word_template"
            )
            if template_choice != "(None)":
                template_key = [k for k, v in NOTE_TEMPLATES.items() if v['name'] == template_choice]
                if template_key and not st.session_state.get('editing_note_idx'):
                    if st.session_state.get('last_applied_template') != template_choice:
                        st.session_state.current_note_content = NOTE_TEMPLATES[template_key[0]]['content']
                        st.session_state.last_applied_template = template_choice
                        st.rerun()
        
        if view_mode == "Edit":
            note_content = st.text_area(
                "Content:",
                value=st.session_state.get('current_note_content', ''),
                height=350,
                key="word_content",
                placeholder="Start writing your notes here...\n\nUse Markdown for formatting:\n- **bold** for bold\n- *italic* for italic\n- ## for headings\n- - for bullet points",
                label_visibility="collapsed"
            )
            st.session_state.current_note_content = note_content
        
        elif view_mode == "Preview":
            st.markdown("**Preview:**")
            content = st.session_state.get('current_note_content', '')
            if content:
                st.markdown(content)
            else:
                st.info("Nothing to preview. Start writing in Edit mode.")
        
        else:
            edit_col, preview_col = st.columns(2)
            with edit_col:
                note_content = st.text_area(
                    "Edit:",
                    value=st.session_state.get('current_note_content', ''),
                    height=300,
                    key="word_content_split",
                    label_visibility="collapsed"
                )
                st.session_state.current_note_content = note_content
            with preview_col:
                st.markdown("**Preview:**")
                if note_content:
                    st.markdown(note_content)
                else:
                    st.caption("Preview appears here...")
        
        tags_col, outcome_col = st.columns(2)
        with tags_col:
            note_tags = st.text_input("Tags (comma-separated):", value=st.session_state.get('current_note_tags', ''), key="word_tags")
        with outcome_col:
            selected_course_data = next((c for c in courses_data if c['code'] == selected_course_code), None)
            outcomes_list = []
            if selected_course_data:
                for lo in selected_course_data.get('learning_outcomes', []):
                    outcomes_list.extend(lo.get('items', []))
            default_outcome = st.session_state.get('current_note_outcome', '')
            note_outcome = st.selectbox(
                "Learning Outcome:",
                options=["(None)"] + outcomes_list[:10],
                index=(outcomes_list.index(default_outcome) + 1) if default_outcome in outcomes_list else 0,
                key="word_outcome"
            )
        
        save_col1, save_col2, save_col3 = st.columns([1, 1, 2])
        with save_col1:
            if st.button("💾 Save Note", type="primary", key="word_save_main", use_container_width=True) or st.session_state.get('trigger_save'):
                st.session_state.pop('trigger_save', None)
                if note_title and st.session_state.get('current_note_content', ''):
                    tags_list = [t.strip() for t in note_tags.split(',') if t.strip()] if note_tags else []
                    
                    note_data = {
                        'title': note_title,
                        'content': st.session_state.current_note_content,
                        'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                        'tags': tags_list,
                        'category': note_category,
                        'importance': note_importance,
                        'learning_outcome': note_outcome if note_outcome != "(None)" else "",
                        'version_history': []
                    }
                    
                    editing_idx = st.session_state.get('editing_note_idx')
                    if editing_idx is not None and editing_idx < len(course_notes):
                        old_note = course_notes[editing_idx]
                        history = old_note.get('version_history', [])
                        if old_note.get('content') != note_data['content']:
                            history.append({
                                'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                                'summary': f"Edited: {old_note.get('title', '')[:30]}"
                            })
                        note_data['version_history'] = history[-10:]
                        st.session_state.study_notes[selected_course_code][editing_idx] = note_data
                    else:
                        st.session_state.study_notes[selected_course_code].append(note_data)
                    
                    st.success("✅ Saved!")
                    st.rerun()
                else:
                    st.warning("Please add a title and content.")
        
        with save_col2:
            if st.session_state.get('editing_note_idx') is not None:
                if st.button("🗑️ Delete", key="word_delete", use_container_width=True):
                    idx = st.session_state.editing_note_idx
                    if idx < len(course_notes):
                        st.session_state.study_notes[selected_course_code].pop(idx)
                        st.session_state.current_note_content = ""
                        st.session_state.pop('editing_note_idx', None)
                        st.session_state.pop('current_note_title', None)
                        st.success("Deleted!")
                        st.rerun()
    
    if st.session_state.get('show_ai_panel'):
        st.markdown("---")
        st.markdown("### 🤖 AI Assistant")
        
        ai_col1, ai_col2 = st.columns([1, 2])
        with ai_col1:
            ai_action = st.radio(
                "AI Action:",
                ["Summarize", "Expand", "Simplify", "Generate Questions", "Fix Grammar", "Add Examples"],
                key="word_ai_action"
            )
        
        with ai_col2:
            if st.button("🚀 Apply AI", type="primary", key="word_ai_apply"):
                content = st.session_state.get('current_note_content', '')
                if content:
                    with st.spinner("Processing..."):
                        prompts = {
                            "Summarize": f"Summarize this content concisely:\n\n{content}",
                            "Expand": f"Expand on this content with more details and examples:\n\n{content}",
                            "Simplify": f"Rewrite this content in simpler terms for easy understanding:\n\n{content}",
                            "Generate Questions": f"Generate 5 study questions based on this content:\n\n{content}",
                            "Fix Grammar": f"Fix any grammar and spelling errors in this text, return the corrected version:\n\n{content}",
                            "Add Examples": f"Add practical examples to illustrate the concepts in this content:\n\n{content}"
                        }
                        try:
                            response = client.chat.completions.create(
                                model="gpt-4o-mini",
                                messages=[
                                    {"role": "system", "content": "You are a helpful study assistant. Provide clear, educational content."},
                                    {"role": "user", "content": prompts[ai_action]}
                                ],
                                max_tokens=1000
                            )
                            result = response.choices[0].message.content
                            st.markdown("**AI Result:**")
                            st.markdown(result)
                            if st.button("📋 Replace Content", key="ai_replace"):
                                st.session_state.current_note_content = result
                                st.rerun()
                            if st.button("➕ Append to Content", key="ai_append"):
                                st.session_state.current_note_content += f"\n\n---\n\n{result}"
                                st.rerun()
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
                else:
                    st.warning("Write some content first.")
    
    if st.session_state.get('show_stats'):
        st.markdown("---")
        st.markdown("### 📊 Statistics")
        
        total_notes = sum(len(notes) for notes in st.session_state.study_notes.values())
        
        stat_cols = st.columns(4)
        with stat_cols[0]:
            st.metric("Total Notes", total_notes)
        with stat_cols[1]:
            critical_count = sum(1 for notes in st.session_state.study_notes.values() for n in notes if n.get('importance') == 'critical')
            st.metric("Critical", critical_count)
        with stat_cols[2]:
            important_count = sum(1 for notes in st.session_state.study_notes.values() for n in notes if n.get('importance') == 'important')
            st.metric("Important", important_count)
        with stat_cols[3]:
            courses_with_notes = sum(1 for notes in st.session_state.study_notes.values() if notes)
            st.metric("Courses", courses_with_notes)
        
        if total_notes > 0:
            cat_col, course_col = st.columns(2)
            with cat_col:
                st.markdown("**By Category:**")
                cat_counts = {}
                for notes in st.session_state.study_notes.values():
                    for note in notes:
                        cat = note.get('category', 'lecture')
                        cat_counts[cat] = cat_counts.get(cat, 0) + 1
                for cat, count in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True):
                    cat_info = NOTE_CATEGORIES.get(cat, NOTE_CATEGORIES['lecture'])
                    st.write(f"{cat_info['icon']} {cat_info['label']}: {count}")
            
            with course_col:
                st.markdown("**By Course:**")
                course_counts = {code: len(notes) for code, notes in st.session_state.study_notes.items() if notes}
                for code, count in sorted(course_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                    st.write(f"{code}: {count}")
    
    if st.session_state.get('show_export'):
        st.markdown("---")
        st.markdown("### 📥 Export Notes")
        
        if course_notes:
            export_format = st.radio("Format:", ["JSON", "Markdown"], horizontal=True, key="export_format")
            
            if export_format == "JSON":
                export_data = {selected_course_code: course_notes}
                export_json = json.dumps(export_data, indent=2, ensure_ascii=False)
                st.download_button(
                    "⬇️ Download JSON",
                    data=export_json,
                    file_name=f"notes_{selected_course_code}_{datetime.now().strftime('%Y%m%d')}.json",
                    mime="application/json"
                )
            else:
                md_content = f"# Study Notes - {selected_course_code}\n\n"
                for note in course_notes:
                    md_content += f"## {note.get('title', 'Untitled')}\n"
                    md_content += f"*{note.get('date', '')}* | {NOTE_CATEGORIES.get(note.get('category', 'lecture'), {}).get('label', '')}\n\n"
                    md_content += note.get('content', '') + "\n\n---\n\n"
                st.download_button(
                    "⬇️ Download Markdown",
                    data=md_content,
                    file_name=f"notes_{selected_course_code}_{datetime.now().strftime('%Y%m%d')}.md",
                    mime="text/markdown"
                )
        else:
            st.info("No notes to export.")
        
        st.session_state.show_export = False
    
    word_count = len(st.session_state.get('current_note_content', '').split())
    char_count = len(st.session_state.get('current_note_content', ''))
    st.caption(f"📝 {word_count} words | {char_count} characters | Course: {selected_course_code}")
    
    with notes_tab:
        col_filter, col_course = st.columns([1, 2])
        with col_course:
            selected_course_label = st.selectbox(
                "Select Course:",
                options=list(course_options.keys()),
                key="notes_course_select"
            )
        selected_course_code = course_options[selected_course_label]
        
        with col_filter:
            category_filter = st.selectbox(
                "Filter by Category:",
                options=["All Categories"] + [f"{v['icon']} {v['label']}" for v in NOTE_CATEGORIES.values()],
                key="notes_category_filter"
            )
        
        if selected_course_code not in st.session_state.study_notes:
            st.session_state.study_notes[selected_course_code] = []
        
        course_notes = st.session_state.study_notes[selected_course_code]
        
        filter_col1, filter_col2, filter_col3 = st.columns([2, 1, 1])
        with filter_col1:
            search_query = st.text_input("🔍 Search notes:", placeholder="Search by title, content, or tags...", key="notes_search")
        with filter_col2:
            importance_filter = st.selectbox(
                "Importance:",
                options=["All"] + [f"{v['icon']} {v['label']}" if v['icon'] else v['label'] for v in IMPORTANCE_LEVELS.values()],
                key="notes_importance_filter"
            )
        with filter_col3:
            sort_option = st.selectbox("Sort by:", ["Newest First", "Oldest First", "Importance", "Category"], key="notes_sort")
        
        filtered_notes = course_notes.copy()
        
        if category_filter != "All Categories":
            cat_key = [k for k, v in NOTE_CATEGORIES.items() if f"{v['icon']} {v['label']}" == category_filter]
            if cat_key:
                filtered_notes = [n for n in filtered_notes if n.get('category') == cat_key[0]]
        
        if importance_filter != "All":
            imp_key = [k for k, v in IMPORTANCE_LEVELS.items() if (f"{v['icon']} {v['label']}" if v['icon'] else v['label']) == importance_filter]
            if imp_key:
                filtered_notes = [n for n in filtered_notes if n.get('importance') == imp_key[0]]
        
        if search_query:
            filtered_notes = [
                note for note in filtered_notes
                if search_query.lower() in note.get('title', '').lower() or 
                   search_query.lower() in note.get('content', '').lower() or
                   any(search_query.lower() in tag.lower() for tag in note.get('tags', []))
            ]
        
        if sort_option == "Newest First":
            filtered_notes.sort(key=lambda x: x.get('date', ''), reverse=True)
        elif sort_option == "Oldest First":
            filtered_notes.sort(key=lambda x: x.get('date', ''))
        elif sort_option == "Importance":
            imp_order = {"critical": 0, "important": 1, "normal": 2}
            filtered_notes.sort(key=lambda x: imp_order.get(x.get('importance', 'normal'), 2))
        elif sort_option == "Category":
            filtered_notes.sort(key=lambda x: x.get('category', 'lecture'))
        
        col_notes, col_editor = st.columns([3, 2])
        
        with col_notes:
            st.subheader(f"📄 Notes ({len(filtered_notes)})")
            
            if filtered_notes:
                for idx, note in enumerate(filtered_notes):
                    orig_idx = course_notes.index(note) if note in course_notes else idx
                    cat = note.get('category', 'lecture')
                    cat_info = NOTE_CATEGORIES.get(cat, NOTE_CATEGORIES['lecture'])
                    imp = note.get('importance', 'normal')
                    imp_info = IMPORTANCE_LEVELS.get(imp, IMPORTANCE_LEVELS['normal'])
                    
                    header_prefix = f"{cat_info['icon']} {imp_info['icon']} " if imp_info['icon'] else f"{cat_info['icon']} "
                    
                    with st.expander(f"{header_prefix}{note.get('title', 'Untitled')} - {note.get('date', 'No date')[:10]}"):
                        if note.get('learning_outcome'):
                            st.caption(f"🎯 Learning Outcome: {note.get('learning_outcome')}")
                        
                        st.markdown(note.get('content', ''))
                        
                        meta_cols = st.columns(3)
                        with meta_cols[0]:
                            st.caption(f"Category: {cat_info['label']}")
                        with meta_cols[1]:
                            if note.get('tags'):
                                st.caption(f"Tags: {', '.join(note.get('tags', []))}")
                        with meta_cols[2]:
                            st.caption(f"Importance: {imp_info['label']}")
                        
                        if note.get('version_history'):
                            with st.expander("📜 Version History"):
                                for v_idx, version in enumerate(note.get('version_history', [])[-5:]):
                                    st.caption(f"v{v_idx+1} - {version.get('date', 'Unknown')}: {version.get('summary', 'No summary')}")
                        
                        btn_cols = st.columns(4)
                        with btn_cols[0]:
                            if st.button("✏️ Edit", key=f"edit_{selected_course_code}_{orig_idx}"):
                                st.session_state[f"editing_note_{selected_course_code}"] = orig_idx
                                st.rerun()
                        with btn_cols[1]:
                            if st.button("📋 Duplicate", key=f"dup_{selected_course_code}_{orig_idx}"):
                                new_note = note.copy()
                                new_note['title'] = f"{note.get('title', 'Untitled')} (Copy)"
                                new_note['date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
                                new_note['version_history'] = []
                                st.session_state.study_notes[selected_course_code].append(new_note)
                                st.success("Note duplicated!")
                                st.rerun()
                        with btn_cols[2]:
                            next_imp = {"normal": "important", "important": "critical", "critical": "normal"}
                            if st.button(f"{'⭐' if imp == 'normal' else '🔥' if imp == 'important' else '◯'}", key=f"imp_{selected_course_code}_{orig_idx}"):
                                st.session_state.study_notes[selected_course_code][orig_idx]['importance'] = next_imp[imp]
                                st.rerun()
                        with btn_cols[3]:
                            if st.button("🗑️ Delete", key=f"delete_{selected_course_code}_{orig_idx}"):
                                st.session_state.study_notes[selected_course_code].pop(orig_idx)
                                st.rerun()
            else:
                st.info("No notes found. Create your first note in the editor!")
        
        with col_editor:
            editing_idx = st.session_state.get(f"editing_note_{selected_course_code}", None)
            is_editing = editing_idx is not None
            
            st.subheader("✏️ Edit Note" if is_editing else "➕ Create New Note")
            
            if is_editing and editing_idx < len(course_notes):
                existing_note = course_notes[editing_idx]
                default_title = existing_note.get('title', '')
                default_content = existing_note.get('content', '')
                default_tags = ', '.join(existing_note.get('tags', []))
                default_category = existing_note.get('category', 'lecture')
                default_importance = existing_note.get('importance', 'normal')
                default_outcome = existing_note.get('learning_outcome', '')
            else:
                default_title = ""
                default_content = ""
                default_tags = ""
                default_category = "lecture"
                default_importance = "normal"
                default_outcome = ""
            
            template_choice = st.selectbox(
                "Start from template:",
                options=["(Keep current)" if is_editing else "(Select template)"] + [t['name'] for t in NOTE_TEMPLATES.values()],
                key="note_template_choice"
            )
            
            if template_choice not in ["(Keep current)", "(Select template)"]:
                template_key = [k for k, v in NOTE_TEMPLATES.items() if v['name'] == template_choice]
                if template_key and not is_editing:
                    template_content = NOTE_TEMPLATES[template_key[0]]['content']
                    content_key = f"note_content_{selected_course_code}"
                    if st.session_state.get(content_key, "") != template_content and st.session_state.get('last_template') != template_choice:
                        st.session_state[content_key] = template_content
                        st.session_state['last_template'] = template_choice
                        st.rerun()
            
            note_title = st.text_input("Title:", value=default_title, key=f"note_title_{selected_course_code}")
            
            ed_col1, ed_col2 = st.columns(2)
            with ed_col1:
                note_category = st.selectbox(
                    "Category:",
                    options=list(NOTE_CATEGORIES.keys()),
                    format_func=lambda x: f"{NOTE_CATEGORIES[x]['icon']} {NOTE_CATEGORIES[x]['label']}",
                    index=list(NOTE_CATEGORIES.keys()).index(default_category) if default_category in NOTE_CATEGORIES else 0,
                    key=f"note_category_{selected_course_code}"
                )
            with ed_col2:
                note_importance = st.selectbox(
                    "Importance:",
                    options=list(IMPORTANCE_LEVELS.keys()),
                    format_func=lambda x: f"{IMPORTANCE_LEVELS[x]['icon']} {IMPORTANCE_LEVELS[x]['label']}" if IMPORTANCE_LEVELS[x]['icon'] else IMPORTANCE_LEVELS[x]['label'],
                    index=list(IMPORTANCE_LEVELS.keys()).index(default_importance) if default_importance in IMPORTANCE_LEVELS else 0,
                    key=f"note_importance_{selected_course_code}"
                )
            
            selected_course_data = next((c for c in courses_data if c['code'] == selected_course_code), None)
            if selected_course_data:
                outcomes_list = []
                for lo in selected_course_data.get('learning_outcomes', []):
                    outcomes_list.extend(lo.get('items', []))
                if outcomes_list:
                    note_outcome = st.selectbox(
                        "Link to Learning Outcome:",
                        options=["(None)"] + outcomes_list[:10],
                        index=outcomes_list.index(default_outcome) + 1 if default_outcome in outcomes_list else 0,
                        key=f"note_outcome_{selected_course_code}"
                    )
                else:
                    note_outcome = "(None)"
            else:
                note_outcome = "(None)"
            
            # Word-like Editor Interface
            st.markdown("---")
            
            # Word-style Ribbon/Toolbar
            ribbon_css = """
            <style>
            .word-ribbon {
                background: linear-gradient(to bottom, #f8f9fa 0%, #e9ecef 100%);
                border: 1px solid #dee2e6;
                border-radius: 4px 4px 0 0;
                padding: 8px;
                margin-bottom: 0;
            }
            .word-editor-container {
                border: 2px solid #0078d4;
                border-radius: 0 0 4px 4px;
                background: white;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            .word-status-bar {
                background: #f8f9fa;
                border-top: 1px solid #dee2e6;
                padding: 4px 8px;
                font-size: 12px;
                color: #6c757d;
            }
            </style>
            """
            st.markdown(ribbon_css, unsafe_allow_html=True)
            
            # Editor Settings Bar (like Word's status bar)
            settings_bar_col1, settings_bar_col2, settings_bar_col3, settings_bar_col4 = st.columns([2, 2, 2, 1])
            with settings_bar_col1:
                editor_mode = st.radio("View Mode", ["📝 Edit", "👁️ Preview", "📄 Both"], 
                                      horizontal=True, key=f"editor_mode_{selected_course_code}", index=2)
            with settings_bar_col2:
                paper_type = st.selectbox("Paper", ["A4", "Letter", "A3", "Custom"], 
                                         index=0, key=f"paper_type_{selected_course_code}")
                # A4 dimensions: 210mm x 297mm (8.27" x 11.69")
                # At 96 DPI: 794px x 1123px
                # For editor, we'll use a scaled version that fits the screen
                paper_map = {
                    "A4": {"width": 794, "height": 1123, "ratio": 1.414},
                    "Letter": {"width": 816, "height": 1056, "ratio": 1.294},
                    "A3": {"width": 1123, "height": 1587, "ratio": 1.414},
                    "Custom": {"width": 794, "height": 1123, "ratio": 1.414}
                }
                paper_dims = paper_map[paper_type]
                # Scale to fit screen (max width ~1200px, maintain aspect ratio)
                scale_factor = min(1.0, 1200 / paper_dims["width"])
                editor_width_px = int(paper_dims["width"] * scale_factor)
                editor_height_px = int(paper_dims["height"] * scale_factor)
            with settings_bar_col3:
                zoom_level = st.slider("Zoom", 50, 200, 100, 10, key=f"zoom_{selected_course_code}")
                # Apply zoom
                editor_width_px = int(editor_width_px * zoom_level / 100)
                editor_height_px = int(editor_height_px * zoom_level / 100)
            with settings_bar_col4:
                show_ruler = st.checkbox("📏 Ruler", value=True, key=f"ruler_{selected_course_code}")
                show_lines = st.checkbox("📝 Lines", value=True, key=f"show_lines_{selected_course_code}")
            
            # Word-like Ribbon Interface
            st.markdown('<div class="word-ribbon">', unsafe_allow_html=True)
            
            # Home Tab (like Word's ribbon)
            ribbon_tabs = st.tabs(["🏠 Home", "✏️ Insert", "📊 Layout", "🎨 Design", "📝 Review"])
            
            with ribbon_tabs[0]:  # Home Tab
                st.markdown("**Clipboard & Font**")
                home_row1 = st.columns(12)
                with home_row1[0]:
                    if st.button("📋", key=f"paste_{selected_course_code}", help="Paste", use_container_width=True):
                        st.info("💡 Use Ctrl+V to paste")
                with home_row1[1]:
                    if st.button("✂️", key=f"cut_{selected_course_code}", help="Cut", use_container_width=True):
                        st.info("💡 Use Ctrl+X to cut")
                with home_row1[2]:
                    if st.button("📄", key=f"copy_{selected_course_code}", help="Copy", use_container_width=True):
                        st.info("💡 Use Ctrl+C to copy")
                
                st.markdown("**Font Formatting**")
                home_row2 = st.columns(12)
                with home_row2[0]:
                    font_family = st.selectbox("Font", ["Arial", "Times New Roman", "Courier New", "Calibri", "Georgia", "Verdana"], 
                                              index=3, key=f"font_family_{selected_course_code}", label_visibility="collapsed")
                with home_row2[1]:
                    font_size_val = st.selectbox("Size", ["8", "9", "10", "11", "12", "14", "16", "18", "20", "24", "28", "36"], 
                                               index=4, key=f"font_size_val_{selected_course_code}", label_visibility="collapsed")
                with home_row2[2]:
                    if st.button("**B**", key=f"ribbon_bold_{selected_course_code}", help="Bold", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "**bold**"
                        st.rerun()
                with home_row2[3]:
                    if st.button("*I*", key=f"ribbon_italic_{selected_course_code}", help="Italic", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "*italic*"
                        st.rerun()
                with home_row2[4]:
                    if st.button("U̲", key=f"ribbon_underline_{selected_course_code}", help="Underline", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "<u>underline</u>"
                        st.rerun()
                with home_row2[5]:
                    if st.button("~~S~~", key=f"ribbon_strike_{selected_course_code}", help="Strikethrough", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "~~strike~~"
                        st.rerun()
                with home_row2[6]:
                    if st.button("🎨", key=f"highlight_{selected_course_code}", help="Highlight", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "<mark>highlighted</mark>"
                        st.rerun()
                with home_row2[7]:
                    text_color = st.color_picker("", "#000000", key=f"text_color_{selected_course_code}", label_visibility="collapsed")
                with home_row2[8]:
                    bg_color = st.color_picker("", "#FFFFFF", key=f"bg_color_{selected_course_code}", label_visibility="collapsed")
                
                st.markdown("**Paragraph**")
                home_row3 = st.columns(8)
                with home_row3[0]:
                    if st.button("•", key=f"bullet_{selected_course_code}", help="Bullets", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "\n- Item\n"
                        st.rerun()
                with home_row3[1]:
                    if st.button("1.", key=f"number_{selected_course_code}", help="Numbering", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "\n1. Item\n"
                        st.rerun()
                with home_row3[2]:
                    align = st.selectbox("Align", ["Left", "Center", "Right", "Justify"], 
                                        key=f"align_{selected_course_code}", label_visibility="collapsed")
                with home_row3[3]:
                    if st.button("📉", key=f"decrease_indent_{selected_course_code}", help="Decrease Indent", use_container_width=True):
                        st.info("💡 Use markdown indentation")
                with home_row3[4]:
                    if st.button("📈", key=f"increase_indent_{selected_course_code}", help="Increase Indent", use_container_width=True):
                        st.info("💡 Use markdown indentation")
                with home_row3[5]:
                    if st.button("🔍", key=f"find_{selected_course_code}", help="Find", use_container_width=True):
                        st.info("💡 Use browser Ctrl+F")
                with home_row3[6]:
                    if st.button("🔄", key=f"replace_{selected_course_code}", help="Replace", use_container_width=True):
                        st.info("💡 Use browser Ctrl+H")
            
            with ribbon_tabs[1]:  # Insert Tab
                st.markdown("**Insert Elements**")
                insert_row1 = st.columns(8)
                with insert_row1[0]:
                    if st.button("📊 Table", key=f"insert_table_{selected_course_code}", use_container_width=True):
                        st.session_state[f"show_table_builder_{selected_course_code}"] = True
                        st.rerun()
                with insert_row1[1]:
                    if st.button("📷 Image", key=f"insert_image_{selected_course_code}", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "\n![Image description](image_url)\n"
                        st.rerun()
                with insert_row1[2]:
                    if st.button("🔗 Link", key=f"insert_link_{selected_course_code}", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "[Link text](https://example.com)"
                        st.rerun()
                with insert_row1[3]:
                    if st.button("📋 Code", key=f"insert_code_{selected_course_code}", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "\n```python\n# Code here\n```\n"
                        st.rerun()
                with insert_row1[4]:
                    if st.button("∑ Formula", key=f"insert_formula_{selected_course_code}", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "\n$$\nformula = \\frac{a}{b}\n$$\n"
                        st.rerun()
                with insert_row1[5]:
                    if st.button("📝 Quote", key=f"insert_quote_{selected_course_code}", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "\n> Quote text\n"
                        st.rerun()
                with insert_row1[6]:
                    if st.button("---", key=f"insert_hr_{selected_course_code}", use_container_width=True):
                        current = st.session_state.get(f"note_content_{selected_course_code}", "")
                        st.session_state[f"note_content_{selected_course_code}"] = current + "\n---\n"
                        st.rerun()
                with insert_row1[7]:
                    if st.button("😊 Emoji", key=f"insert_emoji_{selected_course_code}", use_container_width=True):
                        st.session_state[f"show_emoji_picker_{selected_course_code}"] = True
                        st.rerun()
            
            with ribbon_tabs[2]:  # Layout Tab
                st.markdown("**Page Setup & Layout**")
                layout_row1 = st.columns(6)
                with layout_row1[0]:
                    margins = st.selectbox("Margins", ["Normal", "Narrow", "Moderate", "Wide", "Custom"], key=f"margins_{selected_course_code}")
                    # Apply margin presets
                    margin_presets = {
                        "Normal": {"top": 25, "bottom": 25, "left": 25, "right": 25},
                        "Narrow": {"top": 13, "bottom": 13, "left": 13, "right": 13},
                        "Moderate": {"top": 38, "bottom": 38, "left": 38, "right": 38},
                        "Wide": {"top": 50, "bottom": 50, "left": 50, "right": 50},
                        "Custom": {"top": 25, "bottom": 25, "left": 25, "right": 25}
                    }
                    if margins != "Custom":
                        preset = margin_presets[margins]
                        st.session_state[f"margin_top_{selected_course_code}"] = preset["top"]
                        st.session_state[f"margin_bottom_{selected_course_code}"] = preset["bottom"]
                        st.session_state[f"margin_left_{selected_course_code}"] = preset["left"]
                        st.session_state[f"margin_right_{selected_course_code}"] = preset["right"]
                with layout_row1[1]:
                    orientation = st.radio("Orientation", ["Portrait", "Landscape"], horizontal=True, key=f"orientation_{selected_course_code}")
                with layout_row1[2]:
                    page_size = st.selectbox("Size", ["A4", "Letter", "Legal", "A3"], key=f"page_size_{selected_course_code}")
                st.markdown("**Custom Margins (if Custom selected)**")
                layout_row2 = st.columns(4)
                with layout_row2[0]:
                    margin_top = st.number_input("Top (px)", 0, 100, st.session_state.get(f"margin_top_{selected_course_code}", 25), 5, key=f"margin_top_{selected_course_code}")
                with layout_row2[1]:
                    margin_bottom = st.number_input("Bottom (px)", 0, 100, st.session_state.get(f"margin_bottom_{selected_course_code}", 25), 5, key=f"margin_bottom_{selected_course_code}")
                with layout_row2[2]:
                    margin_left = st.number_input("Left (px)", 0, 100, st.session_state.get(f"margin_left_{selected_course_code}", 25), 5, key=f"margin_left_{selected_course_code}")
                with layout_row2[3]:
                    margin_right = st.number_input("Right (px)", 0, 100, st.session_state.get(f"margin_right_{selected_course_code}", 25), 5, key=f"margin_right_{selected_course_code}")
                st.markdown("**Paragraph Spacing**")
                layout_row3 = st.columns(4)
                with layout_row3[0]:
                    line_spacing = st.selectbox("Line Spacing", ["Single", "1.5", "Double", "Custom"], key=f"line_spacing_{selected_course_code}")
                with layout_row3[1]:
                    space_before = st.number_input("Space Before", 0, 48, 0, 6, key=f"space_before_{selected_course_code}")
                with layout_row3[2]:
                    space_after = st.number_input("Space After", 0, 48, 0, 6, key=f"space_after_{selected_course_code}")
            
            with ribbon_tabs[3]:  # Design Tab
                st.markdown("**Document Formatting**")
                design_row1 = st.columns(4)
                with design_row1[0]:
                    theme = st.selectbox("Theme", ["Default", "Modern", "Classic", "Minimal", "Colorful"], key=f"theme_{selected_course_code}")
                with design_row1[1]:
                    color_scheme = st.selectbox("Colors", ["Office", "Grayscale", "Blue", "Green", "Red"], key=f"colors_{selected_course_code}")
                with design_row1[2]:
                    fonts_theme = st.selectbox("Fonts", ["Office", "Modern", "Classic"], key=f"fonts_{selected_course_code}")
                st.markdown("**Page Background**")
                design_row2 = st.columns(3)
                with design_row2[0]:
                    page_color = st.color_picker("Page Color", "#FFFFFF", key=f"page_color_{selected_course_code}")
                with design_row2[1]:
                    watermark = st.text_input("Watermark", "", key=f"watermark_{selected_course_code}", placeholder="Optional watermark text")
            
            with ribbon_tabs[4]:  # Review Tab
                st.markdown("**Proofing & Language**")
                review_row1 = st.columns(4)
                with review_row1[0]:
                    if SPELLCHECK_AVAILABLE:
                        if st.button("🔍 Spelling", key=f"review_spell_{selected_course_code}", use_container_width=True):
                            st.session_state[f"run_spellcheck_{selected_course_code}"] = True
                            st.rerun()
                    else:
                        st.info("Spell check not available")
                with review_row1[1]:
                    if st.button("📊 Word Count", key=f"review_wordcount_{selected_course_code}", use_container_width=True):
                        st.session_state[f"show_wordcount_{selected_course_code}"] = True
                        st.rerun()
                with review_row1[2]:
                    language = st.selectbox("Language", ["English", "Norwegian", "Auto"], key=f"language_{selected_course_code}")
                st.markdown("**Comments & Tracking**")
                review_row2 = st.columns(3)
                with review_row2[0]:
                    if st.button("💬 Comment", key=f"comment_{selected_course_code}", use_container_width=True):
                        st.info("💡 Add comments in your notes using <!-- comment -->")
                with review_row2[1]:
                    track_changes = st.checkbox("Track Changes", key=f"track_changes_{selected_course_code}")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Word-like Editor Container
            st.markdown('<div class="word-editor-container">', unsafe_allow_html=True)
            
            # Emoji picker (if triggered from ribbon)
            if st.session_state.get(f"show_emoji_picker_{selected_course_code}", False):
                st.markdown("**Emoji Picker:**")
                emoji_categories = {
                    "Common": ["😊", "👍", "❤️", "🎉", "✅", "❌", "⚠️", "💡", "📝", "🔍", "⭐", "🔥", "💯", "🎯", "📚"],
                    "Study": ["📖", "✏️", "📋", "📊", "📈", "📉", "🔬", "🧪", "💻", "📱", "🎓", "🏆", "📌", "🔖", "📑"],
                    "Math": ["∑", "∫", "√", "∞", "π", "α", "β", "γ", "Δ", "θ", "λ", "μ", "σ", "Σ", "≈"],
                    "Arrows": ["→", "←", "↑", "↓", "⇒", "⇐", "⇑", "⇓", "↔", "↕", "⟹", "⟸", "⟶", "⟵", "⇔"]
                }
                for category, emojis in emoji_categories.items():
                    st.markdown(f"**{category}:**")
                    emoji_cols = st.columns(len(emojis))
                    for idx, emoji in enumerate(emojis):
                        with emoji_cols[idx]:
                            if st.button(emoji, key=f"emoji_{emoji}_{selected_course_code}", use_container_width=True):
                                current = st.session_state.get(f"note_content_{selected_course_code}", "")
                                st.session_state[f"note_content_{selected_course_code}"] = current + emoji
                                st.session_state[f"show_emoji_picker_{selected_course_code}"] = False
                                st.rerun()
            
            # Table builder
            if st.session_state.get(f"show_table_builder_{selected_course_code}", False):
                st.markdown("**Table Builder:**")
                table_cols = st.number_input("Number of Columns", min_value=2, max_value=10, value=3, key=f"table_cols_{selected_course_code}")
                table_rows = st.number_input("Number of Rows", min_value=1, max_value=20, value=3, key=f"table_rows_{selected_course_code}")
                if st.button("Generate Table", key=f"gen_table_{selected_course_code}"):
                    current = st.session_state.get(f"note_content_{selected_course_code}", "")
                    # Generate header
                    header = "| " + " | ".join([f"Column {i+1}" for i in range(table_cols)]) + " |\n"
                    separator = "| " + " | ".join(["---" for _ in range(table_cols)]) + " |\n"
                    # Generate rows
                    rows = "\n".join(["| " + " | ".join([f"Cell {i+1},{j+1}" for i in range(table_cols)]) + " |" for j in range(table_rows)])
                    table_md = "\n" + header + separator + rows + "\n"
                    st.session_state[f"note_content_{selected_course_code}"] = current + table_md
                    st.session_state[f"show_table_builder_{selected_course_code}"] = False
                    st.rerun()
                if st.button("Cancel", key=f"cancel_table_{selected_course_code}"):
                    st.session_state[f"show_table_builder_{selected_course_code}"] = False
                    st.rerun()
            
            # Build autocomplete dictionary
            autocomplete_dict = set()
            # Add course terms
            for course in courses_data:
                autocomplete_dict.add(course['code'])
                autocomplete_dict.add(course['name'])
                for term in course.get('knowledge', []):
                    autocomplete_dict.add(term)
                for term in course.get('skills', []):
                    autocomplete_dict.add(term)
            # Add common data analysis terms
            common_terms = [
                "KPI", "ETL", "BI", "Big Data", "Data Warehouse", "Data Lake",
                "Correlation", "Regression", "ANOVA", "Hypothesis Testing",
                "Mean", "Median", "Mode", "Standard Deviation", "Variance",
                "Pandas", "DataFrame", "SQL", "Python", "Excel", "Tableau", "Power BI",
                "GDPR", "Data Ethics", "Machine Learning", "Statistical Significance"
            ]
            autocomplete_dict.update(common_terms)
            
            # A4 Paper-like Editor Area
            if editor_mode == "📝 Edit" or editor_mode == "📄 Both":
                # Get current settings for styling
                current_font = st.session_state.get(f"font_family_{selected_course_code}", "Calibri")
                current_font_size = st.session_state.get(f"font_size_val_{selected_course_code}", "12")
                current_line_spacing = st.session_state.get(f"line_spacing_{selected_course_code}", "Single")
                current_page_color = st.session_state.get(f"page_color_{selected_course_code}", "#FFFFFF")
                current_text_color = st.session_state.get(f"text_color_{selected_course_code}", "#000000")
                
                # Get margin settings
                margin_top = st.session_state.get(f"margin_top_{selected_course_code}", 25)
                margin_bottom = st.session_state.get(f"margin_bottom_{selected_course_code}", 25)
                margin_left = st.session_state.get(f"margin_left_{selected_course_code}", 25)
                margin_right = st.session_state.get(f"margin_right_{selected_course_code}", 25)
                
                # Get show_lines setting
                show_lines = st.session_state.get(f"show_lines_{selected_course_code}", True)
                
                # Word-like editor styling with A4 paper appearance
                line_height_val = 1.5 if current_line_spacing == '1.5' else 2.0 if current_line_spacing == 'Double' else 1.0
                
                # Create ruled paper effect if enabled
                lines_bg = ""
                if show_lines:
                    line_color = "#e0e0e0"
                    line_spacing_px = int(float(current_font_size) * line_height_val * 1.2)
                    lines_bg = f"""
                    background-image: repeating-linear-gradient(
                        {line_color} 0px,
                        {line_color} 1px,
                        transparent 1px,
                        transparent {line_spacing_px}px
                    );
                    background-position: 0 {margin_top}px;
                    """
                
                word_editor_css = f"""
                <style>
                .a4-paper-container {{
                    width: {editor_width_px}px !important;
                    min-height: {editor_height_px}px !important;
                    margin: 20px auto !important;
                    background: #f5f5f5 !important;
                    padding: 20px !important;
                    box-shadow: 0 0 20px rgba(0,0,0,0.1) !important;
                }}
                .a4-paper {{
                    width: {editor_width_px}px !important;
                    min-height: {editor_height_px}px !important;
                    background: {current_page_color} !important;
                    margin: 0 auto !important;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.15) !important;
                    position: relative !important;
                    {lines_bg}
                }}
                .a4-paper::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: {margin_left}px;
                    right: {margin_right}px;
                    bottom: 0;
                    border-left: 1px dashed #d0d0d0;
                    border-right: 1px dashed #d0d0d0;
                    pointer-events: none;
                }}
                .word-editor-textarea {{
                    font-family: '{current_font}', 'Times New Roman', serif !important;
                    font-size: {current_font_size}pt !important;
                    line-height: {line_height_val} !important;
                    padding: {margin_top}px {margin_right}px {margin_bottom}px {margin_left}px !important;
                    border: none !important;
                    background: transparent !important;
                    color: {current_text_color} !important;
                    min-height: {editor_height_px}px !important;
                    width: {editor_width_px}px !important;
                    max-width: {editor_width_px}px !important;
                    resize: none !important;
                    box-sizing: border-box !important;
                }}
                .word-editor-textarea:focus {{
                    outline: none !important;
                }}
                .word-preview-area {{
                    font-family: '{current_font}', 'Times New Roman', serif !important;
                    font-size: {current_font_size}pt !important;
                    line-height: {line_height_val} !important;
                    padding: {margin_top}px {margin_right}px {margin_bottom}px {margin_left}px !important;
                    background: {current_page_color} !important;
                    border: 1px solid #dee2e6 !important;
                    min-height: {editor_height_px}px !important;
                    max-height: {editor_height_px}px !important;
                    width: {editor_width_px}px !important;
                    max-width: {editor_width_px}px !important;
                    overflow-y: auto !important;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.15) !important;
                    {lines_bg}
                }}
                </style>
                """
                st.markdown(word_editor_css, unsafe_allow_html=True)
                
                if editor_mode == "📄 Both":
                    editor_col, preview_col = st.columns([1, 1])
                else:
                    editor_col = st.container()
                    preview_col = None
                
                with editor_col:
                    # A4 Paper Container
                    st.markdown('<div class="a4-paper-container">', unsafe_allow_html=True)
                    st.markdown('<div class="a4-paper">', unsafe_allow_html=True)
                    
                    if show_ruler:
                        ruler_width = editor_width_px - margin_left - margin_right
                        ruler_html = f"""
                        <div style="background: #f8f9fa; border-bottom: 1px solid #dee2e6; padding: 2px {margin_right}px 2px {margin_left}px; font-size: 10px; color: #6c757d; width: {editor_width_px}px; box-sizing: border-box;">
                            {'&nbsp;'.join([str(i) for i in range(0, int(ruler_width/10), 50)])}
                        </div>
                        """
                        st.markdown(ruler_html, unsafe_allow_html=True)
                    
                    st.markdown(f"**📝 Editor** ({paper_type} - {current_font}, {current_font_size}pt)")
                    
                    note_content = st.text_area(
                        "Start typing your note here...",
                        value=default_content,
                        height=editor_height_px,
                        key=f"note_content_{selected_course_code}",
                        help="💡 A4 paper-like editor: Use the ribbon above for formatting, or type markdown directly",
                        label_visibility="collapsed"
                    )
                    
                    st.markdown('</div>', unsafe_allow_html=True)  # Close a4-paper
                    st.markdown('</div>', unsafe_allow_html=True)  # Close a4-paper-container
                    
                    # Enhanced Autocomplete with interactive suggestions
                    current_text = st.session_state.get(f"note_content_{selected_course_code}", "")
                    if current_text:
                        # Get last word or phrase
                        words = current_text.split()
                        if words:
                            last_word = words[-1].strip('.,!?;:')
                            if len(last_word) > 2:
                                suggestions = [term for term in autocomplete_dict if last_word.lower() in term.lower()][:8]
                                if suggestions:
                                    st.markdown("**💡 Autocomplete Suggestions:**")
                                    suggestion_cols = st.columns(min(4, len(suggestions)))
                                    for idx, suggestion in enumerate(suggestions[:4]):
                                        with suggestion_cols[idx]:
                                            if st.button(suggestion, key=f"sugg_{suggestion}_{selected_course_code}", use_container_width=True):
                                                # Replace last word with suggestion
                                                new_text = ' '.join(words[:-1]) + ' ' + suggestion + ' '
                                                st.session_state[f"note_content_{selected_course_code}"] = new_text
                                                st.rerun()
                    
                    # Enhanced Statistics Dashboard
                    st.markdown("---")
                    word_count = len(current_text.split()) if current_text else 0
                    char_count = len(current_text) if current_text else 0
                    char_no_spaces = len(current_text.replace(' ', '')) if current_text else 0
                    line_count = len(current_text.split('\n')) if current_text else 0
                    paragraph_count = len([p for p in current_text.split('\n\n') if p.strip()]) if current_text else 0
                    
                    # Calculate reading time (average 200 words per minute)
                    reading_time = max(1, round(word_count / 200)) if word_count > 0 else 0
                    
                    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
                    with stats_col1:
                        st.metric("📝 Words", word_count)
                        st.caption(f"~{reading_time} min read")
                    with stats_col2:
                        st.metric("📄 Characters", f"{char_count:,}")
                        st.caption(f"{char_no_spaces:,} no spaces")
                    with stats_col3:
                        st.metric("📋 Lines", line_count)
                        st.caption(f"{paragraph_count} paragraphs")
                    with stats_col4:
                        # Calculate markdown elements
                        headings = len(re.findall(r'^#+\s', current_text, re.MULTILINE)) if current_text else 0
                        links = len(re.findall(r'\[.*?\]\(.*?\)', current_text)) if current_text else 0
                        code_blocks = len(re.findall(r'```', current_text)) // 2 if current_text else 0
                        st.metric("📊 Elements", f"{headings}H, {links}L, {code_blocks}C")
                    
                    # Enhanced Spell Check
                    spellcheck_col1, spellcheck_col2 = st.columns([1, 1])
                    with spellcheck_col1:
                        if SPELLCHECK_AVAILABLE:
                            if st.button("🔍 Check Spelling", key=f"spellcheck_{selected_course_code}", use_container_width=True):
                                spell = SpellChecker()
                                words_list = re.findall(r'\b[a-zA-Z]+\b', current_text)
                                misspelled = spell.unknown(words_list)
                                if misspelled:
                                    misspelled_list = list(misspelled)[:15]
                                    st.warning(f"⚠️ **{len(misspelled)} potential errors found:**")
                                    for word in misspelled_list:
                                        corrections = spell.correction(word)
                                        st.text(f"• {word} → {corrections}")
                                else:
                                    st.success("✅ **No spelling errors found!**")
                        else:
                            st.info("💡 Install pyspellchecker for spell checking")
                    
                    with spellcheck_col2:
                        if st.button("📊 Text Analysis", key=f"text_analysis_{selected_course_code}", use_container_width=True):
                            st.session_state[f"show_text_analysis_{selected_course_code}"] = True
                            st.rerun()
                    
                    # Text Analysis
                    if st.session_state.get(f"show_text_analysis_{selected_course_code}", False):
                        st.markdown("**📊 Text Analysis:**")
                        if current_text:
                            # Word frequency
                            words_list = re.findall(r'\b[a-zA-Z]+\b', current_text.lower())
                            word_freq = {}
                            for word in words_list:
                                if len(word) > 3:  # Ignore short words
                                    word_freq[word] = word_freq.get(word, 0) + 1
                            
                            top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
                            if top_words:
                                st.markdown("**Most used words:**")
                                for word, count in top_words:
                                    st.progress(count / top_words[0][1], text=f"{word}: {count}")
                        
                        if st.button("Close Analysis", key=f"close_analysis_{selected_course_code}"):
                            st.session_state[f"show_text_analysis_{selected_course_code}"] = False
                            st.rerun()
                
                    if preview_col:
                        with preview_col:
                            st.markdown(f"**👁️ Preview** ({paper_type} - {current_font}, {current_font_size}pt)")
                            preview_content = st.session_state.get(f"note_content_{selected_course_code}", "")
                            
                            st.markdown('<div class="a4-paper-container">', unsafe_allow_html=True)
                            if preview_content:
                                st.markdown(f'<div class="word-preview-area">', unsafe_allow_html=True)
                                st.markdown(preview_content)
                                st.markdown('</div>', unsafe_allow_html=True)
                            else:
                                st.info("💡 Start typing to see preview...")
                            st.markdown('</div>', unsafe_allow_html=True)
            
            elif editor_mode == "👁️ Preview":
                preview_content = st.session_state.get(f"note_content_{selected_course_code}", default_content)
                current_font = st.session_state.get(f"font_family_{selected_course_code}", "Calibri")
                current_font_size = st.session_state.get(f"font_size_val_{selected_course_code}", "12")
                current_line_spacing = st.session_state.get(f"line_spacing_{selected_course_code}", "Single")
                current_page_color = st.session_state.get(f"page_color_{selected_course_code}", "#FFFFFF")
                margin_top = st.session_state.get(f"margin_top_{selected_course_code}", 25)
                margin_bottom = st.session_state.get(f"margin_bottom_{selected_course_code}", 25)
                margin_left = st.session_state.get(f"margin_left_{selected_course_code}", 25)
                margin_right = st.session_state.get(f"margin_right_{selected_course_code}", 25)
                line_height_val = 1.5 if current_line_spacing == '1.5' else 2.0 if current_line_spacing == 'Double' else 1.0
                
                lines_bg = ""
                if show_lines:
                    line_color = "#e0e0e0"
                    line_spacing_px = int(float(current_font_size) * line_height_val * 1.2)
                    lines_bg = f"""
                    background-image: repeating-linear-gradient(
                        {line_color} 0px,
                        {line_color} 1px,
                        transparent 1px,
                        transparent {line_spacing_px}px
                    );
                    background-position: 0 {margin_top}px;
                    """
                
                preview_css = f"""
                <style>
                .word-preview-area {{
                    font-family: '{current_font}', 'Times New Roman', serif !important;
                    font-size: {current_font_size}pt !important;
                    line-height: {line_height_val} !important;
                    padding: {margin_top}px {margin_right}px {margin_bottom}px {margin_left}px !important;
                    background: {current_page_color} !important;
                    border: 1px solid #dee2e6 !important;
                    min-height: {editor_height_px}px !important;
                    max-height: {editor_height_px}px !important;
                    width: {editor_width_px}px !important;
                    max-width: {editor_width_px}px !important;
                    overflow-y: auto !important;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.15) !important;
                    {lines_bg}
                }}
                </style>
                """
                st.markdown(preview_css, unsafe_allow_html=True)
                st.markdown('<div class="a4-paper-container">', unsafe_allow_html=True)
                st.markdown(f'<div class="word-preview-area">', unsafe_allow_html=True)
                st.markdown(preview_content)
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Word-like Status Bar
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<div class="word-status-bar">', unsafe_allow_html=True)
            
            current_text = st.session_state.get(f"note_content_{selected_course_code}", default_content)
            word_count = len(current_text.split()) if current_text else 0
            char_count = len(current_text) if current_text else 0
            char_no_spaces = len(current_text.replace(' ', '')) if current_text else 0
            page_count = max(1, word_count // 250)  # Approximate pages (250 words per page)
            
            # Get current settings for status bar
            status_font = st.session_state.get(f"font_family_{selected_course_code}", "Calibri")
            status_font_size = st.session_state.get(f"font_size_val_{selected_course_code}", "12")
            status_zoom = st.session_state.get(f"zoom_{selected_course_code}", 100)
            
            status_col1, status_col2, status_col3, status_col4, status_col5 = st.columns(5)
            with status_col1:
                st.caption(f"📝 Words: {word_count:,}")
            with status_col2:
                st.caption(f"📄 Characters: {char_count:,} ({char_no_spaces:,} no spaces)")
            with status_col3:
                st.caption(f"📋 Pages: {page_count}")
            with status_col4:
                st.caption(f"🔍 Zoom: {status_zoom}%")
            with status_col5:
                st.caption(f"📏 {status_font} {status_font_size}pt")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Enhanced Keyboard Shortcuts Help
            with st.expander("⌨️ Keyboard Shortcuts & Tips", expanded=False):
                shortcuts_col1, shortcuts_col2 = st.columns(2)
                
                with shortcuts_col1:
                    st.markdown("""
                    **⌨️ Keyboard Shortcuts:**
                    - `Ctrl+B` / `Cmd+B`: Bold text
                    - `Ctrl+I` / `Cmd+I`: Italic text
                    - `Ctrl+K` / `Cmd+K`: Insert link
                    - `Ctrl+Shift+C`: Code block
                    - `Ctrl+/`: Toggle preview
                    
                    **📝 Quick Markdown:**
                    - `**text**` → **bold**
                    - `*text*` → *italic*
                    - `~~text~~` → ~~strikethrough~~
                    - `` `code` `` → `inline code`
                    - `## Heading` → Heading
                    - `- item` → Bullet list
                    - `1. item` → Numbered list
                    - `> quote` → Blockquote
                    - `[text](url)` → Link
                    - `![alt](url)` → Image
                    """)
                
                with shortcuts_col2:
                    st.markdown("""
                    **🔤 Special Shortcuts:**
                    - Type `$` → LaTeX formula mode
                    - Type `@` → Code suggestions
                    - Type `:` → Emoji picker
                    
                    **📊 Advanced:**
                    - ` ```language` → Code block with syntax
                    - `| col1 | col2 |` → Table
                    - `---` → Horizontal rule
                    - `$$ formula $$` → Block formula
                    
                    **💡 Pro Tips:**
                    - Use toolbar buttons for quick formatting
                    - Click autocomplete suggestions to insert
                    - Check spelling before saving
                    - Use templates for common structures
                    """)
            
            note_tags = st.text_input("Tags (comma-separated):", value=default_tags, key=f"note_tags_{selected_course_code}")
            
            save_col1, save_col2 = st.columns(2)
            with save_col1:
                if st.button("💾 Save Note", type="primary", key=f"save_note_{selected_course_code}"):
                    # Get note_content from session state
                    note_content = st.session_state.get(f"note_content_{selected_course_code}", default_content)
                    if note_title and note_content:
                        tags_list = [tag.strip() for tag in note_tags.split(',') if tag.strip()] if note_tags else []
                        
                        version_entry = None
                        if is_editing and editing_idx < len(course_notes):
                            old_note = course_notes[editing_idx]
                            if old_note.get('content') != note_content:
                                version_entry = {
                                    'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                                    'summary': f"Updated from: {old_note.get('title', 'Untitled')[:30]}..."
                                }
                        
                        note_data = {
                            'title': note_title,
                            'content': note_content,
                            'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                            'tags': tags_list,
                            'category': note_category,
                            'importance': note_importance,
                            'learning_outcome': note_outcome if note_outcome != "(None)" else "",
                            'version_history': []
                        }
                        
                        if is_editing and editing_idx < len(course_notes):
                            existing_history = course_notes[editing_idx].get('version_history', [])
                            if version_entry:
                                existing_history.append(version_entry)
                            note_data['version_history'] = existing_history[-10:]
                            st.session_state.study_notes[selected_course_code][editing_idx] = note_data
                            del st.session_state[f"editing_note_{selected_course_code}"]
                        else:
                            st.session_state.study_notes[selected_course_code].append(note_data)
                        
                        st.success("Note saved!")
                        st.rerun()
                    else:
                        st.warning("Please fill in title and content.")
            
            with save_col2:
                if is_editing and st.button("❌ Cancel", key=f"cancel_edit_{selected_course_code}"):
                    del st.session_state[f"editing_note_{selected_course_code}"]
                    st.rerun()
        
        st.markdown("---")
        exp_col1, exp_col2 = st.columns(2)
        with exp_col1:
            if course_notes:
                export_data = {selected_course_code: course_notes}
                export_json = json.dumps(export_data, indent=2, ensure_ascii=False)
                st.download_button(
                    "📥 Export Notes (JSON)",
                    data=export_json,
                    file_name=f"study_notes_{selected_course_code}_{datetime.now().strftime('%Y%m%d')}.json",
                    mime="application/json"
                )
        with exp_col2:
            uploaded_file = st.file_uploader("📤 Import Notes (JSON)", type=['json'], key="notes_import")
            if uploaded_file:
                try:
                    imported_data = json.load(uploaded_file)
                    if selected_course_code in imported_data:
                        st.session_state.study_notes[selected_course_code].extend(imported_data[selected_course_code])
                        st.success(f"Imported {len(imported_data[selected_course_code])} notes!")
                        st.rerun()
                except Exception as e:
                    st.error(f"Import error: {str(e)}")
    
    with ai_tab:
        st.subheader("🤖 AI Study Assistant")
        st.markdown("*Generate summaries and study materials from course content*")
        
        ai_course_label = st.selectbox(
            "Select Course:",
            options=list(course_options.keys()),
            key="ai_course_select"
        )
        ai_course_code = course_options[ai_course_label]
        ai_course_data = next((c for c in courses_data if c['code'] == ai_course_code), None)
        
        ai_mode = st.radio(
            "What would you like to generate?",
            ["Course Summary", "Key Concepts", "Exam Prep Notes", "Learning Outcome Breakdown"],
            horizontal=True,
            key="ai_mode"
        )
        
        if st.button("🚀 Generate with AI", type="primary", key="ai_generate"):
            if ai_course_data:
                with st.spinner("Generating content..."):
                    course_info = f"Course: {ai_course_data['name']} ({ai_course_data['code']})\n"
                    course_info += f"Credits: {ai_course_data.get('credits', 'N/A')}\n"
                    
                    outcomes_text = ""
                    for lo in ai_course_data.get('learning_outcomes', []):
                        outcomes_text += f"\n{lo.get('type', 'General')}:\n"
                        for item in lo.get('items', []):
                            outcomes_text += f"- {item}\n"
                    
                    if ai_mode == "Course Summary":
                        prompt = f"""Create a comprehensive study summary for this course:
{course_info}

Learning Outcomes:
{outcomes_text}

Format the summary with:
1. Course Overview (2-3 sentences)
2. Key Topics to Master (bullet points)
3. Important Skills to Develop
4. How This Connects to Other Courses
5. Study Tips for This Course

Keep it concise but informative for a student."""
                    
                    elif ai_mode == "Key Concepts":
                        prompt = f"""Extract and explain the key concepts from this course:
{course_info}

Learning Outcomes:
{outcomes_text}

For each key concept, provide:
- Concept name
- Brief definition (1-2 sentences)
- Why it matters
- Example or application

List 5-8 key concepts."""
                    
                    elif ai_mode == "Exam Prep Notes":
                        prompt = f"""Create exam preparation notes for this course:
{course_info}

Learning Outcomes:
{outcomes_text}

Include:
1. Most likely exam topics
2. Key definitions to memorize
3. Common question types to expect
4. Important formulas or frameworks
5. Quick revision checklist

Format for easy memorization."""
                    
                    else:
                        prompt = f"""Break down each learning outcome for this course:
{course_info}

Learning Outcomes:
{outcomes_text}

For each outcome:
- Explain what it means in practical terms
- Give an example of how to demonstrate it
- Suggest how to practice it

Be specific and actionable."""
                    
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {"role": "system", "content": "You are a helpful study assistant for data analytics students. Create clear, well-structured study materials."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=1500
                        )
                        generated_content = response.choices[0].message.content
                        
                        st.markdown("### Generated Content")
                        st.markdown(generated_content)
                        
                        if st.button("💾 Save as Note", key="save_ai_note"):
                            if ai_course_code not in st.session_state.study_notes:
                                st.session_state.study_notes[ai_course_code] = []
                            
                            ai_note = {
                                'title': f"AI Generated: {ai_mode} - {ai_course_code}",
                                'content': generated_content,
                                'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                                'tags': ['ai-generated', ai_mode.lower().replace(' ', '-')],
                                'category': 'summary',
                                'importance': 'important',
                                'learning_outcome': '',
                                'version_history': []
                            }
                            st.session_state.study_notes[ai_course_code].append(ai_note)
                            st.success("Saved to your notes!")
                            st.rerun()
                    
                    except Exception as e:
                        st.error(f"Error generating content: {str(e)}")
            else:
                st.warning("Course data not found.")
    
    with templates_tab:
        st.subheader("📋 Note Templates")
        st.markdown("*Quick-start templates for different types of notes*")
        
        for key, template in NOTE_TEMPLATES.items():
            if key != "blank":
                with st.expander(f"📄 {template['name']}"):
                    st.code(template['content'], language="markdown")
                    if st.button(f"Use This Template", key=f"use_template_{key}"):
                        st.session_state['template_to_use'] = key
                        st.info("Go to 'My Notes' tab and the template will be applied to a new note.")
    
    with stats_tab:
        st.subheader("📊 Notes Statistics")
        
        total_notes = sum(len(notes) for notes in st.session_state.study_notes.values())
        st.metric("Total Notes", total_notes)
        
        if total_notes > 0:
            col_s1, col_s2 = st.columns(2)
            
            with col_s1:
                st.markdown("**Notes by Category**")
                cat_counts = {}
                for notes in st.session_state.study_notes.values():
                    for note in notes:
                        cat = note.get('category', 'lecture')
                        cat_counts[cat] = cat_counts.get(cat, 0) + 1
                
                for cat, count in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True):
                    cat_info = NOTE_CATEGORIES.get(cat, NOTE_CATEGORIES['lecture'])
                    st.write(f"{cat_info['icon']} {cat_info['label']}: {count}")
            
            with col_s2:
                st.markdown("**Notes by Course**")
                course_counts = {code: len(notes) for code, notes in st.session_state.study_notes.items() if notes}
                for code, count in sorted(course_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                    st.write(f"{code}: {count} notes")
            
            st.markdown("---")
            st.markdown("**Important Notes**")
            important_notes = []
            for code, notes in st.session_state.study_notes.items():
                for note in notes:
                    if note.get('importance') in ['important', 'critical']:
                        important_notes.append((code, note))
            
            if important_notes:
                for code, note in important_notes[:10]:
                    imp = note.get('importance', 'normal')
                    icon = "🔥" if imp == "critical" else "⭐"
                    st.write(f"{icon} [{code}] {note.get('title', 'Untitled')}")
            else:
                st.info("No important notes marked yet.")

elif page == "Flashcards":
    st.title("🎴 Flashcards")
    st.markdown("*Learn with spaced repetition*")
    st.markdown("---")
    
    # Initialize flashcard counter if not exists
    if 'flashcard_counter' not in st.session_state:
        st.session_state.flashcard_counter = 0
    
    tab1, tab2, tab3 = st.tabs(["📚 Study", "➕ Create Cards", "📊 Statistics"])
    
    with tab1:
        st.subheader("Study Mode")
        
        # Get cards that need review
        now = datetime.now()
        cards_to_review = []
        for card_id, card in st.session_state.flashcards.items():
            next_review = card.get('next_review')
            if next_review:
                try:
                    next_review_dt = datetime.fromisoformat(next_review)
                    if next_review_dt <= now:
                        cards_to_review.append((card_id, card))
                except:
                    cards_to_review.append((card_id, card))
            else:
                cards_to_review.append((card_id, card))
        
        if not cards_to_review:
            st.info("🎉 No cards need review right now! Create some cards or check back later.")
        else:
            # Filter by course
            course_filter = st.selectbox(
                "Filter by course:",
                ["All Courses"] + [c['code'] for c in courses_data]
            )
            
            if course_filter != "All Courses":
                cards_to_review = [(cid, c) for cid, c in cards_to_review if c.get('course') == course_filter]
            
            if cards_to_review:
                # Get current card
                if 'current_card_idx' not in st.session_state:
                    st.session_state.current_card_idx = 0
                
                current_idx = st.session_state.current_card_idx % len(cards_to_review)
                card_id, current_card = cards_to_review[current_idx]
                
                st.markdown(f"**Card {current_idx + 1} of {len(cards_to_review)}**")
                st.progress((current_idx + 1) / len(cards_to_review))
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("### Front")
                    st.info(current_card.get('front', 'No front text'))
                
                show_answer = st.session_state.get(f"show_answer_{card_id}", False)
                
                if show_answer:
                    with col2:
                        st.markdown("### Back")
                        st.success(current_card.get('back', 'No back text'))
                    
                    st.markdown("---")
                    st.markdown("### How well did you know this?")
                    
                    col_a, col_b, col_c, col_d = st.columns(4)
                    
                    def update_card_difficulty(difficulty):
                        # SM-2 algorithm parameters
                        card = st.session_state.flashcards[card_id]
                        ease_factor = card.get('ease_factor', 2.5)
                        interval = card.get('interval', 1)
                        repetitions = card.get('repetitions', 0)
                        
                        if difficulty == "Again":
                            interval = 1
                            repetitions = 0
                            ease_factor = max(1.3, ease_factor - 0.2)
                        elif difficulty == "Hard":
                            interval = max(1, interval * 1.2)
                            ease_factor = max(1.3, ease_factor - 0.15)
                        elif difficulty == "Good":
                            if repetitions == 0:
                                interval = 1
                            elif repetitions == 1:
                                interval = 6
                            else:
                                interval = int(interval * ease_factor)
                            repetitions += 1
                            ease_factor = ease_factor
                        elif difficulty == "Easy":
                            interval = int(interval * ease_factor * 1.3)
                            repetitions += 1
                            ease_factor = ease_factor + 0.15
                        
                        # Update card
                        next_review = datetime.now() + timedelta(days=interval)
                        st.session_state.flashcards[card_id].update({
                            'interval': interval,
                            'repetitions': repetitions,
                            'ease_factor': ease_factor,
                            'next_review': next_review.isoformat(),
                            'last_reviewed': datetime.now().isoformat()
                        })
                        
                        # Update stats
                        st.session_state.flashcard_stats['cards_reviewed'] = st.session_state.flashcard_stats.get('cards_reviewed', 0) + 1
                        if difficulty in ["Good", "Easy"]:
                            st.session_state.flashcard_stats['cards_mastered'] = st.session_state.flashcard_stats.get('cards_mastered', 0) + 1
                        
                        # Move to next card
                        st.session_state.current_card_idx += 1
                        del st.session_state[f"show_answer_{card_id}"]
                        st.rerun()
                    
                    with col_a:
                        st.button("❌ Again", on_click=lambda: update_card_difficulty("Again"), use_container_width=True)
                    with col_b:
                        st.button("😓 Hard", on_click=lambda: update_card_difficulty("Hard"), use_container_width=True)
                    with col_c:
                        st.button("✅ Good", on_click=lambda: update_card_difficulty("Good"), use_container_width=True, type="primary")
                    with col_d:
                        st.button("😊 Easy", on_click=lambda: update_card_difficulty("Easy"), use_container_width=True)
                else:
                    if st.button("👁️ Show Answer", type="primary", use_container_width=True):
                        st.session_state[f"show_answer_{card_id}"] = True
                        st.rerun()
            else:
                st.info("No cards to review for this course.")
    
    with tab2:
        st.subheader("Create New Flashcard")
        
        col1, col2 = st.columns(2)
        with col1:
            card_course = st.selectbox(
                "Course:",
                [c['code'] for c in courses_data]
            )
            card_front = st.text_area("Front:", height=150, placeholder="Question or term...")
        
        with col2:
            card_back = st.text_area("Back:", height=150, placeholder="Answer or definition...")
            card_tags = st.text_input("Tags (optional):", placeholder="comma-separated")
        
        if st.button("➕ Create Card", type="primary"):
            if card_front and card_back:
                card_id = f"card_{st.session_state.flashcard_counter}"
                st.session_state.flashcard_counter += 1
                
                st.session_state.flashcards[card_id] = {
                    'front': card_front,
                    'back': card_back,
                    'course': card_course,
                    'tags': [t.strip() for t in card_tags.split(',') if t.strip()] if card_tags else [],
                    'interval': 1,
                    'repetitions': 0,
                    'ease_factor': 2.5,
                    'next_review': datetime.now().isoformat(),
                    'created': datetime.now().isoformat()
                }
                
                st.session_state.flashcard_stats['total_cards'] = len(st.session_state.flashcards)
                st.success("Card created!")
                st.rerun()
            else:
                st.warning("Please fill in both front and back.")
        
        # Show existing cards
        st.markdown("---")
        st.subheader("Your Cards")
        
        if st.session_state.flashcards:
            course_filter_create = st.selectbox(
                "Filter by course:",
                ["All Courses"] + [c['code'] for c in courses_data],
                key="filter_create"
            )
            
            filtered_cards = st.session_state.flashcards
            if course_filter_create != "All Courses":
                filtered_cards = {k: v for k, v in filtered_cards.items() if v.get('course') == course_filter_create}
            
            for card_id, card in filtered_cards.items():
                with st.expander(f"📴 {card.get('front', 'No front')[:50]}..."):
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.markdown(f"**Front:** {card.get('front')}")
                    with col_b:
                        st.markdown(f"**Back:** {card.get('back')}")
                    st.caption(f"Course: {card.get('course')} | Next review: {card.get('next_review', 'Not set')}")
                    if st.button(f"🗑️ Delete", key=f"delete_card_{card_id}"):
                        del st.session_state.flashcards[card_id]
                        st.session_state.flashcard_stats['total_cards'] = len(st.session_state.flashcards)
                        st.rerun()
        else:
            st.info("No cards created yet.")
    
    with tab3:
        st.subheader("Statistics")
        
        stats = st.session_state.flashcard_stats
        total = stats.get('total_cards', 0)
        reviewed = stats.get('cards_reviewed', 0)
        mastered = stats.get('cards_mastered', 0)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Cards", total)
        with col2:
            st.metric("Cards Reviewed", reviewed)
        with col3:
            st.metric("Cards Mastered", mastered)
        
        if total > 0:
            st.markdown("---")
            st.markdown(f"**Mastery Rate:** {mastered / reviewed * 100:.1f}%" if reviewed > 0 else "**Mastery Rate:** N/A")
            
            # Cards by course
            course_counts = {}
            for card in st.session_state.flashcards.values():
                course = card.get('course', 'Unknown')
                course_counts[course] = course_counts.get(course, 0) + 1
            
            if course_counts:
                st.markdown("---")
                st.markdown("### Cards by Course")
                for course, count in course_counts.items():
                    st.markdown(f"- **{course}:** {count} cards")

elif page == "Exam Simulator":
    st.title("📋 Exam Simulator")
    st.markdown("*Practice for your exams with timed simulations*")
    st.markdown("---")
    
    if not st.session_state.exam_mode:
        st.subheader("Configure Your Exam")
        
        col1, col2 = st.columns(2)
        with col1:
            exam_course = st.selectbox(
                "Select Course:",
                [c['code'] for c in courses_data]
            )
            num_questions = st.number_input("Number of Questions:", min_value=5, max_value=50, value=10, step=5)
        
        with col2:
            exam_duration = st.number_input("Duration (minutes):", min_value=10, max_value=180, value=60, step=10)
            question_types = st.multiselect(
                "Question Types:",
                ["General", "Knowledge-based", "Skills-based", "Case Study"],
                default=["General", "Knowledge-based"]
            )
        
        if st.button("🚀 Start Exam", type="primary"):
            # Generate exam questions
            selected_course = next(c for c in courses_data if c['code'] == exam_course)
            exam_questions_list = []
            
            type_map = {
                "General": "general",
                "Knowledge-based": "knowledge",
                "Skills-based": "skills",
                "Case Study": "case_study"
            }
            
            with st.spinner("Generating exam questions..."):
                for i in range(num_questions):
                    q_type = type_map.get(question_types[i % len(question_types)], "general")
                    question = generate_practice_question(selected_course, q_type)
                    if question and "Error" not in question:
                        exam_questions_list.append({
                            'id': i,
                            'question': question,
                            'type': q_type,
                            'user_answer': ''
                        })
            
            if exam_questions_list:
                st.session_state.exam_questions = exam_questions_list
                st.session_state.exam_answers = {}
                st.session_state.exam_start_time = time.time()
                st.session_state.exam_duration = exam_duration * 60  # Convert to seconds
                st.session_state.exam_mode = True
                st.session_state.exam_course = exam_course
                st.rerun()
            else:
                st.error("Failed to generate exam questions. Please try again.")
    
    else:
        # Exam in progress
        elapsed_time = time.time() - st.session_state.exam_start_time
        remaining_time = max(0, st.session_state.exam_duration - elapsed_time)
        remaining_minutes = int(remaining_time // 60)
        remaining_seconds = int(remaining_time % 60)
        
        # Timer display
        if remaining_time > 0:
            st.warning(f"⏱️ Time Remaining: {remaining_minutes:02d}:{remaining_seconds:02d}")
            progress = elapsed_time / st.session_state.exam_duration
            st.progress(progress)
        else:
            st.error("⏰ Time's up! Your exam will be submitted automatically.")
            if 'exam_submitted' not in st.session_state:
                st.session_state.exam_submitted = True
                st.rerun()
        
        st.markdown(f"**Course:** {st.session_state.exam_course}")
        st.markdown(f"**Questions:** {len(st.session_state.exam_questions)}")
        
        # Display questions
        st.markdown("---")
        
        view_mode = st.radio("View Mode:", ["One at a time", "All questions"], horizontal=True)
        
        if view_mode == "One at a time":
            if 'current_question_idx' not in st.session_state:
                st.session_state.current_question_idx = 0
            
            current_idx = st.session_state.current_question_idx
            current_q = st.session_state.exam_questions[current_idx]
            
            st.markdown(f"### Question {current_idx + 1} of {len(st.session_state.exam_questions)}")
            
            # Parse question
            if "ANSWER:" in current_q['question']:
                parts = current_q['question'].split("ANSWER:")
                question_text = parts[0].strip()
            else:
                question_text = current_q['question']
            
            st.markdown(f"**{question_text}**")
            
            # Answer input
            answer_key = f"exam_answer_{current_idx}"
            if answer_key not in st.session_state.exam_answers:
                st.session_state.exam_answers[answer_key] = ""
            
            user_answer = st.text_area(
                "Your Answer:",
                value=st.session_state.exam_answers[answer_key],
                height=150,
                key=f"answer_input_{current_idx}"
            )
            st.session_state.exam_answers[answer_key] = user_answer
            
            # Navigation
            col_nav1, col_nav2, col_nav3 = st.columns(3)
            with col_nav1:
                if st.button("⬅️ Previous", disabled=current_idx == 0):
                    st.session_state.current_question_idx = max(0, current_idx - 1)
                    st.rerun()
            with col_nav2:
                st.markdown(f"**{current_idx + 1}/{len(st.session_state.exam_questions)}**")
            with col_nav3:
                if st.button("➡️ Next", disabled=current_idx == len(st.session_state.exam_questions) - 1):
                    st.session_state.current_question_idx = min(len(st.session_state.exam_questions) - 1, current_idx + 1)
                    st.rerun()
        
        else:
            # All questions view
            for idx, q in enumerate(st.session_state.exam_questions):
                with st.expander(f"Question {idx + 1}"):
                    if "ANSWER:" in q['question']:
                        parts = q['question'].split("ANSWER:")
                        question_text = parts[0].strip()
                    else:
                        question_text = q['question']
                    
                    st.markdown(f"**{question_text}**")
                    
                    answer_key = f"exam_answer_{idx}"
                    if answer_key not in st.session_state.exam_answers:
                        st.session_state.exam_answers[answer_key] = ""
                    
                    user_answer = st.text_area(
                        "Your Answer:",
                        value=st.session_state.exam_answers[answer_key],
                        height=100,
                        key=f"answer_all_{idx}"
                    )
                    st.session_state.exam_answers[answer_key] = user_answer
        
        st.markdown("---")
        
        # Submit exam
        col_sub1, col_sub2 = st.columns([1, 1])
        with col_sub1:
            if st.button("📤 Submit Exam", type="primary"):
                st.session_state.exam_submitted = True
                st.rerun()
        with col_sub2:
            if st.button("❌ Cancel Exam"):
                if st.checkbox("Are you sure? This will discard your progress."):
                    st.session_state.exam_mode = False
                    st.session_state.exam_questions = []
                    st.session_state.exam_answers = {}
                    st.session_state.exam_start_time = None
                    st.rerun()
        
        # Auto-submit if time is up
        if remaining_time <= 0 and 'exam_submitted' not in st.session_state:
            st.session_state.exam_submitted = True
            st.rerun()
    
    # Show results if exam submitted
    if st.session_state.get('exam_submitted', False) and st.session_state.exam_mode:
        st.markdown("---")
        st.title("📊 Exam Results")
        
        # Evaluate answers
        results = []
        total_score = 0
        
        for idx, q in enumerate(st.session_state.exam_questions):
            answer_key = f"exam_answer_{idx}"
            user_answer = st.session_state.exam_answers.get(answer_key, "")
            
            # Parse question for correct answer
            if "ANSWER:" in q['question']:
                parts = q['question'].split("ANSWER:")
                question_text = parts[0].strip()
                correct_answer = parts[1].strip() if len(parts) > 1 else ""
            else:
                question_text = q['question']
                correct_answer = "Answer not available"
            
            # Evaluate using AI
            if user_answer.strip():
                feedback = evaluate_answer(question_text, correct_answer, user_answer)
                # Simple scoring: if feedback is positive, give points
                score = 1 if "correct" in feedback.lower() or "good" in feedback.lower() else 0.5
            else:
                feedback = "No answer provided"
                score = 0
            
            total_score += score
            results.append({
                'question': question_text,
                'user_answer': user_answer,
                'correct_answer': correct_answer,
                'feedback': feedback,
                'score': score
            })
        
        # Display results
        percentage = (total_score / len(st.session_state.exam_questions)) * 100
        
        st.metric("Your Score", f"{total_score:.1f}/{len(st.session_state.exam_questions)} ({percentage:.1f}%)")
        
        if percentage >= 80:
            st.success("🎉 Excellent work!")
        elif percentage >= 60:
            st.info("👍 Good job!")
        else:
            st.warning("📚 Keep studying!")
        
        st.markdown("---")
        st.subheader("Detailed Feedback")
        
        for idx, result in enumerate(results):
            with st.expander(f"Question {idx + 1} - Score: {result['score']}/1"):
                st.markdown(f"**Question:** {result['question']}")
                st.markdown(f"**Your Answer:** {result['user_answer'] if result['user_answer'] else 'No answer'}")
                st.markdown(f"**Correct Answer:** {result['correct_answer']}")
                st.markdown(f"**Feedback:** {result['feedback']}")
        
        if st.button("🔄 Take Another Exam"):
            st.session_state.exam_mode = False
            st.session_state.exam_submitted = False
            st.session_state.exam_questions = []
            st.session_state.exam_answers = {}
            st.session_state.exam_start_time = None
            st.rerun()

elif page == "Code Library":
    st.title("💻 Code Library")
    st.markdown("*Useful code snippets and examples*")
    st.markdown("---")
    
    # Initialize default snippets if empty
    if not st.session_state.code_snippets:
        default_snippets = {
            "pandas_basic": {
                "title": "Pandas DataFrame Basics",
                "code": """import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})

# Basic operations
print(df.head())
print(df.describe())
print(df.info())""",
                "language": "python",
                "category": "Pandas",
                "description": "Basic DataFrame creation and operations"
            },
            "pandas_filter": {
                "title": "Filtering DataFrames",
                "code": """# Filter rows
filtered = df[df['age'] > 25]

# Multiple conditions
filtered = df[(df['age'] > 25) & (df['salary'] > 55000)]

# Filter by string contains
filtered = df[df['name'].str.contains('A')]

# Filter by isin
filtered = df[df['name'].isin(['Alice', 'Bob'])]""",
                "language": "python",
                "category": "Pandas",
                "description": "Common filtering operations"
            },
            "pandas_groupby": {
                "title": "GroupBy Operations",
                "code": """# Group by column
grouped = df.groupby('department')

# Aggregations
summary = df.groupby('department').agg({
    'salary': ['mean', 'sum', 'count'],
    'age': 'mean'
})

# Multiple groupby columns
grouped = df.groupby(['department', 'role']).sum()""",
                "language": "python",
                "category": "Pandas",
                "description": "GroupBy and aggregation examples"
            },
            "sql_select": {
                "title": "SQL SELECT Basics",
                "code": """-- Basic SELECT
SELECT * FROM customers;

-- SELECT with WHERE
SELECT name, email 
FROM customers 
WHERE age > 25;

-- SELECT with JOIN
SELECT c.name, o.order_date, o.amount
FROM customers c
JOIN orders o ON c.id = o.customer_id;""",
                "language": "sql",
                "category": "SQL",
                "description": "Basic SQL SELECT queries"
            },
            "sql_aggregate": {
                "title": "SQL Aggregations",
                "code": """-- COUNT, SUM, AVG
SELECT 
    COUNT(*) as total_orders,
    SUM(amount) as total_revenue,
    AVG(amount) as avg_order_value
FROM orders;

-- GROUP BY
SELECT 
    customer_id,
    COUNT(*) as order_count,
    SUM(amount) as total_spent
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 5;""",
                "language": "sql",
                "category": "SQL",
                "description": "SQL aggregation functions"
            },
            "excel_sumif": {
                "title": "Excel SUMIF Function",
                "code": """=SUMIF(range, criteria, sum_range)

-- Examples:
=SUMIF(A2:A10, ">100", B2:B10)
=SUMIF(C2:C10, "North", D2:D10)
=SUMIF(E2:E10, ">=2024-01-01", F2:F10)""",
                "language": "excel",
                "category": "Excel",
                "description": "SUMIF function examples"
            },
            "excel_vlookup": {
                "title": "Excel VLOOKUP",
                "code": """=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])

-- Examples:
=VLOOKUP(A2, Sheet2!A:B, 2, FALSE)
=VLOOKUP("Product1", Products!A:D, 4, FALSE)""",
                "language": "excel",
                "category": "Excel",
                "description": "VLOOKUP function examples"
            },
            "python_stats": {
                "title": "Python Statistical Functions",
                "code": """import numpy as np
from scipy import stats

# Descriptive statistics
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean = np.mean(data)
median = np.median(data)
std = np.std(data)

# Correlation
correlation = np.corrcoef(x, y)[0, 1]

# T-test
t_stat, p_value = stats.ttest_ind(group1, group2)""",
                "language": "python",
                "category": "Statistics",
                "description": "Statistical calculations in Python"
            }
        }
        st.session_state.code_snippets = default_snippets
    
    # Search and filter
    col_search, col_filter = st.columns([2, 1])
    with col_search:
        search_query = st.text_input("🔍 Search snippets:", placeholder="Search by title, description, or code...")
    with col_filter:
        category_filter = st.selectbox(
            "Category:",
            ["All"] + list(set(s.get('category', 'Other') for s in st.session_state.code_snippets.values()))
        )
    
    # Filter snippets
    filtered_snippets = st.session_state.code_snippets
    if search_query:
        filtered_snippets = {
            k: v for k, v in filtered_snippets.items()
            if search_query.lower() in v.get('title', '').lower() or
               search_query.lower() in v.get('description', '').lower() or
               search_query.lower() in v.get('code', '').lower()
        }
    if category_filter != "All":
        filtered_snippets = {
            k: v for k, v in filtered_snippets.items()
            if v.get('category') == category_filter
        }
    
    # Display snippets
    if filtered_snippets:
        for snippet_id, snippet in filtered_snippets.items():
            with st.expander(f"📄 {snippet.get('title', 'Untitled')} - {snippet.get('category', 'Other')}"):
                st.markdown(f"**Description:** {snippet.get('description', 'No description')}")
                st.code(snippet.get('code', ''), language=snippet.get('language', 'python'))
                
                # Copy button (using download button as workaround)
                code_text = snippet.get('code', '')
                st.download_button(
                    "📋 Copy Code",
                    data=code_text,
                    file_name=f"{snippet.get('title', 'code')}.txt",
                    mime="text/plain"
                )
                
                if st.button(f"🗑️ Delete", key=f"delete_snippet_{snippet_id}"):
                    del st.session_state.code_snippets[snippet_id]
                    st.rerun()
    else:
        st.info("No snippets found. Create one below!")
    
    st.markdown("---")
    st.subheader("➕ Add Custom Snippet")
    
    col1, col2 = st.columns(2)
    with col1:
        new_title = st.text_input("Title:")
        new_category = st.selectbox(
            "Category:",
            ["Pandas", "SQL", "Excel", "Statistics", "Python", "Other"]
        )
        new_language = st.selectbox(
            "Language:",
            ["python", "sql", "excel", "javascript", "other"]
        )
    
    with col2:
        new_description = st.text_area("Description:", height=80)
    
    new_code = st.text_area("Code:", height=200, placeholder="Paste your code here...")
    
    if st.button("➕ Add Snippet", type="primary"):
        if new_title and new_code:
            snippet_id = f"custom_{int(time.time())}"
            st.session_state.code_snippets[snippet_id] = {
                'title': new_title,
                'code': new_code,
                'language': new_language,
                'category': new_category,
                'description': new_description
            }
            st.success("Snippet added!")
            st.rerun()
        else:
            st.warning("Please fill in title and code.")

elif page == "Formula Reference":
    st.title("🔢 Formula Reference")
    st.markdown("*Quick reference for statistical formulas*")
    st.markdown("---")
    
    # Category selection
    category = st.selectbox(
        "Select Category:",
        ["Descriptive Statistics", "Inferential Statistics", "Regression", "Correlation", "Probability", "All"]
    )
    
    # Search
    search_query = st.text_input("🔍 Search formulas:", placeholder="Search by name or description...")
    
    # Formula database
    formulas = {
        "Descriptive Statistics": [
            {
                "name": "Mean (Average)",
                "formula": r"\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i",
                "description": "The average of all values in a dataset",
                "example": "For [1, 2, 3, 4, 5]: mean = (1+2+3+4+5)/5 = 3"
            },
            {
                "name": "Median",
                "formula": r"\text{Median} = \begin{cases} x_{\frac{n+1}{2}} & \text{if } n \text{ is odd} \\ \frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2} & \text{if } n \text{ is even} \end{cases}",
                "description": "The middle value when data is sorted",
                "example": "For [1, 2, 3, 4, 5]: median = 3\nFor [1, 2, 3, 4]: median = (2+3)/2 = 2.5"
            },
            {
                "name": "Standard Deviation",
                "formula": r"s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}",
                "description": "Measures the spread of data around the mean",
                "example": "For [1, 2, 3, 4, 5] with mean=3:\ns = √[((1-3)²+(2-3)²+(3-3)²+(4-3)²+(5-3)²)/4] = √2.5 ≈ 1.58"
            },
            {
                "name": "Variance",
                "formula": r"s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2",
                "description": "The square of standard deviation",
                "example": "Variance = (Standard Deviation)²"
            },
            {
                "name": "Range",
                "formula": r"\text{Range} = \max(x_i) - \min(x_i)",
                "description": "Difference between maximum and minimum values",
                "example": "For [1, 2, 3, 4, 5]: range = 5 - 1 = 4"
            }
        ],
        "Inferential Statistics": [
            {
                "name": "Z-Score",
                "formula": r"z = \frac{x - \mu}{\sigma}",
                "description": "Number of standard deviations a value is from the mean",
                "example": "If x=110, μ=100, σ=10: z = (110-100)/10 = 1.0"
            },
            {
                "name": "T-Test (One Sample)",
                "formula": r"t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}",
                "description": "Tests if sample mean differs from population mean",
                "example": "Compare sample mean to hypothesized population mean"
            },
            {
                "name": "Confidence Interval (Mean)",
                "formula": r"\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}",
                "description": "Range likely to contain population mean",
                "example": "95% CI: x̄ ± 1.96 × (σ/√n)"
            },
            {
                "name": "Sample Size",
                "formula": r"n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2",
                "description": "Required sample size for desired margin of error",
                "example": "For E=2, σ=10, 95% confidence: n = (1.96×10/2)² ≈ 96"
            }
        ],
        "Regression": [
            {
                "name": "Simple Linear Regression",
                "formula": r"y = \beta_0 + \beta_1 x + \epsilon",
                "description": "Predicts y from x using a linear relationship",
                "example": "y = 2 + 3x means for each unit increase in x, y increases by 3"
            },
            {
                "name": "Slope (β₁)",
                "formula": r"\beta_1 = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}",
                "description": "Rate of change in y per unit change in x",
                "example": "Positive slope = positive correlation"
            },
            {
                "name": "Intercept (β₀)",
                "formula": r"\beta_0 = \bar{y} - \beta_1 \bar{x}",
                "description": "Value of y when x = 0",
                "example": "Starting point of the regression line"
            },
            {
                "name": "R² (Coefficient of Determination)",
                "formula": r"R^2 = 1 - \frac{SS_{res}}{SS_{tot}}",
                "description": "Proportion of variance explained by the model",
                "example": "R² = 0.85 means 85% of variance is explained"
            }
        ],
        "Correlation": [
            {
                "name": "Pearson Correlation",
                "formula": r"r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2}}",
                "description": "Measures linear relationship between two variables",
                "example": "r ranges from -1 (perfect negative) to +1 (perfect positive)"
            },
            {
                "name": "Covariance",
                "formula": r"\text{Cov}(X,Y) = \frac{1}{n-1}\sum(x_i - \bar{x})(y_i - \bar{y})",
                "description": "Measures how two variables vary together",
                "example": "Positive = variables increase together"
            }
        ],
        "Probability": [
            {
                "name": "Probability",
                "formula": r"P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total outcomes}}",
                "description": "Likelihood of an event occurring",
                "example": "P(rolling 6 on die) = 1/6 ≈ 0.167"
            },
            {
                "name": "Conditional Probability",
                "formula": r"P(A|B) = \frac{P(A \cap B)}{P(B)}",
                "description": "Probability of A given B has occurred",
                "example": "P(rain|cloudy) = probability of rain when it's cloudy"
            },
            {
                "name": "Bayes' Theorem",
                "formula": r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}",
                "description": "Updates probability based on new evidence",
                "example": "Used in medical diagnosis and machine learning"
            }
        ]
    }
    
    # Filter formulas
    display_formulas = {}
    if category == "All":
        display_formulas = formulas
    else:
        if category in formulas:
            display_formulas[category] = formulas[category]
    
    # Apply search filter
    if search_query:
        filtered_formulas = {}
        for cat, form_list in display_formulas.items():
            filtered = [
                f for f in form_list
                if search_query.lower() in f['name'].lower() or
                   search_query.lower() in f['description'].lower()
            ]
            if filtered:
                filtered_formulas[cat] = filtered
        display_formulas = filtered_formulas
    
    # Display formulas
    if display_formulas:
        for cat, form_list in display_formulas.items():
            st.markdown(f"### {cat}")
            for formula in form_list:
                with st.expander(f"**{formula['name']}**"):
                    st.markdown(f"**Description:** {formula['description']}")
                    st.latex(formula['formula'])
                    st.markdown(f"**Example:** {formula['example']}")
            st.markdown("---")
    else:
        st.info("No formulas found. Try a different search or category.")

elif page == "Study Timer":
    st.title("⏱️ Study Timer")
    st.markdown("*Track your study time with Pomodoro technique*")
    st.markdown("---")
    
    # Initialize timer state
    if 'timer_paused' not in st.session_state:
        st.session_state.timer_paused = False
    if 'pomodoro_count' not in st.session_state:
        st.session_state.pomodoro_count = 0
    if 'current_timer_course' not in st.session_state:
        st.session_state.current_timer_course = None
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Timer display
        if st.session_state.study_timer_active:
            elapsed = time.time() - st.session_state.study_timer_start
            remaining = max(0, st.session_state.study_timer_duration - elapsed)
            
            # Convert to minutes and seconds
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            
            # Large timer display
            st.markdown(f"<h1 style='text-align: center; font-size: 72px;'>{minutes:02d}:{seconds:02d}</h1>", unsafe_allow_html=True)
            
            # Progress bar
            progress = 1 - (remaining / st.session_state.study_timer_duration) if st.session_state.study_timer_duration > 0 else 0
            st.progress(progress)
            
            # Course being studied
            if st.session_state.current_timer_course:
                course_name = next((c['name'] for c in courses_data if c['code'] == st.session_state.current_timer_course), "Unknown")
                st.markdown(f"**Studying:** {st.session_state.current_timer_course} - {course_name}")
            
            # Control buttons
            col_btn1, col_btn2, col_btn3 = st.columns(3)
            
            with col_btn1:
                if st.button("⏸️ Pause", use_container_width=True):
                    if not st.session_state.timer_paused:
                        st.session_state.timer_paused = True
                        st.session_state.timer_pause_time = time.time()
                        st.session_state.timer_elapsed_before_pause = elapsed
                    else:
                        st.session_state.timer_paused = False
                        st.session_state.study_timer_start = time.time() - st.session_state.timer_elapsed_before_pause
                    st.rerun()
            
            with col_btn2:
                if st.button("⏹️ Stop", use_container_width=True, type="primary"):
                    # Save session
                    if st.session_state.current_timer_course:
                        course_code = st.session_state.current_timer_course
                        elapsed_total = elapsed if not st.session_state.timer_paused else st.session_state.timer_elapsed_before_pause
                        
                        session_data = {
                            'course': course_code,
                            'duration': int(elapsed_total),
                            'date': datetime.now().isoformat(),
                            'pomodoro': st.session_state.pomodoro_count > 0
                        }
                        st.session_state.study_sessions.append(session_data)
                        
                        # Update course time
                        if course_code not in st.session_state.study_time_by_course:
                            st.session_state.study_time_by_course[course_code] = 0
                        st.session_state.study_time_by_course[course_code] += int(elapsed_total)
                    
                    # Reset timer
                    st.session_state.study_timer_active = False
                    st.session_state.study_timer_start = None
                    st.session_state.timer_paused = False
                    st.session_state.pomodoro_count = 0
                    st.rerun()
            
            with col_btn3:
                if st.button("🔄 Reset", use_container_width=True):
                    st.session_state.study_timer_start = time.time()
                    st.session_state.timer_paused = False
                    st.rerun()
            
            # Auto-stop when timer reaches 0
            if remaining <= 0:
                st.balloons()
                st.success("🎉 Time's up! Great work!")
                
                # Save session
                if st.session_state.current_timer_course:
                    course_code = st.session_state.current_timer_course
                    session_data = {
                        'course': course_code,
                        'duration': st.session_state.study_timer_duration,
                        'date': datetime.now().isoformat(),
                        'pomodoro': True
                    }
                    st.session_state.study_sessions.append(session_data)
                    
                    if course_code not in st.session_state.study_time_by_course:
                        st.session_state.study_time_by_course[course_code] = 0
                    st.session_state.study_time_by_course[course_code] += st.session_state.study_timer_duration
                
                st.session_state.study_timer_active = False
                st.session_state.pomodoro_count += 1
                st.rerun()
            
            # Auto-refresh for timer updates (Streamlit will rerun on interaction)
            # Use a placeholder to trigger updates
            placeholder = st.empty()
            placeholder.markdown("")  # Empty placeholder to allow reruns
        
        else:
            # Timer setup
            st.subheader("Configure Timer")
            
            timer_mode = st.radio(
                "Timer Mode:",
                ["Pomodoro (25 min)", "Short Break (5 min)", "Long Break (15 min)", "Custom"]
            )
            
            if timer_mode == "Pomodoro (25 min)":
                duration_minutes = 25
            elif timer_mode == "Short Break (5 min)":
                duration_minutes = 5
            elif timer_mode == "Long Break (15 min)":
                duration_minutes = 15
            else:
                duration_minutes = st.number_input("Custom Duration (minutes):", min_value=1, max_value=180, value=25)
            
            selected_course = st.selectbox(
                "Select Course (optional):",
                ["None"] + [f"{c['code']} - {c['name']}" for c in courses_data]
            )
            
            if st.button("▶️ Start Timer", type="primary", use_container_width=True):
                st.session_state.study_timer_active = True
                st.session_state.study_timer_start = time.time()
                st.session_state.study_timer_duration = duration_minutes * 60
                st.session_state.timer_paused = False
                
                if selected_course != "None":
                    course_code = selected_course.split(" - ")[0]
                    st.session_state.current_timer_course = course_code
                else:
                    st.session_state.current_timer_course = None
                
                st.rerun()
    
    with col2:
        st.subheader("📊 Statistics")
        
        # Total study time
        total_seconds = sum(s.get('duration', 0) for s in st.session_state.study_sessions)
        total_hours = total_seconds // 3600
        total_minutes = (total_seconds % 3600) // 60
        
        st.metric("Total Study Time", f"{total_hours}h {total_minutes}m")
        st.metric("Total Sessions", len(st.session_state.study_sessions))
        st.metric("Pomodoros Completed", st.session_state.pomodoro_count)
        
        # Study time by course
        if st.session_state.study_time_by_course:
            st.markdown("---")
            st.markdown("### Time by Course")
            for course_code, seconds in sorted(st.session_state.study_time_by_course.items(), key=lambda x: x[1], reverse=True):
                course_name = next((c['name'] for c in courses_data if c['code'] == course_code), course_code)
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                st.markdown(f"**{course_code}**\n- {hours}h {minutes}m")
        
        # Recent sessions
        if st.session_state.study_sessions:
            st.markdown("---")
            st.markdown("### Recent Sessions")
            recent = st.session_state.study_sessions[-5:]
            for session in reversed(recent):
                course_code = session.get('course', 'Unknown')
                duration_min = session.get('duration', 0) // 60
                date_str = session.get('date', '')[:10]
                st.caption(f"{date_str}: {duration_min} min - {course_code}")
        
        # Clear data button
        if st.button("🗑️ Clear All Data"):
            if st.checkbox("Are you sure? This cannot be undone."):
                st.session_state.study_sessions = []
                st.session_state.study_time_by_course = {}
                st.session_state.pomodoro_count = 0
                st.success("Data cleared!")
                st.rerun()

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
    
    # Organize playground tools by course/category
    playground_tools = {
        "Semester 1 - Tool Skills": {
            "FI1BBDF05 - Data Analysis Fundamentals": [
                "BI & Big Data Explorer"
            ],
            "FI1BBSF05 - Spreadsheet Fundamentals": [
                "Excel Formula Simulator",
                "Power Query Simulator"
            ],
            "FI1BBST05 - Statistical Tools": [
                "Statistical Analysis",
                "Z-Score & Outlier Tool"
            ],
            "FI1BBPF20 - Programming Fundamentals": [
                "Python Code Runner"
            ]
        },
        "Semester 2 - Data & Visualization": {
            "FI1BBDC20 - Databases and Cloud Services": [
                "SQL Query Tester"
            ],
            "FI1BBDV15 - Data Visualisation": [
                "Chart Builder",
                "Data Visualization Studio"
            ],
            "FI1BBDD75 - Data Driven Decision-Making": [
                "KPI Dashboard Builder",
                "Decision Analysis Tool"
            ],
            "FI1BBP175 - Semester Project 1": [
                "Project Planning Workshop"
            ],
            "FI1BBAR05 - Analysis Reporting": [
                "Report Writing Workshop"
            ],
            "FI1BBP275 - Exam Project 1": [
                "Exam Project Toolkit"
            ]
        },
        "Semester 3 - Competence Skills": {
            "FI1BBEO10 - Evaluation of Outcomes": [
                "Ethical Analysis Critique",
                "Error Detection Workshop",
                "Confidence Level Planner"
            ]
        }
    }
    
    st.markdown("### Choose a Practice Tool")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Category filter
        available_categories = list(playground_tools.keys())
        selected_category = st.selectbox(
            "📅 Semester/Category:",
            options=["All Categories"] + available_categories
        )
    
    with col2:
        # Course filter
        if selected_category == "All Categories":
            all_courses = []
            for cat in available_categories:
                for course in playground_tools[cat].keys():
                    if course not in all_courses:
                        all_courses.append(course)
            available_pg_courses = all_courses
        else:
            available_pg_courses = list(playground_tools[selected_category].keys())
        
        selected_pg_course = st.selectbox(
            "📚 Course:",
            options=["All Courses"] + available_pg_courses,
            key="pg_course"
        )
    
    # Get filtered tools
    filtered_tools = []
    for category, courses in playground_tools.items():
        if selected_category != "All Categories" and category != selected_category:
            continue
        for course, tools in courses.items():
            if selected_pg_course != "All Courses" and course != selected_pg_course:
                continue
            for tool in tools:
                filtered_tools.append((tool, course, category))
    
    if not filtered_tools:
        st.warning("No tools found for the selected filters.")
        st.stop()
    
    # Show tool count
    st.caption(f"🔧 {len(filtered_tools)} tools available")
    
    # Tool selector
    tool_options = [t[0] for t in filtered_tools]
    playground_tab = st.selectbox(
        "🎯 Select Tool:",
        options=tool_options
    )
    
    # Find course info for selected tool
    tool_course = None
    tool_category = None
    for tool, course, category in filtered_tools:
        if tool == playground_tab:
            tool_course = course
            tool_category = category
            break
    
    # Show context
    st.markdown(f"**{tool_category}** | **{tool_course}**")
    
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
        st.markdown("Practice Excel formulas including VLOOKUP and INDEX/MATCH!")
        
        # Main data table
        st.markdown("### Main Data Table")
        st.caption("Click cells to edit. Use + to add rows.")
        
        if 'excel_data' not in st.session_state:
            st.session_state.excel_data = pd.DataFrame({
                'EmployeeID': ['E001', 'E002', 'E003', 'E004', 'E005'],
                'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
                'Department': ['Sales', 'IT', 'Sales', 'HR', 'Marketing'],
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
        
        # Lookup reference table for VLOOKUP/INDEX-MATCH
        st.markdown("### Lookup Reference Table")
        st.caption("This table is used for VLOOKUP and INDEX/MATCH lookups.")
        
        if 'excel_lookup' not in st.session_state:
            st.session_state.excel_lookup = pd.DataFrame({
                'Department': ['Sales', 'IT', 'HR', 'Marketing', 'Finance'],
                'Manager': ['John Smith', 'Sarah Lee', 'Mike Brown', 'Lisa Chen', 'Tom Wilson'],
                'Budget': [50000, 75000, 40000, 60000, 80000],
                'Bonus_Rate': [0.10, 0.08, 0.05, 0.12, 0.07]
            })
        
        lookup_data = st.data_editor(
            st.session_state.excel_lookup,
            num_rows="dynamic",
            use_container_width=True,
            key="excel_lookup_editor"
        )
        st.session_state.excel_lookup = lookup_data
        
        st.markdown("### Apply Formulas")
        
        formula_categories = {
            "Basic Functions": ["SUM", "AVERAGE", "COUNT", "MAX", "MIN"],
            "Conditional Functions": ["SUMIF", "COUNTIF", "AVERAGEIF"],
            "Lookup Functions": ["VLOOKUP", "INDEX/MATCH", "XLOOKUP"],
            "Formatting & Tables": ["Conditional Formatting", "Pivot Table"],
            "Comparison": ["Excel vs Google Sheets"],
            "Other": ["IF Statement", "Custom Calculation"]
        }
        
        col1, col2 = st.columns(2)
        with col1:
            category = st.selectbox("Category:", list(formula_categories.keys()))
        with col2:
            formula_type = st.selectbox("Formula:", formula_categories[category])
        
        st.markdown("---")
        
        # Basic Functions
        if formula_type in ["SUM", "AVERAGE", "COUNT", "MAX", "MIN"]:
            numeric_cols = edited_data.select_dtypes(include=['number']).columns.tolist()
            if numeric_cols:
                column = st.selectbox("Select column:", numeric_cols)
                
                if st.button("Calculate", type="primary"):
                    try:
                        if formula_type == "SUM":
                            result = edited_data[column].sum()
                        elif formula_type == "AVERAGE":
                            result = edited_data[column].mean()
                        elif formula_type == "COUNT":
                            result = edited_data[column].count()
                        elif formula_type == "MAX":
                            result = edited_data[column].max()
                        elif formula_type == "MIN":
                            result = edited_data[column].min()
                        
                        st.success(f"={formula_type}({column}) = **{result:,.2f}**")
                        st.code(f"Excel: ={formula_type}(B2:B{len(edited_data)+1})")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("No numeric columns available.")
        
        # Conditional Functions
        elif formula_type in ["SUMIF", "COUNTIF", "AVERAGEIF"]:
            crit_col = st.selectbox("Criteria column:", edited_data.columns.tolist())
            criteria = st.text_input("Criteria value:", edited_data[crit_col].iloc[0] if len(edited_data) > 0 else "")
            
            if formula_type != "COUNTIF":
                numeric_cols = edited_data.select_dtypes(include=['number']).columns.tolist()
                if numeric_cols:
                    sum_col = st.selectbox("Value column:", numeric_cols)
            
            if st.button("Calculate", type="primary"):
                try:
                    mask = edited_data[crit_col].astype(str).str.lower() == str(criteria).lower()
                    
                    if formula_type == "SUMIF":
                        result = edited_data.loc[mask, sum_col].sum()
                        st.success(f"=SUMIF({crit_col}, \"{criteria}\", {sum_col}) = **{result:,.2f}**")
                        st.code(f"Excel: =SUMIF(A:A, \"{criteria}\", B:B)")
                    elif formula_type == "COUNTIF":
                        result = mask.sum()
                        st.success(f"=COUNTIF({crit_col}, \"{criteria}\") = **{result}**")
                        st.code(f"Excel: =COUNTIF(A:A, \"{criteria}\")")
                    elif formula_type == "AVERAGEIF":
                        result = edited_data.loc[mask, sum_col].mean()
                        st.success(f"=AVERAGEIF({crit_col}, \"{criteria}\", {sum_col}) = **{result:,.2f}**")
                        st.code(f"Excel: =AVERAGEIF(A:A, \"{criteria}\", B:B)")
                        
                    st.info(f"Found {mask.sum()} matching row(s)")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        
        # VLOOKUP
        elif formula_type == "VLOOKUP":
            st.markdown("**VLOOKUP** finds a value in the first column of the lookup table and returns a value from another column.")
            
            col1, col2 = st.columns(2)
            with col1:
                lookup_value = st.selectbox("Lookup value from main table:", edited_data.columns.tolist())
                row_to_lookup = st.selectbox("Which row to lookup:", list(range(len(edited_data))))
                actual_lookup = edited_data.iloc[row_to_lookup][lookup_value]
                st.info(f"Looking up: **{actual_lookup}**")
            
            with col2:
                return_col = st.selectbox("Return column from lookup table:", lookup_data.columns.tolist()[1:])
            
            if st.button("Run VLOOKUP", type="primary"):
                try:
                    lookup_key_col = lookup_data.columns[0]
                    match = lookup_data[lookup_data[lookup_key_col].astype(str).str.lower() == str(actual_lookup).lower()]
                    
                    if len(match) > 0:
                        result = match.iloc[0][return_col]
                        st.success(f"=VLOOKUP(\"{actual_lookup}\", LookupTable, {list(lookup_data.columns).index(return_col)+1}, FALSE)")
                        st.success(f"Result: **{result}**")
                        st.code(f"Excel: =VLOOKUP(A2, LookupTable!A:D, {list(lookup_data.columns).index(return_col)+1}, FALSE)")
                        
                        st.markdown("**How it works:**")
                        st.markdown(f"1. Search for '{actual_lookup}' in first column of lookup table")
                        st.markdown(f"2. Find matching row")
                        st.markdown(f"3. Return value from '{return_col}' column: **{result}**")
                    else:
                        st.warning(f"No match found for '{actual_lookup}' in lookup table.")
                        st.info("This would return #N/A in Excel")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        
        # INDEX/MATCH
        elif formula_type == "INDEX/MATCH":
            st.markdown("**INDEX/MATCH** is more flexible than VLOOKUP - it can look up values in any column!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**MATCH: Find the row**")
                match_value = st.selectbox("Value to find:", edited_data.columns.tolist())
                row_idx = st.selectbox("From row:", list(range(len(edited_data))))
                actual_match = edited_data.iloc[row_idx][match_value]
                st.info(f"Finding: **{actual_match}**")
                
                match_in_col = st.selectbox("Search in column:", lookup_data.columns.tolist())
            
            with col2:
                st.markdown("**INDEX: Return the value**")
                return_col = st.selectbox("Return from column:", lookup_data.columns.tolist())
            
            if st.button("Run INDEX/MATCH", type="primary"):
                try:
                    match_result = lookup_data[lookup_data[match_in_col].astype(str).str.lower() == str(actual_match).lower()]
                    
                    if len(match_result) > 0:
                        row_num = match_result.index[0]
                        result = lookup_data.loc[row_num, return_col]
                        
                        st.success(f"=INDEX({return_col}, MATCH(\"{actual_match}\", {match_in_col}, 0))")
                        st.success(f"Result: **{result}**")
                        st.code(f"Excel: =INDEX(LookupTable!{return_col}:{return_col}, MATCH(A2, LookupTable!{match_in_col}:{match_in_col}, 0))")
                        
                        st.markdown("**How it works:**")
                        st.markdown(f"1. MATCH finds '{actual_match}' in '{match_in_col}' column")
                        st.markdown(f"2. Returns row position: **{list(lookup_data.index).index(row_num) + 1}**")
                        st.markdown(f"3. INDEX uses that position to get value from '{return_col}': **{result}**")
                        
                        st.info("INDEX/MATCH advantage: Can lookup left (VLOOKUP can only look right)")
                    else:
                        st.warning(f"No match found for '{actual_match}'")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        
        # XLOOKUP (modern alternative)
        elif formula_type == "XLOOKUP":
            st.markdown("**XLOOKUP** is the modern replacement for VLOOKUP (Excel 365/2021+)")
            
            col1, col2 = st.columns(2)
            with col1:
                lookup_col = st.selectbox("Lookup value column:", edited_data.columns.tolist())
                row_idx = st.selectbox("From row:", list(range(len(edited_data))))
                lookup_val = edited_data.iloc[row_idx][lookup_col]
                st.info(f"Looking up: **{lookup_val}**")
            
            with col2:
                search_col = st.selectbox("Search in:", lookup_data.columns.tolist())
                return_col = st.selectbox("Return from:", lookup_data.columns.tolist())
            
            if st.button("Run XLOOKUP", type="primary"):
                try:
                    match = lookup_data[lookup_data[search_col].astype(str).str.lower() == str(lookup_val).lower()]
                    
                    if len(match) > 0:
                        result = match.iloc[0][return_col]
                        st.success(f"=XLOOKUP(\"{lookup_val}\", {search_col}, {return_col})")
                        st.success(f"Result: **{result}**")
                        st.code(f"Excel: =XLOOKUP(A2, LookupTable!{search_col}:{search_col}, LookupTable!{return_col}:{return_col})")
                        
                        st.markdown("**XLOOKUP advantages over VLOOKUP:**")
                        st.markdown("- Can search in any direction (left or right)")
                        st.markdown("- Simpler syntax (no column numbers)")
                        st.markdown("- Built-in error handling")
                    else:
                        st.warning(f"No match found for '{lookup_val}'")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        
        # IF Statement
        elif formula_type == "IF Statement":
            st.markdown("**IF** returns different values based on a condition.")
            
            numeric_cols = edited_data.select_dtypes(include=['number']).columns.tolist()
            if len(numeric_cols) >= 2:
                col1, col2 = st.columns(2)
                with col1:
                    check_col = st.selectbox("Check column:", numeric_cols)
                    operator = st.selectbox("Operator:", [">", "<", ">=", "<=", "="])
                with col2:
                    compare_to = st.selectbox("Compare to:", ["Value", "Another Column"])
                    if compare_to == "Value":
                        compare_val = st.number_input("Value:", value=0)
                    else:
                        compare_col = st.selectbox("Column:", [c for c in numeric_cols if c != check_col])
                
                if st.button("Apply IF Formula", type="primary"):
                    try:
                        if compare_to == "Value":
                            if operator == ">":
                                result = edited_data[check_col] > compare_val
                            elif operator == "<":
                                result = edited_data[check_col] < compare_val
                            elif operator == ">=":
                                result = edited_data[check_col] >= compare_val
                            elif operator == "<=":
                                result = edited_data[check_col] <= compare_val
                            else:
                                result = edited_data[check_col] == compare_val
                            formula_str = f"=IF({check_col}{operator}{compare_val}, \"Yes\", \"No\")"
                        else:
                            if operator == ">":
                                result = edited_data[check_col] > edited_data[compare_col]
                            elif operator == "<":
                                result = edited_data[check_col] < edited_data[compare_col]
                            elif operator == ">=":
                                result = edited_data[check_col] >= edited_data[compare_col]
                            elif operator == "<=":
                                result = edited_data[check_col] <= edited_data[compare_col]
                            else:
                                result = edited_data[check_col] == edited_data[compare_col]
                            formula_str = f"=IF({check_col}{operator}{compare_col}, \"Yes\", \"No\")"
                        
                        result_df = edited_data.copy()
                        result_df['IF_Result'] = result.map({True: 'Yes', False: 'No'})
                        
                        st.success(formula_str)
                        st.dataframe(result_df, use_container_width=True)
                        st.code(f"Excel: =IF(A2{operator}B2, \"Yes\", \"No\")")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
        # Conditional Formatting
        elif formula_type == "Conditional Formatting":
            st.markdown("**Conditional Formatting** applies visual styles based on cell values.")
            st.markdown("Common uses: highlight high/low values, show trends, identify outliers")
            
            numeric_cols = edited_data.select_dtypes(include=['number']).columns.tolist()
            
            if numeric_cols:
                format_col = st.selectbox("Column to format:", numeric_cols)
                
                format_type = st.selectbox(
                    "Formatting rule:",
                    ["Highlight cells > value", "Highlight cells < value", "Color Scale (low to high)", 
                     "Data Bars", "Top/Bottom N values", "Highlight duplicates"]
                )
                
                if format_type == "Highlight cells > value":
                    threshold = st.number_input("Highlight values greater than:", value=float(edited_data[format_col].mean()))
                    highlight_color = st.color_picker("Highlight color:", "#90EE90")
                    
                    if st.button("Apply Formatting", type="primary"):
                        result_df = edited_data.copy()
                        
                        def highlight_above(row):
                            return [f'background-color: {highlight_color}' if col == format_col and pd.notna(row[col]) and row[col] > threshold else '' for col in row.index]
                        
                        styled = result_df.style.apply(highlight_above, axis=1)
                        st.markdown("### Result (cells highlighted in green):")
                        st.dataframe(styled, use_container_width=True)
                        
                        matches = (result_df[format_col] > threshold).sum()
                        st.success(f"Highlighted {matches} cells where {format_col} > {threshold}")
                        st.code(f"Excel: Home > Conditional Formatting > Highlight Cells Rules > Greater Than > {threshold}")
                
                elif format_type == "Highlight cells < value":
                    threshold = st.number_input("Highlight values less than:", value=float(edited_data[format_col].mean()))
                    highlight_color = st.color_picker("Highlight color:", "#FFB6C1")
                    
                    if st.button("Apply Formatting", type="primary"):
                        result_df = edited_data.copy()
                        
                        def highlight_below(row):
                            return [f'background-color: {highlight_color}' if col == format_col and pd.notna(row[col]) and row[col] < threshold else '' for col in row.index]
                        
                        styled = result_df.style.apply(highlight_below, axis=1)
                        st.markdown("### Result (cells highlighted):")
                        st.dataframe(styled, use_container_width=True)
                        
                        matches = (result_df[format_col] < threshold).sum()
                        st.success(f"Highlighted {matches} cells where {format_col} < {threshold}")
                        st.code(f"Excel: Home > Conditional Formatting > Highlight Cells Rules > Less Than > {threshold}")
                
                elif format_type == "Color Scale (low to high)":
                    st.markdown("Color scales show values on a gradient from low (red) to high (green).")
                    
                    if st.button("Apply Color Scale", type="primary"):
                        result_df = edited_data.copy()
                        
                        styled = result_df.style.background_gradient(
                            subset=[format_col],
                            cmap='RdYlGn'
                        )
                        
                        st.markdown("### Result (color gradient applied):")
                        st.dataframe(styled, use_container_width=True)
                        
                        st.success(f"Applied color scale: Red (low) → Yellow (mid) → Green (high)")
                        st.code("Excel: Home > Conditional Formatting > Color Scales > Green-Yellow-Red")
                
                elif format_type == "Data Bars":
                    st.markdown("Data bars show relative values as bars within cells.")
                    
                    if st.button("Apply Data Bars", type="primary"):
                        result_df = edited_data.copy()
                        
                        styled = result_df.style.bar(
                            subset=[format_col],
                            color='#5fba7d',
                            vmin=0
                        )
                        
                        st.markdown("### Result (data bars in cells):")
                        st.dataframe(styled, use_container_width=True)
                        
                        st.success("Applied data bars showing relative values")
                        st.code("Excel: Home > Conditional Formatting > Data Bars > Solid Fill")
                
                elif format_type == "Top/Bottom N values":
                    n_values = st.slider("Number of values:", 1, min(10, len(edited_data)), 3)
                    top_or_bottom = st.radio("Highlight:", ["Top N", "Bottom N"], horizontal=True)
                    
                    if st.button("Apply Formatting", type="primary"):
                        result_df = edited_data.copy()
                        
                        if top_or_bottom == "Top N":
                            threshold = result_df[format_col].nlargest(n_values).min()
                            mask = result_df[format_col] >= threshold
                            color = '#90EE90'
                        else:
                            threshold = result_df[format_col].nsmallest(n_values).max()
                            mask = result_df[format_col] <= threshold
                            color = '#FFB6C1'
                        
                        def highlight_topbottom(row):
                            if mask[row.name]:
                                return [f'background-color: {color}' if col == format_col else '' for col in row.index]
                            return ['' for _ in row.index]
                        
                        styled = result_df.style.apply(highlight_topbottom, axis=1)
                        st.markdown(f"### Result ({top_or_bottom} {n_values} highlighted):")
                        st.dataframe(styled, use_container_width=True)
                        
                        st.success(f"Highlighted {mask.sum()} cells ({top_or_bottom} {n_values})")
                        st.code(f"Excel: Home > Conditional Formatting > Top/Bottom Rules > Top {n_values} Items")
                
                elif format_type == "Highlight duplicates":
                    dup_col = st.selectbox("Check for duplicates in:", edited_data.columns.tolist())
                    
                    if st.button("Find Duplicates", type="primary"):
                        result_df = edited_data.copy()
                        mask = result_df.duplicated(subset=[dup_col], keep=False)
                        
                        def highlight_dups(row):
                            if mask[row.name]:
                                return ['background-color: #FFFF99' if col == dup_col else '' for col in row.index]
                            return ['' for _ in row.index]
                        
                        styled = result_df.style.apply(highlight_dups, axis=1)
                        st.markdown("### Result (duplicates highlighted in yellow):")
                        st.dataframe(styled, use_container_width=True)
                        
                        dup_count = mask.sum()
                        if dup_count > 0:
                            st.warning(f"Found {dup_count} duplicate values in '{dup_col}'")
                        else:
                            st.success("No duplicates found!")
                        
                        st.code("Excel: Home > Conditional Formatting > Highlight Cells Rules > Duplicate Values")
            else:
                st.warning("Need numeric columns for conditional formatting.")
        
        # Pivot Table
        elif formula_type == "Pivot Table":
            st.markdown("**Pivot Tables** summarize and analyze data by grouping and aggregating.")
            st.markdown("Drag-and-drop style: choose rows, columns, and values to create summaries.")
            
            all_cols = edited_data.columns.tolist()
            numeric_cols = edited_data.select_dtypes(include=['number']).columns.tolist()
            categorical_cols = [c for c in all_cols if c not in numeric_cols]
            
            if categorical_cols and numeric_cols:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Rows (Group By):**")
                    row_field = st.selectbox("Row field:", categorical_cols + ["None"])
                    
                    st.markdown("**Columns (Optional):**")
                    col_field = st.selectbox("Column field:", ["None"] + [c for c in categorical_cols if c != row_field])
                
                with col2:
                    st.markdown("**Values:**")
                    value_field = st.selectbox("Value field:", numeric_cols)
                    
                    st.markdown("**Aggregation:**")
                    agg_func = st.selectbox("Function:", ["Sum", "Average", "Count", "Min", "Max"])
                
                if st.button("Create Pivot Table", type="primary"):
                    try:
                        agg_map = {"Sum": "sum", "Average": "mean", "Count": "count", "Min": "min", "Max": "max"}
                        
                        if row_field == "None":
                            st.warning("Please select at least a Row field.")
                        else:
                            if col_field != "None":
                                pivot = pd.pivot_table(
                                    edited_data,
                                    values=value_field,
                                    index=row_field,
                                    columns=col_field,
                                    aggfunc=agg_map[agg_func],
                                    fill_value=0
                                )
                            else:
                                pivot = edited_data.groupby(row_field)[value_field].agg(agg_map[agg_func]).reset_index()
                                pivot.columns = [row_field, f"{agg_func} of {value_field}"]
                            
                            st.markdown("### Pivot Table Result:")
                            st.dataframe(pivot, use_container_width=True)
                            
                            # Add grand totals
                            if col_field != "None":
                                st.markdown(f"**Grand Total ({agg_func}):** {pivot.values.sum():,.2f}")
                            
                            st.code("Excel: Insert > PivotTable > Select data range")
                            st.markdown("**Steps in Excel:**")
                            st.markdown(f"1. Drag '{row_field}' to Rows area")
                            if col_field != "None":
                                st.markdown(f"2. Drag '{col_field}' to Columns area")
                            st.markdown(f"3. Drag '{value_field}' to Values area")
                            st.markdown(f"4. Change aggregation to '{agg_func}'")
                    except Exception as e:
                        st.error(f"Error creating pivot table: {str(e)}")
            else:
                st.warning("Need at least one categorical column and one numeric column for pivot tables.")
                st.info("Try adding a text column (like 'Department' or 'Region') to your data.")
        
        # Excel vs Google Sheets Comparison
        elif formula_type == "Excel vs Google Sheets":
            st.markdown("## Excel vs Google Sheets Comparison")
            st.markdown("Both are powerful spreadsheet tools. Here's when to use each:")
            
            st.markdown("### Feature Comparison")
            
            comparison_data = pd.DataFrame({
                'Feature': [
                    'Best For', 'Collaboration', 'Offline Access', 'Data Size', 
                    'Advanced Features', 'Cost', 'Learning Curve', 'Integration',
                    'Macros/Automation', 'Mobile App'
                ],
                'Microsoft Excel': [
                    'Complex analysis, large datasets', 'SharePoint/OneDrive (paid)', 
                    'Full offline support', 'Millions of rows', 'Power Query, Power Pivot, VBA',
                    'Paid (Office 365)', 'Steeper', 'Microsoft ecosystem',
                    'VBA macros (powerful)', 'Good'
                ],
                'Google Sheets': [
                    'Collaboration, simple tasks', 'Real-time built-in (free)',
                    'Limited (Chrome extension)', '10 million cells max',
                    'Apps Script, Explore feature', 'Free', 'Easier', 'Google Workspace',
                    'Apps Script (web-based)', 'Excellent'
                ]
            })
            
            st.dataframe(comparison_data, use_container_width=True, hide_index=True)
            
            st.markdown("### Formula Differences")
            
            formula_diff = pd.DataFrame({
                'Function': ['VLOOKUP', 'Array Formulas', 'Unique Values', 'Filter Data', 'Import Data'],
                'Excel': ['=VLOOKUP()', 'Ctrl+Shift+Enter (legacy)', '=UNIQUE()', '=FILTER()', '=WEBSERVICE()'],
                'Google Sheets': ['=VLOOKUP()', 'Native (no special entry)', '=UNIQUE()', '=FILTER()', '=IMPORTDATA()']
            })
            
            st.dataframe(formula_diff, use_container_width=True, hide_index=True)
            
            st.markdown("### When to Use Each")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Use Excel When:")
                st.markdown("- Working with very large datasets (100k+ rows)")
                st.markdown("- Need Power Query for data transformation")
                st.markdown("- Require VBA macros for complex automation")
                st.markdown("- Working offline frequently")
                st.markdown("- Need Power Pivot for data modeling")
                st.markdown("- Using advanced statistical tools")
            
            with col2:
                st.markdown("#### Use Google Sheets When:")
                st.markdown("- Real-time collaboration is essential")
                st.markdown("- Team needs free access")
                st.markdown("- Data needs to be always accessible online")
                st.markdown("- Integrating with other Google tools")
                st.markdown("- Simple to medium complexity tasks")
                st.markdown("- Quick sharing without file attachments")
            
            st.markdown("### Key Shortcuts Comparison")
            
            shortcuts = pd.DataFrame({
                'Action': ['Copy', 'Paste', 'Fill Down', 'Select All', 'Find', 'Insert Row', 'Format Cells'],
                'Excel (Windows)': ['Ctrl+C', 'Ctrl+V', 'Ctrl+D', 'Ctrl+A', 'Ctrl+F', 'Ctrl+Shift++', 'Ctrl+1'],
                'Google Sheets': ['Ctrl+C', 'Ctrl+V', 'Ctrl+D', 'Ctrl+A', 'Ctrl+F', 'Ctrl+Shift++', 'Ctrl+\\']
            })
            
            st.dataframe(shortcuts, use_container_width=True, hide_index=True)
            
            st.info("**Tip:** Most basic formulas work the same in both! Learn one, and you'll know 80% of the other.")
        
        # Custom Calculation
        elif formula_type == "Custom Calculation":
            st.markdown("### Add Calculated Column")
            new_col_name = st.text_input("New column name:", "Performance")
            
            numeric_cols = edited_data.select_dtypes(include=['number']).columns.tolist()
            if len(numeric_cols) >= 2:
                col_a = st.selectbox("First column:", numeric_cols)
                operation = st.selectbox("Operation:", ["+", "-", "*", "/"])
                col_b = st.selectbox("Second column:", [c for c in numeric_cols if c != col_a])
                
                if st.button("Add Column"):
                    try:
                        if operation == "+":
                            edited_data[new_col_name] = edited_data[col_a] + edited_data[col_b]
                        elif operation == "-":
                            edited_data[new_col_name] = edited_data[col_a] - edited_data[col_b]
                        elif operation == "*":
                            edited_data[new_col_name] = edited_data[col_a] * edited_data[col_b]
                        elif operation == "/":
                            edited_data[new_col_name] = (edited_data[col_a] / edited_data[col_b]).round(2)
                        
                        st.session_state.excel_data = edited_data
                        st.success(f"Added column: {new_col_name} = {col_a} {operation} {col_b}")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
    
    elif playground_tab == "SQL Query Tester":
        st.subheader("🗄️ SQL Query Tester")
        st.markdown("Write SQL queries against your data - edit the tables below to add your own!")
        
        # Initialize editable tables in session state
        if 'sql_customers' not in st.session_state:
            st.session_state.sql_customers = pd.DataFrame({
                'id': [1, 2, 3, 4, 5],
                'name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown', 'Diana Ross', 'Eve Wilson'],
                'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
                'joined_date': ['2023-01-15', '2023-03-22', '2023-02-10', '2023-04-05', '2023-01-30']
            })
        
        if 'sql_orders' not in st.session_state:
            st.session_state.sql_orders = pd.DataFrame({
                'order_id': [101, 102, 103, 104, 105, 106, 107, 108],
                'customer_id': [1, 2, 1, 3, 4, 2, 5, 1],
                'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Watch', 'Headphones', 'Phone'],
                'amount': [999, 699, 449, 999, 699, 299, 149, 699],
                'order_date': ['2024-01-10', '2024-01-12', '2024-01-15', '2024-02-01', '2024-02-05', '2024-02-10', '2024-02-15', '2024-03-01']
            })
        
        st.markdown("### Your Tables (Edit to add your own data!)")
        
        tab1, tab2 = st.tabs(["customers", "orders"])
        with tab1:
            st.caption("Click cells to edit. Use + to add rows.")
            st.session_state.sql_customers = st.data_editor(
                st.session_state.sql_customers,
                num_rows="dynamic",
                use_container_width=True,
                key="sql_customers_editor"
            )
        with tab2:
            st.caption("Click cells to edit. Use + to add rows.")
            st.session_state.sql_orders = st.data_editor(
                st.session_state.sql_orders,
                num_rows="dynamic",
                use_container_width=True,
                key="sql_orders_editor"
            )
        
        customers = st.session_state.sql_customers
        orders = st.session_state.sql_orders
        
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
        st.markdown("Create visualizations from your own data! Edit the table below.")
        
        # Initialize editable chart data in session state
        if 'chart_data' not in st.session_state:
            st.session_state.chart_data = pd.DataFrame({
                'Category': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                'Value1': [45000, 52000, 48000, 61000, 55000, 67000],
                'Value2': [32000, 35000, 33000, 38000, 36000, 40000]
            })
        
        st.markdown("### Your Data (Edit to add your own!)")
        st.caption("Click cells to edit values. Use + to add rows.")
        st.session_state.chart_data = st.data_editor(
            st.session_state.chart_data,
            num_rows="dynamic",
            use_container_width=True,
            key="chart_data_editor"
        )
        
        chart_data = st.session_state.chart_data
        
        st.markdown("### Choose Chart Type")
        
        col1, col2 = st.columns(2)
        
        # Get numeric columns for Y-axis options
        numeric_cols = chart_data.select_dtypes(include=['number']).columns.tolist()
        all_cols = chart_data.columns.tolist()
        
        with col1:
            chart_type = st.selectbox(
                "Chart type:",
                ["Bar Chart", "Line Chart", "Area Chart", "Scatter Plot"]
            )
        
        with col2:
            x_column = st.selectbox("X-axis (categories):", all_cols, index=0)
            y_column = st.selectbox("Y-axis (values):", numeric_cols if numeric_cols else all_cols)
        
        st.markdown("### Your Chart")
        
        try:
            if chart_type == "Bar Chart":
                st.bar_chart(chart_data.set_index(x_column)[y_column])
            elif chart_type == "Line Chart":
                st.line_chart(chart_data.set_index(x_column)[y_column])
            elif chart_type == "Area Chart":
                st.area_chart(chart_data.set_index(x_column)[y_column])
            elif chart_type == "Scatter Plot":
                if len(numeric_cols) >= 2:
                    import altair as alt
                    x_scatter = st.selectbox("Scatter X:", numeric_cols, key="scatter_x")
                    y_scatter = st.selectbox("Scatter Y:", [c for c in numeric_cols if c != x_scatter], key="scatter_y")
                    scatter = alt.Chart(chart_data).mark_circle(size=100).encode(
                        x=x_scatter,
                        y=y_scatter,
                        tooltip=all_cols
                    ).properties(width=600, height=400)
                    st.altair_chart(scatter, use_container_width=True)
                else:
                    st.info("Scatter plots need at least 2 numeric columns. Add more data!")
        except Exception as e:
            st.warning(f"Could not create chart: {str(e)}")
        
        st.markdown("---")
        st.markdown("**Chart Best Practices:**")
        st.markdown("- **Bar charts**: Best for comparing categories")
        st.markdown("- **Line charts**: Best for showing trends over time")
        st.markdown("- **Area charts**: Good for showing volume/cumulative data")
        st.markdown("- **Scatter plots**: Best for showing relationships between two variables")
    
    elif playground_tab == "Data Visualization Studio":
        st.subheader("🎨 Data Visualization Studio")
        st.markdown("*Practice choosing charts, designing for accessibility, and identifying visualization problems*")
        st.markdown("---")
        
        viz_mode = st.radio(
            "Choose practice mode:",
            ["Chart Selection Advisor", "Accessibility Checker", "Visualization Critique", "Story Builder"],
            horizontal=True
        )
        
        if viz_mode == "Chart Selection Advisor":
            st.markdown("### Chart Selection Advisor")
            st.markdown("*Answer questions about your data to get chart recommendations*")
            
            col1, col2 = st.columns(2)
            with col1:
                data_goal = st.selectbox(
                    "What do you want to show?",
                    ["Compare categories", "Show trend over time", "Show parts of a whole", 
                     "Show relationship between variables", "Show distribution", "Show geographic patterns"]
                )
                num_categories = st.slider("How many categories/data points?", 2, 50, 6)
            
            with col2:
                audience = st.selectbox(
                    "Who is your audience?",
                    ["Executives (quick glance)", "Technical team (detailed analysis)", 
                     "General public", "Mixed audience"]
                )
                interactive = st.checkbox("Does it need to be interactive?")
            
            if st.button("🎯 Get Recommendations", type="primary"):
                st.markdown("---")
                st.markdown("### Recommended Charts")
                
                recommendations = []
                warnings = []
                
                if data_goal == "Compare categories":
                    if num_categories <= 7:
                        recommendations.append(("Bar Chart (horizontal)", "Best for comparing values across categories", "⭐ Top Pick"))
                        recommendations.append(("Column Chart (vertical)", "Good when categories have short labels", ""))
                    else:
                        recommendations.append(("Horizontal Bar Chart", "Essential when you have many categories", "⭐ Top Pick"))
                        warnings.append("With 7+ categories, avoid pie charts - they become unreadable")
                
                elif data_goal == "Show trend over time":
                    recommendations.append(("Line Chart", "Perfect for continuous time series", "⭐ Top Pick"))
                    recommendations.append(("Area Chart", "Good for showing volume/magnitude over time", ""))
                    if num_categories <= 4:
                        recommendations.append(("Multiple Line Chart", "Compare trends across 2-4 series", ""))
                
                elif data_goal == "Show parts of a whole":
                    if num_categories <= 5:
                        recommendations.append(("Pie Chart", "Works well with few categories", "⭐ Top Pick"))
                        recommendations.append(("Donut Chart", "Modern alternative to pie", ""))
                    else:
                        recommendations.append(("Stacked Bar Chart", "Better than pie for many categories", "⭐ Top Pick"))
                        recommendations.append(("Treemap", "Good for hierarchical data", ""))
                        warnings.append("Avoid pie charts with more than 5 slices")
                
                elif data_goal == "Show relationship between variables":
                    recommendations.append(("Scatter Plot", "Shows correlation between variables", "⭐ Top Pick"))
                    recommendations.append(("Bubble Chart", "Adds a third dimension (size)", ""))
                
                elif data_goal == "Show distribution":
                    recommendations.append(("Histogram", "Shows frequency distribution", "⭐ Top Pick"))
                    recommendations.append(("Box Plot", "Shows median, quartiles, outliers", ""))
                
                elif data_goal == "Show geographic patterns":
                    recommendations.append(("Choropleth Map", "Color-coded regions", "⭐ Top Pick"))
                    recommendations.append(("Bubble Map", "Points with size encoding", ""))
                
                if audience == "Executives (quick glance)":
                    recommendations.append(("Single Number + Sparkline", "Maximum simplicity for busy executives", "💼"))
                    warnings.append("Keep it simple - one key insight per visual")
                
                for chart, desc, badge in recommendations:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**{chart}**")
                        st.caption(desc)
                    with col2:
                        if badge:
                            st.markdown(badge)
                
                if warnings:
                    st.markdown("### ⚠️ Watch Out For:")
                    for w in warnings:
                        st.warning(w)
        
        elif viz_mode == "Accessibility Checker":
            st.markdown("### Accessibility Checker")
            st.markdown("*Evaluate your visualization design for accessibility*")
            
            st.markdown("**Rate your visualization on these criteria:**")
            
            checks = {
                "Color contrast": st.select_slider(
                    "Text and data have sufficient contrast against background",
                    options=["No", "Partially", "Yes"],
                    value="Partially"
                ),
                "Color independence": st.select_slider(
                    "Information is conveyed by more than just color (shapes, patterns, labels)",
                    options=["No", "Partially", "Yes"],
                    value="Partially"
                ),
                "Clear labels": st.select_slider(
                    "All axes, legends, and data points are clearly labeled",
                    options=["No", "Partially", "Yes"],
                    value="Partially"
                ),
                "Font readability": st.select_slider(
                    "Font size is large enough and font is sans-serif",
                    options=["No", "Partially", "Yes"],
                    value="Partially"
                ),
                "Title and context": st.select_slider(
                    "Chart has a descriptive title and necessary context",
                    options=["No", "Partially", "Yes"],
                    value="Partially"
                ),
                "Data source": st.select_slider(
                    "Data source is cited",
                    options=["No", "Partially", "Yes"],
                    value="Partially"
                )
            }
            
            if st.button("📋 Generate Accessibility Report", type="primary"):
                st.markdown("---")
                st.markdown("### Accessibility Report")
                
                score = 0
                max_score = len(checks) * 2
                
                for check, value in checks.items():
                    if value == "Yes":
                        st.success(f"✅ **{check}**: Good")
                        score += 2
                    elif value == "Partially":
                        st.warning(f"⚠️ **{check}**: Needs improvement")
                        score += 1
                    else:
                        st.error(f"❌ **{check}**: Missing")
                
                st.markdown("---")
                pct = (score / max_score) * 100
                st.metric("Accessibility Score", f"{pct:.0f}%")
                
                if pct >= 80:
                    st.success("Your visualization meets basic accessibility standards!")
                elif pct >= 50:
                    st.warning("Your visualization needs some improvements for full accessibility.")
                else:
                    st.error("Significant accessibility improvements needed.")
                
                st.markdown("**Tips for improvement:**")
                if checks["Color independence"] != "Yes":
                    st.markdown("- Add patterns, shapes, or direct labels so color isn't the only differentiator")
                if checks["Color contrast"] != "Yes":
                    st.markdown("- Use a contrast checker tool (aim for 4.5:1 ratio)")
                if checks["Clear labels"] != "Yes":
                    st.markdown("- Add axis labels, legend, and data labels where helpful")
        
        elif viz_mode == "Visualization Critique":
            st.markdown("### Visualization Critique")
            st.markdown("*Identify problems in common visualization mistakes*")
            
            critique_scenarios = {
                "Truncated Y-Axis": {
                    "description": "A bar chart shows company revenue: Year 1 = $98M, Year 2 = $100M, Year 3 = $102M. The y-axis starts at $95M.",
                    "problems": ["Y-axis starting at $95M makes 2% differences look like 50%+ differences", "Viewer perceives dramatic growth that doesn't exist"],
                    "fixes": ["Start y-axis at $0 for bar charts", "If small differences matter, use a line chart or table with % change"]
                },
                "Pie Chart Overload": {
                    "description": "A pie chart shows market share with 15 different slices, many smaller than 3%.",
                    "problems": ["Too many slices to compare", "Small slices are indistinguishable", "Colors become repetitive"],
                    "fixes": ["Group small categories into 'Other'", "Use horizontal bar chart instead", "Limit pie charts to 5-7 slices"]
                },
                "3D Chart Distortion": {
                    "description": "A 3D pie chart is used to show budget allocation. The slice at the front appears larger than equal slices at the back.",
                    "problems": ["3D perspective distorts slice sizes", "Front slices appear larger due to perspective", "Harder to compare values accurately"],
                    "fixes": ["Use 2D charts - they're more accurate", "If you must use 3D, provide data labels", "Consider a bar chart instead"]
                },
                "Cherry-Picked Timeframe": {
                    "description": "A chart shows 'Record Growth!' by comparing March (lowest month) to December (highest month), ignoring the full year context.",
                    "problems": ["Misleading comparison (worst to best)", "Hides overall trend", "Reader can't see seasonal patterns"],
                    "fixes": ["Show complete time period", "Compare same periods (year-over-year)", "Include context about seasonality"]
                }
            }
            
            selected_scenario = st.selectbox("Choose a scenario to analyze:", list(critique_scenarios.keys()))
            scenario = critique_scenarios[selected_scenario]
            
            st.markdown(f"**Scenario:** {scenario['description']}")
            
            user_problems = st.text_area(
                "What problems do you see? (List them)",
                placeholder="Enter the issues you identify...",
                height=100
            )
            
            if st.button("🔍 Show Expert Analysis", type="primary"):
                st.markdown("---")
                st.markdown("### Problems Identified:")
                for p in scenario["problems"]:
                    st.error(f"❌ {p}")
                
                st.markdown("### Recommended Fixes:")
                for f in scenario["fixes"]:
                    st.success(f"✅ {f}")
        
        elif viz_mode == "Story Builder":
            st.markdown("### Data Story Builder")
            st.markdown("*Practice structuring a data presentation*")
            
            st.markdown("**Fill in your data story framework:**")
            
            context = st.text_area(
                "1. CONTEXT: Why should the audience care?",
                placeholder="e.g., 'Customer churn has increased 15% this quarter, threatening our revenue targets...'",
                height=80
            )
            
            insight = st.text_area(
                "2. INSIGHT: What does the data reveal?",
                placeholder="e.g., 'Analysis of 5,000 churned customers shows 70% cited 'slow support response' as their top complaint...'",
                height=80
            )
            
            visualization = st.text_input(
                "3. VISUALIZATION: What chart will you show?",
                placeholder="e.g., 'Bar chart comparing churn reasons, with response time highlighted'"
            )
            
            action = st.text_area(
                "4. ACTION: What should happen next?",
                placeholder="e.g., 'Recommend investing $50K in chat support to reduce response time from 4 hours to 30 minutes...'",
                height=80
            )
            
            if st.button("📊 Generate Story Summary", type="primary"):
                if context and insight and action:
                    st.markdown("---")
                    st.markdown("### Your Data Story")
                    
                    story = f"""## Data Story: Executive Summary

### Context
{context}

### Key Insight
{insight}

### Visualization
*{visualization if visualization else '[Add your chart description]'}*

### Recommended Action
{action}

---
*Story Structure: Setup → Insight → Action*
"""
                    st.markdown(story)
                    
                    st.download_button(
                        "📥 Download Story Framework",
                        data=story,
                        file_name="data_story.md",
                        mime="text/markdown"
                    )
                else:
                    st.warning("Please fill in all sections to generate your story.")
    
    elif playground_tab == "Statistical Analysis":
        st.subheader("📊 Statistical Analysis Tool")
        st.markdown("Perform correlation, regression, ANOVA, histogram, and covariance analysis on your data!")
        
        from scipy import stats
        import numpy as np
        
        # Initialize sample data for statistical analysis
        if 'stats_data' not in st.session_state:
            np.random.seed(42)
            st.session_state.stats_data = pd.DataFrame({
                'Advertising': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
                'Sales': [100, 120, 150, 170, 200, 220, 250, 280, 300, 320],
                'Region': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
                'Quarter': ['Q1', 'Q1', 'Q2', 'Q2', 'Q3', 'Q3', 'Q4', 'Q4', 'Q1', 'Q2'],
                'Employees': [5, 8, 10, 12, 15, 18, 20, 22, 25, 28]
            })
        
        st.markdown("### Your Data (Edit to add your own!)")
        st.caption("Click cells to edit. Use + to add rows.")
        st.session_state.stats_data = st.data_editor(
            st.session_state.stats_data,
            num_rows="dynamic",
            use_container_width=True,
            key="stats_data_editor"
        )
        
        stats_data = st.session_state.stats_data
        numeric_cols = stats_data.select_dtypes(include=['number']).columns.tolist()
        categorical_cols = stats_data.select_dtypes(include=['object']).columns.tolist()
        
        st.markdown("### Choose Analysis Type")
        
        analysis_type = st.selectbox(
            "Analysis:",
            ["Correlation Analysis", "Linear Regression", "ANOVA (Analysis of Variance)", 
             "Histogram", "Covariance Analysis", "Descriptive Statistics"]
        )
        
        st.markdown("---")
        
        if analysis_type == "Correlation Analysis":
            st.markdown("**Correlation** measures the strength and direction of relationship between two variables.")
            st.markdown("- Values range from -1 to +1")
            st.markdown("- +1 = perfect positive correlation, -1 = perfect negative correlation, 0 = no correlation")
            
            if len(numeric_cols) >= 2:
                col1, col2 = st.columns(2)
                with col1:
                    var1 = st.selectbox("Variable 1:", numeric_cols)
                with col2:
                    var2 = st.selectbox("Variable 2:", [c for c in numeric_cols if c != var1])
                
                if st.button("Calculate Correlation", type="primary"):
                    try:
                        correlation, p_value = stats.pearsonr(stats_data[var1], stats_data[var2])
                        
                        st.markdown("### Results")
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Correlation (r)", f"{correlation:.4f}")
                        with col2:
                            st.metric("R-squared", f"{correlation**2:.4f}")
                        with col3:
                            st.metric("P-value", f"{p_value:.4f}")
                        
                        # Interpretation
                        if abs(correlation) >= 0.7:
                            strength = "strong"
                        elif abs(correlation) >= 0.4:
                            strength = "moderate"
                        else:
                            strength = "weak"
                        
                        direction = "positive" if correlation > 0 else "negative"
                        
                        st.success(f"There is a **{strength} {direction}** correlation between {var1} and {var2}.")
                        
                        if p_value < 0.05:
                            st.info("The correlation is statistically significant (p < 0.05).")
                        else:
                            st.warning("The correlation is NOT statistically significant (p >= 0.05).")
                        
                        # Show scatter plot
                        st.markdown("### Scatter Plot")
                        import altair as alt
                        scatter = alt.Chart(stats_data).mark_circle(size=60).encode(
                            x=var1,
                            y=var2,
                            tooltip=[var1, var2]
                        ).properties(width=600, height=300)
                        
                        # Add trend line
                        line = scatter.transform_regression(var1, var2).mark_line(color='red')
                        st.altair_chart(scatter + line, use_container_width=True)
                        
                        st.code(f"Excel: =CORREL({var1}:{var1}, {var2}:{var2})")
                        st.code(f"Python: scipy.stats.pearsonr(df['{var1}'], df['{var2}'])")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Need at least 2 numeric columns for correlation analysis.")
        
        elif analysis_type == "Linear Regression":
            st.markdown("**Linear Regression** finds the best-fit line to predict one variable from another.")
            st.markdown("Formula: y = mx + b (where m = slope, b = intercept)")
            
            if len(numeric_cols) >= 2:
                col1, col2 = st.columns(2)
                with col1:
                    x_var = st.selectbox("Independent Variable (X):", numeric_cols)
                with col2:
                    y_var = st.selectbox("Dependent Variable (Y):", [c for c in numeric_cols if c != x_var])
                
                if st.button("Run Regression", type="primary"):
                    try:
                        slope, intercept, r_value, p_value, std_err = stats.linregress(
                            stats_data[x_var], stats_data[y_var]
                        )
                        
                        st.markdown("### Regression Results")
                        
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.metric("Slope (m)", f"{slope:.4f}")
                        with col2:
                            st.metric("Intercept (b)", f"{intercept:.4f}")
                        with col3:
                            st.metric("R-squared", f"{r_value**2:.4f}")
                        with col4:
                            st.metric("P-value", f"{p_value:.4f}")
                        
                        st.success(f"**Equation:** {y_var} = {slope:.2f} * {x_var} + {intercept:.2f}")
                        
                        st.markdown("**Interpretation:**")
                        st.markdown(f"- For every 1 unit increase in {x_var}, {y_var} increases by {slope:.2f}")
                        st.markdown(f"- The model explains {r_value**2*100:.1f}% of the variance in {y_var}")
                        
                        # Prediction tool
                        st.markdown("### Make a Prediction")
                        pred_x = st.number_input(f"Enter {x_var} value:", value=float(stats_data[x_var].mean()))
                        pred_y = slope * pred_x + intercept
                        st.info(f"Predicted {y_var}: **{pred_y:.2f}**")
                        
                        # Show regression plot
                        import altair as alt
                        scatter = alt.Chart(stats_data).mark_circle(size=60).encode(
                            x=x_var,
                            y=y_var,
                            tooltip=[x_var, y_var]
                        ).properties(width=600, height=300)
                        line = scatter.transform_regression(x_var, y_var).mark_line(color='red')
                        st.altair_chart(scatter + line, use_container_width=True)
                        
                        st.code(f"Excel: =SLOPE({y_var}:{y_var}, {x_var}:{x_var}), =INTERCEPT({y_var}:{y_var}, {x_var}:{x_var})")
                        st.code(f"Python: scipy.stats.linregress(df['{x_var}'], df['{y_var}'])")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Need at least 2 numeric columns for regression analysis.")
        
        elif analysis_type == "ANOVA (Analysis of Variance)":
            st.markdown("**ANOVA** tests if there are significant differences between group means.")
            st.markdown("- Used when comparing means across 2+ groups")
            st.markdown("- Null hypothesis: All group means are equal")
            
            if categorical_cols and numeric_cols:
                col1, col2 = st.columns(2)
                with col1:
                    group_col = st.selectbox("Grouping Variable (categorical):", categorical_cols)
                with col2:
                    value_col = st.selectbox("Value Variable (numeric):", numeric_cols)
                
                if st.button("Run ANOVA", type="primary"):
                    try:
                        groups = [group[value_col].values for name, group in stats_data.groupby(group_col)]
                        
                        if len(groups) >= 2:
                            f_stat, p_value = stats.f_oneway(*groups)
                            
                            st.markdown("### ANOVA Results")
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                st.metric("F-statistic", f"{f_stat:.4f}")
                            with col2:
                                st.metric("P-value", f"{p_value:.4f}")
                            
                            if p_value < 0.05:
                                st.success("**Result:** The differences between groups ARE statistically significant (p < 0.05).")
                                st.markdown("At least one group mean is different from the others.")
                            else:
                                st.info("**Result:** The differences between groups are NOT statistically significant (p >= 0.05).")
                                st.markdown("The group means are not significantly different.")
                            
                            # Show group statistics
                            st.markdown("### Group Statistics")
                            group_stats = stats_data.groupby(group_col)[value_col].agg(['count', 'mean', 'std'])
                            group_stats.columns = ['Count', 'Mean', 'Std Dev']
                            st.dataframe(group_stats, use_container_width=True)
                            
                            # Box plot
                            import altair as alt
                            box = alt.Chart(stats_data).mark_boxplot().encode(
                                x=group_col,
                                y=value_col
                            ).properties(width=600, height=300)
                            st.altair_chart(box, use_container_width=True)
                            
                            st.code("Excel: Data Analysis ToolPak > Anova: Single Factor")
                            st.code(f"Python: scipy.stats.f_oneway(*groups)")
                        else:
                            st.warning("Need at least 2 groups for ANOVA.")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Need at least 1 categorical column and 1 numeric column for ANOVA.")
        
        elif analysis_type == "Histogram":
            st.markdown("**Histogram** shows the distribution of values in a dataset.")
            st.markdown("- Helps identify patterns like normal distribution, skewness, outliers")
            
            if numeric_cols:
                hist_col = st.selectbox("Select column:", numeric_cols)
                bins = st.slider("Number of bins:", 5, 30, 10)
                
                if st.button("Create Histogram", type="primary"):
                    try:
                        import altair as alt
                        
                        hist = alt.Chart(stats_data).mark_bar().encode(
                            alt.X(hist_col, bin=alt.Bin(maxbins=bins)),
                            y='count()'
                        ).properties(width=600, height=300)
                        st.altair_chart(hist, use_container_width=True)
                        
                        # Distribution statistics
                        st.markdown("### Distribution Statistics")
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.metric("Mean", f"{stats_data[hist_col].mean():.2f}")
                        with col2:
                            st.metric("Median", f"{stats_data[hist_col].median():.2f}")
                        with col3:
                            st.metric("Std Dev", f"{stats_data[hist_col].std():.2f}")
                        with col4:
                            skewness = stats.skew(stats_data[hist_col])
                            st.metric("Skewness", f"{skewness:.2f}")
                        
                        # Interpretation
                        if abs(skewness) < 0.5:
                            st.success("The distribution is approximately **symmetric** (normal-like).")
                        elif skewness > 0:
                            st.info("The distribution is **right-skewed** (tail extends to the right).")
                        else:
                            st.info("The distribution is **left-skewed** (tail extends to the left).")
                        
                        st.code("Excel: Insert > Charts > Histogram")
                        st.code(f"Python: plt.hist(df['{hist_col}'], bins={bins})")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Need at least 1 numeric column for histogram.")
        
        elif analysis_type == "Covariance Analysis":
            st.markdown("**Covariance** measures how two variables change together.")
            st.markdown("- Positive: variables increase together")
            st.markdown("- Negative: one increases as other decreases")
            st.markdown("- Unlike correlation, covariance is not standardized (affected by scale)")
            
            if len(numeric_cols) >= 2:
                if st.button("Calculate Covariance Matrix", type="primary"):
                    try:
                        cov_matrix = stats_data[numeric_cols].cov()
                        
                        st.markdown("### Covariance Matrix")
                        st.dataframe(cov_matrix.round(2), use_container_width=True)
                        
                        st.markdown("### Interpretation")
                        st.markdown("- **Diagonal values**: Variance of each variable")
                        st.markdown("- **Off-diagonal values**: Covariance between variable pairs")
                        st.markdown("- Larger absolute values = stronger relationship")
                        
                        # Also show correlation for comparison
                        st.markdown("### Correlation Matrix (for comparison)")
                        corr_matrix = stats_data[numeric_cols].corr()
                        st.dataframe(corr_matrix.round(2), use_container_width=True)
                        
                        st.info("Correlation is preferred when comparing relationships because it's standardized (-1 to +1).")
                        
                        st.code("Excel: Data Analysis ToolPak > Covariance")
                        st.code("Python: df.cov()")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Need at least 2 numeric columns for covariance analysis.")
        
        elif analysis_type == "Descriptive Statistics":
            st.markdown("**Descriptive Statistics** summarize the main features of a dataset.")
            
            if numeric_cols:
                selected_col = st.selectbox("Select column:", numeric_cols)
                
                if st.button("Calculate Statistics", type="primary"):
                    try:
                        data = stats_data[selected_col]
                        
                        st.markdown("### Summary Statistics")
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Count", f"{len(data)}")
                            st.metric("Mean", f"{data.mean():.2f}")
                            st.metric("Median", f"{data.median():.2f}")
                        with col2:
                            st.metric("Std Dev", f"{data.std():.2f}")
                            st.metric("Variance", f"{data.var():.2f}")
                            st.metric("Range", f"{data.max() - data.min():.2f}")
                        with col3:
                            st.metric("Min", f"{data.min():.2f}")
                            st.metric("Max", f"{data.max():.2f}")
                            st.metric("Sum", f"{data.sum():.2f}")
                        
                        st.markdown("### Quartiles")
                        q1 = data.quantile(0.25)
                        q2 = data.quantile(0.50)
                        q3 = data.quantile(0.75)
                        iqr = q3 - q1
                        
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.metric("Q1 (25%)", f"{q1:.2f}")
                        with col2:
                            st.metric("Q2 (50%)", f"{q2:.2f}")
                        with col3:
                            st.metric("Q3 (75%)", f"{q3:.2f}")
                        with col4:
                            st.metric("IQR", f"{iqr:.2f}")
                        
                        st.code("Excel: =AVERAGE(), =MEDIAN(), =STDEV(), =QUARTILE()")
                        st.code(f"Python: df['{selected_col}'].describe()")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Need at least 1 numeric column.")
    
    elif playground_tab == "Power Query Simulator":
        st.subheader("⚡ Power Query Simulator")
        st.markdown("Learn data transformation steps like Power Query in Excel!")
        
        # Sample raw data that needs cleaning
        if 'pq_raw_data' not in st.session_state:
            st.session_state.pq_raw_data = pd.DataFrame({
                'Date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
                'Product_ID': ['P001', 'P002', 'P001', 'P003', 'P002'],
                'Sales_Amount': [1500, 2200, 1800, None, 2500],
                'Region': ['north', 'SOUTH', 'North', 'east', 'South'],
                'Notes': ['  Good sale  ', 'Discount applied', None, 'New customer', 'Repeat']
            })
        
        st.markdown("### Source Data")
        st.caption("This data has common issues: missing values, inconsistent casing, extra spaces")
        st.session_state.pq_raw_data = st.data_editor(
            st.session_state.pq_raw_data,
            num_rows="dynamic",
            use_container_width=True,
            key="pq_raw_editor"
        )
        
        raw_data = st.session_state.pq_raw_data.copy()
        
        st.markdown("### Transform Steps")
        st.markdown("Select transformations to apply (like Power Query steps):")
        
        transformations = {
            "Remove Duplicates": st.checkbox("Remove Duplicates", key="pq_dedup"),
            "Fill Missing Values": st.checkbox("Fill Missing Values (with 0 or 'Unknown')", key="pq_fill"),
            "Standardize Text Case": st.checkbox("Standardize Text Case (Title Case)", key="pq_case"),
            "Trim Whitespace": st.checkbox("Trim Whitespace", key="pq_trim"),
            "Filter Rows": st.checkbox("Filter Rows (remove nulls)", key="pq_filter"),
            "Add Calculated Column": st.checkbox("Add Calculated Column", key="pq_calc"),
            "Change Data Types": st.checkbox("Convert Date Column", key="pq_types"),
            "Sort Data": st.checkbox("Sort Data", key="pq_sort")
        }
        
        if st.button("Apply Transformations", type="primary"):
            transformed = raw_data.copy()
            steps_applied = []
            
            try:
                if transformations["Remove Duplicates"]:
                    before = len(transformed)
                    transformed = transformed.drop_duplicates()
                    steps_applied.append(f"Removed Duplicates: {before - len(transformed)} rows removed")
                
                if transformations["Fill Missing Values"]:
                    for col in transformed.columns:
                        if transformed[col].dtype == 'object':
                            transformed[col] = transformed[col].fillna('Unknown')
                        else:
                            transformed[col] = transformed[col].fillna(0)
                    steps_applied.append("Filled Missing Values: Numeric with 0, Text with 'Unknown'")
                
                if transformations["Standardize Text Case"]:
                    for col in transformed.select_dtypes(include=['object']).columns:
                        transformed[col] = transformed[col].astype(str).str.title()
                    steps_applied.append("Standardized Text Case: Converted to Title Case")
                
                if transformations["Trim Whitespace"]:
                    for col in transformed.select_dtypes(include=['object']).columns:
                        transformed[col] = transformed[col].astype(str).str.strip()
                    steps_applied.append("Trimmed Whitespace: Removed leading/trailing spaces")
                
                if transformations["Filter Rows"]:
                    before = len(transformed)
                    transformed = transformed.dropna()
                    steps_applied.append(f"Filtered Rows: Removed {before - len(transformed)} rows with nulls")
                
                if transformations["Add Calculated Column"]:
                    if 'Sales_Amount' in transformed.columns:
                        transformed['Sales_Amount'] = pd.to_numeric(transformed['Sales_Amount'], errors='coerce')
                        transformed['Tax_10pct'] = transformed['Sales_Amount'] * 0.10
                        steps_applied.append("Added Column: Tax_10pct = Sales_Amount * 0.10")
                
                if transformations["Change Data Types"]:
                    if 'Date' in transformed.columns:
                        transformed['Date'] = pd.to_datetime(transformed['Date'], errors='coerce')
                        transformed['Year'] = transformed['Date'].dt.year
                        transformed['Month'] = transformed['Date'].dt.month
                        steps_applied.append("Changed Types: Converted Date, extracted Year and Month")
                
                if transformations["Sort Data"]:
                    if 'Date' in transformed.columns:
                        transformed = transformed.sort_values('Date')
                        steps_applied.append("Sorted Data: By Date ascending")
                
                st.markdown("### Applied Steps")
                for i, step in enumerate(steps_applied, 1):
                    st.markdown(f"{i}. {step}")
                
                if not steps_applied:
                    st.info("No transformations selected. Check some boxes above.")
                else:
                    st.markdown("### Transformed Data")
                    st.dataframe(transformed, use_container_width=True)
                    
                    st.markdown("### Power Query M Code Equivalent")
                    m_code = "let\n    Source = Excel.CurrentWorkbook(){[Name=\"Table1\"]}[Content],\n"
                    for step in steps_applied:
                        m_code += f"    // {step}\n"
                    m_code += "    Result = Source\nin\n    Result"
                    st.code(m_code, language="text")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        st.markdown("---")
        st.markdown("**Common Power Query Operations:**")
        st.markdown("- **Remove Duplicates**: Eliminate duplicate rows")
        st.markdown("- **Fill Down/Replace Nulls**: Handle missing data")
        st.markdown("- **Change Type**: Convert data types")
        st.markdown("- **Split/Merge Columns**: Restructure data")
        st.markdown("- **Pivot/Unpivot**: Reshape tables")
        st.markdown("- **Group By**: Aggregate data")
    
    elif playground_tab == "Z-Score & Outlier Tool":
        st.subheader("📏 Z-Score & Outlier Detection")
        st.markdown("Calculate z-scores and identify outliers in your data!")
        
        from scipy import stats
        import numpy as np
        
        st.markdown("### What is a Z-Score?")
        st.markdown("""
        - **Z-score** measures how many standard deviations a value is from the mean
        - Formula: z = (x - mean) / standard_deviation
        - Values with |z| > 2 or 3 are often considered outliers
        """)
        
        # Sample data with potential outliers
        if 'zscore_data' not in st.session_state:
            st.session_state.zscore_data = pd.DataFrame({
                'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
                'Salary': [52000, 55000, 48000, 150000, 53000, 51000, 54000, 49000, 56000, 52000],
                'Performance': [85, 78, 92, 88, 15, 82, 79, 91, 84, 80],
                'Hours_Worked': [42, 45, 40, 38, 80, 41, 43, 39, 44, 42]
            })
        
        st.markdown("### Your Data (Edit to add your own!)")
        st.caption("This sample data contains some outliers. Can you spot them?")
        st.session_state.zscore_data = st.data_editor(
            st.session_state.zscore_data,
            num_rows="dynamic",
            use_container_width=True,
            key="zscore_data_editor"
        )
        
        zscore_data = st.session_state.zscore_data
        numeric_cols = zscore_data.select_dtypes(include=['number']).columns.tolist()
        
        if numeric_cols:
            col1, col2 = st.columns(2)
            with col1:
                selected_col = st.selectbox("Select column to analyze:", numeric_cols)
            with col2:
                threshold = st.slider("Z-score threshold for outliers:", 1.0, 4.0, 2.0, 0.5)
            
            if st.button("Calculate Z-Scores", type="primary"):
                try:
                    data = zscore_data[selected_col]
                    mean = data.mean()
                    std = data.std()
                    
                    # Calculate z-scores
                    z_scores = (data - mean) / std
                    
                    # Create results dataframe
                    results = zscore_data.copy()
                    results['Z_Score'] = z_scores.round(2)
                    results['Is_Outlier'] = abs(z_scores) > threshold
                    
                    st.markdown("### Statistics")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Mean", f"{mean:.2f}")
                    with col2:
                        st.metric("Std Dev", f"{std:.2f}")
                    with col3:
                        outlier_count = results['Is_Outlier'].sum()
                        st.metric("Outliers Found", f"{outlier_count}")
                    
                    st.markdown("### Results with Z-Scores")
                    
                    # Highlight outliers
                    def highlight_outliers(row):
                        if row['Is_Outlier']:
                            return ['background-color: #ffcccc'] * len(row)
                        return [''] * len(row)
                    
                    styled = results.style.apply(highlight_outliers, axis=1)
                    st.dataframe(results, use_container_width=True)
                    
                    if outlier_count > 0:
                        st.markdown("### Identified Outliers")
                        outliers = results[results['Is_Outlier']]
                        st.dataframe(outliers, use_container_width=True)
                        
                        st.warning(f"Found {outlier_count} outlier(s) with |z-score| > {threshold}")
                        
                        # Show how to handle outliers
                        st.markdown("### How to Handle Outliers")
                        handling = st.selectbox(
                            "Choose handling method:",
                            ["View only", "Remove outliers", "Cap outliers (Winsorization)", "Replace with mean"]
                        )
                        
                        if handling == "Remove outliers":
                            cleaned = zscore_data[abs(z_scores) <= threshold]
                            st.markdown("**Data with outliers removed:**")
                            st.dataframe(cleaned, use_container_width=True)
                            st.info(f"Removed {len(zscore_data) - len(cleaned)} rows")
                        
                        elif handling == "Cap outliers (Winsorization)":
                            lower_bound = mean - threshold * std
                            upper_bound = mean + threshold * std
                            capped = zscore_data.copy()
                            capped[selected_col] = capped[selected_col].clip(lower_bound, upper_bound)
                            st.markdown("**Data with outliers capped:**")
                            st.dataframe(capped, use_container_width=True)
                            st.info(f"Values capped to range [{lower_bound:.2f}, {upper_bound:.2f}]")
                        
                        elif handling == "Replace with mean":
                            replaced = zscore_data.copy()
                            replaced.loc[abs(z_scores) > threshold, selected_col] = mean
                            st.markdown("**Data with outliers replaced by mean:**")
                            st.dataframe(replaced, use_container_width=True)
                    else:
                        st.success(f"No outliers found with |z-score| > {threshold}")
                    
                    # Visualization
                    st.markdown("### Z-Score Distribution")
                    import altair as alt
                    
                    z_df = pd.DataFrame({
                        'Value': data,
                        'Z_Score': z_scores,
                        'Is_Outlier': abs(z_scores) > threshold
                    })
                    
                    scatter = alt.Chart(z_df).mark_circle(size=100).encode(
                        x='Value',
                        y='Z_Score',
                        color=alt.condition(
                            alt.datum.Is_Outlier,
                            alt.value('red'),
                            alt.value('steelblue')
                        ),
                        tooltip=['Value', 'Z_Score']
                    ).properties(width=600, height=300)
                    
                    # Add threshold lines
                    rule_upper = alt.Chart(pd.DataFrame({'y': [threshold]})).mark_rule(color='orange', strokeDash=[5,5]).encode(y='y')
                    rule_lower = alt.Chart(pd.DataFrame({'y': [-threshold]})).mark_rule(color='orange', strokeDash=[5,5]).encode(y='y')
                    
                    st.altair_chart(scatter + rule_upper + rule_lower, use_container_width=True)
                    st.caption("Red points are outliers. Orange lines show the threshold.")
                    
                    st.code(f"Excel: =(A2-AVERAGE(A:A))/STDEV(A:A)")
                    st.code(f"Python: scipy.stats.zscore(df['{selected_col}'])")
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Need at least 1 numeric column.")
    
    elif playground_tab == "Ethical Analysis Critique":
        st.subheader("⚖️ Ethical Analysis Critique")
        st.markdown("*Practice assessing and critiquing analysis approaches using ethical principles*")
        st.markdown("---")
        
        ethical_scenarios = {
            "Hiring Algorithm Bias": {
                "scenario": """
**Scenario: AI-Powered Hiring Recommendations**

A company has deployed an AI model to screen job applications. The model was trained on 5 years of historical hiring decisions.

**Analysis Approach Used:**
- Model trained on past successful hires
- Features include: education, experience, skills, resume keywords
- 87% accuracy on test data
- No demographic data explicitly used

**Recent Findings:**
- Female candidates rejected at 2x rate of male candidates
- Candidates from certain universities favored regardless of qualifications
- Model seems to prefer resumes with "aggressive" language

**The data team says:** "The model is objective - it's just learning from data."
                """,
                "critique_points": [
                    "Historical bias: Training on past decisions encodes past discrimination",
                    "Proxy discrimination: Non-demographic features may correlate with protected groups",
                    "Outcome fairness: Disparate impact on protected groups requires investigation",
                    "Transparency: Can decisions be explained to rejected candidates?",
                    "Accountability: Who is responsible when the model discriminates?",
                    "Alternative approaches: Blind resume screening, structured interviews, diverse training data"
                ],
                "suggested_alternatives": [
                    "Audit model for demographic disparities before deployment",
                    "Remove features that correlate with protected characteristics",
                    "Use balanced training data or apply fairness constraints",
                    "Implement human review for borderline decisions",
                    "Regularly monitor outcomes for bias after deployment"
                ]
            },
            "Healthcare Risk Scoring": {
                "scenario": """
**Scenario: Patient Risk Prediction**

A hospital uses a predictive model to identify high-risk patients who need extra care.

**Analysis Approach Used:**
- Model predicts risk based on past healthcare costs
- Higher predicted cost = higher risk score
- Used to allocate care management resources

**Problem Discovered:**
- Black patients assigned systematically lower risk scores than equally sick white patients
- Root cause: Using healthcare cost as proxy for health need
- Black patients historically had less access to care, so lower costs
- Result: Sicker Black patients denied extra care resources

**The vendor says:** "We don't use race in the model, so it can't be biased."
                """,
                "critique_points": [
                    "Construct validity: Healthcare cost ≠ health need",
                    "Historical inequity: Past access barriers encoded in data",
                    "Disparate impact: Equal treatment doesn't mean equitable outcomes",
                    "Proxy variables: Cost correlates with race due to systemic factors",
                    "Harm potential: Life-or-death consequences of misallocation",
                    "The 'colorblind' fallacy: Not using race doesn't prevent racial bias"
                ],
                "suggested_alternatives": [
                    "Use actual health outcomes (diagnoses, lab results) instead of costs",
                    "Validate model performance across demographic groups",
                    "Apply equity-aware adjustments to scores",
                    "Involve affected communities in model design",
                    "Regular audits for disparate impact"
                ]
            },
            "Credit Scoring Transparency": {
                "scenario": """
**Scenario: Loan Application Denial**

A bank uses a machine learning model to approve or deny loan applications.

**Analysis Approach Used:**
- Complex neural network with 200+ features
- Very high accuracy (94% on test data)
- Considers: income, employment, credit history, spending patterns, social media activity

**Customer Complaint:**
A customer with good credit history and stable income was denied. When they asked why:
- Bank said: "Our model determined you're high risk"
- Customer asked for specifics: "We can't explain the model's decision"
- Customer discovered neighbors with similar profiles were approved

**The bank says:** "The model is proprietary and we can't reveal how it works."
                """,
                "critique_points": [
                    "Explainability: Customers have right to understand decisions affecting them",
                    "GDPR Article 22: Right to explanation for automated decisions",
                    "Fairness: Similar cases should have similar outcomes",
                    "Social media data: Ethical concerns about using personal data",
                    "Accountability gap: Who is responsible if model is wrong?",
                    "Trust: Unexplainable decisions erode public trust"
                ],
                "suggested_alternatives": [
                    "Use interpretable models (decision trees, logistic regression)",
                    "Implement SHAP/LIME for feature importance explanations",
                    "Provide customers with key factors in their decision",
                    "Remove social media features (privacy concerns)",
                    "Create appeals process with human review"
                ]
            },
            "Predictive Policing": {
                "scenario": """
**Scenario: Crime Prediction Hotspots**

A city police department uses predictive analytics to allocate patrol resources.

**Analysis Approach Used:**
- Model trained on historical arrest data
- Predicts "crime hotspots" for next week
- More officers sent to high-prediction areas

**Observed Feedback Loop:**
- Model sends more officers to historically over-policed areas
- More officers → more arrests (for same crime rates)
- More arrests → model predicts more crime there
- Cycle reinforces itself regardless of actual crime rates

**Police chief says:** "We're just following the data."
                """,
                "critique_points": [
                    "Feedback loops: Predictions become self-fulfilling",
                    "Historical bias: Arrest data reflects policing patterns, not crime rates",
                    "Disparate impact: Certain communities disproportionately affected",
                    "Measurement error: Arrests ≠ crimes committed",
                    "Amplification: Model amplifies existing biases over time",
                    "Community harm: Erodes trust, over-surveillance of communities"
                ],
                "suggested_alternatives": [
                    "Use victimization surveys instead of arrest data",
                    "Include decay factor to break feedback loops",
                    "Monitor and cap predictions for any single area",
                    "Community input on policing priorities",
                    "Regular equity audits of model predictions vs outcomes"
                ]
            }
        }
        
        selected_scenario = st.selectbox("Select a scenario to critique:", list(ethical_scenarios.keys()))
        
        scenario_data = ethical_scenarios[selected_scenario]
        
        st.markdown("### The Scenario")
        st.markdown(scenario_data["scenario"])
        
        st.markdown("---")
        st.markdown("### Your Ethical Critique")
        st.markdown("*Consider: What ethical issues do you see? What principles are violated? What would you recommend?*")
        
        user_critique = st.text_area(
            "Write your critique here:",
            height=200,
            placeholder="Identify ethical issues, violated principles, and suggest alternatives..."
        )
        
        col1, col2 = st.columns(2)
        with col1:
            show_critique = st.button("📋 Show Expert Critique", type="primary")
        with col2:
            show_alternatives = st.button("💡 Show Recommended Alternatives")
        
        if show_critique:
            st.markdown("### Expert Critique Points")
            for point in scenario_data["critique_points"]:
                st.markdown(f"- {point}")
        
        if show_alternatives:
            st.markdown("### Recommended Alternatives")
            for alt in scenario_data["suggested_alternatives"]:
                st.markdown(f"✓ {alt}")
        
        st.markdown("---")
        st.markdown("### Ethical Principles Checklist")
        
        principles = [
            ("Fairness", "Does the approach treat all groups equitably?"),
            ("Transparency", "Can decisions be explained to affected parties?"),
            ("Accountability", "Is there clear responsibility for outcomes?"),
            ("Privacy", "Is personal data used appropriately?"),
            ("Non-maleficence", "Could this cause harm to individuals or groups?"),
            ("Autonomy", "Do people have meaningful choice about data use?")
        ]
        
        st.markdown("*Rate this analysis approach on each principle:*")
        
        for principle, description in principles:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.selectbox(
                    principle,
                    ["Not assessed", "Serious concern", "Minor concern", "Acceptable", "Good practice"],
                    key=f"eth_{principle}"
                )
            with col2:
                st.caption(description)
    
    elif playground_tab == "Error Detection Workshop":
        st.subheader("🔍 Error Detection Workshop")
        st.markdown("*Practice identifying erroneous data and facilitating solution discussions*")
        st.markdown("---")
        
        if 'error_workshop_data' not in st.session_state:
            st.session_state.error_workshop_data = pd.DataFrame({
                'Customer_ID': ['C001', 'C002', 'C003', 'C004', 'C002', 'C006', 'C007', 'C008'],
                'Name': ['Alice Brown', 'Bob Smith', 'Carol White', 'David Lee', 'Bob Smith', 'Eve Clark', 'Frank Miller', 'Grace Kim'],
                'Age': [28, 35, -5, 42, 35, 150, 31, 29],
                'Email': ['alice@email.com', 'bob@email', 'carol@email.com', '', 'bob@email', 'eve@email.com', 'frank@email.com', 'grace@email.com'],
                'Order_Amount': [150.00, 2500.00, 89.50, 320.00, 2500.00, 175.00, 999999.99, 210.00],
                'Order_Date': ['2024-01-15', '2024-13-01', '2024-02-28', '2024-03-10', '2024-01-15', '2024-04-05', '2024-05-20', '1924-06-15'],
                'Region': ['North', 'South', 'East', 'West', 'South', 'north', 'NORTH', 'East']
            })
        
        st.markdown("### Dataset with Errors")
        st.markdown("*This dataset contains various data quality issues. Can you identify them all?*")
        
        st.dataframe(st.session_state.error_workshop_data, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Error Identification")
        st.markdown("*Select all the errors you can identify:*")
        
        error_types = {
            "Duplicate records": {
                "hint": "Look for identical Customer_ID and Name combinations",
                "location": "Rows 2 and 5 (C002 - Bob Smith appears twice)",
                "impact": "Double-counting customers, inflated metrics",
                "solution": "Deduplicate based on Customer_ID, keep most recent record"
            },
            "Invalid age values": {
                "hint": "Age should be between 0 and ~120",
                "location": "Row 3: Age=-5, Row 6: Age=150",
                "impact": "Statistical calculations will be skewed, demographic analysis invalid",
                "solution": "Flag for review, set to NULL or impute based on customer segment"
            },
            "Invalid email format": {
                "hint": "Emails should contain @ and a domain extension",
                "location": "Row 2: 'bob@email' (missing .com), Row 4: empty",
                "impact": "Email campaigns will fail, communication gaps",
                "solution": "Validate format, request corrections from customers"
            },
            "Outlier amounts": {
                "hint": "Look for unusually high or low order amounts",
                "location": "Row 7: $999,999.99 is suspiciously high",
                "impact": "Revenue metrics distorted, may indicate data entry error or fraud",
                "solution": "Investigate source, verify with order system, cap or remove if erroneous"
            },
            "Invalid date format": {
                "hint": "Check for impossible dates",
                "location": "Row 2: '2024-13-01' (month 13 doesn't exist)",
                "impact": "Date parsing will fail, time-series analysis broken",
                "solution": "Parse dates strictly, flag failures for manual review"
            },
            "Historical date anomaly": {
                "hint": "Check if dates make business sense",
                "location": "Row 8: '1924-06-15' is 100 years ago",
                "impact": "Time-based analysis will include ancient outliers",
                "solution": "Set business rules for valid date ranges (e.g., company founding date)"
            },
            "Inconsistent region coding": {
                "hint": "Check for case sensitivity issues",
                "location": "'North', 'north', 'NORTH' are all different",
                "impact": "Grouping by region will split what should be one category",
                "solution": "Standardize to consistent case (e.g., Title Case)"
            }
        }
        
        identified_errors = []
        for error_type in error_types.keys():
            if st.checkbox(error_type, key=f"err_{error_type}"):
                identified_errors.append(error_type)
        
        if st.button("📊 Check My Answers", type="primary"):
            score = len(identified_errors)
            total = len(error_types)
            
            if score == total:
                st.success(f"🎉 Excellent! You found all {total} error types!")
            elif score >= total * 0.7:
                st.info(f"Good job! You found {score}/{total} error types.")
            else:
                st.warning(f"You found {score}/{total} error types. Keep looking!")
            
            st.markdown("### Detailed Error Analysis")
            
            for error_type, details in error_types.items():
                with st.expander(f"{'✓' if error_type in identified_errors else '✗'} {error_type}"):
                    st.markdown(f"**Location:** {details['location']}")
                    st.markdown(f"**Impact:** {details['impact']}")
                    st.markdown(f"**Solution:** {details['solution']}")
        
        st.markdown("---")
        st.markdown("### Facilitating Solution Discussions")
        st.markdown("*Practice communicating data issues to stakeholders*")
        
        discussion_scenario = st.selectbox(
            "Select a discussion scenario:",
            [
                "Presenting errors to business stakeholders",
                "Discussing impact with analytics team",
                "Proposing fixes to data engineering",
                "Escalating critical issues to management"
            ]
        )
        
        discussion_templates = {
            "Presenting errors to business stakeholders": """
**Template: Business Stakeholder Briefing**

1. **Summary Statement** (plain language)
   "We've found some data quality issues that could affect our [X] reports."

2. **Business Impact** (focus on what they care about)
   - "Our customer count may be inflated by X% due to duplicates"
   - "Revenue figures could be off because of data entry errors"

3. **Recommended Actions**
   - "We recommend pausing the report until data is cleaned"
   - "This will take approximately X days to fix"

4. **Ask**
   - "Do you need the approximate numbers now, or can you wait for accurate data?"
            """,
            "Discussing impact with analytics team": """
**Template: Analytics Team Discussion**

1. **Technical Summary**
   "I've identified X types of data quality issues in the customer dataset"

2. **Specific Issues** (with evidence)
   - Issue 1: Duplicates on Customer_ID (X records affected)
   - Issue 2: Invalid values in Age column (Y records affected)

3. **Impact on Analysis**
   - "Demographic segmentation will be skewed"
   - "Time-series trends may show artifacts"

4. **Proposed Validation Rules**
   - Age: 0 < age < 120
   - Email: regex pattern matching
   - Date: within business operation period

5. **Discussion Points**
   - "How should we handle edge cases?"
   - "What's our tolerance for missing data?"
            """,
            "Proposing fixes to data engineering": """
**Template: Data Engineering Request**

1. **Issue Identification**
   "Request to add data validation rules to the ingestion pipeline"

2. **Specific Rules Needed**
   ```
   - Deduplicate on Customer_ID (keep latest)
   - Validate: Age BETWEEN 0 AND 120
   - Validate: Email matches pattern '@.+\\.'
   - Validate: Order_Date > '2020-01-01'
   - Standardize: Region to Title Case
   ```

3. **Priority Justification**
   "These issues affect X% of records and impact downstream reports"

4. **Suggested Implementation**
   - Add validation at ingestion
   - Route failures to quarantine table
   - Alert on failure rate threshold
            """,
            "Escalating critical issues to management": """
**Template: Management Escalation**

1. **Issue Summary** (1-2 sentences)
   "We've discovered data quality issues that affect the accuracy of [critical report/decision]"

2. **Business Risk** (quantified if possible)
   - "Customer metrics may be overstated by X%"
   - "This affects decisions worth $Y"

3. **Current Status**
   - Issue identified on [date]
   - Root cause: [brief explanation]
   - Estimated fix time: [duration]

4. **Decision Required**
   - "Should we pause reporting until fixed?"
   - "What's the acceptable error margin?"

5. **Recommendation**
   "We recommend [specific action] because [reasoning]"
            """
        }
        
        st.markdown(discussion_templates[discussion_scenario])
        
        st.markdown("---")
        st.markdown("### Practice Your Communication")
        user_discussion = st.text_area(
            f"Write your own message for: {discussion_scenario}",
            height=150,
            placeholder="Draft your message to stakeholders..."
        )
        
        if user_discussion and st.button("Get Feedback"):
            st.info("💡 **Tips for effective communication:**\n"
                   "- Lead with impact, not technical details\n"
                   "- Quantify issues when possible\n"
                   "- Always propose solutions, not just problems\n"
                   "- Be clear about what decision or action you need")
    
    elif playground_tab == "Confidence Level Planner":
        st.subheader("📊 Confidence Level Planner")
        st.markdown("*Develop work methods for handling data with different confidence levels*")
        st.markdown("---")
        
        st.markdown("### Understanding Confidence Levels")
        
        confidence_info = pd.DataFrame({
            'Confidence Level': ['99%', '95%', '90%', '80%', '70%'],
            'Z-Score': [2.576, 1.960, 1.645, 1.282, 1.036],
            'Margin of Error (n=100)': ['±12.9%', '±9.8%', '±8.2%', '±6.4%', '±5.2%'],
            'Typical Use': ['Medical/safety decisions', 'Academic research', 'Quality control', 'Business planning', 'Quick estimates']
        })
        st.dataframe(confidence_info, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Confidence Level Decision Framework")
        
        problem_domains = {
            "Medical/Healthcare": {
                "recommended_confidence": "99%",
                "reasoning": "Patient safety is paramount; false negatives could mean missed diagnoses",
                "work_methods": [
                    "Require large sample sizes for clinical decisions",
                    "Always report confidence intervals in results",
                    "Use conservative estimates (lower bound of CI)",
                    "Require peer review before recommendations",
                    "Document uncertainty explicitly in reports"
                ],
                "decision_rules": {
                    "High confidence (>99%)": "Proceed with treatment recommendation",
                    "Medium confidence (95-99%)": "Recommend additional testing",
                    "Low confidence (<95%)": "Do not make clinical recommendations"
                }
            },
            "Financial/Investment": {
                "recommended_confidence": "95%",
                "reasoning": "Balance between action and risk; financial impact can be significant",
                "work_methods": [
                    "Use 95% CI for major investment decisions",
                    "90% acceptable for operational decisions",
                    "Always calculate potential loss at confidence bounds",
                    "Stress test with worst-case scenarios",
                    "Document assumptions and limitations"
                ],
                "decision_rules": {
                    "High confidence (>95%)": "Recommend investment/action",
                    "Medium confidence (90-95%)": "Present options with risk assessment",
                    "Low confidence (<90%)": "Recommend gathering more data"
                }
            },
            "Marketing/Customer Analytics": {
                "recommended_confidence": "90%",
                "reasoning": "Speed often matters; decisions are reversible; cost of error is lower",
                "work_methods": [
                    "Use 90% CI for campaign decisions",
                    "80% acceptable for exploratory analysis",
                    "A/B test with statistical significance checks",
                    "Monitor results and iterate quickly",
                    "Build in review cycles to catch errors"
                ],
                "decision_rules": {
                    "High confidence (>90%)": "Launch campaign/feature",
                    "Medium confidence (80-90%)": "Small-scale pilot test first",
                    "Low confidence (<80%)": "Continue testing or try different approach"
                }
            },
            "Operations/Supply Chain": {
                "recommended_confidence": "95%",
                "reasoning": "Inventory and logistics decisions have cost implications both ways",
                "work_methods": [
                    "Use 95% CI for demand forecasting",
                    "Build safety stock based on confidence bounds",
                    "Monitor forecast accuracy over time",
                    "Adjust confidence requirements by product criticality",
                    "Document service level agreements tied to confidence"
                ],
                "decision_rules": {
                    "High confidence (>95%)": "Set optimal inventory levels",
                    "Medium confidence (90-95%)": "Add safety stock buffer",
                    "Low confidence (<90%)": "Increase safety stock significantly or source alternatives"
                }
            },
            "Research/Academic": {
                "recommended_confidence": "95% (p < 0.05)",
                "reasoning": "Scientific credibility requires rigorous standards",
                "work_methods": [
                    "Pre-register hypotheses before analysis",
                    "Use 95% CI as minimum for publication",
                    "Report exact p-values, not just significance",
                    "Calculate and report effect sizes",
                    "Acknowledge limitations and confidence bounds"
                ],
                "decision_rules": {
                    "Statistically significant (p<0.05)": "Report finding with confidence interval",
                    "Marginally significant (0.05<p<0.10)": "Report as suggestive, needs replication",
                    "Not significant (p>0.10)": "Report null result, discuss sample size"
                }
            }
        }
        
        selected_domain = st.selectbox("Select a problem domain:", list(problem_domains.keys()))
        
        domain_data = problem_domains[selected_domain]
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Recommended Confidence Level", domain_data["recommended_confidence"])
        with col2:
            st.info(f"**Reasoning:** {domain_data['reasoning']}")
        
        st.markdown("### Work Methods for This Domain")
        for method in domain_data["work_methods"]:
            st.markdown(f"• {method}")
        
        st.markdown("### Decision Rules Based on Confidence")
        for level, action in domain_data["decision_rules"].items():
            st.markdown(f"**{level}:** {action}")
        
        st.markdown("---")
        st.markdown("### Interactive Confidence Calculator")
        
        col1, col2 = st.columns(2)
        with col1:
            sample_size = st.number_input("Sample Size (n):", min_value=10, max_value=10000, value=100)
            sample_mean = st.number_input("Sample Mean:", value=50.0)
            sample_std = st.number_input("Sample Std Dev:", min_value=0.1, value=10.0)
        
        with col2:
            confidence_level = st.selectbox(
                "Confidence Level:",
                ["99%", "95%", "90%", "80%"],
                index=1
            )
            
            z_scores = {"99%": 2.576, "95%": 1.960, "90%": 1.645, "80%": 1.282}
            z = z_scores[confidence_level]
            
            margin_error = z * (sample_std / (sample_size ** 0.5))
            lower_bound = sample_mean - margin_error
            upper_bound = sample_mean + margin_error
        
        st.markdown("### Results")
        
        result_col1, result_col2, result_col3 = st.columns(3)
        with result_col1:
            st.metric("Lower Bound", f"{lower_bound:.2f}")
        with result_col2:
            st.metric("Point Estimate", f"{sample_mean:.2f}")
        with result_col3:
            st.metric("Upper Bound", f"{upper_bound:.2f}")
        
        st.markdown(f"**{confidence_level} Confidence Interval:** [{lower_bound:.2f}, {upper_bound:.2f}]")
        st.markdown(f"**Margin of Error:** ±{margin_error:.2f} ({(margin_error/sample_mean)*100:.1f}% of mean)")
        
        st.markdown("---")
        st.markdown("### Create Your Work Method Document")
        
        st.markdown("*Based on your domain and confidence requirements, document your work method:*")
        
        work_method_template = st.text_area(
            "Your Work Method Document:",
            value=f"""WORK METHOD: {selected_domain} Analysis

CONFIDENCE STANDARD: {domain_data['recommended_confidence']}

DATA REQUIREMENTS:
- Minimum sample size: [specify based on required precision]
- Data quality checks: [list validation rules]
- Exclusion criteria: [what data to remove]

ANALYSIS PROTOCOL:
1. Calculate point estimate and confidence interval
2. Apply decision rules based on confidence level
3. Document assumptions and limitations
4. Review with [stakeholder/peer]

REPORTING REQUIREMENTS:
- Always report confidence intervals
- Flag results below confidence threshold
- Document sample size and methodology

ESCALATION:
- If confidence < threshold: [specific action]
- If data quality issues: [specific action]
""",
            height=400
        )
        
        if st.button("💾 Save Work Method (Download)", type="primary"):
            st.download_button(
                label="Download Work Method Document",
                data=work_method_template,
                file_name=f"work_method_{selected_domain.lower().replace('/', '_')}.txt",
                mime="text/plain"
            )
    
    elif playground_tab == "BI & Big Data Explorer":
        st.subheader("📊 BI & Big Data Explorer")
        st.markdown("*Explore Business Intelligence concepts and identify Big Data scenarios*")
        st.markdown("---")
        
        explorer_mode = st.radio(
            "Choose exploration mode:",
            ["BI vs Big Data Classifier", "Data Volume Calculator", "BI Tool Selector"],
            horizontal=True
        )
        
        if explorer_mode == "BI vs Big Data Classifier":
            st.markdown("### Classify Your Data Scenario")
            st.markdown("*Answer these questions to determine if your scenario is BI or Big Data*")
            
            col1, col2 = st.columns(2)
            with col1:
                data_volume = st.select_slider(
                    "Data Volume:",
                    options=["Megabytes", "Gigabytes", "Terabytes", "Petabytes"],
                    value="Gigabytes"
                )
                data_velocity = st.select_slider(
                    "Data Velocity:",
                    options=["Daily updates", "Hourly updates", "Real-time streaming", "Millisecond events"],
                    value="Daily updates"
                )
            with col2:
                data_variety = st.multiselect(
                    "Data Types (Variety):",
                    ["Structured tables", "Text documents", "Images", "Videos", "Sensor data", "Social media"],
                    default=["Structured tables"]
                )
                analysis_goal = st.selectbox(
                    "Primary Goal:",
                    ["Report what happened", "Understand why it happened", "Predict what will happen", "Automate decisions"]
                )
            
            if st.button("🔍 Classify Scenario", type="primary"):
                score = 0
                reasons = []
                
                if data_volume in ["Terabytes", "Petabytes"]:
                    score += 2
                    reasons.append(f"High volume ({data_volume})")
                if data_velocity in ["Real-time streaming", "Millisecond events"]:
                    score += 2
                    reasons.append(f"High velocity ({data_velocity})")
                if len(data_variety) > 2:
                    score += 1
                    reasons.append(f"High variety ({len(data_variety)} types)")
                if "Images" in data_variety or "Videos" in data_variety or "Sensor data" in data_variety:
                    score += 1
                    reasons.append("Unstructured data types")
                if analysis_goal in ["Predict what will happen", "Automate decisions"]:
                    score += 1
                    reasons.append(f"Advanced analytics goal")
                
                st.markdown("---")
                if score >= 4:
                    st.error("🔴 **Big Data Scenario**")
                    st.markdown("Your scenario exhibits Big Data characteristics:")
                    for r in reasons:
                        st.markdown(f"- {r}")
                    st.markdown("**Recommended Tools:** Hadoop, Spark, Python, Cloud Data Platforms")
                elif score >= 2:
                    st.warning("🟡 **Hybrid Scenario**")
                    st.markdown("Your scenario has some Big Data elements but may work with BI tools:")
                    for r in reasons:
                        st.markdown(f"- {r}")
                    st.markdown("**Recommended:** Start with BI tools, scale to Big Data if needed")
                else:
                    st.success("🟢 **Business Intelligence Scenario**")
                    st.markdown("Your scenario is well-suited for traditional BI approaches.")
                    st.markdown("**Recommended Tools:** Excel, Tableau, Power BI, SQL databases")
        
        elif explorer_mode == "Data Volume Calculator":
            st.markdown("### Calculate Your Data Volume")
            
            col1, col2 = st.columns(2)
            with col1:
                records_per_day = st.number_input("Records generated per day:", min_value=1, value=1000)
                bytes_per_record = st.number_input("Average bytes per record:", min_value=1, value=500)
                retention_years = st.number_input("Years of data to retain:", min_value=1, value=3)
            
            with col2:
                daily_bytes = records_per_day * bytes_per_record
                yearly_bytes = daily_bytes * 365
                total_bytes = yearly_bytes * retention_years
                
                def format_bytes(b):
                    if b >= 1e15:
                        return f"{b/1e15:.2f} PB"
                    elif b >= 1e12:
                        return f"{b/1e12:.2f} TB"
                    elif b >= 1e9:
                        return f"{b/1e9:.2f} GB"
                    elif b >= 1e6:
                        return f"{b/1e6:.2f} MB"
                    else:
                        return f"{b/1e3:.2f} KB"
                
                st.metric("Daily Data", format_bytes(daily_bytes))
                st.metric("Yearly Data", format_bytes(yearly_bytes))
                st.metric(f"Total ({retention_years} years)", format_bytes(total_bytes))
                
                if total_bytes >= 1e12:
                    st.warning("⚠️ This volume may require Big Data infrastructure")
                else:
                    st.success("✓ This volume is manageable with traditional BI tools")
        
        elif explorer_mode == "BI Tool Selector":
            st.markdown("### Find the Right BI Tool")
            
            user_needs = st.multiselect(
                "What do you need to do?",
                ["Create dashboards", "Ad-hoc analysis", "Share reports", "Self-service analytics",
                 "Advanced calculations", "Real-time monitoring", "Mobile access", "Embedded analytics"]
            )
            
            budget = st.radio("Budget:", ["Free/Low cost", "Medium", "Enterprise"], horizontal=True)
            tech_level = st.radio("Technical level:", ["Beginner", "Intermediate", "Advanced"], horizontal=True)
            
            if st.button("🎯 Get Recommendations"):
                st.markdown("### Recommended Tools")
                
                recommendations = []
                
                if budget == "Free/Low cost" and tech_level == "Beginner":
                    recommendations.append(("Google Sheets + Looker Studio", "Free, easy to use, good for basic dashboards"))
                    recommendations.append(("Excel + Power BI (free tier)", "Familiar interface, powerful calculations"))
                
                if "Create dashboards" in user_needs:
                    recommendations.append(("Tableau Public", "Beautiful visualizations, free for public data"))
                    recommendations.append(("Power BI Desktop", "Free, integrates with Microsoft ecosystem"))
                
                if "Advanced calculations" in user_needs and tech_level in ["Intermediate", "Advanced"]:
                    recommendations.append(("Python + Jupyter", "Maximum flexibility, requires coding"))
                
                if budget == "Enterprise":
                    recommendations.append(("Tableau Server/Cloud", "Full-featured, enterprise security"))
                    recommendations.append(("Power BI Premium", "Microsoft integration, AI features"))
                
                if not recommendations:
                    recommendations.append(("Excel", "Versatile starting point for any analysis"))
                
                for tool, reason in recommendations:
                    st.markdown(f"**{tool}**")
                    st.caption(reason)
    
    elif playground_tab == "KPI Dashboard Builder":
        st.subheader("📈 KPI Dashboard Builder")
        st.markdown("*Design and visualize Key Performance Indicators for different business functions*")
        st.markdown("---")
        
        business_function = st.selectbox(
            "Select business function:",
            ["Sales", "Marketing", "Finance", "Operations", "HR", "Customer Service"]
        )
        
        kpi_templates = {
            "Sales": {
                "kpis": [
                    {"name": "Revenue", "target": 100000, "actual": 0, "unit": "$", "higher_better": True},
                    {"name": "Deals Closed", "target": 50, "actual": 0, "unit": "", "higher_better": True},
                    {"name": "Conversion Rate", "target": 25, "actual": 0, "unit": "%", "higher_better": True},
                    {"name": "Average Deal Size", "target": 2000, "actual": 0, "unit": "$", "higher_better": True},
                    {"name": "Sales Cycle (days)", "target": 30, "actual": 0, "unit": "days", "higher_better": False}
                ]
            },
            "Marketing": {
                "kpis": [
                    {"name": "Website Traffic", "target": 50000, "actual": 0, "unit": "visits", "higher_better": True},
                    {"name": "Lead Generation", "target": 500, "actual": 0, "unit": "leads", "higher_better": True},
                    {"name": "Cost per Lead", "target": 50, "actual": 0, "unit": "$", "higher_better": False},
                    {"name": "Email Open Rate", "target": 25, "actual": 0, "unit": "%", "higher_better": True},
                    {"name": "Social Engagement", "target": 5, "actual": 0, "unit": "%", "higher_better": True}
                ]
            },
            "Finance": {
                "kpis": [
                    {"name": "Gross Margin", "target": 40, "actual": 0, "unit": "%", "higher_better": True},
                    {"name": "Operating Expenses", "target": 50000, "actual": 0, "unit": "$", "higher_better": False},
                    {"name": "Cash Flow", "target": 25000, "actual": 0, "unit": "$", "higher_better": True},
                    {"name": "Accounts Receivable Days", "target": 30, "actual": 0, "unit": "days", "higher_better": False},
                    {"name": "Budget Variance", "target": 5, "actual": 0, "unit": "%", "higher_better": False}
                ]
            },
            "Operations": {
                "kpis": [
                    {"name": "Production Output", "target": 1000, "actual": 0, "unit": "units", "higher_better": True},
                    {"name": "Defect Rate", "target": 2, "actual": 0, "unit": "%", "higher_better": False},
                    {"name": "On-Time Delivery", "target": 95, "actual": 0, "unit": "%", "higher_better": True},
                    {"name": "Inventory Turnover", "target": 6, "actual": 0, "unit": "x", "higher_better": True},
                    {"name": "Equipment Uptime", "target": 98, "actual": 0, "unit": "%", "higher_better": True}
                ]
            },
            "HR": {
                "kpis": [
                    {"name": "Employee Turnover", "target": 10, "actual": 0, "unit": "%", "higher_better": False},
                    {"name": "Time to Hire", "target": 30, "actual": 0, "unit": "days", "higher_better": False},
                    {"name": "Training Hours", "target": 40, "actual": 0, "unit": "hrs", "higher_better": True},
                    {"name": "Employee Satisfaction", "target": 80, "actual": 0, "unit": "%", "higher_better": True},
                    {"name": "Absenteeism Rate", "target": 3, "actual": 0, "unit": "%", "higher_better": False}
                ]
            },
            "Customer Service": {
                "kpis": [
                    {"name": "Customer Satisfaction", "target": 90, "actual": 0, "unit": "%", "higher_better": True},
                    {"name": "First Response Time", "target": 2, "actual": 0, "unit": "hrs", "higher_better": False},
                    {"name": "Resolution Rate", "target": 85, "actual": 0, "unit": "%", "higher_better": True},
                    {"name": "NPS Score", "target": 50, "actual": 0, "unit": "", "higher_better": True},
                    {"name": "Tickets per Agent", "target": 20, "actual": 0, "unit": "", "higher_better": True}
                ]
            }
        }
        
        st.markdown(f"### {business_function} KPIs")
        st.markdown("*Enter your actual values to see RAG status*")
        
        template = kpi_templates[business_function]
        kpi_data = []
        
        for i, kpi in enumerate(template["kpis"]):
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            with col1:
                st.markdown(f"**{kpi['name']}**")
            with col2:
                actual = st.number_input(
                    f"Actual",
                    value=float(kpi["target"] * 0.9),
                    key=f"kpi_{business_function}_{i}",
                    label_visibility="collapsed"
                )
            with col3:
                st.caption(f"Target: {kpi['target']}{kpi['unit']}")
            with col4:
                if kpi["higher_better"]:
                    pct = (actual / kpi["target"]) * 100 if kpi["target"] > 0 else 0
                else:
                    if actual <= 0:
                        pct = 100
                    else:
                        pct = (kpi["target"] / actual) * 100
                
                if pct >= 100:
                    st.success("🟢")
                elif pct >= 80:
                    st.warning("🟡")
                else:
                    st.error("🔴")
            
            kpi_data.append({"KPI": kpi["name"], "Actual": actual, "Target": kpi["target"], "Achievement": f"{pct:.0f}%"})
        
        st.markdown("---")
        st.markdown("### Dashboard Summary")
        
        df_kpi = pd.DataFrame(kpi_data)
        st.dataframe(df_kpi, use_container_width=True)
        
        st.markdown("**RAG Legend:** 🟢 On track (≥100%) | 🟡 At risk (80-99%) | 🔴 Off track (<80%)")
    
    elif playground_tab == "Decision Analysis Tool":
        st.subheader("🎯 Decision Analysis Tool")
        st.markdown("*Practice the four analytics philosophies: Descriptive, Diagnostic, Predictive, Prescriptive*")
        st.markdown("---")
        
        analysis_type = st.radio(
            "Select analysis type:",
            ["Descriptive (What happened?)", "Diagnostic (Why did it happen?)", 
             "Predictive (What will happen?)", "Prescriptive (What should we do?)"],
            horizontal=False
        )
        
        if "Descriptive" in analysis_type:
            st.markdown("### Descriptive Analysis: What Happened?")
            st.markdown("*Summarize historical data to understand past performance*")
            
            if 'decision_data' not in st.session_state:
                st.session_state.decision_data = pd.DataFrame({
                    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                    'Sales': [45000, 52000, 48000, 61000, 55000, 67000],
                    'Customers': [120, 135, 128, 152, 145, 168],
                    'Returns': [12, 8, 15, 9, 11, 7]
                })
            
            st.markdown("**Your Data:**")
            st.session_state.decision_data = st.data_editor(
                st.session_state.decision_data,
                num_rows="dynamic",
                use_container_width=True
            )
            
            if st.button("📊 Generate Descriptive Summary"):
                data = st.session_state.decision_data
                st.markdown("### Summary Statistics")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Sales", f"${data['Sales'].sum():,}")
                    st.metric("Avg Monthly Sales", f"${data['Sales'].mean():,.0f}")
                with col2:
                    st.metric("Total Customers", f"{data['Customers'].sum():,}")
                    st.metric("Avg Monthly Customers", f"{data['Customers'].mean():.0f}")
                with col3:
                    st.metric("Total Returns", f"{data['Returns'].sum()}")
                    st.metric("Return Rate", f"{(data['Returns'].sum() / data['Sales'].sum()) * 100:.2f}%")
        
        elif "Diagnostic" in analysis_type:
            st.markdown("### Diagnostic Analysis: Why Did It Happen?")
            st.markdown("*Investigate root causes using the 5 Whys technique*")
            
            problem = st.text_input("What problem are you investigating?", "Sales dropped 20% in March")
            
            st.markdown("**Apply the 5 Whys:**")
            why1 = st.text_input("Why #1:", placeholder="Enter first why...")
            why2 = st.text_input("Why #2:", placeholder="Enter second why...")
            why3 = st.text_input("Why #3:", placeholder="Enter third why...")
            why4 = st.text_input("Why #4:", placeholder="Enter fourth why...")
            why5 = st.text_input("Why #5:", placeholder="Enter fifth why (root cause)...")
            
            if why5:
                st.markdown("---")
                st.success(f"**Root Cause Identified:** {why5}")
                st.markdown("**Next Steps:**")
                st.markdown("1. Validate this root cause with data")
                st.markdown("2. Develop action plan to address it")
                st.markdown("3. Implement preventive measures")
        
        elif "Predictive" in analysis_type:
            st.markdown("### Predictive Analysis: What Will Happen?")
            st.markdown("*Use trends to forecast future outcomes*")
            
            col1, col2 = st.columns(2)
            with col1:
                current_value = st.number_input("Current month value:", value=50000)
                growth_rate = st.slider("Expected monthly growth rate (%):", -20, 50, 5)
                months_ahead = st.slider("Months to forecast:", 1, 12, 6)
            
            with col2:
                st.markdown("### Forecast")
                forecast = []
                value = current_value
                for m in range(1, months_ahead + 1):
                    value = value * (1 + growth_rate / 100)
                    forecast.append({"Month": f"M+{m}", "Forecast": value})
                
                df_forecast = pd.DataFrame(forecast)
                st.dataframe(df_forecast.style.format({"Forecast": "${:,.0f}"}), use_container_width=True)
                
                st.metric(f"Predicted value in {months_ahead} months", f"${value:,.0f}")
                st.metric("Total growth", f"{((value - current_value) / current_value) * 100:.1f}%")
        
        elif "Prescriptive" in analysis_type:
            st.markdown("### Prescriptive Analysis: What Should We Do?")
            st.markdown("*Evaluate options and recommend actions*")
            
            st.markdown("**Define Your Decision Options:**")
            
            option1_name = st.text_input("Option 1:", "Increase marketing spend")
            option1_cost = st.number_input("Cost ($):", value=10000, key="opt1_cost")
            option1_benefit = st.number_input("Expected benefit ($):", value=25000, key="opt1_ben")
            option1_risk = st.slider("Risk level:", 1, 10, 3, key="opt1_risk")
            
            st.markdown("---")
            
            option2_name = st.text_input("Option 2:", "Hire more sales staff")
            option2_cost = st.number_input("Cost ($):", value=50000, key="opt2_cost")
            option2_benefit = st.number_input("Expected benefit ($):", value=80000, key="opt2_ben")
            option2_risk = st.slider("Risk level:", 1, 10, 5, key="opt2_risk")
            
            if st.button("🎯 Get Recommendation"):
                st.markdown("### Decision Matrix")
                
                roi1 = ((option1_benefit - option1_cost) / option1_cost) * 100 if option1_cost > 0 else 0
                roi2 = ((option2_benefit - option2_cost) / option2_cost) * 100 if option2_cost > 0 else 0
                
                score1 = roi1 / (option1_risk + 1)
                score2 = roi2 / (option2_risk + 1)
                
                comparison = pd.DataFrame({
                    'Option': [option1_name, option2_name],
                    'Cost': [f"${option1_cost:,}", f"${option2_cost:,}"],
                    'Benefit': [f"${option1_benefit:,}", f"${option2_benefit:,}"],
                    'ROI': [f"{roi1:.0f}%", f"{roi2:.0f}%"],
                    'Risk': [option1_risk, option2_risk],
                    'Score': [f"{score1:.1f}", f"{score2:.1f}"]
                })
                st.dataframe(comparison, use_container_width=True)
                
                if score1 > score2:
                    st.success(f"**Recommendation:** {option1_name} (higher risk-adjusted return)")
                else:
                    st.success(f"**Recommendation:** {option2_name} (higher risk-adjusted return)")
    
    elif playground_tab == "Project Planning Workshop":
        st.subheader("📋 Project Planning Workshop")
        st.markdown("*Practice planning a data analysis project with proper phases and deliverables*")
        st.markdown("---")
        
        st.markdown("### Define Your Project")
        
        project_name = st.text_input("Project Name:", "Customer Churn Analysis")
        project_duration = st.slider("Total Project Duration (weeks):", 2, 16, 8)
        
        st.markdown("### Project Phases")
        st.markdown("*Allocate percentage of time to each phase (should total 100%)*")
        
        col1, col2 = st.columns(2)
        with col1:
            phase1 = st.slider("1. Problem Definition & Scoping", 0, 100, 15, format="%d%%")
            phase2 = st.slider("2. Data Collection & Cleaning", 0, 100, 25, format="%d%%")
            phase3 = st.slider("3. Exploratory Analysis", 0, 100, 20, format="%d%%")
        with col2:
            phase4 = st.slider("4. In-depth Analysis", 0, 100, 20, format="%d%%")
            phase5 = st.slider("5. Reporting & Presentation", 0, 100, 15, format="%d%%")
            phase6 = st.slider("6. Review & Documentation", 0, 100, 5, format="%d%%")
        
        total = phase1 + phase2 + phase3 + phase4 + phase5 + phase6
        
        if total != 100:
            st.warning(f"⚠️ Total allocation is {total}%. Please adjust to equal 100%.")
        else:
            st.success("✓ Allocation totals 100%")
        
        st.markdown("---")
        st.markdown("### Project Timeline")
        
        phases = [
            ("Problem Definition & Scoping", phase1),
            ("Data Collection & Cleaning", phase2),
            ("Exploratory Analysis", phase3),
            ("In-depth Analysis", phase4),
            ("Reporting & Presentation", phase5),
            ("Review & Documentation", phase6)
        ]
        
        timeline_data = []
        current_week = 0
        for phase_name, pct in phases:
            weeks = (pct / 100) * project_duration
            timeline_data.append({
                "Phase": phase_name,
                "Weeks": f"{weeks:.1f}",
                "Start": f"Week {current_week + 1:.0f}",
                "End": f"Week {current_week + weeks:.0f}"
            })
            current_week += weeks
        
        df_timeline = pd.DataFrame(timeline_data)
        st.dataframe(df_timeline, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Deliverables Checklist")
        
        deliverables = {
            "Problem Definition & Scoping": ["Problem statement document", "Stakeholder requirements", "Success criteria defined"],
            "Data Collection & Cleaning": ["Data sources identified", "Data quality report", "Clean dataset ready"],
            "Exploratory Analysis": ["Summary statistics", "Initial visualizations", "Key patterns identified"],
            "In-depth Analysis": ["Analysis methodology documented", "Statistical tests completed", "Findings validated"],
            "Reporting & Presentation": ["Executive summary", "Detailed report", "Presentation slides"],
            "Review & Documentation": ["Peer review completed", "Documentation finalized", "Lessons learned"]
        }
        
        for phase_name, items in deliverables.items():
            with st.expander(f"📁 {phase_name}"):
                for item in items:
                    st.checkbox(item, key=f"del_{phase_name}_{item}")
        
        st.markdown("---")
        if st.button("📥 Generate Project Plan Summary", type="primary"):
            plan_summary = f"""PROJECT PLAN: {project_name}
========================================
Duration: {project_duration} weeks

PHASE ALLOCATION:
"""
            for phase_name, pct in phases:
                weeks = (pct / 100) * project_duration
                plan_summary += f"- {phase_name}: {pct}% ({weeks:.1f} weeks)\n"
            
            plan_summary += f"""
KEY MILESTONES:
- Week 1: Project kickoff
- Week {int(project_duration * 0.4)}: Data ready for analysis
- Week {int(project_duration * 0.7)}: Analysis complete
- Week {project_duration}: Final delivery

DELIVERABLES:
- Problem statement and scope document
- Data quality and cleaning report
- Analysis report with findings
- Executive presentation
- Project documentation
"""
            st.text_area("Project Plan Summary:", value=plan_summary, height=400)
            st.download_button(
                "Download Project Plan",
                data=plan_summary,
                file_name=f"project_plan_{project_name.lower().replace(' ', '_')}.txt",
                mime="text/plain"
            )
    
    elif playground_tab == "Report Writing Workshop":
        st.subheader("📝 Report Writing Workshop")
        st.markdown("*Practice writing professional analysis reports with proper structure and clarity*")
        st.markdown("---")
        
        report_mode = st.radio(
            "Choose practice mode:",
            ["Executive Summary Builder", "Clarity Rewriter", "Report Structure Planner", "Caption Writer"],
            horizontal=True
        )
        
        if report_mode == "Executive Summary Builder":
            st.markdown("### Executive Summary Builder")
            st.markdown("*Create a concise executive summary from your analysis findings*")
            
            st.markdown("**Enter your analysis details:**")
            
            col1, col2 = st.columns(2)
            with col1:
                main_finding = st.text_area(
                    "Main Finding:",
                    placeholder="e.g., Customer churn increased 25% last quarter",
                    height=80
                )
                root_cause = st.text_area(
                    "Root Cause/Key Insight:",
                    placeholder="e.g., Analysis of 500 surveys found 67% cited slow support response",
                    height=80
                )
            
            with col2:
                business_impact = st.text_input(
                    "Business Impact:",
                    placeholder="e.g., Estimated $200K in lost annual revenue"
                )
                recommendation = st.text_area(
                    "Recommendation:",
                    placeholder="e.g., Implement chat support system ($50K investment)",
                    height=80
                )
            
            audience = st.selectbox(
                "Target Audience:",
                ["C-Suite Executives", "Department Managers", "Technical Team", "External Clients"]
            )
            
            if st.button("📋 Generate Executive Summary", type="primary"):
                if main_finding and recommendation:
                    st.markdown("---")
                    st.markdown("### Your Executive Summary")
                    
                    if audience == "C-Suite Executives":
                        tone = "Focus on business impact and ROI"
                        length = "Ultra-brief (3-5 sentences)"
                    elif audience == "Department Managers":
                        tone = "Balance of impact and actionable details"
                        length = "Brief (5-7 sentences)"
                    elif audience == "Technical Team":
                        tone = "Include methodology context"
                        length = "Moderate detail (7-10 sentences)"
                    else:
                        tone = "Professional, accessible language"
                        length = "Clear and complete (5-8 sentences)"
                    
                    summary = f"""## Executive Summary

**Key Finding:** {main_finding}

**Impact:** {business_impact if business_impact else '[Add business impact]'}

**Analysis Insight:** {root_cause if root_cause else '[Add key insight from analysis]'}

**Recommendation:** {recommendation}

---
*Note: This summary is tailored for {audience}. Tone: {tone}. Recommended length: {length}.*
"""
                    st.markdown(summary)
                    
                    st.download_button(
                        "📥 Download Executive Summary",
                        data=summary,
                        file_name="executive_summary.md",
                        mime="text/markdown"
                    )
                    
                    st.markdown("### Writing Tips for Your Audience:")
                    if audience == "C-Suite Executives":
                        st.info("- Lead with the bottom line\n- Quantify everything\n- Keep to 1 page maximum\n- Focus on decisions, not details")
                    elif audience == "Department Managers":
                        st.info("- Include actionable next steps\n- Show department-level impact\n- Provide timeline expectations\n- Mention resource requirements")
                    elif audience == "Technical Team":
                        st.info("- Can include methodology references\n- Technical terms are acceptable\n- Include data quality notes\n- Reference appendix for details")
                    else:
                        st.info("- Avoid internal jargon\n- Explain technical concepts\n- Focus on value delivered\n- Include clear next steps")
                else:
                    st.warning("Please fill in at least the main finding and recommendation.")
        
        elif report_mode == "Clarity Rewriter":
            st.markdown("### Clarity Rewriter")
            st.markdown("*Practice rewriting complex technical text for non-technical audiences*")
            
            sample_texts = {
                "Statistical finding": "The multivariate regression analysis yielded a statistically significant coefficient (β=0.43, p<0.01) for the marketing expenditure variable, indicating a positive relationship with sales outcomes.",
                "Data quality issue": "The dataset exhibited substantial missing value prevalence (23.7% null rate) concentrated primarily in temporal fields, necessitating imputation via mean substitution methodology.",
                "Correlation analysis": "Pearson correlation coefficient analysis revealed a strong positive correlation (r=0.82) between customer satisfaction metrics and repeat purchase behavior, suggesting potential causative linkages.",
                "Forecasting result": "The ARIMA(2,1,1) model generated forecasts with a MAPE of 8.3%, outperforming the baseline exponential smoothing approach by 2.1 percentage points.",
                "Custom text": ""
            }
            
            selected_text = st.selectbox("Choose a text to rewrite:", list(sample_texts.keys()))
            
            if selected_text == "Custom text":
                original_text = st.text_area(
                    "Enter your technical text:",
                    placeholder="Paste your complex technical text here...",
                    height=100
                )
            else:
                original_text = sample_texts[selected_text]
                st.markdown(f"**Original text:** {original_text}")
            
            user_rewrite = st.text_area(
                "Your simplified version:",
                placeholder="Rewrite the text in plain language...",
                height=100
            )
            
            if st.button("📖 Show Expert Rewrite", type="primary") and original_text:
                st.markdown("---")
                
                expert_rewrites = {
                    "Statistical finding": "Our analysis found that marketing spending has a strong positive effect on sales. For every additional $1,000 spent on marketing, sales increased by approximately $430. This relationship is statistically reliable.",
                    "Data quality issue": "About 24% of the data was missing, mainly in date-related fields. We filled in these gaps using average values to ensure complete analysis.",
                    "Correlation analysis": "We found a strong link between customer satisfaction and repeat purchases. Customers who are more satisfied are significantly more likely to buy again.",
                    "Forecasting result": "Our forecast model predicted sales with 92% accuracy, performing 2% better than our previous method. This gives us reliable predictions for planning.",
                    "Custom text": "Consider: 1) Replace jargon with plain words, 2) Explain what numbers mean practically, 3) Focus on the 'so what?' for the business."
                }
                
                st.markdown("### Expert Rewrite:")
                st.success(expert_rewrites.get(selected_text, expert_rewrites["Custom text"]))
                
                st.markdown("### Rewriting Principles:")
                st.markdown("""
| Technical Term | Plain Language |
|---------------|----------------|
| Statistically significant | Reliable/consistent pattern |
| Correlation | Relationship/link |
| Coefficient | Effect size/impact |
| Null values | Missing data |
| Imputation | Filling in gaps |
| MAPE/RMSE | Accuracy percentage |
""")
        
        elif report_mode == "Report Structure Planner":
            st.markdown("### Report Structure Planner")
            st.markdown("*Plan the sections and content of your analysis report*")
            
            report_type = st.selectbox(
                "What type of report are you writing?",
                ["Client Report", "Executive Summary", "Technical Report", "Ad-hoc Analysis", "Dashboard Report"]
            )
            
            report_structures = {
                "Client Report": {
                    "sections": ["Executive Summary", "Background & Objectives", "Methodology Overview", "Key Findings", "Recommendations", "Next Steps", "Appendix"],
                    "page_range": "5-15 pages",
                    "tips": "Focus on actionable insights. Minimize technical jargon. Include clear recommendations with expected outcomes."
                },
                "Executive Summary": {
                    "sections": ["Key Finding", "Business Impact", "Recommendation", "Next Steps"],
                    "page_range": "1-2 pages",
                    "tips": "Lead with the conclusion. Quantify everything. Maximum 1-2 pages. Support details in appendix only."
                },
                "Technical Report": {
                    "sections": ["Abstract", "Introduction", "Data Sources", "Methodology", "Results", "Discussion", "Limitations", "Conclusions", "References", "Appendix"],
                    "page_range": "10-30 pages",
                    "tips": "Full methodology documentation. Include code/query references. Reproducibility is key."
                },
                "Ad-hoc Analysis": {
                    "sections": ["Question/Request", "Approach", "Findings", "Answer/Recommendation"],
                    "page_range": "2-5 pages",
                    "tips": "Direct answer to the question asked. Quick turnaround expected. Keep focused."
                },
                "Dashboard Report": {
                    "sections": ["KPI Summary", "Trends", "Alerts/Exceptions", "Actions Needed"],
                    "page_range": "1-3 pages",
                    "tips": "Visual-heavy. Consistent format for regular updates. Clear RAG status indicators."
                }
            }
            
            structure = report_structures[report_type]
            
            st.markdown(f"### {report_type} Structure")
            st.caption(f"Typical length: {structure['page_range']}")
            
            st.markdown("**Recommended Sections:**")
            for i, section in enumerate(structure["sections"], 1):
                st.markdown(f"{i}. {section}")
            
            st.info(f"**Tips:** {structure['tips']}")
            
            st.markdown("---")
            st.markdown("### Plan Your Content")
            
            content_plan = {}
            for section in structure["sections"]:
                content_plan[section] = st.text_input(
                    f"{section}:",
                    placeholder=f"Brief notes for {section}...",
                    key=f"plan_{section}"
                )
            
            if st.button("📥 Generate Report Outline", type="primary"):
                outline = f"""# {report_type} Outline

Type: {report_type}
Target Length: {structure['page_range']}

## Sections

"""
                for section, notes in content_plan.items():
                    outline += f"### {section}\n"
                    outline += f"{notes if notes else '[Add content notes]'}\n\n"
                
                outline += f"""---
## Writing Tips
{structure['tips']}
"""
                
                st.text_area("Your Report Outline:", value=outline, height=400)
                st.download_button(
                    "Download Outline",
                    data=outline,
                    file_name=f"{report_type.lower().replace(' ', '_')}_outline.md",
                    mime="text/markdown"
                )
        
        elif report_mode == "Caption Writer":
            st.markdown("### Caption Writer")
            st.markdown("*Practice writing professional captions for figures and tables*")
            
            visual_type = st.selectbox(
                "What type of visual are you captioning?",
                ["Bar Chart", "Line Chart", "Pie Chart", "Table", "Scatter Plot", "Dashboard Screenshot"]
            )
            
            col1, col2 = st.columns(2)
            with col1:
                figure_number = st.number_input("Figure/Table Number:", min_value=1, value=1)
                title = st.text_input("Visual Title:", placeholder="e.g., Quarterly Revenue by Region")
            
            with col2:
                key_insight = st.text_input("Key Insight:", placeholder="e.g., North region leads by 15%")
                data_source = st.text_input("Data Source:", placeholder="e.g., Sales Database, Q4 2025")
            
            if st.button("✍️ Generate Caption", type="primary"):
                if title:
                    st.markdown("---")
                    st.markdown("### Generated Captions")
                    
                    prefix = "Figure" if visual_type != "Table" else "Table"
                    
                    brief_caption = f"{prefix} {figure_number}: {title}."
                    
                    standard_caption = f"{prefix} {figure_number}: {title}. {key_insight if key_insight else ''}"
                    if data_source:
                        standard_caption += f" Source: {data_source}."
                    
                    detailed_caption = f"{prefix} {figure_number}: {title}. "
                    if key_insight:
                        detailed_caption += f"Key insight: {key_insight}. "
                    detailed_caption += f"This {visual_type.lower()} illustrates [add interpretation]. "
                    if data_source:
                        detailed_caption += f"Data source: {data_source}."
                    
                    st.markdown("**Brief Caption:**")
                    st.code(brief_caption)
                    
                    st.markdown("**Standard Caption (Recommended):**")
                    st.code(standard_caption)
                    
                    st.markdown("**Detailed Caption:**")
                    st.code(detailed_caption)
                    
                    st.markdown("### Caption Best Practices:")
                    st.markdown("""
- ✓ Always include figure/table number
- ✓ Use descriptive title (not just "Revenue")
- ✓ State the key insight readers should take away
- ✓ Include data source for credibility
- ✓ Keep captions concise but complete
- ✓ Place below figures, above tables
""")
                else:
                    st.warning("Please enter at least a title for your visual.")
    
    elif playground_tab == "Exam Project Toolkit":
        st.subheader("🎓 Exam Project Toolkit")
        st.markdown("*Practice planning and executing your comprehensive data analysis project*")
        st.markdown("---")
        
        toolkit_mode = st.radio(
            "Choose practice mode:",
            ["Problem Statement Builder", "Project Scope Planner", "Quality Self-Assessment", "Presentation Planner"],
            horizontal=True
        )
        
        if toolkit_mode == "Problem Statement Builder":
            st.markdown("### Problem Statement Builder")
            st.markdown("*Craft a clear, professional problem statement for your project*")
            
            col1, col2 = st.columns(2)
            with col1:
                organization = st.text_input(
                    "Organization/Client:",
                    placeholder="e.g., Oslo Retail Group, Local Healthcare Clinic"
                )
                topic = st.text_input(
                    "What needs to be understood?",
                    placeholder="e.g., customer churn patterns, inventory inefficiencies"
                )
            
            with col2:
                action = st.text_input(
                    "Purpose (in order to...):",
                    placeholder="e.g., improve retention strategies, reduce waste"
                )
                data_sources = st.text_input(
                    "Data to be examined:",
                    placeholder="e.g., 2 years of customer data, daily sales records"
                )
            
            deliverable = st.text_input(
                "Deliverable:",
                placeholder="e.g., recommendation report, dashboard, presentation"
            )
            deadline = st.text_input(
                "Deadline:",
                placeholder="e.g., March 15, 2026"
            )
            
            if st.button("📝 Generate Problem Statement", type="primary"):
                if organization and topic and action:
                    st.markdown("---")
                    st.markdown("### Your Problem Statement")
                    
                    problem_statement = f"""**{organization}** needs to understand **{topic}** in order to **{action}**. 

This analysis will examine **{data_sources if data_sources else '[specify data sources]'}** to provide **{deliverable if deliverable else '[specify deliverable]'}** by **{deadline if deadline else '[specify deadline]'}**."""
                    
                    st.success(problem_statement)
                    
                    st.markdown("### Quality Check:")
                    checks = [
                        ("Organization/stakeholder identified", bool(organization)),
                        ("Clear question to answer", bool(topic)),
                        ("Business purpose stated", bool(action)),
                        ("Data sources specified", bool(data_sources)),
                        ("Deliverable defined", bool(deliverable)),
                        ("Deadline included", bool(deadline))
                    ]
                    
                    for check, passed in checks:
                        if passed:
                            st.markdown(f"✅ {check}")
                        else:
                            st.markdown(f"⚠️ {check} - *add this for completeness*")
                    
                    st.download_button(
                        "📥 Download Problem Statement",
                        data=problem_statement,
                        file_name="problem_statement.md",
                        mime="text/markdown"
                    )
                else:
                    st.warning("Please fill in organization, topic, and purpose at minimum.")
        
        elif toolkit_mode == "Project Scope Planner":
            st.markdown("### Project Scope Planner")
            st.markdown("*Define clear boundaries for your project*")
            
            st.markdown("**Project Duration:**")
            project_weeks = st.slider("Total project time (weeks):", 4, 16, 10, key="scope_project_weeks")
            
            st.markdown("---")
            st.markdown("### In Scope vs Out of Scope")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**✅ In Scope** (what you WILL do)")
                in_scope_1 = st.text_input("Question 1:", placeholder="e.g., Analyze sales trends for 2024-2025", key="scope_in_1")
                in_scope_2 = st.text_input("Question 2:", placeholder="e.g., Identify top-performing products", key="scope_in_2")
                in_scope_3 = st.text_input("Question 3:", placeholder="e.g., Create visualization dashboard", key="scope_in_3")
            
            with col2:
                st.markdown("**❌ Out of Scope** (explicitly excluded)")
                out_scope_1 = st.text_input("Excluded 1:", placeholder="e.g., Competitor analysis", key="scope_out_1")
                out_scope_2 = st.text_input("Excluded 2:", placeholder="e.g., Predictive modeling", key="scope_out_2")
                out_scope_3 = st.text_input("Excluded 3:", placeholder="e.g., Real-time data integration", key="scope_out_3")
            
            st.markdown("---")
            st.markdown("### Time Allocation")
            
            phases = {
                "Planning & Research": st.slider("Planning & Research %:", 10, 30, 20, key="scope_phase_1"),
                "Data Collection & Cleaning": st.slider("Data Collection & Cleaning %:", 15, 35, 25, key="scope_phase_2"),
                "Analysis & Exploration": st.slider("Analysis & Exploration %:", 20, 40, 25, key="scope_phase_3"),
                "Reporting & Visualization": st.slider("Reporting & Visualization %:", 15, 30, 20, key="scope_phase_4"),
                "Review & Finalization": st.slider("Review & Finalization %:", 5, 20, 10, key="scope_phase_5")
            }
            
            total_pct = sum(phases.values())
            if total_pct != 100:
                st.warning(f"Total allocation is {total_pct}%. Adjust to equal 100%.")
            else:
                st.success("✅ Time allocation totals 100%")
            
            if st.button("📊 Generate Project Scope Document", type="primary"):
                st.markdown("---")
                st.markdown("### Project Scope Document")
                
                scope_doc = f"""# Project Scope Document

## Duration
**{project_weeks} weeks**

## In Scope
"""
                for item in [in_scope_1, in_scope_2, in_scope_3]:
                    if item:
                        scope_doc += f"- {item}\n"
                
                scope_doc += """
## Out of Scope
"""
                for item in [out_scope_1, out_scope_2, out_scope_3]:
                    if item:
                        scope_doc += f"- {item}\n"
                
                scope_doc += """
## Timeline
"""
                current_week = 1
                for phase, pct in phases.items():
                    weeks = (pct / 100) * project_weeks
                    end_week = current_week + weeks - 1
                    scope_doc += f"- **{phase}**: Weeks {current_week:.0f}-{end_week:.0f} ({pct}%)\n"
                    current_week = end_week + 1
                
                st.text_area("Scope Document:", value=scope_doc, height=400)
                st.download_button(
                    "Download Scope Document",
                    data=scope_doc,
                    file_name="project_scope.md",
                    mime="text/markdown"
                )
        
        elif toolkit_mode == "Quality Self-Assessment":
            st.markdown("### Quality Self-Assessment")
            st.markdown("*Evaluate your project against professional standards before submission*")
            
            st.markdown("Rate each area honestly (1-5):")
            st.caption("1=Not done, 2=Partial, 3=Adequate, 4=Good, 5=Excellent")
            
            categories = {
                "Project Execution": [
                    "Problem clearly defined and scoped",
                    "Data sourced ethically with documentation",
                    "Methodology appropriate and documented",
                    "Analysis thorough and validated"
                ],
                "Technical Quality": [
                    "Data cleaned properly with decisions documented",
                    "Calculations verified and accurate",
                    "Code/formulas organized and commented",
                    "Process is reproducible"
                ],
                "Report Quality": [
                    "Executive summary is clear and actionable",
                    "Report has logical structure",
                    "Visualizations are accessible and labeled",
                    "Recommendations are specific and supported"
                ],
                "Presentation Quality": [
                    "Within time limit",
                    "Key points are clear",
                    "Visuals are readable from distance",
                    "Prepared for likely questions"
                ]
            }
            
            scores = {}
            for category, items in categories.items():
                st.markdown(f"**{category}**")
                for i, item in enumerate(items):
                    scores[item] = st.slider(item, 1, 5, 3, key=f"qa_{category}_{i}")
            
            if st.button("📋 Generate Assessment Report", type="primary"):
                st.markdown("---")
                st.markdown("### Your Assessment Results")
                
                total_score = sum(scores.values())
                max_score = len(scores) * 5
                percentage = (total_score / max_score) * 100
                
                if percentage >= 80:
                    st.success(f"Overall Score: {total_score}/{max_score} ({percentage:.0f}%) - **Ready to submit!**")
                elif percentage >= 60:
                    st.warning(f"Overall Score: {total_score}/{max_score} ({percentage:.0f}%) - **Good progress, address weak areas**")
                else:
                    st.error(f"Overall Score: {total_score}/{max_score} ({percentage:.0f}%) - **Needs more work**")
                
                st.markdown("### Areas to Improve:")
                weak_areas = [item for item, score in scores.items() if score < 3]
                if weak_areas:
                    for area in weak_areas:
                        st.markdown(f"- ⚠️ {area}")
                else:
                    st.markdown("No critical areas identified - great work!")
                
                st.markdown("### Strengths:")
                strong_areas = [item for item, score in scores.items() if score >= 4]
                if strong_areas:
                    for area in strong_areas:
                        st.markdown(f"- ✅ {area}")
        
        elif toolkit_mode == "Presentation Planner":
            st.markdown("### Presentation Planner")
            st.markdown("*Plan your project presentation structure*")
            
            total_time = st.slider("Total presentation time (minutes):", 10, 30, 18, key="exam_pres_total_time")
            
            sections = {
                "Opening": {"default": 2, "tip": "Introduce yourself, project, hook with key finding"},
                "Context": {"default": 3, "tip": "Business background, why it matters, objectives"},
                "Methodology": {"default": 3, "tip": "Data sources, tools used, key decisions"},
                "Findings": {"default": 5, "tip": "Main results with visuals, patterns identified"},
                "Recommendations": {"default": 3, "tip": "Actionable suggestions, expected impact"},
                "Conclusion": {"default": 2, "tip": "Summary, lessons learned, Q&A invitation"}
            }
            
            st.markdown("### Time Allocation per Section")
            allocations = {}
            for section, info in sections.items():
                col1, col2 = st.columns([1, 2])
                with col1:
                    allocations[section] = st.number_input(
                        f"{section} (min):",
                        min_value=1,
                        max_value=15,
                        value=info["default"],
                        key=f"pres_{section}"
                    )
                with col2:
                    st.caption(info["tip"])
            
            allocated = sum(allocations.values())
            if allocated != total_time:
                st.warning(f"Allocated {allocated} minutes, but total is {total_time} minutes. Adjust to match.")
            else:
                st.success(f"✅ Time allocation matches {total_time} minutes")
            
            st.markdown("---")
            st.markdown("### Key Points per Section")
            
            key_points = {}
            for section in sections.keys():
                key_points[section] = st.text_area(
                    f"{section} - Main points:",
                    placeholder=f"What will you cover in the {section.lower()} section?",
                    height=60,
                    key=f"kp_{section}"
                )
            
            if st.button("📊 Generate Presentation Outline", type="primary"):
                st.markdown("---")
                st.markdown("### Your Presentation Outline")
                
                outline = f"""# Project Presentation Outline
Total Time: {total_time} minutes

"""
                for section, minutes in allocations.items():
                    outline += f"## {section} ({minutes} min)\n"
                    outline += f"**Tip:** {sections[section]['tip']}\n"
                    if key_points[section]:
                        outline += f"**Your notes:** {key_points[section]}\n"
                    outline += "\n"
                
                outline += """---
## Presentation Tips
- Practice out loud at least 3 times
- Time yourself to ensure you fit the limit
- Have backup slides for anticipated questions
- Speak to the audience, not the slides
- Pause after key findings to let them sink in
"""
                
                st.text_area("Presentation Outline:", value=outline, height=500)
                st.download_button(
                    "Download Outline",
                    data=outline,
                    file_name="presentation_outline.md",
                    mime="text/markdown"
                )

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
