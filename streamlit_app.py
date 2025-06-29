from utils.model_loader import ModelLoader
from prompt_library import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessageState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
import streamlit as st
import datetime
import requests
import sys
 
BASE_URL = "http://localhost:8000" # Backend Endpoint

st.set_page_config(
    page_title = "✈️ Your AI Travel Planner",   
    layout = "centered",
    initial_sidebar_state = "expanded",
    page_icon = "✈️"
)
st.title("Anywhere Voyager")
# Inititalizing the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
st.header("Hey! I am your friendly AI trip and expense planner.. \nWith My stand Anywhere voyager, I can help you seamlessly😊")

with st.form():
    user_input = st.text_input("Enter your request here..", placeholder = "E.g: Plan a trip to Orlando, Florida")
    submit_button = st.form_submit_button("➡️")

if submit_button and user_input.strip():
    try:
        with st.spinner("Stand is working on your request.. Please wait."):
            payload = {"question" : user_input}
            response = requests.post(f"{BASE_URL}/query", json = payload)

        if response.status_code == 200:
            answer = response.json()
            markdown_content = f"""# Travel Plan"""
        st.markdown(answer)
    except Exception as e:
        raise f"The response has failed due to {e}"