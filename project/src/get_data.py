import yfinance as yf
from utils import save_csv

tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]
df_api = yf.download(tickers, start="2018-08-01", end="2023-08-01").reset_index()

_ = save_csv(df_api, prefix='api', source='yfinance', symbol=tickers)
