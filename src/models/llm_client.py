import os

def ask_llm(prompt):
    # If running on Streamlit Cloud → simulate response
    if "STREAMLIT_SERVER_ENABLED" in os.environ:
        return f"Reflected on result: Simulated response from agent for task: {prompt}"

    # Local execution → use Ollama
    try:
        from langchain_community.chat_models import ChatOllama
        llm = ChatOllama(model="gemma:2b")
        return llm.invoke(prompt).content
    except Exception as e:
        return f"(Error using Ollama locally) {str(e)}"
