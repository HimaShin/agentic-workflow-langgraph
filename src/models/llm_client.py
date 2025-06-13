import os

def ask_llm(prompt):
    # This is a fake response ONLY for Streamlit Cloud
    if "STREAMLIT_SERVER_ENABLED" in os.environ:
        return f"Reflected on result: Simulated response from agent for task: {prompt}"
    
    # Local Ollama usage (ONLY when run locally)
    try:
        from langchain_community.chat_models import ChatOllama
        llm = ChatOllama(model="gemma:2b")
        return llm.invoke(prompt).content
    except Exception as e:
        return f"(Error using Ollama locally) {str(e)}"
