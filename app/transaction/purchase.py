from decimal import Decimal
from datetime import datetime

from app.db.crypto_wallet_db import update_crypto_wallet
from app.db.fiat_wallet_db import update_fiat_wallet

def process_crypto_purchase(user_id, wallet, fiat_wallet, form_data):
    if wallet is None:
        print(f"[DEBUG] No crypto wallet found for user_id: {user_id}")
        return False, ('No crypto wallet found for the user.', 'error')

    if fiat_wallet is None:
        print(f"[DEBUG] No fiat wallet found for user_id: {user_id}")
        return False, ('No fiat wallet found for the user.', 'error')

    try:
        coin = form_data['coin-selection']
        amount = form_data['coin-amount']
        amount = Decimal(amount)

        print(f"[DEBUG] Coin selected: {coin}, Amount to purchase: {amount}")

        print(f"[DEBUG] Adding {amount} {coin} to crypto wallet.")
        wallet.add_coins(coin, amount, datetime.now())
        wallet.add_deposit_to_history(datetime.now(), amount)
        wallet.calculate_total_coin_value()
        wallet.update_last_accessed()
        # fiat_wallet.decrease_wallet_balance(amount)
        update_crypto_wallet(wallet)
        update_fiat_wallet(fiat_wallet)

        print(f"[DEBUG] Updated crypto wallet: {wallet}")
        print(f"[DEBUG] Updated fiat wallet: {fiat_wallet}")
        
        return True, (f'Successfully purchased {amount} {coin}', 'success')
    
    except Exception as e:
        print(f"[DEBUG] Error occurred: {e}")
        return False, ('An error occurred during the purchase process. Please try again.', 'error')
