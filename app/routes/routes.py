import string
from random import choices
from os import getenv
from dotenv import load_dotenv
from requests import get, post

from flask import render_template, redirect, url_for, jsonify, request, session

from app.controllers.auth_controller import handle_login, handle_settings, handle_deposit

load_dotenv()

# OAuth credentials
client_id = getenv("GOOGLE_CLIENT_ID")
client_secret = getenv("GOOGLE_CLIENT_SECRET")
redirect_uri = 'http://localhost:5000/callback'
mock_user_data = {
    'id': '12345',
    'email': 'mockuser@example.com',
    'name': 'Mock User',
}

def generate_mock_oauth_token():
    return {
        'access_token': ''.join(choices(string.ascii_letters + string.digits, k=40)),
        'token_type': 'bearer',
        'expires_in': 3600,  
    }

def register_routes(app):
    @app.route("/")
    def index():
        return render_template("landing.html")

    @app.route("/terms")
    def terms():
        return render_template("terms.html")
    
    @app.route("/privacy")
    def privacy():
        return render_template("privacy.html")
    
    @app.route("/cookies")
    def cookies():
        return render_template("cookies.html")
    
    @app.route("/signup")
    def signup():
        return render_template("signup.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            return handle_login(request)
        return render_template("login.html")
    
    @app.route("/login/reset-password")
    def reset_password():
        return render_template("reset-password.html")
    
    @app.route("/oauth_google")
    def oauth_google():
        oauth_url = (
            f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code"
            f"&client_id={client_id}&redirect_uri={redirect_uri}&scope=email%20profile"
        )
        return redirect(oauth_url)
    
    @app.route("/callback", methods=["GET"])
    def callback():
        code = request.args.get('code')
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

    @app.route("/profile", methods=["GET"])
    def profile():
        user_info = session.get('user_info')
        if user_info:
            return jsonify(user_info)
        else:
            return "User not logged in!", 400

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for('.index'))

    @app.route("/home")
    def home():
        return render_template("home.html")
    
    @app.route("/trade", methods=["GET", "POST"])
    def trade():
        return render_template("trade.html") 

    @app.route("/wallet", methods=["GET", "POST"])
    def wallet():
        return render_template("wallet.html")
    
    @app.route("/deposit")
    def deposit():
        return handle_deposit()

    @app.route("/settings", methods=["GET", "POST"])
    def settings():
        return handle_settings(request)

    @app.route("/support", methods=["GET", "POST"])
    def support():
        return render_template("support.html")
    