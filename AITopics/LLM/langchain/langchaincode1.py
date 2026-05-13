from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(model="gpt-5-nano", temperature=0.9)
user_input = input("Enter your message: ")
agent = create_agent(model=model)

response = agent.invoke({"messages": [("user", user_input)]})
print(response["messages"][-1].content)
