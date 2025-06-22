import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="굿리치플러스 AI 서비스", layout="wide", initial_sidebar_state="collapsed")

# ✅ 페이지 스타일 그대로 유지
st.markdown("""
<style>
/* 기존 CSS 그대로 유지 */
html, body, [data-testid="stAppViewContainer"], .main, .block-container {
    background: linear-gradient(135deg, #1a2a6c, #b21f1f) !important;
    background-attachment: fixed;
    background-size: cover;
    color: white !important;
}
[data-testid="stSidebar"] {
    background-color: rgba(0, 0, 0, 0.4) !important;
}
[data-testid="collapsedControl"] {
    color: white !important;
}
.grid-container {
    margin-top: 120px;
    padding: 20px;
    width: 100%;
    display: grid;
    grid-template-columns: repeat(4, minmax(300px, 1fr));
    gap: 20px;
    max-width: 1600px;
    margin: 0 auto;
    padding-left: 0 !important;
    padding-right: 0 !important;
}
.grid-item {
    text-align: left;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    backdrop-filter: blur(5px);
    padding: 20px;
    margin-bottom: 20px;
    transition: all 0.3s ease;
}
.grid-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}
.title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 1rem;
    color: white;
}
.grid-content {
    flex: 1;
    line-height: 1.6;
    font-size: 1.2rem;
    color: white;
}
@media (max-width: 1200px) {
    .grid-container {
        grid-template-columns: repeat(2, 1fr);
        display: grid !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ✅ 상단 타이틀
st.markdown("<h2 style='color: white; text-align: center;'>굿리치플러스 AI 서비스</h2>", unsafe_allow_html=True)
st.markdown("")
st.markdown("<h5 style='color: white; text-align: center;'>보험 상담에 특화된 다양한 AI 챗봇 서비스를 선택해보세요.</h5>", unsafe_allow_html=True)

# ✅ 카드형 그리드 컨테이너
st.markdown('<div class="grid-container">', unsafe_allow_html=True)

colors = ['#feba28', '#4cc844', '#03f4fc']  # 각 카드 제목 색상

services = [
    {"title": "스마트 컨설팅 매니저", "desc": "영업 상황에 관한 스크립트 및 챗봇 기능을 지원합니다.", "page": "chatbot_sale"},
    {"title": "응대닥터 CARE+", "desc": "고객 민원 대응 및 클레임 처리 가이드를 제공합니다.", "page": "chatbot_comp"},
    {"title": "스테이온(StayOn)", "desc": "청약 철회 및 해지를 방어하기 위한 대응 전략을 안내합니다.", "page": "chatbot_prev"},
]

# 카드 렌더링 시작
for i, svc in enumerate(services):
    color = colors[i % len(colors)]  # 색상 순환 (서비스 개수보다 색상 적을 경우 대비)

    with st.form(key=f"form_{svc['page']}"):
        st.markdown(f"""
        <div class="grid-item">
            <div class="title" style="color: {color}; font-weight: bold;">{svc['title']}</div>
            <div class="grid-content">{svc['desc']}</div>
            <div class="button-wrapper">
        """, unsafe_allow_html=True)

        submitted = st.form_submit_button("👉 바로가기")

        st.markdown("""
            </div>
        </div>
        """, unsafe_allow_html=True)

        if submitted:
            switch_page(svc["page"])


        
st.markdown("""
<style>
.stButton > button {
    background-color: rgba(255, 255, 255, 0.15);
    color: white;
    border: 1px solid white;
    border-radius: 8px;
    font-size: 16px;
    padding: 0.5rem 1.2rem;
    transition: 0.3s ease;
}
.stButton > button:hover {
    background-color: #FFD700;
    color: black;
}
</style>
""", unsafe_allow_html=True)
