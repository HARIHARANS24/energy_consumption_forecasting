# src/forecasting_pipeline.py
import os
import pandas as pd

from src.utils.config import load_config
from src.data.data_loader import load_raw_data
from src.data.preprocess import clean_data, resample_data
from src.data.feature_engineering import create_time_features, add_lag_features
from src.models.xgboost_model import XGBoostModel
from src.evaluation.metrics import rmse, mae, mape
from src.utils.logger import get_logger

logger = get_logger(__name__)

def main():
    config = load_config(os.path.join('configs', 'config.yaml'))
    data_path = config['data']['raw_data_path']
    logger.info("Loading raw data...")
    df = load_raw_data(data_path)
    
    logger.info("Cleaning data...")
    df = clean_data(df)
    df.index = pd.to_datetime(df[config['data']['datetime_column']])
    df = df.drop(columns=[config['data']['datetime_column']])
    
    logger.info("Resampling data...")
    df = resample_data(df, freq=config['data']['resample_freq'])
    
    logger.info("Creating features...")
    df = create_time_features(df)
    df = add_lag_features(df, lag_hours=config['model']['lag_hours'])
    
    X = df.drop(columns=['energy_consumption'])
    y = df['energy_consumption']
    
    logger.info("Training model...")
    model = XGBoostModel(params=config['model']['xgboost_params'])
    model.train(X, y)
    
    logger.info("Saving model...")
    model.save(config['model']['model_save_path'])
    
    logger.info("Evaluating model on training data...")
    preds = model.predict(X)
    logger.info(f"RMSE: {rmse(y, preds)}")
    logger.info(f"MAE: {mae(y, preds)}")
    logger.info(f"MAPE: {mape(y, preds)}")

if __name__ == "__main__":
    main()
