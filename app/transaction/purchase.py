import traceback
from decimal import Decimal
from datetime import datetime

from app.db.crypto_wallet_db import update_crypto_wallet
from app.db.fiat_wallet_db import update_fiat_wallet

def process_crypto_purchase(crypto_wallet, fiat_wallet, form_data):
    if crypto_wallet is None:
        return False, ('No crypto wallet found for the user.', 'error')

    if fiat_wallet is None:
        return False, ('No fiat wallet found for the user.', 'error')
    
    try:
        coin = form_data['coin-selection']
        coin_amount = form_data['coin-amount']
        coin_amount = Decimal(coin_amount)
        coin_cost = form_data['total-cost']
        coin_cost = coin_cost.replace('$', '').replace(',', '').strip()
        coin_cost = Decimal(coin_cost)

        if not fiat_wallet.has_sufficient_funds(coin_cost):
            formatted_balance = f"{fiat_wallet.balance:.2f}"
            return False, (f'Insufficient balance: ${formatted_balance}', 'danger')

        else:
            crypto_wallet.add_coins(coin, coin_amount, datetime.now())
            crypto_wallet.calculate_total_coin_value()
            crypto_wallet.update_last_accessed()
            fiat_wallet.update_last_accessed()
            fiat_wallet.decrease_wallet_balance(coin_cost)
            update_crypto_wallet(crypto_wallet)
            update_fiat_wallet(fiat_wallet)
        
            return True, (f'Successfully bought {coin_amount} {coin} for ${coin_cost}', 'success')
    

    except Exception as e:
        error_details = traceback.format_exc()
        print(error_details)
        return False, ('An error occurred during the purchase process. Please try again.', 'error')