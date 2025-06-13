from src.models.llm_client import ask_llm

def plan_agent(query):
    prompt = f"Break this task into smaller subtasks: {query}"
    return ask_llm(prompt)
