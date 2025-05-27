# src/models/model_utils.py
import os

def save_model(model, path: str):
    """
    Save the model object to disk.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    model.save(path)

def load_model(model_class, path: str):
    """
    Load model object from disk.
    """
    model = model_class()
    model.load(path)
    return model
