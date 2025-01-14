from flask import Blueprint, render_template, redirect, url_for, session, jsonify

from app.db.crypto_wallet_db import get_crypto_wallet_by_user_id
from app.controllers.auth_controller import check_authentication

from app.db.crypto_wallet_db import get_crypto_wallet_by_user_id

wallet_values = Blueprint('wallet_values', __name__)

@wallet_values.route('/wallet', methods=['GET'])
def create_wallet_form():
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response

    return render_template('wallet.html')

@wallet_values.route('/wallet/values', methods=['GET'])
def get_wallet_values():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))

    user_wallet = get_crypto_wallet_by_user_id(user_id)

    if user_wallet:
        mock_prices = {
            'BTC': 950000,
            'ETH': 3000,
            'LTC': 150
        }

        wallet_data = {}

        for coin, amount in user_wallet.coins.items():
            if coin in mock_prices:
                current_price = mock_prices[coin]
                coin_value = current_price * amount
                wallet_data[coin] = {
                    'amount': amount,
                    'current_price': current_price,
                    'total_value': coin_value
                }

        return jsonify({'coins': wallet_data})
    else:
        return redirect(url_for('login'))

