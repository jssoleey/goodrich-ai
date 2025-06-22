import streamlit as st
from chatbots.prevent.chatbot import run_prevent_bot

st.set_page_config(page_title="스테이온(StayOn)", layout="wide")

run_prevent_bot()
