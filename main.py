import streamlit as st
import model
import time
import subprocess
import json

st.title("Chat With Mistral")

model.model_load()

st.write("Bot is Ready")

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
    # Créer le corps de la requête JSON en utilisant la variable prompt
    data = {
        "model": "mistral",
        "prompt": prompt
    }

    # Convertir le dictionnaire en chaîne JSON
    data_st = json.dumps(data)

    command = [
        "curl ", 
        "http://localhost:11434/api/generate ", 
        "-d ", 
        data_st
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    try:
        response_json = json.loads(result.stdout)
        response = response_json.get('response', 'Element not found')
    except:
        st.write("Erreur lors de la requete")

    for word in response.split():
        yield word + " "
        time.sleep(0.15)

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})