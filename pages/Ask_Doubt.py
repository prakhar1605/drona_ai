import streamlit as st

# Set title
st.title("❓ Ask a Doubt")

# Initialize session state if not present
if "doubt_count" not in st.session_state:
    st.session_state.doubt_count = 0

# Show current count
st.markdown(f"📚 You have used **{st.session_state.doubt_count} / 3** doubts today (Free Plan)")

# Input box
doubt = st.text_area("Enter your exam-related doubt:")

# Button
if st.button("Get Answer"):
    if st.session_state.doubt_count >= 3:
        st.error("⚠️ You’ve reached the daily limit (3 doubts). Please upgrade to Pro.")
    elif doubt.strip() == "":
        st.warning("Please enter a valid doubt.")
    else:
        st.session_state.doubt_count += 1
        st.success("✅ AI Answer: This is a sample AI-generated response. (Pro version will use real AI!)")
