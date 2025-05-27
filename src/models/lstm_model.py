# src/models/lstm_model.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from src.models.base_model import BaseModel

class LSTMModel(BaseModel):
    def __init__(self, input_shape):
        self.model = Sequential([
            LSTM(64, activation='relu', input_shape=input_shape),
            Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mse')

    def train(self, X, y, epochs=10, batch_size=32):
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=2)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, path: str):
        self.model.save(path)

    def load(self, path: str):
        self.model = tf.keras.models.load_model(path)
