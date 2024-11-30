import streamlit as st
import requests

# Constants for Voiceflow API
PROJECT_ID = "674aa3851f89e3926fa7fbe8"
API_KEY = "VF.DM.674b34d8b282b73cf09600d7.CQMQFNo9YGXfWhiy"
VOICEFLOW_URL = f"https://general-runtime.voiceflow.com/state/{PROJECT_ID}/interact"

# Voiceflow interaction function
def interact(user_id, user_input):
    """Send a message to Voiceflow and receive a response."""
    response = requests.post(
        f'https://general-runtime.voiceflow.com/state/user/{user_id}/interact',
        json={'request': {"type": "text", "payload": user_input}},
        headers={
            'Authorization': API_KEY,
            'versionID': 'production'
        },
    )

    if response.status_code != 200:
        return [f"Error: {response.status_code} - {response.text}"]

    try:
        messages = []
        response_json = response.json()
        for trace in response_json:
            if isinstance(trace, dict) and trace.get('type') == 'text':
                messages.append(trace['payload']['message'])
        return messages
    except Exception as e:
        return [f"Error parsing response: {e}"]

# Initialize session state for chat history and intermediate input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_id" not in st.session_state:
    st.session_state.user_id = "unique_user_id"  # Generate a unique user ID per session

if "temp_input" not in st.session_state:
    st.session_state.temp_input = ""

# Function to handle sending messages
def send_message():
    user_message = st.session_state.temp_input  # Use temp_input instead of user_input
    if user_message.strip().lower() == "end":
        st.write("Conversation ended.")
    else:
        # Add user message to chat history
        st.session_state.chat_history.append(f"You: {user_message}")

        # Call the interact function and get bot responses
        bot_responses = interact(st.session_state.user_id, user_message)

        # Add each bot response to the chat history
        for bot_response in bot_responses:
            st.session_state.chat_history.append(f"Bot: {bot_response}")

        # Clear temp_input after sending
        st.session_state.temp_input = ""

# Text input for user message
st.text_input(
    "You: ",
    key="temp_input",  # Use a separate key for temporary input
    on_change=send_message,  # Call the send_message function when input changes
)

# Display chat history
st.subheader("Chat History")
for message in st.session_state.chat_history:
    st.write(message)

# End conversation button
if st.button("End Conversation"):
    st.write("Conversation has ended.")
    st.session_state.chat_history = []  # Clear the chat history

st.page_link("streamlit_app.py", label="Home", icon="🏠")