from os import path

def get_db_host():
    if path.exists("/.dockerenv"):
        return "host.docker.internal"  
    else:
        return "localhost"  

class Config:
    USER_DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": get_db_host(),  
        "port": 3306,  
        "database": "marketplace_users"
    }

    COIN_DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": get_db_host(),  
        "port": 3306,
        "database": "marketplace_coins"
    }

    WALLET_DB_CONFIG = {
        "user": "root",
        "password": "root",
        "host": get_db_host(), 
        "port": 3306,
        "database": "marketplace_wallets"
    }
