from src.workflow.graph import build_workflow

if __name__ == "__main__":
    workflow = build_workflow()
    query = input("Enter your task: ")
    result = workflow.invoke({"query": query})
    print("\nFinal Output:\n", result["final_output"])
