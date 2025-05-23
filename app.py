import streamlit as st

st.set_page_config(page_title="DronaAI", layout="centered")

st.title("🇮🇳 DronaAI - India’s First AI Tutor for Exam Doubts")
st.subheader("Your smart companion for doubt solving & timetable planning")

st.markdown("### 👇 What do you want to do?")
col1, col2 = st.columns(2)

with col1:
    if st.button("❓ Ask a Doubt"):
        st.switch_page("pages/Ask_Doubt.py")

with col2:
    if st.button("🕒 Create Timetable"):
        st.switch_page("pages/Timetable.py")

st.markdown("---")
st.markdown("### 💡 Plans:")
st.markdown("✅ **Free**: Ask up to 3 doubts/day  \n💎 **Pro ₹99/month**: Unlimited access to AI tutor")

if st.button("See Pricing & Upgrade"):
    st.switch_page("pages/Pricing.py")
