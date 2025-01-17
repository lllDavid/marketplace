from mariadb import ConnectionPool

from config import Config
from app.coin.coin import Coin
from app.coin.coin_specs import CoinSpecs
from app.coin.coin_market_data import CoinMarketData

pool = ConnectionPool(
    pool_name="coin_db_pool",
    pool_size=10,
    user=Config.COIN_DB_CONFIG["user"],
    password=Config.COIN_DB_CONFIG["password"],
    host=Config.COIN_DB_CONFIG["host"],
    port=Config.COIN_DB_CONFIG["port"],
    database=Config.COIN_DB_CONFIG["database"]
)

# --------------------------------------------------------------
# Section 1: Insert, Update and Delete Coin Data
# --------------------------------------------------------------

def insert_coin(coin: Coin) -> Coin | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO coin (name, symbol, category, description, price) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (coin.name, coin.symbol, coin.category, coin.description, coin.price)
                )

                coin_id = cursor.lastrowid

                cursor.execute(
                    "INSERT INTO coin_specs (coin_id, algorithm, consensus_mechanism, blockchain_network, average_block_time, "
                    "security_features, privacy_features, max_supply, genesis_block_date, token_type, governance_model, "
                    "development_activity, hard_cap, forking_coin, tokenomics) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (coin_id,
                        coin.coin_specs.algorithm, coin.coin_specs.consensus_mechanism, coin.coin_specs.blockchain_network, coin.coin_specs.average_block_time,
                        coin.coin_specs.security_features, coin.coin_specs.privacy_features, coin.coin_specs.max_supply, coin.coin_specs.genesis_block_date,
                        coin.coin_specs.token_type, coin.coin_specs.governance_model, coin.coin_specs.development_activity, coin.coin_specs.hard_cap,
                        coin.coin_specs.forking_coin, coin.coin_specs.tokenomics
                    )
                )

                cursor.execute(
                    "INSERT INTO coin_market_data (coin_id, rank, price_usd, market_cap_usd, volume_24h_usd, high_24h_usd, low_24h_usd, "
                    "change_24h_percent, all_time_high, all_time_low, circulating_supply, market_dominance, "
                    "last_updated) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (coin_id,
                        coin.coin_market_data.rank, coin.coin_market_data.price_usd, coin.coin_market_data.market_cap_usd, coin.coin_market_data.volume_24h_usd,
                        coin.coin_market_data.high_24h_usd, coin.coin_market_data.low_24h_usd, coin.coin_market_data.change_24h_percent,
                        coin.coin_market_data.all_time_high, coin.coin_market_data.all_time_low, coin.coin_market_data.circulating_supply,
                        coin.coin_market_data.market_dominance, coin.coin_market_data.last_updated
                    )
                )

                conn.commit()  
                print("Coin inserted into the database.")
                coin.id = coin_id
                return coin
    except Exception as e:
        print(f"Error occurred: {e}")
        return None 

def update_coin(coin: Coin) -> Coin | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE coin SET name = %s, symbol = %s, category = %s, description = %s, price = %s WHERE id = %s",
                    (coin.name, coin.symbol, coin.category, coin.description, coin.price, coin.id)
                )

                cursor.execute(
                    "UPDATE coin_specs SET algorithm = %s, consensus_mechanism = %s, blockchain_network = %s, "
                    "average_block_time = %s, security_features = %s, privacy_features = %s, max_supply = %s, "
                    "genesis_block_date = %s, token_type = %s, governance_model = %s, development_activity = %s, "
                    "hard_cap = %s, forking_coin = %s, tokenomics = %s WHERE coin_id = %s",
                    (coin.coin_specs.algorithm, coin.coin_specs.consensus_mechanism, coin.coin_specs.blockchain_network,
                     coin.coin_specs.average_block_time, coin.coin_specs.security_features, coin.coin_specs.privacy_features,
                     coin.coin_specs.max_supply, coin.coin_specs.genesis_block_date, coin.coin_specs.token_type,
                     coin.coin_specs.governance_model, coin.coin_specs.development_activity, coin.coin_specs.hard_cap,
                     coin.coin_specs.forking_coin, coin.coin_specs.tokenomics, coin.id)
                )

                cursor.execute(
                    "UPDATE coin_market_data SET rank = %s, price_usd = %s, market_cap_usd = %s, volume_24h_usd = %s, "
                    "high_24h_usd = %s, low_24h_usd = %s, change_24h_percent = %s, all_time_high = %s, "
                    "all_time_low = %s, circulating_supply = %s, market_dominance = %s, last_updated = %s WHERE coin_id = %s",
                    (coin.coin_market_data.rank, coin.coin_market_data.price_usd, coin.coin_market_data.market_cap_usd,
                     coin.coin_market_data.volume_24h_usd, coin.coin_market_data.high_24h_usd,
                     coin.coin_market_data.low_24h_usd, coin.coin_market_data.change_24h_percent,
                     coin.coin_market_data.all_time_high, coin.coin_market_data.all_time_low,
                     coin.coin_market_data.circulating_supply, coin.coin_market_data.market_dominance,
                     coin.coin_market_data.last_updated, coin.id)
                )

                conn.commit()  
                print("Coin updated successfully.")
                return coin
    except Exception as e:
        print(f"Error occurred while updating coin: {e}")
        return None
    
