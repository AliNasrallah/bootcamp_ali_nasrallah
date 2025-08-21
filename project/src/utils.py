import pandas as pd
from dotenv import load_dotenv
import os, datetime as dt
from pathlib import Path


load_dotenv()
RAW = Path(os.getenv('DATA_DIR_RAW'))
PROC = Path(os.getenv('DATA_DIR_PROCESSED'))

def ts():
    return dt.datetime.now().strftime('%Y%m%d-%H%M%S')

def save_csv(df: pd.DataFrame, prefix: str, **meta):
    mid = '_'.join([f"{k}-{v}" for k,v in meta.items()])
    path = RAW / f"{prefix}_{mid}_{ts()}.csv"
    df.to_csv(path, index=False)
    return path

def save_parquet(df: pd.DataFrame, prefix: str, **meta):
    mid = '_'.join([f"{k}-{v}" for k,v in meta.items()])
    path = PROC / f"{prefix}_{mid}_{ts()}.parquet"
    df.to_parquet(path, index=False)
    return path


