🌍 AI-Powered Carbon Emission Forecast & Energy Mix Optimization Dashboard
🔋 Project Overview

This project forecasts India’s electricity generation and carbon emissions using real historical data (1985–2023).
It predicts future energy production for Coal, Solar, Wind, Hydro, Nuclear, Gas, Oil, and Bioenergy up to 2035, and calculates the resulting CO₂ emissions using emission factors.

An interactive Streamlit Dashboard visualizes all forecasts with charts, tables, KPIs, and a What-If Scenario Simulator to explore how increasing renewables or reducing coal impacts future emissions.

This project was completed as part of the AICTE Virtual Internship Program.

🎯 Key Objectives

Forecast India’s electricity generation (1985–2035)

Predict total carbon emissions using scientific emission factors

Build an interactive Streamlit dashboard

Provide actionable insights on improving India’s energy mix

Simulate renewable adoption vs emission reduction scenarios

🧠 Tech Stack

Python 3.x

Prophet (Time-series forecasting)

Pandas, NumPy

Plotly

Matplotlib

Streamlit (Dashboard)

Git & GitHub

📂 Project Structure
carbon_emission_project/
│
├── data/
│   ├── generation_data.csv
│   └── emission_factors.csv
│
├── result/
│   ├── cleaned_generation_data.csv
│   ├── total_emission_forecast.csv
│   └── forecasts/
│       ├── coal_forecast.csv
│       ├── solar_forecast.csv
│       ├── wind_forecast.csv
│       ├── gas_forecast.csv
│       ├── oil_forecast.csv
│       ├── nuclear_forecast.csv
│       ├── hydro_forecast.csv
│       └── bioenergy_forecast.csv
│
├── script/
│   ├── data_cleaning.py
│   ├── forecast_engine.py
│   └── emission_calculator.py
│
├── app.py              # Streamlit Dashboard
└── README.md

🧹 Data Processing

Cleaned inconsistent values

Handled missing entries

Converted TWh → MWh where needed

Merged datasets into a unified model-ready file

📈 Forecasting Models

Each energy source is modeled independently using:

✔ Facebook Prophet
✔ Auto-tuned parameters
✔ Trend + seasonality adjustments
✔ Linear fallback for flat series

This produces accurate & stable forecasts up to 2035.

🏭 Carbon Emission Calculation

CO₂ is calculated using:

Emissions (kgCO₂) = Generation (MWh) × Emission Factor (kgCO₂/MWh)


Final results include:

Emissions per energy source

Total annual emissions

Trend analysis

🖥️ Interactive Streamlit Dashboard
The dashboard includes:

✔ Plotly interactive charts
✔ Electricity forecast comparison
✔ Auto-generated Key Insights
✔ Color-coded tables
✔ KPI Cards (Total electricity, renewable % share, CO₂ emissions)
✔ What-If Simulator

Increase Solar

Increase Wind

Reduce Coal

See predicted CO₂ impact instantly

Run it using:

streamlit run app.py

📊 Key Results

Solar & Wind show massive projected growth till 2035

Coal remains high but its growth slows

Total emissions continue to rise unless coal is reduced

What-If Simulator shows up to 20–40% CO₂ reduction through renewable adoption

🧩 Improvements Implemented

Built full interactive dashboard

Added scenario-based optimization simulator

Auto-insight generation for forecasts

Clean UI with color-coded tables

KPI summary section

📝 Conclusion

This project demonstrates how machine learning + visualization + policy simulation can support sustainable energy planning in India.
It provides clear insights to researchers, policymakers, and students on how renewable growth affects long-term CO₂ emissions.

👨‍💻 Author

Astha Maurya
AI/ML Intern • Energy & Sustainability Enthusiast 🌱