def delete_coin(coin_id: int) -> None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM coin_market_data WHERE coin_id = %s", (coin_id,))
                cursor.execute("DELETE FROM coin_specs WHERE coin_id = %s", (coin_id,))
                cursor.execute("DELETE FROM coin WHERE id = %s", (coin_id,))
                conn.commit()
                print(f"Coin with ID {coin_id} deleted successfully.")
    except Exception as e:
        print(f"Error occurred while deleting coin with ID {coin_id}: {e}")

# --------------------------------------------------------------
# Section 2: Coin Retrieval by Specific Criteria
# --------------------------------------------------------------

def get_coin_by_id(id: int) -> Coin | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name, symbol, category, description, price FROM coin WHERE id = %s", (id,))
                coin = cursor.fetchone()

        if coin:
            return get_complete_coin(coin[0])
        return None
    except Exception as e:
        print(f"Error retrieving coin by ID: {e}")
        return None

def get_coin_by_symbol(symbol: str) -> Coin | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name, symbol, category, description, price FROM coin WHERE symbol = %s", (symbol,))
                coin = cursor.fetchone()

        if coin:
            return get_complete_coin(coin[0])
        return None
    except Exception as e:
        print(f"Error retrieving coin by symbol: {e}")
        return None

def get_coin_by_name(name: str) -> Coin | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name, symbol, category, description, price FROM coin WHERE name = %s", (name,))
                coin = cursor.fetchone()

        if coin:
            return get_complete_coin(coin[0])
        return None
    except Exception as e:
        print(f"Error retrieving coin by name: {e}")
        return None

# --------------------------------------------------------------
# Section 3: Coin Components Retrieval by Coin ID
# --------------------------------------------------------------

def get_coin(coin_id: int):
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name, symbol, category, description, price FROM coin WHERE id = %s", (coin_id,))
                coin_data = cursor.fetchone()

        if coin_data:
            return coin_data
        return None
    except Exception as e:
        print(f"Error retrieving coin data: {e}")
        return None

def get_coin_specs(coin_id: int) -> CoinSpecs | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT algorithm, consensus_mechanism, blockchain_network, average_block_time, security_features, "
                    "privacy_features, max_supply, genesis_block_date, token_type, governance_model, development_activity, "
                    "hard_cap, forking_coin, tokenomics FROM coin_specs WHERE coin_id = %s", (coin_id,)
                )
                specs = cursor.fetchone()

        if specs:
            return CoinSpecs(*specs)
        return None
    except Exception as e:
        print(f"Error retrieving coin specs: {e}")
        return None

def get_coin_market_data(coin_id: int) -> CoinMarketData | None:
    try:
        with pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT rank, price_usd, market_cap_usd, volume_24h_usd, high_24h_usd, low_24h_usd, change_24h_percent, "
                    "all_time_high, all_time_low, circulating_supply, market_dominance, last_updated "
                    "FROM coin_market_data WHERE coin_id = %s", (coin_id,)
                )
                market_data = cursor.fetchone()

        if market_data:
            return CoinMarketData(*market_data)
        return None
    except Exception as e:
        print(f"Error retrieving coin market data: {e}")
        return None

# --------------------------------------------------------------
# Section 4: Complete Coin Retrieval
# --------------------------------------------------------------

def get_complete_coin(coin_id: int) -> Coin | None:
    try:
        coin_data = get_coin(coin_id)
        if not coin_data:
            return None

        coin_specs = get_coin_specs(coin_id)
        if not coin_specs:
            return None

        coin_market_data = get_coin_market_data(coin_id)
        if not coin_market_data:
            return None

        return Coin(
            id=coin_id,
            name=coin_data[1],
            symbol=coin_data[2],
            category=coin_data[3],
            description=coin_data[4],
            price=coin_data[5],
            coin_specs=coin_specs,
            coin_market_data=coin_market_data
        )
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
