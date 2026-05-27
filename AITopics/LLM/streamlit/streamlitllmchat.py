import streamlit as st 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
load_dotenv()

st.set_page_config(page_title="LLM Chat", page_icon=":speech_balloon:")
st.title("LLM Chat")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [ AIMessage(content="Hello! I'm your AI assistant. How can I help you today?")]

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

if prompt := st.chat_input("Type your message here..."):
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)
    
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    response = llm.invoke(st.session_state.chat_history)
    
    st.session_state.chat_history.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)