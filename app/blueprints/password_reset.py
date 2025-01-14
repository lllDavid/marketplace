from os import getenv
from dotenv import load_dotenv

from flask import Blueprint, render_template, redirect, url_for, flash, request
from itsdangerous import URLSafeTimedSerializer

from app.user.user_security import UserSecurity
from app.db.user_db import update_password, get_user_by_email
from helpers.validation import is_valid_password


load_dotenv()

reset_password = Blueprint('reset_password', __name__)

SECRET_KEY = getenv('URL_STS_SECRET_KEY')
if SECRET_KEY:
    s = URLSafeTimedSerializer(SECRET_KEY)
else:
    print("Not secret key provided")

TOKEN_EXPIRATION_TIME = 3600  

def send_reset_email(to_email, reset_url):
    from app import mail
    from flask_mail import Message
    msg = Message(
        'Password Reset Request',
        sender=getenv('GMAIL_ADDRESS'),
        recipients=[to_email]
    )
    msg.body = f'Click the link to reset your password: {reset_url}'
    mail.send(msg)

@reset_password.route('/reset-password', methods=['GET', 'POST'])
def reset_user_password():
    if request.method == 'POST':
        email = request.form['email']
        token = s.dumps(email, salt="reset-password")
        reset_url = url_for('reset_password.reset_user_password_token', token=token, _external=True)
        send_reset_email(email, reset_url)
        flash('A password reset link has been sent to your email!', 'success')
        return redirect(url_for('reset_password.reset_user_password'))
    
    return render_template('reset-password.html')

@reset_password.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_user_password_token(token):
    try:
        email = s.loads(token, salt="reset-password", max_age=TOKEN_EXPIRATION_TIME)
    except Exception:
        flash('The password reset link is invalid or has expired.', 'danger')
        return redirect(url_for('reset_password.reset_user_password'))

    user = get_user_by_email(email)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('reset_password.reset_user_password'))

    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_new_password = request.form['confirm_new_password']

        if not UserSecurity.validate_password_hash(old_password, user.user_security.password_hash):
            flash('Incorrect old password.', 'danger')
            return render_template('reset-password-token.html', token=token)

        if new_password != confirm_new_password:
            flash('New password and confirmation do not match.', 'danger')
            return render_template('reset-password-token.html', token=token)

        if is_valid_password(new_password) and is_valid_password(confirm_new_password):
            hashed_password = UserSecurity.hash_password(new_password)
            if user.id:
                update_password(user.id, hashed_password)

            flash('Your password has been updated successfully!', 'success')
            return redirect(url_for('login'))

    return render_template('reset-password-token.html', token=token)
