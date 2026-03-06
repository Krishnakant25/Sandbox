# ------------------------------------------------------------
# 🧠 AI Chatbot using Streamlit + LangChain + OpenAI
# ------------------------------------------------------------
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit  as st
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

st.title("🤖 AI Chatbot")

# ------------------------------------------------------------
# Initialize chat history (with system message)
# ------------------------------------------------------------
if "messages" not in st.session_state():
    st.session_state.messages = [
        SystemMessage(content="you are an helpful AI assistant.")
    ]

# ------------------------------------------------------------
# Add a "Clear Chat" button
# ------------------------------------------------------------
if st.button("Clear-Chat"):
    st.session_state.messages = [
        SystemMessage(content="you are an helpful AI assistant.")
    ]
    st.experimental_rerun()

# ------------------------------------------------------------
# Display the previous chat history
# ------------------------------------------------------------
for msg in st.session_state.messages():
    if isinstance(msg,HumanMessage):
        with st.chat_message("user"):
             st.markdown(msg.content)

    elif isinstance(msg,AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

    
# ------------------------------------------------------------
# Get new user input
# ------------------------------------------------------------

if prompt := st.chat_input("Type your message..."):

    # ------------------------------------------------------------
    # Add the user's message to the conversation history
    # ------------------------------------------------------------
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # ------------------------------------------------------------
    # Generate AI response
    # ------------------------------------------------------------
    response = model.invoke(st.session_state.messages)
    ai_reply = response.content

    # ------------------------------------------------------------
    # Add AI's reply to the session and display it
    # ------------------------------------------------------------
    st.session_state.messages.append(AIMessage(content=ai_reply))
    with st.chat_message("assistant"):
        st.markdown(ai_reply)