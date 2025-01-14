from dataclasses import dataclass
from decimal import Decimal

from app.coin.coin_specs import CoinSpecs
from app.coin.coin_market_data import CoinMarketData

@dataclass
class Coin:
    id: int | None 
    name: str
    symbol: str
    category: str
    description: str
    price: Decimal
    coin_specs: CoinSpecs 
    coin_market_data: CoinMarketData 

    def update_name(self, new_name: str):
        self.name = new_name

    def update_symbol(self, new_symbol: str):
        self.symbol = new_symbol

    def update_category(self, new_category: str):
        self.category = new_category

    def update_description(self, new_description: str):
        self.description = new_description

    def update_price(self, new_price: Decimal):
        self.price = new_price

    def update_coin_specs(self, new_coin_specs: CoinSpecs):
        self.coin_specs = new_coin_specs
    
    def update_coin_market_data(self, new_coin_market_data: CoinMarketData):
        self.coin_market_data = new_coin_market_data



