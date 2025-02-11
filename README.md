# Crypto Marketplace (Development Prototype)

- This platform simulates a crypto marketplace environment, allowing users to explore features such as buying and selling crypto, viewing market data, and managing wallets. 
- **Note**: This is not an actual exchange and does not involve real transactions. It is intended as a development prototype for educational and demonstration purposes.

## Features:
- Cryptocurrency buying and selling functionality (Mock Implementation) 
- Dashboard showing Market Data (Mock Implementation) 
- Wallet showing coins and values 
- Store coins and coin data in a database
- Store users and user data in a database
- Flask-based REST APIs
- Integration with MariaDB for data storage 
- Using OAuth2 to login with Google Account
- Secure password hashing (Argon2id) 
- Secure authentication (2FA via Authenticator App not yet implemented) 

## Prerequisites:
- Python 3.12+
- MariaDB
- `pip`

## Setting up Environment Variables:

To use certain features, you'll need to create a `.env` file in the root of the project with the following content: 
(Otherwise, OAuth signup and login will not function, and you'll be unable to send password reset emails or messages to the support email address.)

```bash
# Google OAuth credentials
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret

# Gmail credentials for sending emails
GMAIL_ADDRESS=your_gmail_address
GMAIL_PASSWORD=your_gmail_password

# Email address user sends support messages to
SUPPORT_EMAIL=your_email_address

# Secret key for URLSafeTimedSerializer
URLSafeTimedSerializer_SECRET_KEY=your_urlsafetimedserializer_secret_key

# Secret Key for the Flask App
APP_SECRET_KEY=your_secret_key

```

## Setting up OAuth2 with Google:
https://support.google.com/cloud/answer/6158849?hl=en#zippy=

https://developers.google.com/identity/protocols/oauth2/web-server

Authorized redirect URIs needed for OAuth2:

- http://localhost:5000/login
- http://localhost:5000/authorize
- http://127.0.0.1:5000/authorize


## Installation

You can set up the **Marketplace** in two ways: using **Git** or **Docker**.

### 1. **How to Use with Git**:

1. **Clone the Repository:**

```bash
   git clone https://github.com/lllDavid/marketplace.git
```

2. **Navigate into the Project Directory and install dependencies:**

```bash
cd marketplace
pip install -r requirements.txt
```

3. **Set up MariaDB:**

Ubuntu/Debian:
```bash
sudo apt-get install mariadb-server
sudo service mysql start
```
Windows:

You can download and install MariaDB from their official site: [MariaDB](https://mariadb.com/downloads/)

5. **Create the Database:** 

Log in to MariaDB and create the necessary database for the project.
```bash
mysql -u root -p CREATE DATABASE marketplace;
```

6. **Configure the Database:**

The database configuration is located in the config.py file in the root directory.

The SQL scripts for the tables can be found in the /db directory.

7. **Run the Flask Application:**

```bash
python run.py
```

8. **This will start the app at http://127.0.0.1:5000/.**

### 2. **How to Use with Docker**:

**Prerequisites**:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

1. **Clone the Repository and navigate to the project directory:**
```bash
git clone https://github.com/lllDavid/marketplace.git
cd marketplace
```

2. **Build and Start the Application:**

```bash
docker-compose up 
```

If you get any errors try running:

```bash
docker-compose --build
```

3. **Access the Application:** 

This will start the app at http://127.0.0.1:5000/.