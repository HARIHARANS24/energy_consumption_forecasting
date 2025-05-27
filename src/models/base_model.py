# src/models/base_model.py
from abc import ABC, abstractmethod

class BaseModel(ABC):
    """
    Abstract base class for forecasting models.
    """
    
    @abstractmethod
    def train(self, X, y):
        pass
    
    @abstractmethod
    def predict(self, X):
        pass
    
    @abstractmethod
    def save(self, path: str):
        pass
    
    @abstractmethod
    def load(self, path: str):
        pass
