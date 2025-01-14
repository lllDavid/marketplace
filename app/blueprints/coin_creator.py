from flask import Blueprint, render_template, redirect, url_for, flash, request, session

from app.coin.coin_creator import CoinCreator

coin_creator = Blueprint('coin_creator', __name__)