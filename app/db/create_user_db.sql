CREATE DATABASE marketplace_users;
USE marketplace_users;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    role INT,
    CHECK (role IN (1, 2, 3))
);

CREATE TABLE user_bank (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    bank_name VARCHAR(255),
    account_holder VARCHAR(255),
    account_number VARCHAR(50),
    routing_number VARCHAR(50),
    iban VARCHAR(50),
    swift_code VARCHAR(50),
    date_linked TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE user_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    is_banned BOOLEAN DEFAULT FALSE,
    is_inactive BOOLEAN DEFAULT FALSE,
    ban_type VARCHAR(50),
    ban_reason TEXT,
    ban_duration INT,
    ban_start_time TIMESTAMP,
    ban_end_time TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE user_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    login_count INT DEFAULT 0,
    last_login TIMESTAMP,
    failed_login_count INT DEFAULT 0,
    last_failed_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    transaction_history JSON,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE user_security (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    password_hash VARCHAR(255),
    two_factor_enabled BOOLEAN DEFAULT FALSE,
    two_factor_secret_key VARCHAR(255),
    two_factor_backup_codes_hash JSON,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE user_fingerprint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    username_history JSON,
    email_address_history JSON,
    mac_address VARCHAR(50),
    associated_ips JSON,
    avg_login_frequency JSON,
    avg_session_duration JSON,
    geolocation_country VARCHAR(255),
    geolocation_city VARCHAR(255),
    geolocation_latitude DECIMAL(9, 6),
    geolocation_longitude DECIMAL(9, 6),
    browser_info VARCHAR(255),
    os_name VARCHAR(255),
    os_version VARCHAR(50),
    device_type VARCHAR(50),
    device_manufacturer VARCHAR(255),
    device_model VARCHAR(255),
    user_preferences JSON,
    user_agent VARCHAR(255),
    device_id VARCHAR(50),
    screen_resolution VARCHAR(50),
    two_factor_enabled BOOLEAN,
    vpn_usage BOOLEAN,
    behavioral_biometrics JSON,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
