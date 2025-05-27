
# Energy Consumption Forecasting

## Project Overview

This project provides an end-to-end pipeline for forecasting energy consumption using time series data. It includes data loading, preprocessing, feature engineering, model training, evaluation, and deployment with a Streamlit web app for interactive forecasting and visualization.

---

## Project Structure

```plaintext
energy_consumption_forecasting/
│
├── data/
│   ├── raw/                  # Raw source data (immutable)
│   ├── processed/            # Cleaned and feature-engineered data
│   ├── external/             # External data sources (weather, holidays, etc.)
│   └── README.md             # Data description and sources info
│
├── notebooks/
│   ├── exploratory_data_analysis.ipynb
│   ├── feature_engineering.ipynb
│   └── model_experiments.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── data_loader.py            # Load raw & processed data
│   │   ├── preprocess.py             # Cleaning & preprocessing functions
│   │   └── feature_engineering.py    # Feature creation & selection
│   │
│   ├── models/
│   │   ├── base_model.py             # Abstract base class for models
│   │   ├── lstm_model.py             # LSTM deep learning model
│   │   ├── xgboost_model.py          # XGBoost model
│   │   └── model_utils.py            # Training, evaluation, saving models
│   │
│   ├── evaluation/
│   │   └── metrics.py                # Custom metrics (RMSE, MAE, MAPE, etc.)
│   │
│   ├── utils/
│   │   ├── config.py                 # Configuration loader (YAML/JSON)
│   │   ├── logger.py                 # Logging setup
│   │   └── helpers.py                # Utility functions
│   │
│   ├── visualization/
│   │   └── viz.py                   # Visualization utilities for reports & EDA
│   │
│   └── forecasting_pipeline.py      # Main pipeline orchestration
│
├── tests/
│   ├── test_data_loader.py
│   ├── test_preprocess.py
│   ├── test_feature_engineering.py
│   ├── test_models.py
│   └── test_forecasting_pipeline.py
│
├── configs/
│   ├── config.yaml                  # All hyperparameters, paths, settings
│   └── logging.yaml                 # Logging configuration
│
├── scripts/
│   ├── run_train.sh                 # Bash script to train model
│   ├── run_inference.sh             # Bash script for inference
│   └── setup_env.sh                 # Setup environment (install deps, etc.)
│
├── requirements.txt                 # Python dependencies
├── Dockerfile                      # Containerization for deployment
├── docker-compose.yml              # Multi-container setup (optional)
├── README.md
├── app.py
├── main.py
├── LICENSE
└── .gitignore
```

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/HARIHARANS24/energy_consumption_forecasting.git
   cd energy_consumption_forecasting
   ```

2. Set up Python virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Run Jupyter notebooks in `notebooks/` for data exploration and feature engineering.

4. Train models via scripts or notebook:
   ```bash
   bash scripts/run_train.sh
   ```

5. Launch the Streamlit app for forecasting and visualization:
   ```bash
   streamlit run app.py
   ```

---

## Usage

- **Data**: Place raw time series CSV files under `data/raw/`.
- **Model**: Trained models saved in `src/models/`.
- **Forecasting**: Use the Streamlit app for interactive energy consumption predictions.
- **Visualization**: Explore historical consumption trends with interactive charts.
- **Testing**: Unit tests available under `tests/` for pipeline components.

---

## Features

- Data preprocessing and feature engineering with lag variables and time features.
- Model training with XGBoost and deep learning models (LSTM).
- Custom evaluation metrics for regression accuracy (RMSE, MAE, MAPE).
- Streamlit app with user input controls and live predictions.
- Interactive time series visualizations of historical energy consumption.
- Insights based on temperature, time of day, and recent consumption trends.

---

## Modeling Approach

- **XGBoost Model:** Gradient boosting trees trained on lagged features, temperature, and time.
- **LSTM Model:** Recurrent neural network capturing temporal dependencies.

Feature engineering includes lag features, rolling statistics, time-based encoding, and external factors like temperature.

Model selection and hyperparameter tuning are documented and performed through experiments logged in Jupyter notebooks.

---

## Testing

Run tests using:

```bash
pytest tests/
```
Tests cover data loading, preprocessing, feature engineering, model training, and pipeline orchestration.

---

## Configuration

All parameters are configurable via `configs/config.yaml`.

Logging is controlled by `configs/logging.yaml`.

Easily modify model hyperparameters, data paths, feature settings, and more through these configuration files.

---

## Deployment

- A `Dockerfile` is provided for containerizing the application.
- Use `docker-compose.yml` to run multi-container setups if needed (e.g., separate API and database).
- The project can be deployed on cloud providers or local servers with ease.

---

## Contribution

Contributions welcome! Please:
- Fork the repo
- Create a feature branch
- Submit pull requests with clear descriptions
- Ensure tests pass and code is documented

---
