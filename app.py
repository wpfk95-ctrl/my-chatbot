import streamlit as st

# st.title("강남구청")

# st.header("AI Agent 과정")

# st.write("Hello World")

page_1 = st.Page("page_1.py", title="홈 탭", icon="❤️")
page_2 = st.Page("page_2.py", title="챗봇", icon="👍")
page_3 = st.Page("page_3.py", title="프로필 페이지", icon="🤷‍♂️")

pages = st.navigation([page_1, page_2, page_3], position="top")

pages.run()
