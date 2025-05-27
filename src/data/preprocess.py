# src/data/preprocess.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning of data: handle missing values, duplicates.
    """
    df = df.drop_duplicates()
    df = df.fillna(method='ffill').fillna(method='bfill')
    return df

def resample_data(df: pd.DataFrame, freq: str = 'H') -> pd.DataFrame:
    """
    Resample data to uniform frequency (e.g., hourly).
    Assumes DataFrame index is a datetime index.
    """
    df = df.resample(freq).mean()
    return df
