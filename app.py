# app.py

import streamlit as st
from utils import analyze_code

# Title for the web app
st.title("Code Quality Checker")

# User Input: Code and Checklist
code_input = st.text_area("Enter your code", height=300)
checklist_input = st.text_area("Enter your checklist (one item per line)")

# Button to trigger analysis
if st.button("Analyze"):
    if not code_input.strip() or not checklist_input.strip():
        st.warning("Please provide both code and checklist.")
    else:
        # Analyze code quality based on checklist
        observations, suggestions = analyze_code(code_input, checklist_input)
        
        # Display observations and suggestions
        st.subheader("Observations")
        for obs in observations:
            st.write(f"- {obs}")
        
        st.subheader("Suggestions for Improvement")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")