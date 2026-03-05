# ⚡ Energy Consumption Forecasting

## 📋 Project Overview

This project provides an end-to-end pipeline for forecasting energy consumption using time series data. It includes data loading, preprocessing, feature engineering, model training, evaluation, and deployment with a Streamlit web app for interactive forecasting and visualization.

## 👨‍💻 Author  

**Hariharan S**  
- GitHub: [@HARIHARANS24](https://github.com/HARIHARANS24)  
- LinkedIn: [Hariharan S](https://www.linkedin.com/in/hariharan-s-24/)
- Email: hariharans24@gmail.com 
    
## ✨ Features  
 
- **🔄 Data Processing Pipeline**   
  - Raw data ingestion and validation 
  - Automated data cleaning and preprocessing
  - Feature engineering with lag variables and time features
  - External data integration (weather, holidays)

- **🤖 Machine Learning Models**
  - XGBoost for traditional ML approach
  - LSTM for deep learning approach
  - Model comparison and selection
  - Hyperparameter tuning

- **📊 Evaluation Metrics**
  - RMSE (Root Mean Square Error)
  - MAE (Mean Absolute Error)
  - MAPE (Mean Absolute Percentage Error)
  - Custom evaluation visualizations

- **🌐 Interactive Web Application**
  - Streamlit-based dashboard
  - Real-time forecasting
  - Interactive visualizations
  - Historical data analysis

## 📁 Project Structure

```
Directory structure:
└── hariharans24-energy_consumption_forecasting/
    ├── README.md
    ├── app.py
    ├── docker-compose.yml
    ├── Dockerfile
    ├── generate_synthetic_data_full.py
    ├── LICENSE
    ├── main.py
    ├── requirements.txt
    ├── configs/
    │   ├── config.yaml
    │   └── logging.yaml
    ├── data/
    │   ├── README.md
    │   └── raw/
    │       ├── energy_consumption.csv
    │       └── energy_consumption_dataset.csv
    ├── models/
    │   └── xgboost_model.pkl
    ├── notebooks/
    │   ├── exploratory_data_analysis.ipynb
    │   ├── feature_engineering.ipynb
    │   └── model_experiments.ipynb
    ├── scripts/
    │   ├── run_inference.sh
    │   ├── run_train.sh
    │   └── setup_env.sh
    ├── src/
    │   ├── __init__.py
    │   ├── forecasting_pipeline.py
    │   ├── __pycache__/
    │   ├── data/
    │   │   ├── data_loader.py
    │   │   ├── feature_engineering.py
    │   │   ├── preprocess.py
    │   │   └── __pycache__/
    │   ├── evaluation/
    │   │   ├── metrics.py
    │   │   └── __pycache__/
    │   ├── models/
    │   │   ├── base_model.py
    │   │   ├── lstm_model.py
    │   │   ├── model_utils.py
    │   │   ├── xgboost_model.py
    │   │   └── __pycache__/
    │   ├── utils/
    │   │   ├── config.py
    │   │   ├── helpers.py
    │   │   ├── logger.py
    │   │   └── __pycache__/
    │   └── visualization/
    │       └── viz.py
    └── tests/
        ├── test_data_loader.py
        ├── test_feature_engineering.py
        ├── test_forecasting_pipeline.py
        ├── test_models.py
        └── test_preprocess.py
```

## 🚀 Setup Instructions

1. **📥 Clone the Repository**
   ```bash
   git clone https://github.com/HARIHARANS24/energy_consumption_forecasting.git
   cd energy_consumption_forecasting
   ```

2. **🔧 Set Up Python Environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Unix/MacOS:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **📊 Generate Synthetic Data (Optional)**
   ```bash
   python generate_synthetic_data_full.py
   ```

4. **🧪 Run Tests**
   ```bash
   pytest tests/
   ```

5. **🤖 Train Models**
   ```bash
   # Using script
   bash scripts/run_train.sh
   
   # Or using Python directly
   python main.py --mode train
   ```

6. **🌐 Launch Web Application**
   ```bash
   streamlit run app.py
   ```

## 💡 Usage

### 📂 Data Management
- Place raw time series CSV files in `data/raw/`
- Processed data will be stored in `data/processed/`
- External data (weather, holidays) should be placed in `data/external/`

### 🤖 Model Training
- Configure model parameters in `configs/config.yaml`
- Run training scripts from `scripts/` directory
- Trained models are saved in `models/` directory

### 🌐 Web Application
- Access the Streamlit app at `http://localhost:8501`
- Upload new data or use existing datasets
- View forecasts and visualizations
- Download predictions and reports

## ⚙️ Configuration

### 🔧 Model Parameters
Edit `configs/config.yaml` to modify:
- Model hyperparameters
- Feature engineering settings
- Training parameters
- Data paths
- Evaluation metrics

### 📝 Logging
Configure logging in `configs/logging.yaml`:
- Log levels
- Output formats
- File paths

## 👨‍💻 Development

### ✨ Adding New Features
1. Create feature branch
2. Add tests in `tests/`
3. Implement feature
4. Run tests
5. Submit pull request

### 🧪 Running Tests
```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_models.py

# Run with coverage
pytest --cov=src tests/
```

## 🚢 Deployment

### 🐳 Docker Deployment
1. Build Docker image:
   ```bash
   docker build -t energy-forecast .
   ```

2. Run container:
   ```bash
   docker run -p 8501:8501 energy-forecast
   ```

### 🐳 Docker Compose
For multi-container setup:
```bash
docker-compose up -d
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by various time series forecasting projects
- Built with Streamlit, PyTorch, and XGBoost

















