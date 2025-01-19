USE marketplace_wallets;

CREATE TABLE fiat_wallet (
    wallet_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    balance DECIMAL(20, 8),
    iban VARCHAR(34),
    swift_code VARCHAR(11),
    routing_number VARCHAR(9),
    last_accessed TIMESTAMP,
    encryption_key VARCHAR(255),
    deposit_history JSON DEFAULT '{}',
    withdrawal_history JSON DEFAULT '{}',
    FOREIGN KEY (user_id) REFERENCES marketplace_users(id)
);
