# scripts/forecast_engine.py
import pandas as pd
from prophet import Prophet
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import os

# ---------- 1️⃣ Load cleaned data ----------
df = pd.read_csv("result/cleaned_generation_data.csv")

# Remove 'entity' column if present
if 'entity' in df.columns:
    df = df.drop(columns=['entity'])

# List of energy sources to forecast
sources = ['bioenergy', 'solar', 'wind', 'hydro', 'nuclear', 'oil', 'gas', 'coal']

# Ensure output folder exists
os.makedirs("result/forecasts", exist_ok=True)

# ---------- 2️⃣ Forecast Each Source ----------
for source in sources:
    print(f"\n🔮 Forecasting {source.capitalize()} ...")

    data = df[['year', source]].rename(columns={'year': 'ds', source: 'y'})
    data['ds'] = pd.to_datetime(data['ds'], format='%Y')

    # If the data is flat or has low variation, use Linear Regression fallback
    if data['y'].nunique() < 5 or data['y'].std() < 1:
        print(f"⚠️ {source.capitalize()} has low variation — using Linear Regression.")
        X = np.array(range(len(data))).reshape(-1, 1)
        y = data['y'].values
        model = LinearRegression().fit(X, y)

        future_years = 10
        future_X = np.array(range(len(data) + future_years)).reshape(-1, 1)
        y_pred = model.predict(future_X)

        forecast_df = pd.DataFrame({
            'ds': pd.date_range(start=data['ds'].iloc[0], periods=len(future_X), freq='Y'),
            'yhat': y_pred
        })
    else:
        model = Prophet(
            yearly_seasonality=False,
            changepoint_prior_scale=0.2
        )
        model.fit(data)
        future = model.make_future_dataframe(periods=10, freq='Y')
        forecast_df = model.predict(future)[['ds', 'yhat']]

    # Save forecast
    out_file = f"result/forecasts/{source}_forecast.csv"
    forecast_df.to_csv(out_file, index=False)
    print(f"✅ Saved forecast: {out_file}")

    # Plot for quick check
    plt.figure(figsize=(7,4))
    plt.plot(data['ds'], data['y'], 'bo-', label='Actual')
    plt.plot(forecast_df['ds'], forecast_df['yhat'], 'r--', label='Forecast')
    plt.title(f"{source.capitalize()} Generation Forecast (TWh)")
    plt.xlabel("Year")
    plt.ylabel("Generation (TWh)")
    plt.legend()
    plt.tight_layout()
    plt.show()

print("\n🎉 All forecasts completed successfully!")
