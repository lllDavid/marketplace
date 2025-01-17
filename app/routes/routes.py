from flask import render_template, redirect, url_for, request, session

from app.db.user_db import get_user_by_email
from app.user.user_creator import UserCreator
from app.wallets.fiat.fiat_wallet_creator import create_fiat_wallet
from app.wallets.crypto.crypto_wallet_creator import create_cryto_wallet
from app.controllers.auth_controller import handle_login, handle_settings, handle_deposit

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
    
    @app.route("/oauth-signup")
    def oauth_signup():
        redirect_uri = url_for('authorize', _external=True)
        return app.google.authorize_redirect(redirect_uri)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            return handle_login(request)
        return render_template("login.html")
    
    @app.route("/oauth-login")
    def oauth_login():
        redirect_uri = url_for('authorize', _external=True)
        return app.google.authorize_redirect(redirect_uri)
    
    @app.route("/login/reset-password")
    def reset_password():
        return render_template("reset-password.html")

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
    
    @app.route('/authorize')
    def authorize():
        token = app.google.authorize_access_token()
        resp = app.google.get('userinfo')
        user_info = resp.json()

        session["email"] = user_info["email"]
        email = user_info["email"]
        
        user = get_user_by_email(email)

        if user_info:
            if not user:
                user_creator = UserCreator()
                user = user_creator.create_user(user_info["name"], user_info["email"], password="")
                user_creator.save_user(user)
                if user.id:
                    create_fiat_wallet(user.id)
                    create_cryto_wallet(user.id)
                session["user_id"] = user.id
                session["username"] = user.username
                session["email"] = user.email
                session.modified = True

        if user:
            session["user_id"] = user.id
            session["username"] = user.username
            session.modified = True

            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))

    