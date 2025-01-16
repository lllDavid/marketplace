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
- Using OAuth2 to login with Google Account (Mock Implementation) 
- Secure password hashing (Argon2id) 
- Secure authentication (2FA via Authenticator App not yet implemented) 

---

#### Prerequisites:
- Python 3.12+
- MariaDB
- `pip` (Python package installer)

## Setting up Environment Variables

To run the application, you'll need to create a `.env` file in the root of the project with the following content:

```bash
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret

GMAIL_ADDRESS=your_gmail_address
GMAIL_PASSWORD=your_gmail_password

URL_STS_SECRET_KEY=your_url_sts_secret_key

SUPPORT_EMAIL=your_email_address
```
## Installation

You can set up the **Marketplace** in two ways: using **Git** or **Docker**.

### 1. **How to Use with Git**:

Follow these steps to install and run the project using Git.

#### Steps:

1. **Clone the Repository**:

```bash
   git clone https://github.com/lllDavid/marketplace.git
```

2. **Navigate into the Project Directory:**

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

You can download and install MariaDB from their official site. [MariaDB](https://mariadb.com/downloads/)

5. **Create the Database:** 

Log in to MariaDB and create the necessary database for the project.
```bash
mysql -u root -p
CREATE DATABASE marketplace;
```

6. **Configure Database and Database Connection:**

The Database config is located in config.py in the root directory

The SQL scripts for creating the necessary tables are located in the /db directory.

7. **Run the Flask Application:**

```bash
cd /marketplace
python run.py
```

8. **This will start the Flask development server at http://127.0.0.1:5000/ by default.**

### 2. **How to Use with Docker**:
Follow these steps to run the project using Docker.

**Prerequisites**:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
or
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

**Steps**:

Clone the Repository:
```bash
git clone https://github.com/lllDavid/marketplace.git
cd marketplace
```

**Build and Start the Application Using Docker Compose:**

Run the following command to build and start the application (including the database):
```bash
docker-compose up 
```

**Access the Application:** 

Once the containers are up and running, you can access the Flask app in your browser at:
http://localhost:5000

**Stop the Docker Containers:**

To stop the running Docker containers, use the following command:
```bash
docker-compose down
```