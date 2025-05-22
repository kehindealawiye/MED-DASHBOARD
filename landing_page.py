import streamlit as st

st.set_page_config(page_title="M&E Dashboard Hub", layout="wide")

# === Background Overlay and Logo ===
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,50,0.85), rgba(0,0,50,0.85)), url("background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
    }
    .logo-overlay {
        position: fixed;
        top: 10px;
        left: 10px;
        width: 60px;
        z-index: 100;
    }
    h1, h2, h3, h4, h5, h6, p, div, span {
        color: white !important;
    }
    </style>
    <img src="logo.png" class="logo-overlay">
""", unsafe_allow_html=True)

# === Tabs ===
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📊 Dashboards", "ℹ️ About"])

# === Home Tab ===
with tab1:
    st.title("📊 Monitoring & Evaluation Dashboard Suite")
    st.subheader("Empowering Data-Driven Governance with Real-Time Insights")

    st.markdown("""
    Welcome to the official dashboard hub of the **Monitoring and Evaluation Department**,  
    **Ministry of Economic Planning and Budget**.

    This hub provides real-time access to insights on government projects — from performance tracking to certification for payments.
    """)

# === Dashboards Tab ===
with tab2:
    st.markdown("## 📈 Available Dashboards")
    st.markdown("Explore the dashboards below:")

    col1, col2 = st.columns(2)

    with col1:
        st.image("pmr_review.jpg", caption="📊 Performance Management Report (PMR) Dashboard", use_container_width=True)
        st.markdown("🔗 [Launch PMR Dashboard](https://pmr-app.streamlit.app/)", unsafe_allow_html=True)

    with col2:
        st.image("cert_preview.jpg", caption="✅ Prepayment Certification Insights Dashboard", use_container_width=True)
        st.markdown("🔗 [Launch Certification Dashboard](https://med-data.streamlit.app/)", unsafe_allow_html=True)

# === About Tab ===
with tab3:
    st.markdown("## ℹ️ About the Dashboards")
    st.markdown("""
    ### 🏛️ Department Overview
    The **Monitoring and Evaluation Department (MED)** operates as a pivotal unit within the Ministry of Economic Planning and Budget (MEPB), Lagos State. 
    Its existence is anchored in the need to institutionalize performance tracking, ensure evidence-based decision-making, and monitor the implementation and impact of Government Programs and Projects across the State.
    The **Monitoring and Evaluation Department** ensures strategic project oversight across Lagos State, focusing on:
    - Timely inspection of capital projects
    - Evaluation of outcomes
    - Transparent certification processes

    ### 📊 Performance Management Report (PMR) Dashboard
    This dashboard tracks:
    - Programme and project output across MDAs
    - Sector-based trends
    - Budget and performance summaries
    - Export-ready reports

    ### ✅ Prepayment Certification Dashboard
    This dashboard analyzes:
    - All capital projects approved for payment
    - Inspection outcomes
    - Certification history by MDA and sector

    ### 📈 Why This Matters
    Data-driven M&E enhances transparency, ensures accountability, and supports planning that delivers impact to citizens.
    """)

st.markdown("---")
st.caption("© 2025 Monitoring and Evaluation Department, Ministry of Economic Planning and Budget | Powered by Streamlit")
