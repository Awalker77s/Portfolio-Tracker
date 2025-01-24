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



stock_choice = input("Give the ticker symbol for stock: ")

print(stock_choice, ":", fetch_stock_price(stock_choice), "\n")






# Code to get live crypto price
def fetch_crypto_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    return response.json()[symbol]["usd"]

crypto_choice = input("Give the name for crypto: ")
print(crypto_choice, ":", fetch_crypto_price(crypto_choice))