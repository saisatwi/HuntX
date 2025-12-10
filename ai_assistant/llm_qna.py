import os
import pandas as pd
from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

# Load your dataset
df = pd.read_csv("./data/processed/master_data.csv")

# Load your API key (PowerShell setx already saved it)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found!")

# Initialize OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",      # best cheap model
    temperature=0,
    openai_api_key=api_key
)

# Create the dataframe agent
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True
)

# Ask your question
response = agent.invoke("List the 5 most hunted animals and how many times each appears.")
print(response)
