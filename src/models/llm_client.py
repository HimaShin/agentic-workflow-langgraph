from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="gemma:2b")
  # Runs locally using Ollama

def ask_llm(prompt):
    return llm.invoke(prompt).content
