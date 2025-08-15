import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지 설정
st.set_page_config(layout="wide", page_title="자료구조 교육 시뮬레이터")

# HTML 파일의 경로를 지정합니다.
# 이 파일들을 Streamlit 앱과 같은 디렉토리에 두는 것이 가장 간단합니다.
# 첫 번째 HTML 파일 (정렬 알고리즘)
SORTING_HTML_FILE_PATH = "index2.html" 
# 두 번째 HTML 파일 (탐색 알고리즘)
SEARCHING_HTML_FILE_PATH = "index1.html"

# HTML 파일을 읽어오는 함수
def load_html_file(file_path):
    # 파일이 존재하는지 확인
    if not os.path.exists(file_path):
        st.error(f"오류: HTML 파일이 '{file_path}' 경로에 없습니다. 파일을 업로드하거나 경로를 확인해주세요.")
        st.stop() # 파일이 없으면 앱 실행 중지
    
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content

st.sidebar.title("탐색 메뉴 📚")
page_selection = st.sidebar.radio(
    "원하는 알고리즘 페이지를 선택하세요:",
    ("정렬 알고리즘", "탐색 알고리즘")
)

st.title("자료구조 교육 시뮬레이터 🧑‍💻")
st.write("다양한 자료구조 알고리즘의 동작을 시뮬레이션을 통해 직접 확인하고 배워보세요!")

if page_selection == "정렬 알고리즘":
    st.header("정렬 알고리즘의 세계 🚀")
    html_content = load_html_file(SORTING_HTML_FILE_PATH)
    # height와 scrolling 속성은 필요에 따라 조절할 수 있습니다.
    components.html(html_content, height=10000, scrolling=True) # 정렬 페이지는 내용이 길므로 height를 충분히 줌
elif page_selection == "탐색 알고리즘":
    st.header("탐색 알고리즘의 세계 🔍")
    html_content = load_html_file(SEARCHING_HTML_FILE_PATH)
    # height와 scrolling 속성은 필요에 따라 조절할 수 있습니다.
    components.html(html_content, height=5000, scrolling=True) # 탐색 페이지도 충분한 height를 줌

st.markdown("---")
st.write("질문이 있으시면 언제든지 문의해주세요!")

