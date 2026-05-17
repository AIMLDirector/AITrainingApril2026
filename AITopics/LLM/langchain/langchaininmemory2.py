from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from dotenv import load_dotenv
load_dotenv()


checkpointer = InMemorySaver()

agent = create_agent(
    model="gpt-5.4",
    tools=[],
    middleware=[
        SummarizationMiddleware(
            model="gpt-5.4-mini",
            trigger=("tokens", 4000),
            keep=("messages", 20)
        )
    ],
    checkpointer=checkpointer,
)

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("\nBot: Goodbye!")
        break

    response = agent.invoke(
        {
            "messages": [{"role": "user","content": user_input}],
        },
        config=RunnableConfig(configurable={"thread_id": "chat_session_001"})
    )

    print(f"\nBot: {response["messages"][-1].content}\n")   