from decimal import Decimal
from datetime import datetime

from app.db.crypto_wallet_db import update_crypto_wallet
from app.db.fiat_wallet_db import update_fiat_wallet

def process_crypto_liquidation(user_id, wallet, fiat_wallet, form_data):
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

        print(f"[DEBUG] Coin selected: {coin}, Amount to sell: {amount}")

        print(f"[DEBUG] Removing {amount} {coin} from crypto wallet.")
        wallet.remove_coins(coin, amount, datetime.now(), "")
        wallet.add_withdrawal_to_history(datetime.now(), amount, method="crypto_withdraw")
        wallet.calculate_total_coin_value()
        wallet.update_last_accessed()
        # fiat_wallet.increase_wallet_balance(amount)
        update_crypto_wallet(wallet)
        update_fiat_wallet(fiat_wallet)
        
        print(f"[DEBUG] Updated crypto wallet after sell: {wallet}")
        print(f"[DEBUG] Updated fiat wallet: {fiat_wallet}")
        
        return True, (f'Successfully sold {amount} {coin}', 'success')

    except Exception as e:
        print(f"[DEBUG] Error occurred: {e}")
        return False, ('An error occurred during the sale process. Please try again.', 'error')
