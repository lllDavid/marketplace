from app.wallets.crypto.crypto_wallet import CryptoWallet
from app.db.crypto_wallet_db import insert_crypto_wallet
from app.db.user_db import get_complete_user

def create_cryto_wallet(user_id) -> CryptoWallet | None:
    user = get_complete_user(user_id)
    if user is not None:
        wallet_id = None
        wallet_address=None
        coins= {}
        total_coin_value = None
        last_accessed= None
        encryption_key= None
        deposit_history= {}
        withdrawal_history= {}

        wallet = CryptoWallet(
            user_id= user.id,
            wallet_id=wallet_id,
            wallet_address=wallet_address,
            coins=coins,
            total_coin_value=total_coin_value,
            deposit_history=deposit_history,
            withdrawal_history=withdrawal_history,
            last_accessed=last_accessed,
            encryption_key=encryption_key
        )
        insert_crypto_wallet(wallet)
        
        return wallet
    