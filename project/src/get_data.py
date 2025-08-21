import yfinance as yf
from utils import save_csv, save_parquet

tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]
df_api = yf.download(tickers, start="2020-08-17", end="2025-08-17", auto_adjust=False).reset_index()

csv_path = save_csv(df_api, prefix='api', source='yfinance', symbol=tickers)

parquet_path = save_parquet(df_api, prefix='api', source='yfinance', symbol=tickers)


