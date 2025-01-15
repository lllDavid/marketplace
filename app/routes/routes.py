from flask import render_template, redirect, url_for, request, session

from app.blueprints.oauth import oauth_google, callback
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
    
    @app.route("/oauth_google")
    def oauth_google_route():
        return oauth_google()

    @app.route("/callback", methods=["GET"])
    def callback_route():
        code = request.args.get('code')
        return callback(code)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            return handle_login(request)
        return render_template("login.html")
    
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
    