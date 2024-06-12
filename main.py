import streamlit as st
import model
import time
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

st.title("Chat With Mistral")

# model.model_load()

st.write("Bot is Ready")

client = MistralClient(api_key="xkbaxNdKcVCEDOlpcXurZ5zmbMr9tgJg")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Streamed response emulator
def response_generator():
    if prompt:
        chat_response = client.chat(
            model="mistral-large-latest",
            messages=[ChatMessage(role="user", content=f"{prompt}")]
        )
    else:
        chat_response = client.chat(
            model="mistral-large-latest",
            messages=[ChatMessage(role="user", content="Je parle francais. Disponible ?")]
        )

    response = chat_response.choices[0].message.content

    return response


    # for word in response.split():
    #     yield word + " "
    #     time.sleep(0.15)

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write(response_generator())
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})