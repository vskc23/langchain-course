import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()
def main():
    name = "Srinivasa Ramanujan"
    summary_template = """ 
    Based on this person:
    {name}, generate the following:
    1. Two major achievements
    2. Two major controversies
    """
    summary_prompt = PromptTemplate(input_variables=["name"], template=summary_template)
    
    llm = ChatOpenAI(
    temperature=1,
    model="gpt-6-luna",
)
    chain = summary_prompt | llm
    response = chain.invoke(input={"name": name})
    print(response.content)

if __name__ == "__main__":
    main()