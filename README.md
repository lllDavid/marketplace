# Crypto Marketplace (Development Prototype)

This platform simulates a cryptocurrency marketplace environment, allowing users to explore features such as buying and selling cryptocurrency, viewing market data, and managing wallets. **Note**: This is not an actual exchange and does not involve real transactions. It is intended as a development prototype for educational and demonstration purposes.

## Features:
- Cryptocurrency buying and selling functionality (Mock Implementation) – Simulated trades and transactions.
- Dashboard showing Market Data (Mock Implementation) – Data is randomly generated; it’s for demonstration purposes.
- Wallet showing Coins and Values.
- Store coins and coin data in a database.
- Store users and user data in a database.
- Flask-based REST API – For interacting with the platform programmatically (mock data).
- Integration with MariaDB for data storage – Persistent data storage with mock content.
- Using OAuth2 to login with Google Account (Mock Implementation) – Simulated login process.
- Secure password hashing (Argon2id) – For securing user credentials.
- Secure authentication (2FA via Authenticator App not yet implemented) – Placeholder for future 2FA.

---

## Installation

You can set up the **Crypto Marketplace** in two ways: using **Git** or **Docker**.

### 1. **How to Use with Git**:

Follow these steps to install and run the project using Git.

#### Prerequisites:
- Python 3.x
- MariaDB
- `pip` (Python package installer)

#### Steps:

1. **Clone the Repository**:
   Clone the repository from GitHub to your local machine.
```bash
   git clone https://github.com/lllDavid/marketplace.git
```

2. **Navigate into the Project Directory:**
After cloning, go to the project directory.
```bash
cd marketplace
pip install -r requirements.txt
```

3. **Set up MariaDB: Install MariaDB on your local machine.**
You can do so by running the following commands depending on your operating system.

Ubuntu/Debian:
```bash
sudo apt-get install mariadb-server
sudo service mysql start
```
Windows:

You can download and install MariaDB from their official site. [MariaDB](https://mariadb.com/downloads/)

5. **Create the Database:** 
Log in to MariaDB and create the necessary database for the project.
mysql -u root -p
CREATE DATABASE marketplace;

6. **Configure Database and Database Connection: config.py**

The sql scripts to create the tables needed are located in /db 

7. **Run the Flask Application:**
Run the Flask app with the following command:
```bash
cd /path/to/your/project
python run.py
```

8. **This will start the Flask development server at http://127.0.0.1:5000/ by default.**

Access the Application: You can now access it by opening a web browser and navigating to:

http://127.0.0.1:5000/

### 2. **How to Use with Docker**:
Follow these steps to run the project using Docker and Docker Compose.

**Prerequisites**:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

**Steps**:

Clone the Repository: If you haven't cloned the repository yet, run the following command:
```bash
git clone https://github.com/lllDavid/marketplace.git
cd marketplace
```

**Build and Start the Application Using Docker Compose:**

The repository contains a docker-compose.yml file that simplifies the process of running the application with Docker.
Run the following command to build and start the application (including the database):
```bash
docker-compose up --build
This will build the Docker image if necessary, start the Flask application, and start the MariaDB container.
```

**Access the Application:** 

Once the containers are up and running, you can access your Flask app in your browser at:
http://localhost:5000

**Stop the Docker Containers:**

To stop the running Docker containers, use the following command:
```bash
docker-compose down
```
This will stop and remove the containers but leave the images intact.