import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

st.title("My Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown(
    """
    <style>
    .typing-indicator {
        display: inline-flex;
        gap: 6px;
        align-items: center;
        padding: 4px 0;
    }

    .typing-indicator span {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #9ca3af;
        animation: typing-bounce 1.2s infinite ease-in-out;
    }

    .typing-indicator span:nth-child(2) {
        animation-delay: 0.2s;
    }

    .typing-indicator span:nth-child(3) {
        animation-delay: 0.4s;
    }

    @keyframes typing-bounce {
        0%, 80%, 100% {
            transform: translateY(0);
            opacity: 0.45;
        }
        40% {
            transform: translateY(-5px);
            opacity: 1;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("무엇이든 물어보세요")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown(
            """
            <div class="typing-indicator" aria-label="답변 작성 중">
                <span></span><span></span><span></span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        try:
            response = client.responses.create(
                model="gpt-5.5",
                input=prompt,
            )
            answer = response.output_text
        except Exception as error:
            response_placeholder.empty()
            st.error("답변을 생성하는 중 오류가 발생했습니다.")
            st.exception(error)
            st.stop()

        response_placeholder.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
