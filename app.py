import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Analyst Study App",
    page_icon="📊",
    layout="wide"
)

courses_data = [
    {"code": "FI1BBDF05", "name": "Fundamentals of Data Analysis", "type": "Core Course", "credits": 5, "semester": "2025 Spring"},
    {"code": "FI1BBSF05", "name": "Spreadsheet Fundamentals", "type": "Core Course", "credits": 5, "semester": "2025 Spring"},
    {"code": "FI1BBDD75", "name": "Data-Driven Decision Making", "type": "Core Course", "credits": 7.5, "semester": "2025 Spring"},
    {"code": "FI1BBST05", "name": "Statistical Tools", "type": "Core Course", "credits": 5, "semester": "2025 Spring"},
    {"code": "FI1BBP175", "name": "Semester Project 1", "type": "Core Course", "credits": 7.5, "semester": "2025 Spring"},
    {"code": "FI1BBEO10", "name": "Evaluating Outcomes", "type": "Core Course", "credits": 10, "semester": "2025 Fall"},
    {"code": "FI1BBDV75", "name": "Data Visualization", "type": "Core Course", "credits": 7.5, "semester": "2025 Fall"},
    {"code": "FI1BBAR05", "name": "Analysis Reporting", "type": "Core Course", "credits": 5, "semester": "2025 Fall"},
    {"code": "FI1BBP275", "name": "Exam Project 1", "type": "Core Course", "credits": 7.5, "semester": "2025 Fall"},
    {"code": "FI2BCDC75", "name": "Databases and Cloud Services", "type": "Core Course", "credits": 7.5, "semester": "2026 Spring"},
    {"code": "FI2BCPP10", "name": "Programming Principles", "type": "Core Course", "credits": 10, "semester": "2026 Spring"},
    {"code": "FI2BCPA05", "name": "Programmatic Data Analysis", "type": "Core Course", "credits": 5, "semester": "2026 Spring"},
    {"code": "FI2BCP175", "name": "Semester Project 2", "type": "Core Course", "credits": 7.5, "semester": "2026 Spring"},
    {"code": "FI2BCIT75", "name": "Industry Tools", "type": "Core Course", "credits": 7.5, "semester": "2026 Fall"},
    {"code": "FI2BCCT05", "name": "Critical Data Thinking", "type": "Core Course", "credits": 5, "semester": "2026 Fall"},
    {"code": "FI2BCBD05", "name": "Big Data and Advanced Topics", "type": "Core Course", "credits": 5, "semester": "2026 Fall"},
    {"code": "FI2BCID05", "name": "Interactive Dashboards", "type": "Core Course", "credits": 5, "semester": "2026 Fall"},
    {"code": "FI2BCP275", "name": "Exam Project 2", "type": "Core Course", "credits": 7.5, "semester": "2026 Fall"},
]

knowledge_outcomes = [
    "Concepts and theories used in data analysis",
    "Processes and tools used for data analysis",
    "Databases, cloud services and native cloud tools",
    "Programming and programmatic data analysis",
    "Processes and tools for data visualization",
    "Methods for problem identification and data error discovery",
    "Report writing methods for clear communication",
    "Real-world situations to guide decision making",
    "Industry-relevant tools for field data analysis",
    "Big data and data science concepts",
    "Dashboard theory and universal design principles",
    "Regulations, data analysis lifecycle and GDPR",
]

skills_outcomes = [
    "Apply data model results to business problems",
    "Data collection and cleaning from various sources",
    "Relevant tools and techniques for data analysis",
    "Generate and visualize data through reports",
    "Explain career choices in data analysis",
    "Reflect on own professional practice",
    "Find information about data analysis techniques",
    "Identify workflow problems",
    "Interact with large data sources",
]

competence_outcomes = [
    "Understand ethical principles for data",
    "Plan and execute data analysis tasks",
    "Exchange views with other analysts",
    "Contribute to quality assurance and optimization",
    "Contribute to data security",
    "Develop products of relevance to data analysis",
]

if 'completed_courses' not in st.session_state:
    st.session_state.completed_courses = []
if 'knowledge_progress' not in st.session_state:
    st.session_state.knowledge_progress = [False] * len(knowledge_outcomes)
if 'skills_progress' not in st.session_state:
    st.session_state.skills_progress = [False] * len(skills_outcomes)
if 'competence_progress' not in st.session_state:
    st.session_state.competence_progress = [False] * len(competence_outcomes)

st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Select page:",
    ["Overview", "Course Plan", "Progress", "Learning Outcomes", "About"]
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
    
    df = pd.DataFrame(courses_data)
    df.columns = ["Course Code", "Course Name", "Type", "Credits", "Semester"]
    
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
            filtered_df["Course Name"].str.lower().str.contains(search.lower()) |
            filtered_df["Course Code"].str.lower().str.contains(search.lower())
        ]
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.subheader("📊 Credits per Semester")
    
    semester_credits = df.groupby("Semester")["Credits"].sum().reset_index()
    semester_order = ["2025 Spring", "2025 Fall", "2026 Spring", "2026 Fall"]
    semester_credits["Semester"] = pd.Categorical(semester_credits["Semester"], categories=semester_order, ordered=True)
    semester_credits = semester_credits.sort_values("Semester")
    
    st.bar_chart(semester_credits.set_index("Semester"))

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
    st.title("🎯 Learning Outcomes")
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["Knowledge", "Skills", "General Competence"])
    
    with tab1:
        st.subheader("📖 Knowledge")
        st.markdown("*After completing the program, the candidate should have knowledge of:*")
        
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
        st.markdown("*After completing the program, the candidate should be able to:*")
        
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
        st.markdown("*After completing the program, the candidate should:*")
        
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
    ## About the Program
    
    Data analysts play a central role in any modern business environment. Their ability to guide 
    business leaders to make informed decisions using relevant and up-to-date information 
    based on real data makes them a highly sought-after addition to any leadership team.
    
    **Effective data analysis can:**
    - Isolate bottlenecks in workflows
    - Reduce operating costs
    - Solve overarching problems
    - Identify ineffective processes
    
    ---
    
    ## Program Content
    
    This program combines:
    - 📚 **Theoretical knowledge**
    - 🛠️ **Practical skills**
    - 💻 **Technical competence**
    
    ### Tools you will learn:
    - Microsoft Excel and Google Sheets
    - Python programming
    - Databases and cloud services
    - Data visualization and dashboards
    - Statistical analysis tools
    
    ---
    
    ## Who is this program for?
    
    - People interested in real-world data
    - Those who want to learn basic data analysis from scratch
    - Established professionals who want to update their skills
    - Candidates from other fields who want to leverage data better
    
    ---
    
    ## Study Details
    
    | Detail | Value |
    |--------|-------|
    | Total Credits | 120 |
    | Duration | 2 years |
    | Study Start | Spring 2025 |
    | Type | Full-time study |
    
    ---
    
    📖 [View full study catalog](https://studiekatalog.edutorium.no/voc/en/programme/PDAN/2025-autumn)
    """)
