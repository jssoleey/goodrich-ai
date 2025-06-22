import streamlit as st
from chatbots.complaint.chatbot import run_complaint_bot

st.set_page_config(page_title="응대닥터 CARE+", layout="wide")

run_complaint_bot()
