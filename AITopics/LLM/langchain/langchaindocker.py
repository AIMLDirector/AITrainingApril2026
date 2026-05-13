from dotenv import load_dotenv
load_dotenv()
import docker
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,AIMessage
from langchain.agents.middleware import SummarizationMiddleware

client = docker.from_env()

model = ChatOpenAI(model="gpt-5-nano",temperature=0.2)

@tool
def list_containers(dummy: str = "") -> str:
    """
    List all running Docker containers
    """

    containers = client.containers.list()

    if not containers:
        return "No running containers"

    result = []

    for container in containers:
        result.append(
            f"""
            Name: {container.name}
            Status: {container.status}
            Image: {container.image.tags}
            """
        )

    return "\n".join(result)


@tool
def get_container_logs(container_name: str) -> str:
    """
    Get Docker container logs
    """

    try:
        container = client.containers.get(container_name)

        logs = container.logs(
            tail=50
        ).decode("utf-8")

        return logs

    except Exception as e:
        return str(e)


@tool
def inspect_container(container_name: str) -> str:
    """
    Inspect Docker container
    """

    try:
        container = client.containers.get(container_name)

        return f"""
        Container: {container.name}

        Status: {container.status}

        Image:
        {container.image.tags}

        Started:
        {container.attrs['State']['StartedAt']}

        Restart Count:
        {container.attrs['RestartCount']}
        """

    except Exception as e:
        return str(e)


@tool
def analyze_container_issue(logs: str) -> str:
    """
    Analyze container issues
    """

    if "connection refused" in logs.lower():
        return """
        Root Cause:
        Service dependency unavailable

        Short-Term Fix:
        Restart dependent service

        Long-Term Solution:
        Add health checks and retry logic
        """

    if "out of memory" in logs.lower():
        return """
        Root Cause:
        Container memory exceeded

        Solution:
        Increase memory limits
        """

    return """
    No critical issue detected.
    Manual investigation recommended.
    """



tools = [
    list_containers,
    get_container_logs,
    inspect_container,
    analyze_container_issue
]


middleware = [

    SummarizationMiddleware(
        model=model,
        max_tokens_before_summary=2000
    )

]


agent = create_agent(
    model=model,
    tools=tools,
    middleware=middleware,

    system_prompt="""
    You are an Infrastructure AI Assistant.

    Responsibilities:
    - Analyze Docker container issues
    - Troubleshoot infrastructure problems
    - Help DevOps teams
    - Recommend production fixes

    Always provide:
    1. Root cause
    2. Short-term fix
    3. Long-term solution
    """
)



chat_history = []



print("\n===== Docker Infrastructure AI Agent =====")

while True:

    user_input = input("\nInfra Team: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    chat_history.append(
        HumanMessage(content=user_input)
    )
    response = agent.invoke({
        "messages": chat_history
    })
    ai_message = response["messages"][-1]

    print("\nAI Assistant:\n")
    print(ai_message.content)
    chat_history.append(
        AIMessage(content=ai_message.content)
    )