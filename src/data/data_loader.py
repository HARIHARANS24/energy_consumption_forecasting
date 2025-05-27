# src/data/data_loader.py
import pandas as pd
import os

def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load raw energy consumption data from CSV.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found at {path}")
    return pd.read_csv(path)

def load_processed_data(path: str) -> pd.DataFrame:
    """
    Load processed data ready for modeling.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Processed data not found at {path}")
    return pd.read_csv(path)
