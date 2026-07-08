import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title("My Chatbot")

# 1. 세션 상태(대화 기록) 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. 페이지가 새로고침될 때마다 기존 대화 기록을 화면에 먼저 렌더링
for message in st.session_state.messages:
    with st.chat_message(message['role']): 
        st.write(message['content'])

# 3. 사용자 입력 받기
prompt = st.chat_input("무엇이든 물어보세요")

if prompt:
    # 3-1. 사용자가 질문을 입력하자마자 화면에 즉시 팝업
    with st.chat_message('user'):
        st.write(prompt)
    
    # 대화 기록에 사용자 질문 추가
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    # 3-2. AI가 답변을 준비하는 동안 ... 애니메이션(스피너) 띄우기
    with st.chat_message('ai'):
        with st.spinner("AI가 답변을 준비하고 있습니다..."):
            # 기존에 사용하시던 API 규격 그대로 호출
            response = client.responses.create(
                model="gpt-5.5",
                input=prompt
            )
            ai_response = response.output_text
            
            # 답변이 완료되면 스피너가 사라지고 그 자리에 답변 텍스트가 노출됨
            st.write(ai_response)
    
    # 대화 기록에 AI 답변 추가
    st.session_state.messages.append({'role': 'ai', 'content': ai_response})