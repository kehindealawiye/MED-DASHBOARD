
import streamlit as st

# Inject custom background and logo
st.markdown("""
    <style>
    .stApp {{
        background-image: url("background.jpg");
        background-size: cover;
        background-position: center;
        color: white;
    }}
    .logo-overlay {{
        position: fixed;
        top: 10px;
        left: 10px;
        width: 60px;
        z-index: 100;
    }}
    </style>
    <img src="logo.png" class="logo-overlay">
""", unsafe_allow_html=True)

st.title("📊 Monitoring & Evaluation Dashboard Suite")
st.subheader("Insightful Dashboards for Data-Driven Governance")

st.markdown("""
Welcome to the official dashboard hub of the **Monitoring and Evaluation Department**,  
**Ministry of Economic Planning and Budget**.

These tools enable real-time tracking, analysis, and reporting on government programmes, projects, and payment certifications — ensuring transparency, performance, and value for public investments.
""")

st.markdown("### 🚀 Available Dashboards")

col1, col2 = st.columns(2)

with col1:
    st.image("background.jpg", caption="Performance Management Dashboard", use_column_width=True)
    st.markdown("🔗 [Open PMR Dashboard](https://pmr-app.streamlit.app/)", unsafe_allow_html=True)

with col2:
    st.image("background.jpg", caption="Medical Programme Data Analyzer", use_column_width=True)
    st.markdown("🔗 [Open Medical Data Analyzer](https://med-data.streamlit.app/)", unsafe_allow_html=True)

st.markdown("### 📌 About the Tools")

st.markdown("""
#### 1. **Performance Management Report (PMR) Dashboard**
This dashboard tracks programme and project performance across Ministries, Departments, and Agencies (MDAs), presenting:
- Real-time performance metrics
- Budget utilization insights
- Sector-based drilldowns
- Export-ready reports for policy and review meetings

#### 2. **Medical Data Analyzer**
An AI-powered dashboard for analysing health survey data:
- Generates charts, summaries, and trends from raw medical field data
- Supports decision-making in public health planning
- Includes built-in statistical tests and interpretation
""")

st.markdown("### 📬 Need Support or Custom Access?")
st.markdown("If you require tailored access or improvements, reach out to the M&E Tech Team at **meplanning@lagosstate.gov.ng**.")

st.markdown("---")
st.caption("© 2025 Monitoring and Evaluation Department, Ministry of Economic Planning and Budget | Powered by Streamlit")
