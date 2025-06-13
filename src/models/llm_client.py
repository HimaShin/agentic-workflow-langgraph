import os

def ask_llm(prompt):
    # Simulated response for Streamlit Cloud
    if "STREAMLIT_SERVER_ENABLED" in os.environ:
        return f"Simulated response for: {prompt}"
    else:
        # This works only in local machine with Ollama
        from langchain_community.chat_models import ChatOllama
        llm = ChatOllama(model="gemma:2b")
        return llm.invoke(prompt).content
