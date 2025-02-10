# If We want to chat history then session_state require...
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq 
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="My Chatbot")
st.header("👋👋 I am your chatbot 💬, Ask me a question ❓")

chat = ChatGroq(model="llama3-8b-8192", temperature=0.5)

if 'mymessages' not in st.session_state:
    st.session_state['mymessages'] = [
        SystemMessage(content="You are Man Dhanani's chatbot.")
    ]

def chatmodel_response(question):
    st.session_state['mymessages'].append(HumanMessage(content=question))
    response = chat.invoke(st.session_state['mymessages'])
    st.session_state['mymessages'].append(AIMessage(content=response.content))
    return response.content

st.subheader("Chat History 🗨️")
for msg in st.session_state['mymessages']:
    if isinstance(msg, HumanMessage):
        st.write(f"**You:** {msg.content}")
    elif isinstance(msg, AIMessage):
        st.write(f"**Chatbot:** {msg.content}")

input_text = st.text_input("Input:", key="input")
submit_button = st.button("Ask Question 🙋❓")

if submit_button and input_text:
    response = chatmodel_response(input_text)
    st.subheader("This is your Response: 👇")
    st.write(response)



# import streamlit as st
# from langchain.schema import HumanMessage, SystemMessage, AIMessage
# from langchain_groq import ChatGroq 
# from dotenv import load_dotenv
# import os

# load_dotenv()

# st.set_page_config(page_title="My chatbot")
# st.header("👋👋 I am your chatbot 💬, Ask me a question ❓")

# chat = ChatGroq(model="llama3-8b-8192", temperature=0.5)

# if 'mymessages' not in st.session_state:
#     st.session_state['mymessages'] = [
#         SystemMessage(content="You are Man Dhanani's chatbot.")
#     ]

# def chatmodel_response(question):
#     st.session_state['mymessages'].append(HumanMessage(content=question))
#     response = chat(st.session_state['mymessages'])
#     st.session_state['mymessages'].append(AIMessage(content=response.content))
#     return response.content


# input_text = st.text_input("Input:", key="input")
# submit_button = st.button("Ask Question 🙋❓")

# if submit_button and input_text:
#     response = chatmodel_response(input_text)
#     st.subheader("This is your Response: 👇")
#     st.write(response)



# Simple chatbot without session state

# import streamlit as st
# from langchain.schema import HumanMessage
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# import os

# load_dotenv()

# st.set_page_config(page_title="My Chatbot")
# st.header("👋👋 I am your chatbot 💬, Ask me a question ❓")


# chat = ChatGroq(model="llama3-8b-8192", temperature=0.5)

# def chatmodel_response(question):
#     response = chat.invoke([HumanMessage(content=question)])
#     return response.content

# input_text = st.text_input("Input:", key="input")
# submit_button = st.button("Ask Question 🙋❓")

# if submit_button and input_text:
#     response = chatmodel_response(input_text)
#     st.subheader("This is your Response: 👇")
#     st.write(response)
