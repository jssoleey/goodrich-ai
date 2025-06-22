import streamlit as st
from chatbots.sale.chatbot import run_sale_bot

st.set_page_config(page_title="스마트 컨설팅 매니저", layout="wide")

run_sale_bot()
