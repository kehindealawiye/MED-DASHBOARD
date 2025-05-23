import streamlit as st
import os
import shutil
import base64
from PIL import Image

# Encode logo as base64
with open(logo_png, "rb") as img_file:
    logo_base64 = base64.b64encode(img_file.read()).decode("utf-8")

# === Streamlit App ===
st.set_page_config(page_title="M&E Dashboard Hub", layout="wide")

# === Page Styling and Logo Overlay ===
st.markdown(f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,50,0.85), rgba(0,0,50,0.85)), url("background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
    }}
    .logo-overlay {{
        position: fixed;
        top: 10px;
        left: 10px;
        width: 60px;
        z-index: 100;
    }}
    h1, h2, h3, h4, h5, h6, p, div, span {{
        color: white !important;
    }}
    .block-container {{
        padding-top: 6rem;
    }}
    </style>
    <img src="data:image/png;base64,{logo_base64}" class="logo-overlay">
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

    # Check image presence (for debugging)
    if os.path.exists("pmr_preview.jpg") and os.path.exists("cert_preview.jpg"):
        col1, col2 = st.columns(2)

        with col1:
            st.image("pmr_preview.jpg", caption="📊 Performance Management Report (PMR) Dashboard", use_container_width=True)
            st.markdown("🔗 [Launch PMR Dashboard](https://pmr-app.streamlit.app/)", unsafe_allow_html=True)

        with col2:
            st.image("cert_preview.jpg", caption="✅ Prepayment Certification Insights Dashboard", use_container_width=True)
            st.markdown("🔗 [Launch Certification Dashboard](https://med-data.streamlit.app/)", unsafe_allow_html=True)
    else:
        st.error("Preview images not found. Please confirm pmr_preview.jpg and cert_preview.jpg exist in the same folder.")

# === About Tab ===
with tab3:
    st.markdown("## ℹ️ About the Dashboards")
    st.markdown("""
    ### 🏛️ Department Overview
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

    ### 🎯 Purpose
    These tools enhance transparency, accountability, and strategic decision-making across all government project workflows.
    """)

# === Footer ===
st.markdown("---")
st.caption("© 2025 Monitoring and Evaluation Department, Ministry of Economic Planning and Budget | Powered by Streamlit")
