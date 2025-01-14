from re import match

from flask import flash
from mariadb import connect

from config import Config

conn = connect(
    user=Config.USER_DB_CONFIG["user"],
    password=Config.USER_DB_CONFIG["password"],
    host=Config.USER_DB_CONFIG["host"],
    port=Config.USER_DB_CONFIG["port"],
    database=Config.USER_DB_CONFIG["database"]
)

def is_unique_username(username: str) -> bool:
    cursor = conn.cursor()
    cursor.execute("""SELECT username FROM user WHERE username = %s""", (username,))
    username = cursor.fetchone()
    cursor.close()
    return username is None

def is_unique_email(email: str) -> bool:
    cursor = conn.cursor()
    cursor.execute("""SELECT email FROM user WHERE email = %s""", (email,))
    email = cursor.fetchone()
    cursor.close()
    return email is None

def is_unique_user_and_email(username: str, email: str):
    cursor = conn.cursor()
    cursor.execute(""" 
        SELECT username, email FROM user WHERE username = %s OR email = %s """, (username, email))
    user = cursor.fetchone()
    cursor.close()

    if user:
        if user[0] == username:
            return "username"
        elif user[1] == email:
            return "email"
    return None

def is_valid_username(username):
    if len(username) < 3 or len(username) > 20:
        return "Username must be between 3 and 20 characters long."
    
    if not match(r'^[A-Za-z0-9_-]+$', username):
        return "Username contains invalid characters."

    if username != username.strip():
        return "Username cannot have leading or trailing spaces."

    reserved_words = ['admin', 'support', 'root', 'superuser', 'localhost']
    if username.lower() in reserved_words:
        return "Username contains restricted terms."

    sql_keywords = ['select', 'insert', 'delete', 'drop', 'update', 'truncate', 'union', 'where', 'from', 'alter', 'join', 'drop']
    if any(keyword in username.lower() for keyword in sql_keywords):
        return "Username contains restricted terms."

    linux_commands = ['ls', 'rm', 'cat', 'chmod', 'chown', 'touch', 'mkdir', 'rmdir', 'sudo', 'passwd', 'shutdown', 'reboot', 'halt', 'ping', 'ps', 'kill', 'ifconfig', 'df', 'mount']
    if any(command in username.lower() for command in linux_commands):
        return "Username contains restricted terms."

    return True

def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(match(email_regex, email))

def is_valid_password(password: str) -> bool:
    password = password.strip()

    if len(password) > 40:
        return False

    regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_])[\s\S]{30,}$'

    if not match(regex, password):
        return False

    return True

def validate_user_input(username, email, password):
    if not all([username, email, password]):
        flash("All fields are required!", "error")
        return False
    
    user_status = is_unique_user_and_email(username, email)
    
    if user_status == "username":
        flash("Username is already taken.", "error")
        return False
    elif user_status == "email":
        flash("Email is already taken.", "error")
        return False
    
    username_validation = is_valid_username(username)
    if username_validation != True:
        flash(username_validation, "error")
        return False

    if not is_valid_email(email):
        flash("Invalid email format.", "error")
        return False

    if not is_valid_password(password):
        flash("Password must be between 30 and 40 characters, contain an uppercase letter, a number, and a special character.", "error")
        return False
    
    return True