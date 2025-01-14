CREATE DATABASE marketplace_wallets;
USE marketplace_wallets;

CREATE TABLE crypto_wallet (
    wallet_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    wallet_address VARCHAR(255),
    coins JSON DEFAULT '{}',
    total_coin_value DECIMAL(20, 8),
    last_accessed TIMESTAMP,
    encryption_key VARCHAR(255),
    deposit_history JSON DEFAULT '{}',
    withdrawal_history JSON DEFAULT '{}',
    FOREIGN KEY (user_id) REFERENCES marketplace_users.user(id)
);
