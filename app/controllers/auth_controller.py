from datetime import datetime

from flask import render_template, redirect, url_for, flash, session

from app.user.user_security import UserSecurity
from app.db.crypto_wallet_db import delete_crypto_wallet
from app.db.fiat_wallet_db import delete_fiat_wallet
from helpers.validation import is_valid_password, is_unique_username, is_unique_email
from app.db.user_db import update_username, update_email, update_password, update_user_bank, get_complete_user,get_user_bank, get_user_by_id, get_user_by_email, get_user_by_username, delete_user

def handle_login(request):
    oauth_token = session.get('oauth_token')
    
    if oauth_token:
        user_info = session.get('user_info')
        if user_info:
            email = user_info.get('email')
            user = get_user_by_email(email)
            '''
            if not user:
                user = User(
                    username=user_info.get('name'),
                    email=email,
                    oauth_provider='google',
                )
                save_user(user) 
                '''
            if user:
                session["user_id"] = user.id
                session["username"] = user.username
                session["email"] = user.email
                session.modified = True
            
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))  
    
    username = request.form.get("username")
    password = request.form.get("password")

    user = get_user_by_username(username)
    if user and UserSecurity.validate_password_hash(password, user.user_security.password_hash):
        session["user_id"] = user.id
        session["username"] = user.username
        session["email"] = user.email
        session.modified = True
        
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))

def handle_logout():
    session.pop("user_id", None)
    session.pop("username", None)
    session.pop("email", None)
    session.clear() 
    return redirect(url_for("index"))

def check_authentication():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return None

def get_authenticated_user(user_id):
    return get_user_by_id(user_id)

def update_current_username(user_id, new_username):
    if is_unique_username(new_username):
        update_username(user_id, new_username)
        session["username"] = new_username
    else:
        flash("The new username is not valid. Please try again.", "error")

def update_current_email(user_id, new_email):
    if is_unique_email(new_email):
        update_email(user_id, new_email)
        session["email"] = new_email
    else:
        flash("The new email is not valid. Please try again.", "error")

def update_current_password(user_id, new_password):
    if is_valid_password(new_password):
        update_password(user_id, new_password)
    else:
        flash("The new password is not valid. Please try again.", "error")

def delete_user_account(user_id):
    try:
        delete_crypto_wallet(user_id)
        delete_fiat_wallet(user_id)
        delete_user(user_id)
        flash('Your account has been successfully deleted.', 'success')
        return redirect(url_for("login"))
    except Exception as e:
        print("Error: ", e)
        flash("An error occurred while deleting your account. Please try again.", "error")
        return redirect(url_for("settings"))

from datetime import datetime
from flask import request, redirect, render_template, flash, url_for, session


def handle_settings(request):
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    user_id = session["user_id"]
    user = get_authenticated_user(user_id)
    if not user:
        return redirect(url_for("login"))

    current_username = session.get("username")
    current_email = user.email

    if request.method == "POST":
        if 'delete-account' in request.form:
            return delete_user_account(user_id)

        handle_user_info_update(request, user_id)

        handle_bank_info_update(request, user_id)

        user = get_user_by_id(user_id)

        flash('Your account settings have been updated successfully.', 'success')
        return redirect(url_for("settings"))

    return render_template("settings.html", username=current_username, email=current_email, user=user)


def handle_user_info_update(request, user_id):
    new_username = request.form.get("username")
    new_email = request.form.get("email")
    new_password = request.form.get("new-password")

    if new_username:
        update_current_username(user_id, new_username)

    if new_email:
        update_current_email(user_id, new_email)

    if new_password:
        update_current_password(user_id, new_password)


def handle_bank_info_update(request, user_id):
    new_bank_name = request.form.get("bank_name")
    new_account_holder = request.form.get("bank_account_holder")
    new_account_number = request.form.get("account_number")
    new_routing_number = request.form.get("routing_number")
    new_iban = request.form.get("iban")
    new_swift_code = request.form.get("swift")

    user_bank = get_user_bank(user_id)

    if user_bank:
        if not any([new_bank_name, new_account_holder, new_account_number, new_routing_number, new_iban, new_swift_code]):
            if not user_bank.date_linked:
                user_bank.date_linked = datetime.now()

        if new_bank_name:
            user_bank.bank_name = new_bank_name
            update_user_bank(user_id, user_bank)

        if new_account_holder:
            user_bank.account_holder = new_account_holder
            update_user_bank(user_id, user_bank)

        if new_account_number:
            user_bank.account_number = new_account_number
            update_user_bank(user_id, user_bank)

        if new_routing_number:
            user_bank.routing_number = new_routing_number
            update_user_bank(user_id, user_bank)

        if new_iban:
            user_bank.iban = new_iban
            update_user_bank(user_id, user_bank)

        if new_swift_code:
            user_bank.swift_code = new_swift_code
            update_user_bank(user_id, user_bank)

def handle_deposit():
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    user_id = session["user_id"]
    user = get_authenticated_user(user_id)
    
    if not user:
        return redirect(url_for("login"))

    account_holder_data = get_complete_user(session["user_id"])

    if account_holder_data is not None and account_holder_data.user_bank:
        account_holder = account_holder_data.user_bank.account_holder
    else:
        account_holder = None

    return render_template("deposit.html", account_holder=account_holder)


    

    
    

