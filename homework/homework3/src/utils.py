import pandas as pd

def get_mean_std(df, column):
    return df[column].mean(), df[column].std()

