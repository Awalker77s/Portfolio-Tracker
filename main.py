# This is used for regular stock prices
import yfinance as yf
# This is used for crytpocurrencies
import requests
# Data frame
import pandas as pd

# Code to get live stock price
def fetch_stock_price(ticker):
    stock = yf.Ticker(ticker)
    live_price = stock.history(period="1d")["Close"].iloc[-1]
    return live_price




# Initialize a list and add each stock or crypto in until you say "done"
stock_list = [""]

while True:
    stock_choice = input("Give the ticker symbol for stock: ")   
    if stock_choice.lower() == 'done': break
    stock_list.append(stock_choice)

for stock in stock_list:
    try:
        print(stock, "->", fetch_stock_price(stock))
    except Exception as e:
        print(f"Could not fetch price for {stock}. Error: {e}")




# Code to get live crypto price
def fetch_crypto_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    return response.json()[symbol]["usd"]


crypto_list = [""]

while True:
    crypto_choice = input("Give the name for crypto stock: ")   
    if crypto_choice.lower() == 'done': break
    crypto_list.append(crypto_choice)

for crypto in crypto_list:
    try:
        print(crypto, "->", fetch_crypto_price(crypto))
    except Exception as e:
        print(f"Could not fetch price for {crypto}. Error: {e}")
