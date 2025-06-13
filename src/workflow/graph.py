from langgraph.graph import StateGraph, END
from src.agents.plan_agent import plan_agent
from src.agents.tool_agent import tool_agent
from src.agents.reflection_agent import reflection_agent

def build_workflow():
    graph = StateGraph(dict)

    def plan(state):
        return {"plan": plan_agent(state["query"])}

    def execute(state):
        return {"result": tool_agent(state["plan"])}

    def reflect(state):
        return {"final_output": reflection_agent(state["result"])}

    graph.add_node("plan", plan)
    graph.add_node("execute", execute)
    graph.add_node("reflect", reflect)

    graph.set_entry_point("plan")
    graph.add_edge("plan", "execute")
    graph.add_edge("execute", "reflect")
    graph.add_edge("reflect", END)

    return graph.compile()
