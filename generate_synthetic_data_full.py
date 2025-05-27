import pandas as pd
import numpy as np

# Define start and end datetime
start_date = pd.Timestamp('2015-01-01 00:00:00')
end_date = pd.Timestamp('2025-05-28 00:00:00')

# Generate datetime range with hourly frequency
date_range = pd.date_range(start=start_date, end=end_date, freq='H')

num_hours = len(date_range)

# Generate synthetic temperature data with seasonal pattern + noise
days = np.array([dt.dayofyear for dt in date_range])
temperature = 10 + 15 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 3, size=num_hours)

# Generate synthetic energy consumption influenced by temperature and time of day
hours = np.array([dt.hour for dt in date_range])
base_consumption = 50 + 10 * np.sin(2 * np.pi * hours / 24)  # daily pattern
temp_effect = (25 - temperature) * 2  # more energy when colder
noise = np.random.normal(0, 5, size=num_hours)

energy_consumption = base_consumption + temp_effect + noise
energy_consumption = np.clip(energy_consumption, a_min=10, a_max=None)  # no negatives

# Create DataFrame
df = pd.DataFrame({
    'datetime': date_range,
    'temperature': temperature,
    'energy_consumption': energy_consumption
})

# Save to CSV
df.to_csv('synthetic_energy_consumption_2015_to_2025.csv', index=False)
print(f"Synthetic data saved to synthetic_energy_consumption_2015_to_2025.csv with {num_hours} rows.")
