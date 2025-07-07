import os
from dotenv import load_dotenv

load_dotenv()

def get_db_host():
    if os.path.exists("/.dockerenv"):
        return os.getenv("DOCKER_DB_HOST", "db")
    else:
        return os.getenv("LOCAL_DB_HOST", "localhost")

class Config:
    USER_DB_CONFIG = {
        "user": os.getenv("USER_DB_USER", ""),
        "password": os.getenv("USER_DB_PASSWORD", ""),
        "host": get_db_host(),
        "port": int(os.getenv("USER_DB_PORT", 3306)),
        "database": os.getenv("USER_DB_NAME", "marketplace_users")
    }

    COIN_DB_CONFIG = {
        "user": os.getenv("COIN_DB_USER", ""),
        "password": os.getenv("COIN_DB_PASSWORD", ""),
        "host": get_db_host(),
        "port": int(os.getenv("COIN_DB_PORT", 3306)),
        "database": os.getenv("COIN_DB_NAME", "marketplace_coins")
    }

    WALLET_DB_CONFIG = {
        "user": os.getenv("WALLET_DB_USER", ""),
        "password": os.getenv("WALLET_DB_PASSWORD", ""),
        "host": get_db_host(),
        "port": int(os.getenv("WALLET_DB_PORT", 3306)),
        "database": os.getenv("WALLET_DB_NAME", "marketplace_wallets")
    }