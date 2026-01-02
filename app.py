import streamlit as st
import pandas as pd
from openai import OpenAI
import os

st.set_page_config(
    page_title="Data Analyst Study App",
    page_icon="📊",
    layout="wide"
)

client = OpenAI(
    api_key=os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY"),
    base_url=os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL")
)

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

if 'completed_courses' not in st.session_state:
    st.session_state.completed_courses = []
if 'knowledge_progress' not in st.session_state:
    st.session_state.knowledge_progress = [False] * len(knowledge_outcomes)
if 'skills_progress' not in st.session_state:
    st.session_state.skills_progress = [False] * len(skills_outcomes)
if 'competence_progress' not in st.session_state:
    st.session_state.competence_progress = [False] * len(competence_outcomes)
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = ""
if 'feedback' not in st.session_state:
    st.session_state.feedback = None

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

def explain_topic(topic, course_name):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an educational assistant explaining topics for a Data Analyst program. Be clear, practical, and give examples."},
                {"role": "user", "content": f"Explain this topic from the course '{course_name}' in simple terms with a practical example: '{topic}'. Keep it to 4-5 sentences."}
            ],
            max_tokens=250
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Select page:",
    ["Overview", "Course Plan", "Learn & Practice", "Progress", "Learning Outcomes", "About"]
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
    st.subheader("🔗 Useful Links")
    st.markdown("[📖 Study Catalog](https://studiekatalog.edutorium.no/voc/en/programme/PDAN/2025-autumn)")

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
    
    tab1, tab2, tab3 = st.tabs(["Course Content", "Practice Questions", "Topic Explorer"])
    
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
                st.markdown(f"- {item}")
        
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
    
    with tab3:
        st.subheader("🔍 Topic Explorer")
        st.markdown("Click on any topic to get a detailed explanation.")
        
        all_topics = course['knowledge'] + course['skills'] + course['competence']
        
        selected_topic = st.selectbox("Select a topic to explore:", options=all_topics)
        
        if st.button("Explain This Topic"):
            with st.spinner("Generating explanation..."):
                explanation = explain_topic(selected_topic, course['name'])
                st.info(explanation)

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
