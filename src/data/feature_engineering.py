# src/data/feature_engineering.py
import pandas as pd

def create_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract time-based features from datetime index.
    """
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['month'] = df.index.month
    return df

def add_lag_features(df: pd.DataFrame, lag_hours: int = 24) -> pd.DataFrame:
    """
    Add lag features (previous values) to help forecasting.
    """
    for lag in range(1, lag_hours + 1):
        df[f'lag_{lag}'] = df['energy_consumption'].shift(lag)
    df = df.dropna()
    return df
