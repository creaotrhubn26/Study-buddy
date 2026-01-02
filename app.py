import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataanalytiker Studie-app",
    page_icon="📊",
    layout="wide"
)

# Course data
courses_data = [
    {"code": "FI1BBDF05", "name": "Grunnleggende dataanalyse", "type": "Kjernekurs", "credits": 5, "semester": "2025 H"},
    {"code": "FI1BBSF05", "name": "Grunnleggende om regneark", "type": "Kjernekurs", "credits": 5, "semester": "2025 H"},
    {"code": "FI1BBDD75", "name": "Datadrevet beslutningstaking", "type": "Kjernekurs", "credits": 7.5, "semester": "2025 H"},
    {"code": "FI1BBST05", "name": "Statistiske verktøy", "type": "Kjernekurs", "credits": 5, "semester": "2025 H"},
    {"code": "FI1BBP175", "name": "Semesterprosjekt 1", "type": "Kjernekurs", "credits": 7.5, "semester": "2025 H"},
    {"code": "FI1BBEO10", "name": "Evaluering av resultater", "type": "Kjernekurs", "credits": 10, "semester": "2026 V"},
    {"code": "FI1BBDV75", "name": "Datavisualisering", "type": "Kjernekurs", "credits": 7.5, "semester": "2026 V"},
    {"code": "FI1BBAR05", "name": "Analyserapportering", "type": "Kjernekurs", "credits": 5, "semester": "2026 V"},
    {"code": "FI1BBP275", "name": "Eksamensprosjekt 1", "type": "Kjernekurs", "credits": 7.5, "semester": "2026 V"},
    {"code": "FI2BCDC75", "name": "Databaser og skytjenester", "type": "Kjernekurs", "credits": 7.5, "semester": "2026 H"},
    {"code": "FI2BCPP10", "name": "Grunnleggende programmering", "type": "Kjernekurs", "credits": 10, "semester": "2026 H"},
    {"code": "FI2BCPA05", "name": "Programmatisk dataanalyse", "type": "Kjernekurs", "credits": 5, "semester": "2026 H"},
    {"code": "FI2BCP175", "name": "Semesterprosjekt 2", "type": "Kjernekurs", "credits": 7.5, "semester": "2026 H"},
    {"code": "FI2BCIT75", "name": "Industriverktøy", "type": "Kjernekurs", "credits": 7.5, "semester": "2027 V"},
    {"code": "FI2BCCT05", "name": "Kritisk datatenkning", "type": "Kjernekurs", "credits": 5, "semester": "2027 V"},
    {"code": "FI2BCBD05", "name": "Stordata og avanserte emner", "type": "Kjernekurs", "credits": 5, "semester": "2027 V"},
    {"code": "FI2BCID05", "name": "Interaktive dashbord", "type": "Kjernekurs", "credits": 5, "semester": "2027 V"},
    {"code": "FI2BCP275", "name": "Eksamensprosjekt 2", "type": "Kjernekurs", "credits": 7.5, "semester": "2027 V"},
]

# Learning outcomes
knowledge_outcomes = [
    "Konsepter og teorier innen dataanalyse",
    "Prosesser og verktøy for dataanalyse",
    "Databaser, skytjenester og native skyverktøy",
    "Programmering og programmatisk dataanalyse",
    "Prosesser og verktøy for datavisualisering",
    "Metoder for problemidentifisering og oppdagelse av datafeil",
    "Rapportskrivingsmetoder for klar kommunikasjon",
    "Virkelige situasjoner for beslutningstaking",
    "Bransjerelevante verktøy for feltdataanalyse",
    "Stordata og datavitenskap konsepter",
    "Dashbordteori og universelle designprinsipper",
    "Regelverk, dataanalysens livssyklus og GDPR",
]

skills_outcomes = [
    "Anvende datamodellresultater på forretningsproblemer",
    "Datainnsamling og -rensing fra ulike kilder",
    "Relevante verktøy og teknikker for dataanalyse",
    "Generere og visualisere data gjennom rapporter",
    "Forklare yrkesvalg innen dataanalyse",
    "Reflektere over egen yrkespraksis",
    "Finne informasjon om dataanalyseteknikker",
    "Identifisere arbeidsflytproblemer",
    "Samhandle med store datakilder",
]

competence_outcomes = [
    "Forstå etiske prinsipper for data",
    "Planlegge og utføre dataanalyseoppgaver",
    "Utveksle synspunkter med andre analytikere",
    "Bidra til kvalitetssikring og optimalisering",
    "Bidra til datasikkerhet",
    "Utvikle produkter av relevans for dataanalyse",
]

# Initialize session state for progress tracking
if 'completed_courses' not in st.session_state:
    st.session_state.completed_courses = []
