# scripts/data_cleaning.py
import pandas as pd
import os

# ---------- 1️⃣ Load raw data ----------
gen_path = "C:\\Users\\Lenovo\\Downloads\\int\\data\\generation_data.csv"
ef_path  = "C:\\Users\\Lenovo\\Downloads\\int\\data\\emission_factors.csv"

generation_df = pd.read_csv(gen_path)
emission_df   = pd.read_csv(ef_path)

# ---------- 2️⃣ Clean & format ----------
# Standardize column names
generation_df.columns = [c.strip().lower().replace(" ", "_") for c in generation_df.columns]

# Fill missing values with 0
generation_df = generation_df.fillna(0)

# Ensure 'year' column is integer
generation_df['year'] = generation_df['year'].astype(int)

# Remove duplicate years if any
generation_df = generation_df.drop_duplicates(subset='year').sort_values('year')

# ---------- 3️⃣ Check emission factors ----------
emission_df.columns = [c.strip().lower() for c in emission_df.columns]

# Verify expected sources
print("✅ Energy sources in emission factors:", list(emission_df['source']))

# ---------- 4️⃣ Save cleaned data ----------
os.makedirs("result", exist_ok=True)
generation_df.to_csv("result/cleaned_generation_data.csv", index=False)
print("🎉 Cleaned data saved to result/cleaned_generation_data.csv")

# Optional: show quick summary
print("\n📊 Data summary:")
print(generation_df.describe())
