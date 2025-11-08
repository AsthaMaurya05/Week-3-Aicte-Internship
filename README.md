 # 🌍 Carbon Emission Forecast & Energy Mix Optimization

> **AICTE Internship Project — Week 2: Forecasting & Emission Prediction**

This project focuses on **analyzing and forecasting carbon emissions** from India’s electricity generation sector based on its energy mix — including **coal, gas, oil, hydro, nuclear, solar, wind, and bioenergy**.

In **Week 2**, we moved from *data cleaning* to *forecasting and insights* — building models that predict future renewable energy share and CO₂ emissions for India’s power generation sector.

---

## 📅 Week 2 Focus — Forecasting & Emission Prediction

### 🎯 Objectives
- Predict **renewable energy share (%)** for the next decade.  
- Forecast **total CO₂ emissions (MtCO₂)** using time-series models.  
- Compare **Linear Regression** and **Facebook Prophet** forecasting approaches.  
- Save and visualize predictions for future analysis and dashboard integration.

---

## 🧠 Key Learnings
- How to apply **machine learning** and **time-series modeling** for energy forecasting.  
- Estimating CO₂ emissions using emission factors and generation data.  
- Understanding model differences (Linear vs Prophet) for trend predictions.

---

## 🗂️ Project Structure
carbon_emission_project/
│
├── data/
│ ├── generation_data.csv # Raw electricity generation data (TWh)
│ └── emission_factors.csv # Emission factors (kg CO₂/MWh)
│
├── results/
│ ├── forecast_and_emissions.csv # Cleaned + Linear Regression results
│ ├── prophet_renewable_forecast.csv # Prophet forecast (Renewable share)
│ └── prophet_emission_forecast.csv # Prophet forecast (CO₂ emissions)
│
├── app.py # Linear Regression forecasting script
└── prophet_forecast.py # Prophet-based time-series forecasting


---

## ⚙️ Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python 3.x |
| Data Handling | pandas, numpy |
| Forecasting | scikit-learn (Linear Regression), **Facebook Prophet** |
| Visualization | matplotlib |
| Data Format | CSV (TWh, kg CO₂/MWh, Mt CO₂) |

---

## 🚀 Implementation Details

### **1️⃣ Linear Regression (app.py)**
- Trained a simple **Linear Regression** model to predict renewable energy share for the next 5 years.
- Calculated **total CO₂ emissions** using emission factors.
- Visualized renewable share and total emissions trends.
- Saved output to `results/forecast_and_emissions.csv`.

### **2️⃣ Prophet Forecasting (prophet_forecast.py)**
- Used **Facebook Prophet** for advanced forecasting with trend & uncertainty intervals.
- Forecasted both:
  - ✅ Renewable Share (%)  
  - ✅ CO₂ Emissions (MtCO₂)
- Extended prediction horizon to **10 years**.
- Saved results as:
  - `prophet_renewable_forecast.csv`
  - `prophet_emission_forecast.csv`

---

## 📈 Results & Insights

### 📊 Renewable Share Forecast
- **Upward trend** in renewable generation share.
- Strong linear and Prophet-based growth projections toward 2030.

### 🌫️ CO₂ Emission Forecast
- **Gradual decline** in total CO₂ emissions.
- Indicates effective decarbonization through renewable expansion.

---

## 🧾 Output Files

| File | Description |
|------|--------------|
| `forecast_and_emissions.csv` | Clean dataset + Linear Regression forecast |
| `prophet_renewable_forecast.csv` | Prophet model forecast for renewable share |
| `prophet_emission_forecast.csv` | Prophet model forecast for CO₂ emissions |

---

## 🔍 Model Comparison

| Model | Forecast Horizon | Strengths | Limitation |
|--------|------------------|------------|-------------|
| Linear Regression | 5 Years | Simple, fast, interpretable | Misses complex seasonality |
| Prophet | 10 Years | Handles trends, uncertainty, long-term predictions | Requires time conversion & tuning |

---

## 🌟 Week Summary

| Week | Stage | Description | Status |
|------|--------|-------------|---------|
| Week 1 | Data Collection & Cleaning | Load, clean, merge datasets | ✅ Completed |
| **Week 2** | **Forecasting & Emission Prediction** | Predict renewable share & CO₂ emissions using ML models | ✅ Completed |
| Week 3 | Visualization Dashboard | Build Streamlit dashboard for insights | 🔜 Upcoming |
| Week 4 | Final Report | Documentation & presentation of insights | ⏳ Pending |

---

## 📚 Data Source
- **Our World in Data** – [Electricity Mix Dataset](https://ourworldindata.org/electricity-mix)

---

## 🧠 Next Steps (Week 3 Preview)
- Build a **Streamlit Dashboard** to visualize:
  - Historical vs. Forecasted Renewable Shares
  - CO₂ Emission Trends
  - Renewable vs. Non-Renewable Contributions
- Enable user uploads and dynamic forecasts.

---

## 👩‍💻 Author
**Astha Maurya**  
*AICTE Internship 2025 — Carbon Emission Forecast & Energy Mix Optimization*  
📍 India | 💡 Passionate about Data Science & Climate Tech  

---

