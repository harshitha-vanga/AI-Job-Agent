import streamlit as st
from google import genai


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Job Agent",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🤖 AI Job Agent")
st.write(
    "AI-powered job recommendations based on your resume."
)


# -----------------------------
# Gemini API
# -----------------------------

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)

except Exception:
    st.error(
        "Gemini API key is not configured. "
        "Add GEMINI_API_KEY in Streamlit Secrets."
    )
    st.stop()


# -----------------------------
# Resume Input
# -----------------------------

st.header("📄 Your Resume")

resume = st.text_area(
    "Paste your resume here",
    height=250,
    placeholder="""
Example:

B.Tech Computer Science student specializing in AI & ML.
Skills: Python, SQL, Machine Learning, Pandas, NumPy,
Scikit-learn and Streamlit.

Projects:
AI Study Planner
Smart Diet Planner

Looking for AI/ML, Python Developer,
Data Analyst and Software Developer opportunities.
"""
)


# -----------------------------
# Sample Job Data
# -----------------------------

jobs = [
    {
        "title": "Python Developer Intern",
        "company": "ABC Technologies",
        "location": "Hyderabad",
        "skills": "Python, SQL, APIs",
        "description": "Work on backend applications and APIs using Python and SQL."
    },
    {
        "title": "AI/ML Intern",
        "company": "XYZ AI Labs",
        "location": "Remote",
        "skills": "Python, Machine Learning, Pandas",
        "description": "Work on machine learning projects, data processing and AI applications."
    },
    {
        "title": "Data Analyst Intern",
        "company": "Data Solutions",
        "location": "Bangalore",
        "skills": "Python, SQL, Excel, Data Analytics",
        "description": "Analyze datasets and create reports using Python, SQL and Excel."
    },
    {
        "title": "Full Stack Developer Intern",
        "company": "WebTech",
        "location": "Remote",
        "skills": "Python, HTML, CSS, JavaScript",
        "description": "Develop web applications and work on frontend and backend features."
    },
    {
        "title": "Machine Learning Intern",
        "company": "AI Solutions",
        "location": "Hyderabad",
        "skills": "Python, Machine Learning, Scikit-learn",
        "description": "Build and test machine learning models using Python and Scikit-learn."
    },
    {
        "title": "Junior Python Developer",
        "company": "Software Labs",
        "location": "Remote",
        "skills": "Python, APIs, Git",
        "description": "Develop Python applications and work with APIs and software development tools."
    },
    {
        "title": "Data Science Intern",
        "company": "Analytics Labs",
        "location": "Bangalore",
        "skills": "Python, Pandas, NumPy, Machine Learning",
        "description": "Work with datasets and develop data science solutions using Python."
    },
    {
        "title": "Software Developer Intern",
        "company": "Tech Innovations",
        "location": "Remote",
        "skills": "Python, SQL, Git",
        "description": "Assist in software development projects and database-related tasks."
    },
    {
        "title": "AI Research Intern",
        "company": "Research AI",
        "location": "Remote",
        "skills": "Python, Machine Learning, Research",
        "description": "Assist with AI research projects and machine learning experiments."
    },
    {
        "title": "Python Full Stack Intern",
        "company": "Digital Systems",
        "location": "Hyderabad",
        "skills": "Python, Streamlit, HTML, CSS",
        "description": "Build web applications using Python and frontend technologies."
    }
]


# -----------------------------
# Find Jobs Button
# -----------------------------

if st.button("🔎 Find My Top 10 Jobs", use_container_width=True):

    if not resume.strip():

        st.warning("Please paste your resume first.")

    else:

        job_text = ""

        for index, job in enumerate(jobs, start=1):

            job_text += f"""
JOB {index}
Title: {job['title']}
Company: {job['company']}
Location: {job['location']}
Required Skills: {job['skills']}
Description: {job['description']}
"""


        # -----------------------------
        # AI Prompt
        # -----------------------------

        prompt = f"""
You are an AI Job Matching Agent.

CANDIDATE RESUME:
{resume}

AVAILABLE JOBS:
{job_text}

Analyze every available job against the candidate's resume.

Select the 10 most relevant jobs.

For every recommended job provide:

1. Job Title
2. Company
3. Location
4. Match Percentage
5. Matching Skills
6. Missing Skills
7. Why the job matches
8. Short job summary

Sort the recommendations from highest match percentage
to lowest.

IMPORTANT:
- Only use information provided in the resume and job data.
- Do not invent companies.
- Do not invent application links.
- Keep the explanation concise and professional.
"""


        # -----------------------------
        # Gemini
        # -----------------------------

        with st.spinner("🤖 AI is analyzing the jobs..."):

            try:

                interaction = client.interactions.create(
                    model="gemini-3.5-flash",
                    input=prompt
                )

                result = interaction.output_text

            except Exception as e:

                st.error(f"AI Error: {e}")
                st.stop()


        # -----------------------------
        # Results
        # -----------------------------

        st.success("✅ Job analysis completed!")

        st.header("🌟 Top 10 Job Recommendations")

        st.markdown(result)


# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.caption(
    "AI Job Agent • Resume-based job matching powered by Gemini"
)
