from os import urandom
from os import getenv
from dotenv import load_dotenv

from flask import Flask  
from flask_mail import Mail
from flask_wtf import CSRFProtect
from authlib.integrations.flask_client import OAuth

from config import Config
from app.blueprints.user_creator import user_creator
from app.blueprints.crypto_purchase import crypto_purchase
from app.blueprints.crypto_liquidation import crypto_liquidation
from app.blueprints.wallet_values import wallet_values
from app.blueprints.password_reset import reset_password
from app.blueprints.support_email import support_email
from app.routes.routes import register_routes

load_dotenv()

csrf = CSRFProtect()  

mail = Mail()

def create_app() -> Flask:
    marketplace = Flask(__name__, static_folder="static", template_folder="templates")
    oauth = OAuth(marketplace)
    csrf.init_app(marketplace)
    marketplace.secret_key = getenv('APP_SECRET_KEY', urandom(24)) # Fallback to urandom if not found
    marketplace.config.from_object(Config)
    marketplace.config.from_object(Config)

    google = oauth.register(
        name='google',
        client_id=getenv('GOOGLE_CLIENT_ID'),
        client_secret=getenv('GOOGLE_CLIENT_SECRET'),
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        access_token_url='https://accounts.google.com/o/oauth2/token',
        refresh_token_url=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        client_kwargs={'scope': 'openid profile email'},
        jwks_uri="https://www.googleapis.com/oauth2/v3/certs",
        userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo'
    )

    marketplace.google = google

    marketplace.config['MAIL_SERVER'] = 'smtp.gmail.com' 
    marketplace.config['MAIL_PORT'] = 587
    marketplace.config['MAIL_USE_TLS'] = True
    marketplace.config['MAIL_USERNAME'] = getenv('GMAIL_ADDRESS')  
    marketplace.config['MAIL_PASSWORD'] = getenv('GMAIL_PASSWORD') 

    mail.init_app(marketplace)

    marketplace.register_blueprint(user_creator)
    marketplace.register_blueprint(wallet_values)
    marketplace.register_blueprint(crypto_purchase)
    marketplace.register_blueprint(crypto_liquidation)
    marketplace.register_blueprint(reset_password)
    marketplace.register_blueprint(support_email)
            
    register_routes(marketplace)

    return marketplace
