import yfinance as yf
from utils import save_csv

tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]
df_api = yf.download(tickers, start="2020-08-17", end="2025-08-17").reset_index()

_ = save_csv(df_api, prefix='api', source='yfinance', symbol=tickers)
