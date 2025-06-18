from flask import Blueprint, render_template, redirect, url_for, flash, session, request

from app.db.fiat_wallet_db import get_fiat_wallet_by_user_id
from app.db.crypto_wallet_db import get_crypto_wallet_by_user_id
from app.transaction.liquidation import process_crypto_liquidation
from app.controllers.auth_controller import check_authentication

crypto_liquidation = Blueprint('crypto_liquidation', __name__)

@crypto_liquidation.route('/trade/sell', methods=['GET'])
def create_trade_form():
    redirect_response = check_authentication()
    if redirect_response:
        return redirect_response
        
    return render_template('trade.html')

@crypto_liquidation.route('/trade/sell', methods=['POST'])
def liquidate_crypto():
    user_id = session.get('user_id')
    if user_id is None:
        flash('You must be logged in to perform this action.', 'error')
        return redirect(url_for('login'))
    
    try:
        fiat_wallet = get_fiat_wallet_by_user_id(user_id)
        crypto_wallet = get_crypto_wallet_by_user_id(user_id)

        success, message = process_crypto_liquidation(crypto_wallet, fiat_wallet, request.form)

        flash(message[0], message[1])
        return redirect(url_for('trade'))

    except Exception as e:
        flash('An error occurred during the sale process. Please try again.', 'error')
        return redirect(url_for('trade'))
