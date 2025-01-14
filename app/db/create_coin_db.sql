CREATE DATABASE marketplace_coins;
USE marketplace_coins;

CREATE TABLE coin_specs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    algorithm VARCHAR(255),
    consensus_mechanism VARCHAR(255),
    blockchain_network VARCHAR(255),
    average_block_time FLOAT,
    security_features VARCHAR(255),
    privacy_features VARCHAR(255),
    max_supply DECIMAL(20, 8),
    genesis_block_date DATE,
    token_type VARCHAR(255),
    governance_model VARCHAR(255),
    development_activity VARCHAR(255),
    hard_cap DECIMAL(20, 8),
    forking_coin VARCHAR(255),
    tokenomics VARCHAR(255)
);

CREATE TABLE coin_market_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rank INT,
    price_usd DECIMAL(20, 8),
    market_cap_usd DECIMAL(20, 8),
    volume_24h_usd DECIMAL(20, 8),
    high_24h_usd DECIMAL(20, 8),
    low_24h_usd DECIMAL(20, 8),
    change_24h_percent DECIMAL(10, 4),
    all_time_high DECIMAL(20, 8),
    all_time_low DECIMAL(20, 8),
    circulating_supply DECIMAL(20, 8),
    market_dominance DECIMAL(10, 4),
    last_updated DATETIME
);

CREATE TABLE coin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    symbol VARCHAR(50),
    category VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL(20, 8),
    coin_specs_id INT,
    coin_market_data_id INT,
    FOREIGN KEY (coin_specs_id) REFERENCES coin_specs(id) ON DELETE CASCADE,
    FOREIGN KEY (coin_market_data_id) REFERENCES coin_market_data(id) ON DELETE CASCADE
);
