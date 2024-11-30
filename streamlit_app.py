import streamlit as st

pg = st.navigation([st.Page("streamlit_app.py"),st.Page("out.py"), st.Page("cook.py")])

# st.sidebar.selectbox("Group", ["A","B","C"], key="group")

pg.run()

# import streamlit as st
# import os
# from dotenv import load_dotenv
# from authlib.integrations.requests_client import OAuth2Session
# from urllib.parse import urlencode

# # Load environment variables from .env file
# load_dotenv()

# # Auth0 configurations from environment variables
# AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
# AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
# AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
# AUTH0_CALLBACK_URL = os.getenv("AUTH0_CALLBACK_URL")

# # Auth0 Authorization and Token URLs
# AUTHORIZATION_URL = f"https://{AUTH0_DOMAIN}/authorize"
# TOKEN_URL = f"https://{AUTH0_DOMAIN}/oauth/token"
# USERINFO_URL = f"https://{AUTH0_DOMAIN}/userinfo"

# # Initialize OAuth2 session
# oauth = OAuth2Session(AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, redirect_uri=AUTH0_CALLBACK_URL)

# # Check if the user is logged in
# if "user" not in st.session_state:
#     st.session_state.user = None

# # Function to handle the login flow
# def login():
#     # Step 1: Generate the authorization URL
#     authorization_url, state = oauth.create_authorization_url(AUTHORIZATION_URL)

#     # Redirect the user to the Auth0 login page
#     st.write(f"Please [log in]({authorization_url})")

# # Function to handle the logout
# def logout():
#     st.session_state.user = None
#     st.write("You are logged out.")

# # Callback function to handle the Auth0 redirect
# def callback():
#     # Step 2: Fetch the access token
#     token = oauth.fetch_token(TOKEN_URL, authorization_response=st.experimental_get_query_params())

#     # Step 3: Retrieve the user info
#     user_info = oauth.get(USERINFO_URL).json()

#     # Store the user info in session state
#     st.session_state.user = user_info
#     st.write(f"Logged in as: {user_info['name']}")

# # Main Streamlit app logic
# def main():
#     st.title("🎈 My Streamlit App with Auth0")

#     # Show login/logout based on session state
#     if st.session_state.user is None:
#         login()  # Prompt for login if not logged in
#     else:
#         st.write(f"Welcome, {st.session_state.user['name']}!")
#         st.button("Logout", on_click=logout)  # Logout button

#     # Example of using the login status
#     if st.session_state.user:
#         st.write("User Data:", st.session_state.user)

# # Check if this is a callback URL
# query_params = st.query_params()

# # If there is an `code` query parameter, handle the callback (successful login)
# if "code" in query_params:
#     callback()

# else:
#     # Otherwise, show the main page
#     main()
