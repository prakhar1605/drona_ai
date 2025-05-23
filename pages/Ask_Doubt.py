import streamlit as st

st.title("❓ Ask a Doubt")
doubt = st.text_area("Enter your exam-related doubt below:")

if st.button("Get Answer"):
    if doubt.strip() == "":
        st.warning("Please enter a doubt first.")
    else:
        st.success("Answer: (AI logic to be added here later)")
