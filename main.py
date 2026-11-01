
import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-6-astra",
    temperature=1,
)

# Initialize Tavily search
search_tool = TavilySearch(
    max_results=5,
    topic="general",
)

# Create the agent
agent = create_agent(
    model=llm,
    tools=[search_tool],
    system_prompt="""
    You are a helpful research assistant.

    Use the Tavily search tool whenever the user
    asks for current or up-to-date information.

    Provide clear, accurate answers based on
    the search results.
    """
)


def main():
    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Search for Tokyo's current weather"
            }
        ]
    })

    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()
