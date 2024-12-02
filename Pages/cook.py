import streamlit as st
import requests
import speech_recognition as sr
import tempfile
import dotenv
from dotenv import load_dotenv
import os

# Constants for Voiceflow API
PROJECT_ID = "TEMPORARY PLACEHOLDER"
API_KEY = "TEMPORARY PLACEHOLDER"

load_dotenv()  # take environment variables from .env.

PROJECT_ID = os.getenv("PROJECT_ID")
API_KEY = os.getenv("API_KEY")

# Constants for Voiceflow API
VOICEFLOW_URL = f"https://general-runtime.voiceflow.com/state/{PROJECT_ID}/interact"

st.set_page_config(initial_sidebar_state="collapsed", page_title="Mealami-cook", layout="centered", page_icon="🍳")

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


# Function to handle sending messages
def send_message(user_message):
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
            st.write(bot_response)

        st.session_state.temp_input = ""

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file
    try:
        return recognizer.recognize_google(audio_data)  # Transcribe using Google API
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Speech Recognition error: {e}"

# Initialize session state for chat history and intermediate input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_id" not in st.session_state:
    st.session_state.user_id = "unique_user_id"  # Generate a unique user ID per session

if "temp_input" not in st.session_state:
    st.session_state.temp_input = ""


st.text_input(
    "You: ",
    key="temp_input",  # Use a separate key for temporary input
    on_change=lambda: send_message(st.session_state.temp_input)  # Pass the input as an argument
)

if st.button("Record Audio"):
    st.info("Recording... Please wait.")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.listen(source, timeout=3)  # Listen for 5 seconds
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(audio_data.get_wav_data())  # Save as WAV file
                temp_audio_path = temp_audio.name

            # Transcribe audio and send to chatbot
            transcription = transcribe_audio(temp_audio_path)
            st.write(transcription)
            if transcription:  # Ensure transcription is valid before sending
                st.session_state.chat_history.append(f"You (Voice): {transcription}")
                bot_responses = interact(st.session_state.user_id, transcription)
                for bot_response in bot_responses:
                    st.session_state.chat_history.append(f"Bot: {bot_response}")
                    st.write(bot_response)

        except Exception as e:
            st.error(f"Error during recording: {e}")

st.subheader("Chat History")
for message in st.session_state.chat_history:
    st.write(message)
# End conversation button
if st.button("End Conversation"):
    st.write("Conversation has ended.")
    st.session_state.chat_history = []  # Clear the chat history

st.page_link("streamlit_app.py", label="Home", icon="🏠")
