from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from typing import TypedDict

llm = ChatOpenAI(model="gpt-4o-mini")

class AgentState(TypedDict):
    query: str
    response: str

def research_agent(state):
    query = state["query"]
    result = llm.invoke(f"Research this topic: {query}")
    return {"response": result.content}

def coding_agent(state):
    query = state["query"]
    result = llm.invoke(f"Generate python code for: {query}")
    return {"response": result.content}

workflow = StateGraph(AgentState)

workflow.add_node("research", research_agent)
workflow.add_node("coding", coding_agent)

workflow.set_entry_point("research")

workflow.add_edge("research", "coding")
workflow.add_edge("coding", END)

app = workflow.compile()

while True:
    user_input = input("Enter your query (or 'exit' to quit): ")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Exiting application. Goodbye!")
        break
    else:
        result = app.invoke({"query": user_input})

print(response["messages"][-1].content)