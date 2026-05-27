import streamlit as st 

st.title("AI SRE Copilot")
st.subheader("Ask questions about SRE, DevOps, Observability, Reliability, etc...")

# user_input = st.text_input("Enter your question here") 
# chat_input = st.chat_input("Ask about SRE, DevOps, Observability, Reliability...")
with st.form("User input Gathering form", clear_on_submit=False):
    st.subheader("Gathering user requirements")
    user_input = st.text_input("Enter your question here")
    user_email = st.text_input("Enter your email here")
    Gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    submit_button = st.form_submit_button(label="Submit")


with st.sidebar:
     temp = st.slider("Temperature", 0.0, 1.0, 0.7)
     top_k = st.slider("Top K", 1, 10, 3)
     st.write(f"Temperature: {temp}")
     st.write(f"Top K: {top_k}")
