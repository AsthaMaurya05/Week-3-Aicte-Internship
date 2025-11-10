# scripts/emission_calculator.py
import pandas as pd
import os

# ---------- 1️⃣ Load emission factors ----------
ef_df = pd.read_csv("data/emission_factors.csv")
ef_df.columns = ["fuel_type", "kgCO2_per_MWh"]

# Convert kgCO2/MWh → MtCO2/TWh (1 TWh = 1,000,000 MWh; 1 Mt = 1e9 kg)
ef_df["MtCO2_per_TWh"] = ef_df["kgCO2_per_MWh"] * 1_000_000 / 1e9

# ---------- 2️⃣ Load all forecast files ----------
folder = "result/forecasts/"
all_forecasts = {}

for file in os.listdir(folder):
    if file.endswith("_forecast.csv"):
        fuel = file.replace("_forecast.csv", "")
        df = pd.read_csv(os.path.join(folder, file))
        df["ds"] = pd.to_datetime(df["ds"])
        df = df.rename(columns={"yhat": fuel})
        all_forecasts[fuel] = df.set_index("ds")[fuel]

# Merge all forecasts into one dataframe
merged = pd.concat(all_forecasts.values(), axis=1)
merged = merged.fillna(0)
merged.reset_index(inplace=True)
merged.rename(columns={"index": "year"}, inplace=True)

# Extract year number
merged["year"] = merged["ds"].dt.year

# ---------- 3️⃣ Calculate Emissions ----------
for fuel, factor in zip(ef_df["fuel_type"], ef_df["MtCO2_per_TWh"]):
    if fuel.lower() in merged.columns:
        merged[f"{fuel.lower()}_emission"] = merged[fuel.lower()] * factor

# Total emissions per year
merged["total_emission_MtCO2"] = merged[[c for c in merged.columns if c.endswith("_emission")]].sum(axis=1)

# ---------- 4️⃣ Save result ----------
out_path = "result/total_emission_forecast.csv"
merged.to_csv(out_path, index=False)
print(f"✅ Saved total emission forecast to {out_path}")

# ---------- 5️⃣ Quick check ----------
print("\n📊 Emission Summary (MtCO2):")
print(merged[["year", "total_emission_MtCO2"]].tail(10))
