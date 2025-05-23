import streamlit as st

st.title("🕒 AI Timetable Planner")

st.markdown("**Enter your details to generate a study plan:**")
exam = st.text_input("Your Target Exam (e.g., NEET, JEE)")
subjects = st.text_input("Subjects (comma separated)")
hours = st.slider("How many hours per day can you study?", 1, 12, 6)

if st.button("Generate Timetable"):
    st.success("AI-generated timetable will appear here (logic to be added)")
