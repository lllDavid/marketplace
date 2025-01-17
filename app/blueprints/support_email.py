from os import getenv
from dotenv import load_dotenv

from flask import Blueprint, render_template, redirect, url_for, flash,  request, session
from app.controllers.auth_controller import check_authentication

load_dotenv()

support_email = Blueprint('support_email', __name__)

SUPPORT_EMAIL = getenv('SUPPORT_EMAIL')

def send_email(to_email, user_email, subject, message):
    from flask_mail import Message
    from app import mail
    msg = Message(
        subject=subject,
        sender=user_email,
        recipients=[to_email]
    )
    msg.body = f"Message from: {user_email}\n\nUser's Message:\n{message}"
    mail.send(msg)

@support_email.route('/support', methods=['GET'])
def create_support_form():
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response
    return render_template('support.html')

@support_email.route('/support', methods=['POST'])
def send_support_email():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))

    subject = request.form['subject']
    user_email = request.form['email']
    message = request.form['message']

    send_email(SUPPORT_EMAIL, user_email, subject, message)

    flash('Message has been sent to support! We will get back to you shortly.', 'success')
    return redirect(url_for('support'))
