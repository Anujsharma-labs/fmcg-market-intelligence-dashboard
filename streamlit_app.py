import streamlit as st
from pipeline import run_pipeline

st.set_page_config(
    page_title="FMCG Intelligence Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown("""
<style>

/* Main Background */

.stApp{
background:linear-gradient(135deg,#050505,#101010,#191919);
}

/* Padding */

.block-container{
padding-top:2rem;
padding-bottom:2rem;
padding-left:3rem;
padding-right:3rem;
}

/* Hide Streamlit Branding */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Titles */

h1,h2,h3{
color:white;
}

/* Paragraph */

p{
color:#d3d3d3;
}

/* Button */

.stButton>button{
width:100%;
height:3.4em;
background:#E50914;
color:white;
font-size:18px;
font-weight:bold;
border:none;
border-radius:12px;
transition:0.3s;
}

.stButton>button:hover{

background:#B00000;

transform:scale(1.02);

box-shadow:0px 0px 20px rgba(229,9,20,.4);

}

/* Metric Cards */

.metric-card{

background:rgba(255,255,255,.05);

padding:20px;

border-radius:18px;

border:1px solid rgba(229,9,20,.25);

backdrop-filter:blur(12px);

text-align:center;

}

.footer{

text-align:center;

color:gray;

padding-top:40px;

}

</style>
""",unsafe_allow_html=True)




st.markdown("""
<div style="text-align:center; padding:30px 0px;">

<h1 style="color:white;font-size:52px;">
📊 FMCG Intelligence Hub
</h1>

<p style="color:#cfcfcf;font-size:22px;">
AI-Powered Market Intelligence & Newsletter Generator
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.markdown("## ⚙️ Dashboard Settings")

    article_count = st.slider(
        "Number of Articles",
        min_value=5,
        max_value=100,
        value=20,
        step=5
    )

    st.divider()

    st.markdown("### 🤖 AI Model")
    st.success("Gemini 3.5 Flash")

    st.markdown("### 📰 News Source")
    st.info("NewsAPI")

    st.divider()

    st.markdown("### 👨‍💻 Developer")

    st.markdown("""
**Anuj Sharma**

Machine Learning Engineer

📍 India
""")
    

    # ---------------- Generate Newsletter ---------------- #

st.markdown("## 🚀 Generate Today's Intelligence Report")

st.write(
    "Click the button below to fetch the latest FMCG news, analyze it using AI, and generate a professional market intelligence newsletter."
)

if st.button("🚀 Generate Newsletter"):

    with st.spinner("🤖 AI is analyzing market news..."):

        newsletter = run_pipeline()

    st.success("✅ Newsletter Generated Successfully!")

    st.divider()

    st.markdown("## 📰 Today's Newsletter")

    with st.expander("📄 View Newsletter", expanded=True):

        st.markdown(newsletter)

    st.download_button(
        label="⬇️ Download Newsletter",
        data=newsletter,
        file_name="newsletter.md",
        mime="text/markdown"
    )





    # ---------------- Footer ---------------- #

st.divider()

st.markdown("""
<div style="text-align:center;padding:20px;">

<h3 style="color:#E50914;">
🚀 Built by Anuj Sharma
</h3>

<p style="font-size:18px;color:#D3D3D3;">
Machine Learning Engineer
</p>

<p style="color:gray;">
Python • Streamlit • Gemini AI • NewsAPI
</p>

</div>
""", unsafe_allow_html=True)
