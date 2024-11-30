import streamlit as st
import requests


API_KEY = 'VF.DM.674b34d8b282b73cf09600d7.CQMQFNo9YGXfWhiy'
PROJECT_ID = '674aa3851f89e3926fa7fbe8'
VOICEFLOW_URL = f"https://general-runtime.voiceflow.com/state/{PROJECT_ID}/interact"


def interact(user_id, request):
    response = requests.post(
        f'https://general-runtime.voiceflow.com/state/user/{user_id}/interact',
        json={'request': request},
        headers={
            'Authorization': API_KEY,
            'versionID': 'production'
        },
    )
    for trace in response.json():
        if trace['type'] == 'text':
            print(trace['payload']['message'])

st.title("Chef bot")

st.write(interact("user", { 'type': 'launch' }))

user_input = st.text_input("Enter:")
while True:
    st.write(interact(user_input, { 'type': 'text', 'payload': user_input }))