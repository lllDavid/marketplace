import traceback
from decimal import Decimal
from datetime import datetime

from app.db.crypto_wallet_db import update_crypto_wallet
from app.db.fiat_wallet_db import update_fiat_wallet

def process_crypto_liquidation(crypto_wallet, fiat_wallet, form_data):
    if crypto_wallet is None:
        return False, ('No crypto wallet found for the user.', 'error')

    if fiat_wallet is None:
        return False, ('No fiat wallet found for the user.', 'error')

    try:
        coin = form_data['coin-selection']
        coin_amount = form_data['coin-amount']
        coin_amount = Decimal(coin_amount)
        coin_worth = form_data['total-worth']
        coin_worth = coin_worth.replace('$', '').replace(',', '').strip()
        coin_worth = Decimal(coin_worth)

        available_amount = crypto_wallet.coins.get(coin, Decimal('0'))
        if coin_amount > available_amount:
              rounded_available = available_amount.quantize(Decimal('0.00000001'))
              return False, (f'Insufficient balance: {rounded_available} {coin}.', 'error')
        else:
            crypto_wallet.remove_coins(coin, coin_amount, datetime.now(), "")
            crypto_wallet.calculate_total_coin_value()
            crypto_wallet.update_last_accessed()
            fiat_wallet.update_last_accessed()
            fiat_wallet.increase_wallet_balance(coin_worth)
            update_crypto_wallet(crypto_wallet)
            update_fiat_wallet(fiat_wallet)
            
            return True, (f'Successfully sold {coin_amount} {coin} for ${coin_worth}', 'success')

    except Exception as e:
        error_details = traceback.format_exc()
        print(error_details)
        return False, ('An error occurred during the purchase process. Please try again.', 'error')

