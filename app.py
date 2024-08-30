import requests
import streamlit as st

from src.logger import logger

# SageMaker endpoint URL
ENDPOINT_URL = "https://dw33y794mc.execute-api.us-east-1.amazonaws.com/text2SQL"

def query_endpoint(query):
    try:
        response = requests.get(ENDPOINT_URL, params={"query": query})
        logger.info(f"Response: {response}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error querying the endpoint: {str(e)}")
        return None

st.title("Text to SQL Converter")

# User input
user_input = st.text_area("Enter your text query:", height=100)

if st.button("Convert to SQL"):
    if user_input:
        logger.info(f"User input: {user_input}")
        with st.spinner("Converting..."):
            result = query_endpoint(user_input)
            logger.info(f"Result: {result}")
            
        if result:
            st.subheader("Generated SQL Query:")
            st.code(result, language="sql")
            # st.code(result.get("sql_query", "No SQL query generated"), language="sql")
            
    else:
        st.warning("Please enter a text query.")

st.sidebar.header("About")
st.sidebar.info(
    "This app converts natural language text to SQL queries using a "
    "machine learning model. Enter your query in plain English, and "
    "get the corresponding SQL query."
)