if 'knowledge_progress' not in st.session_state:
    st.session_state.knowledge_progress = [False] * len(knowledge_outcomes)
if 'skills_progress' not in st.session_state:
    st.session_state.skills_progress = [False] * len(skills_outcomes)
if 'competence_progress' not in st.session_state:
    st.session_state.competence_progress = [False] * len(competence_outcomes)

# Sidebar navigation
st.sidebar.title("📊 Navigasjon")
page = st.sidebar.radio(
    "Velg side:",
    ["Oversikt", "Kursplan", "Fremdrift", "Læringsutbytte", "Om programmet"]
)

# Main content
if page == "Oversikt":
    st.title("🎓 Dataanalytiker 2 - Studie-app")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_credits = sum(c["credits"] for c in courses_data)
    completed_credits = sum(c["credits"] for c in courses_data if c["code"] in st.session_state.completed_courses)
    
    with col1:
        st.metric("Totalt studiepoeng", f"{int(total_credits)}")
    with col2:
        st.metric("Fullført", f"{completed_credits:.1f}")
    with col3:
        st.metric("Gjenstående", f"{total_credits - completed_credits:.1f}")
    with col4:
        progress_pct = (completed_credits / total_credits * 100) if total_credits > 0 else 0
        st.metric("Fremgang", f"{progress_pct:.0f}%")
    
    st.markdown("---")
    st.subheader("📅 Studieløp")
    
    semesters = ["2025 H", "2026 V", "2026 H", "2027 V"]
    semester_names = {
        "2025 H": "Høst 2025",
        "2026 V": "Vår 2026", 
        "2026 H": "Høst 2026",
        "2027 V": "Vår 2027"
    }
    
    cols = st.columns(4)
    for i, sem in enumerate(semesters):
        with cols[i]:
            st.markdown(f"**{semester_names[sem]}**")
            sem_courses = [c for c in courses_data if c["semester"] == sem]
            sem_credits = sum(c["credits"] for c in sem_courses)
            st.caption(f"{sem_credits:.0f} studiepoeng")
            
            for course in sem_courses:
                is_completed = course["code"] in st.session_state.completed_courses
                status = "✅" if is_completed else "📚"
                st.markdown(f"{status} {course['name']}")
    
    st.markdown("---")
    st.subheader("🔗 Nyttige lenker")
    st.markdown("[📖 Studiekatalog](https://studiekatalog.edutorium.no/voc/en/programme/PDAN/2025-autumn)")

elif page == "Kursplan":
    st.title("📚 Kursplan")
    st.markdown("---")
    
    df = pd.DataFrame(courses_data)
    df.columns = ["Kurskode", "Kursnavn", "Type", "Studiepoeng", "Semester"]
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        semester_filter = st.multiselect(
            "Filtrer etter semester:",
            options=["2025 H", "2026 V", "2026 H", "2027 V"],
            default=[]
        )
    with col2:
        search = st.text_input("Søk etter kurs:", "")
    
    filtered_df = df.copy()
    if semester_filter:
        filtered_df = filtered_df[filtered_df["Semester"].isin(semester_filter)]
    if search:
        filtered_df = filtered_df[
            filtered_df["Kursnavn"].str.lower().str.contains(search.lower()) |
            filtered_df["Kurskode"].str.lower().str.contains(search.lower())
        ]
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.subheader("📊 Studiepoeng per semester")
    
    semester_credits = df.groupby("Semester")["Studiepoeng"].sum().reset_index()
    semester_order = ["2025 H", "2026 V", "2026 H", "2027 V"]
    semester_credits["Semester"] = pd.Categorical(semester_credits["Semester"], categories=semester_order, ordered=True)
    semester_credits = semester_credits.sort_values("Semester")
    
    st.bar_chart(semester_credits.set_index("Semester"))

elif page == "Fremdrift":
    st.title("📈 Min fremdrift")
    st.markdown("---")
    
    st.subheader("Marker fullførte kurs")
    
    semesters = ["2025 H", "2026 V", "2026 H", "2027 V"]
    semester_names = {
        "2025 H": "Høst 2025",
        "2026 V": "Vår 2026", 
        "2026 H": "Høst 2026",
        "2027 V": "Vår 2027"
    }
    
    for sem in semesters:
        st.markdown(f"**{semester_names[sem]}**")
        sem_courses = [c for c in courses_data if c["semester"] == sem]
        
        cols = st.columns(2)
        for i, course in enumerate(sem_courses):
            with cols[i % 2]:
                is_checked = st.checkbox(
                    f"{course['name']} ({course['credits']} sp)",
                    value=course["code"] in st.session_state.completed_courses,
                    key=f"course_{course['code']}"
                )
                if is_checked and course["code"] not in st.session_state.completed_courses:
                    st.session_state.completed_courses.append(course["code"])
                elif not is_checked and course["code"] in st.session_state.completed_courses:
                    st.session_state.completed_courses.remove(course["code"])
        
        st.markdown("---")
    
    # Progress summary
    total_credits = sum(c["credits"] for c in courses_data)
    completed_credits = sum(c["credits"] for c in courses_data if c["code"] in st.session_state.completed_courses)
    progress = completed_credits / total_credits if total_credits > 0 else 0
    
    st.subheader("Oppsummering")
    st.progress(progress)
    st.write(f"**{completed_credits:.1f} / {total_credits:.0f} studiepoeng fullført ({progress*100:.0f}%)**")

