import os
from requests import post, get
from flask import redirect, session, url_for
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("GOOGLE_CLIENT_ID")
client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
redirect_uri = 'http://localhost:5000/callback'

def oauth_google():
    oauth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code"
        f"&client_id={client_id}&redirect_uri={redirect_uri}&scope=email%20profile"
    )
    return redirect(oauth_url)

def callback(code):
    if not code:
        return "Error: No authorization code provided by OAuth provider.", 400

    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }
    token_response = post(token_url, data=token_data)
    token_info = token_response.json()

    if token_response.status_code == 200:
        session['oauth_token'] = token_info
        user_info_response = get(
            "https://www.googleapis.com/oauth2/v3/userinfo", 
            headers={"Authorization": f"Bearer {token_info['access_token']}"}
        )
        session['user_info'] = user_info_response.json()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
