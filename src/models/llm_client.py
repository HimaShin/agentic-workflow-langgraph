import os

def ask_llm(prompt):
    if "STREAMLIT_SERVER_ENABLED" in os.environ:
        return f"Simulated response from agent for: {prompt}"
    else:
        from langchain_community.chat_models import ChatOllama
        llm = ChatOllama(model="gemma:2b")
        return llm.invoke(prompt).content
