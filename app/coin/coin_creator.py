from decimal import Decimal
from datetime import datetime

from app.db import coin_db
from app.coin.coin import Coin
from app.coin.coin_specs import CoinSpecs
from app.coin.coin_market_data import CoinMarketData

class CoinCreator:
    def create_coin_specs(self, 
                          algorithm: str, 
                          consensus_mechanism: str, 
                          blockchain_network: str, 
                          average_block_time: Decimal, 
                          security_features: str, 
                          privacy_features: str, 
                          max_supply: Decimal, 
                          genesis_block_date: str, 
                          token_type: str, 
                          governance_model: str, 
                          development_activity: str, 
                          hard_cap: Decimal, 
                          forking_coin: str, 
                          tokenomics: str) -> CoinSpecs:
        return CoinSpecs(
            algorithm=algorithm,
            consensus_mechanism=consensus_mechanism,
            blockchain_network=blockchain_network,
            average_block_time=average_block_time,
            security_features=security_features,
            privacy_features=privacy_features,
            max_supply=max_supply,
            genesis_block_date=genesis_block_date,
            token_type=token_type,
            governance_model=governance_model,
            development_activity=development_activity,
            hard_cap=hard_cap,
            forking_coin=forking_coin,
            tokenomics=tokenomics
        )
  
    def create_coin_market_data(self, 
                                 rank: int, 
                                 price_usd: Decimal, 
                                 market_cap_usd: Decimal, 
                                 volume_24h_usd: Decimal, 
                                 high_24h_usd: Decimal, 
                                 low_24h_usd: Decimal, 
                                 change_24h_percent: Decimal, 
                                 all_time_high: Decimal, 
                                 all_time_low: Decimal, 
                                 circulating_supply: Decimal, 
                                 market_dominance: Decimal, 
                                 last_updated: datetime) -> CoinMarketData:
        return CoinMarketData(
            rank=rank,
            price_usd=price_usd,
            market_cap_usd=market_cap_usd,
            volume_24h_usd=volume_24h_usd,
            high_24h_usd=high_24h_usd,
            low_24h_usd=low_24h_usd,
            change_24h_percent=change_24h_percent,
            all_time_high=all_time_high,
            all_time_low=all_time_low,
            circulating_supply=circulating_supply,
            market_dominance=market_dominance,
            last_updated=last_updated
        )

    def create_coin(self, 
                    name: str, 
                    symbol: str, 
                    category: str, 
                    description: str, 
                    price: Decimal, 
                    coin_specs: CoinSpecs, 
                    coin_market_data: CoinMarketData) -> Coin:
        try: 
            coin = Coin(
                id=None,
                name=name, 
                symbol=symbol, 
                category=category,
                description=description, 
                price=price,
                coin_specs=coin_specs,
                coin_market_data=coin_market_data
            )
            return coin
    
        except Exception as e:
                print(f"Error: {e}")
                raise ValueError("Coin couldn't be created")  
    
    def save_user(self, coin):
        try:
            coin_db.insert_coin(coin)  
        except Exception as e:
            print(f"Error: {e}")
            raise ValueError("Coin couldn't be saved to database.")
