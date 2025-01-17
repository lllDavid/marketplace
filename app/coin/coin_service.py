from requests import get
from decimal import Decimal
from dataclasses import dataclass

from app.coin.coin_market_data import CoinMarketData

@dataclass
class CoinService:
    api_url = str
    # Mock feature
    def fetch_coin_data(self, coin_id: str) -> CoinMarketData:
        response = get(f"{self.api_url}/coins/{coin_id}")
        data = response.json()
        
        return CoinMarketData(
            rank=data['market_data']['rank'],
            price_usd=Decimal(data['market_data']['current_price']['usd']),
            market_cap_usd=Decimal(data['market_data']['market_cap']['usd']),
            volume_24h_usd=Decimal(data['market_data']['total_volume']['usd']),
            high_24h_usd=Decimal(data['market_data']['high_24h']['usd']),
            low_24h_usd=Decimal(data['market_data']['low_24h']['usd']),
            change_24h_percent=Decimal(data['market_data']['price_change_percentage_24h']),
            all_time_high=Decimal(data['market_data']['ath']['usd']),
            all_time_low=Decimal(data['market_data']['atl']['usd']),
            circulating_supply=Decimal(data['market_data']['circulating_supply']),
            market_dominance=Decimal(data['market_data']['market_cap_percentage']['usd']),
            last_updated=data['last_updated']
        )
