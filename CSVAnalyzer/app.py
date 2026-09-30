import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd

#BackEnd

def query_agent(data,query):
    datafile=pd.read_csv(data)
    llm=OllamaLLM(model="llama3.2",temperature=0)
    agent=create_pandas_dataframe_agent(llm,datafile,verbose=True,allow_dangerous_code=True)
    return agent.run(query)


#UI

st.title("Let's do some analysis on your CSV")
st.header("Please upload your CSV file here:")

data = st.file_uploader("Upload CSV file", type="csv")

query = st.text_area("Enter your query")
button = st.button("Generate Response")

if button:
    answer=query_agent(data,query)
    # Get Response
    st.write(answer)



