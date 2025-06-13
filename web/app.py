import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.workflow.graph import build_workflow

st.set_page_config(page_title="Agentic Workflow", layout="centered")
st.title("🤖 Agentic Workflow with LangGraph & Ollama")

query = st.text_area("Enter your task:", height=150)

if st.button("Run Agentic Workflow"):
    if query.strip() == "":
        st.warning("Please enter a task.")
    else:
        with st.spinner("Thinking..."):
            workflow = build_workflow()
            result = workflow.invoke({"query": query})
            st.success("Done!")
            st.markdown("### 🧠 Final Output")
            st.markdown(result["final_output"])
