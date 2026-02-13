# Binance Futures Trading Bot (Testnet)

## Overview

This project is a command-line (CLI) based trading bot built in Python that allows users to place orders on the Binance USDT-M Futures Testnet.

The application supports Market and Limit orders with proper input validation, structured logging, and robust error handling. The codebase follows a modular design, separating responsibilities into different components such as client initialization, order execution, validation, and CLI handling.

This project is designed as a simplified trading bot for demonstration and testing purposes.

---

## Features

* Place Market Orders (BUY / SELL)
* Place Limit Orders (BUY / SELL)
* Command-line interface (CLI)
* Input validation with clear error messages
* Structured logging to file
* Error handling for API failures and invalid inputs
* Clean and modular project structure

---

## Project Structure

project/
├── cli.py                # CLI entry point
├── client.py             # Binance client setup
├── logging_config.py     # Logging configuration
├── validators.py         # Input validation
├── market_orders.py      # Market order logic
├── limit_orders.py       # Limit order logic
├── requirements.txt      # Project dependencies
├── README.md             # Documentation
└── bot.log               # Log file (generated after execution)

---

## Setup Instructions

### 1. Create Binance Futures Testnet Account

* Visit Binance Futures Testnet
* Register or log in
* Generate API Key and Secret

---

### 2. Clone the Repository

git clone https://github.com/your-username/binance-trading-bot.git
cd binance-trading-bot

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Configure Environment Variables

You can configure your Binance API credentials using either a `.env` file or environment variables.

#### Option A: Using .env file (Recommended)

Create a file named `.env` in the project root:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret

---

#### Option B: Using environment variables

For Linux / Mac:

export BINANCE_API_KEY=your_api_key
export BINANCE_API_SECRET=your_api_secret

For Windows:

set BINANCE_API_KEY=your_api_key
set BINANCE_API_SECRET=your_api_secret

---

## Usage

### Place a Market Order

python cli.py BTCUSDT BUY MARKET 0.001

---

### Place a Limit Order

python cli.py BTCUSDT SELL LIMIT 0.001 --price 50000

---

## Example Output

===== ORDER REQUEST =====
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

===== ORDER RESPONSE =====
Order ID      : 12345678
Status        : FILLED
Executed Qty  : 0.001
Avg Price     : 43000

Order placed successfully

---

## Logging

All API requests, responses, and errors are logged in:

bot.log

Example:

2026-02-13 12:00:00 | INFO | Order placed | Symbol=BTCUSDT | Side=BUY | Type=MARKET | Quantity=0.001

---

## Error Handling

The application handles:

* Invalid user input
* Missing parameters
* API errors
* Network issues

Example:

Order failed
Reason: Price is required for LIMIT orders

---

## Assumptions

* The application uses Binance Futures Testnet
* API credentials are valid
* Internet connection is available

---

## Requirements

python-binance
python-dotenv

---

## Notes

* This project is for testing and educational purposes only
* Do not use testnet credentials in production

---

## Author

Mansi
Python Developer Candidate
