import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Paths
model_path = 'models/xgboost_model.pkl'
data_path = 'data/raw/energy_consumption_dataset.csv'

@st.cache_data
def load_model(path):
    return joblib.load(path)

@st.cache_data
def load_data(path):
    df = pd.read_csv(path, parse_dates=['datetime'])
    df.set_index('datetime', inplace=True)
    return df

# Load model and data
model = load_model(model_path)
data = load_data(data_path)

st.title("🔋 Energy Consumption Forecasting")

# Show available data range
st.write(f"📊 Data available from: {data.index.min()} to {data.index.max()}")

# ===== Visualization Section =====
st.header("📈 Historical Energy Consumption Over Time")

# Date range filter for visualization
start_date = st.date_input("Start date", value=data.index.min().date())
end_date = st.date_input("End date", value=data.index.max().date())

# Ensure start_date <= end_date
if start_date > end_date:
    st.error("Error: Start date must be before or equal to end date.")
else:
    filtered_data = data.loc[start_date.strftime('%Y-%m-%d'): end_date.strftime('%Y-%m-%d')]
    if filtered_data.empty:
        st.warning("No data available for the selected date range.")
    else:
        st.line_chart(filtered_data['energy_consumption'])

# ===== Additional Visualization: Average Consumption by Hour or Day =====
st.header("📊 Average Energy Consumption Analysis")

option = st.selectbox("Choose aggregation to visualize:", ["Average by Hour of Day", "Average by Day of Week"])

if option == "Average by Hour of Day":
    avg_by_hour = data.groupby(data.index.hour)['energy_consumption'].mean()
    st.bar_chart(avg_by_hour)
elif option == "Average by Day of Week":
    avg_by_dow = data.groupby(data.index.dayofweek)['energy_consumption'].mean()
    dow_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    avg_by_dow.index = dow_labels
    st.bar_chart(avg_by_dow)

st.markdown("---")

# Date input: ensure at least 24 hours of data available
default_start = (data.index.min() + pd.Timedelta(hours=24)).date()
forecast_date = st.date_input("📅 Select forecast date", value=default_start)
forecast_hour = st.slider("⏰ Select forecast hour", 0, 23, 12)

# Combine to forecast timestamp
forecast_datetime = pd.Timestamp(forecast_date) + pd.Timedelta(hours=forecast_hour)

# Extract time features
month = forecast_datetime.month
dayofweek = forecast_datetime.dayofweek
hour = forecast_datetime.hour

# Prepare lag features
lags = {}
missing_lags = False
for lag in range(1, 25):
    lag_time = forecast_datetime - pd.Timedelta(hours=lag)
    if lag_time in data.index:
        lags[f'lag_{lag}'] = data.loc[lag_time, 'energy_consumption']
    else:
        lags[f'lag_{lag}'] = np.nan
        missing_lags = True

# Get temperature at forecast_datetime
if forecast_datetime in data.index:
    temperature = data.loc[forecast_datetime, 'temperature']
else:
    temperature = np.nan
    st.warning("⚠️ Missing temperature data for the forecast time.")

# Build input dataframe
input_data = pd.DataFrame([{
    'temperature': temperature,
    'month': month,
    'dayofweek': dayofweek,
    'hour': hour,
    **lags
}])

st.write("### 🧮 Input features")
st.write(input_data)

# Check for missing values
if input_data.isnull().any().any():
    st.warning("⚠️ Some input features are missing (NaN). Cannot perform prediction reliably.")
else:
    # Reorder columns to match model's expected features
    expected_cols = model.get_booster().feature_names
    input_data = input_data[expected_cols]

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🔮 Predicted energy consumption for {forecast_datetime}: **{prediction:.2f}**")

        # Additional Insights Section
        st.markdown("---")
        st.header("🔍 Insights")

        # Insight 1: Temperature effect
        temp_val = input_data.loc[0, 'temperature']
        if temp_val < 10:
            st.write(f"🌡️ Temperature is low ({temp_val:.1f}°C), which usually corresponds to higher energy consumption for heating.")
        elif temp_val > 25:
            st.write(f"🌡️ Temperature is high ({temp_val:.1f}°C), which may indicate increased energy use for cooling.")
        else:
            st.write(f"🌡️ Temperature is moderate ({temp_val:.1f}°C), energy consumption might be closer to average.")

        # Insight 2: Hour of day effect
        hr = input_data.loc[0, 'hour']
        if 6 <= hr <= 9:
            st.write(f"🕘 Forecast is during morning peak hours (hour {hr}), energy demand is typically higher.")
        elif 17 <= hr <= 20:
            st.write(f"🌆 Forecast is during evening peak hours (hour {hr}), expect higher energy use.")
        else:
            st.write(f"🕒 Forecast is during off-peak hours (hour {hr}), energy demand might be lower.")

        # Insight 3: Recent consumption trend based on lags
        lag_values = input_data.filter(like='lag_').values.flatten()
        recent_avg = np.nanmean(lag_values[:3])  # average of last 3 hours
        overall_avg = np.nanmean(lag_values)
        if recent_avg > overall_avg:
            st.write(f"📈 Recent energy consumption (last 3 hours avg: {recent_avg:.2f}) is higher than average ({overall_avg:.2f}), possibly indicating increasing demand.")
        else:
            st.write(f"📉 Recent energy consumption (last 3 hours avg: {recent_avg:.2f}) is lower than average ({overall_avg:.2f}), possibly indicating decreasing demand.")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
