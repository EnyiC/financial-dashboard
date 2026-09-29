import yfinance as yf
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

tickers = ["SPY","QQQ","AAPL","MSFT","NVDA","JPM","XOM"]
data = yf.download(tickers, start="2021-01-01", end="2026-09-28", auto_adjust=True)["Close"]
data = data.ffill().dropna()
data.to_csv("data/raw/prices.csv")
print("Shape:", data.shape)
print(data.tail())