elif page == "Læringsutbytte":
    st.title("🎯 Læringsutbytte")
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["Kunnskap", "Ferdigheter", "Generell kompetanse"])
    
    with tab1:
        st.subheader("📖 Kunnskap")
        st.markdown("*Etter endt utdanning skal kandidaten ha kunnskap om:*")
        
        for i, outcome in enumerate(knowledge_outcomes):
            checked = st.checkbox(
                outcome,
                value=st.session_state.knowledge_progress[i],
                key=f"knowledge_{i}"
            )
            st.session_state.knowledge_progress[i] = checked
        
        completed = sum(st.session_state.knowledge_progress)
        st.progress(completed / len(knowledge_outcomes))
        st.caption(f"{completed} / {len(knowledge_outcomes)} læringsmål oppnådd")
    
    with tab2:
        st.subheader("🛠️ Ferdigheter")
        st.markdown("*Etter endt utdanning skal kandidaten kunne:*")
        
        for i, outcome in enumerate(skills_outcomes):
            checked = st.checkbox(
                outcome,
                value=st.session_state.skills_progress[i],
                key=f"skills_{i}"
            )
            st.session_state.skills_progress[i] = checked
        
        completed = sum(st.session_state.skills_progress)
        st.progress(completed / len(skills_outcomes))
        st.caption(f"{completed} / {len(skills_outcomes)} læringsmål oppnådd")
    
    with tab3:
        st.subheader("💡 Generell kompetanse")
        st.markdown("*Etter endt utdanning skal kandidaten:*")
        
        for i, outcome in enumerate(competence_outcomes):
            checked = st.checkbox(
                outcome,
                value=st.session_state.competence_progress[i],
                key=f"competence_{i}"
            )
            st.session_state.competence_progress[i] = checked
        
        completed = sum(st.session_state.competence_progress)
        st.progress(completed / len(competence_outcomes))
        st.caption(f"{completed} / {len(competence_outcomes)} læringsmål oppnådd")

elif page == "Om programmet":
    st.title("ℹ️ Om Dataanalytiker-programmet")
    st.markdown("---")
    
    st.markdown("""
    ## Om studiet
    
    Dataanalytikere har en sentral rolle i ethvert moderne bedriftsmiljø. Deres evne til å veilede 
    bedriftsledere til å ta informerte beslutninger ved hjelp av relevant og oppdatert informasjon 
    basert på reelle data gjør dem til et svært ønsket tilskudd til ethvert lederteam.
    
    **Effektiv dataanalyse kan:**
    - Isolere flaskehalser i arbeidsflyten
    - Redusere driftskostnader
    - Løse overordnede problemer
    - Identifisere ineffektive prosesser
    
    ---
    
    ## Programinnhold
    
    Dette programmet kombinerer:
    - 📚 **Teoretisk kunnskap**
    - 🛠️ **Praktiske ferdigheter**
    - 💻 **Teknisk kompetanse**
    
    ### Verktøy du vil lære:
    - Microsoft Excel og Google Regneark
    - Python programmering
    - Databaser og skytjenester
    - Datavisualisering og dashbord
    - Statistiske analyseverktøy
    
    ---
    
    ## Hvem passer programmet for?
    
    - Personer interessert i data fra den virkelige verden
    - De som ønsker å lære grunnleggende dataanalyse fra bunnen av
    - Etablerte fagfolk som ønsker å oppdatere ferdighetene sine
    - Kandidater fra andre felt som vil lære å utnytte data bedre
    
    ---
    
    ## Studiedetaljer
    
    | Detalj | Verdi |
    |--------|-------|
    | Totalt studiepoeng | 120 |
    | Varighet | 2 år |
    | Studiestart | Høst 2025 |
    | Type | Heltidsstudium |
    
    ---
    
    📖 [Se fullstendig studiekatalog](https://studiekatalog.edutorium.no/voc/en/programme/PDAN/2025-autumn)
    """)
