# src/models/xgboost_model.py
import xgboost as xgb
from src.models.base_model import BaseModel
import joblib

class XGBoostModel(BaseModel):
    def __init__(self, params=None):
        self.model = xgb.XGBRegressor(**(params or {}))

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, path: str):
        joblib.dump(self.model, path)

    def load(self, path: str):
        self.model = joblib.load(path)
