import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# File paths
data_path = Path("../../cleaned/energy_security_master.csv")
visual_path = Path("../../visualizations")
visual_path.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_csv(data_path)

# Clean column names just in case
df.columns = df.columns.str.strip().str.lower()

# Keep 2024 only
df_2024 = df[df["year"] == 2024].copy()

# Convert numeric columns 
numeric_cols = [
    "renewable_growth_pct",
    "oil_consumption_change_pct",
    "oil_exposure_pct",
    "spr_days_2026"
]

for col in numeric_cols:
    df_2024[col] = pd.to_numeric(df_2024[col], errors="coerce")

# Preview
print("\n2024 Energy Security Analysis Table:")
print(df_2024[[
    "country",
    "renewable_growth_pct",
    "oil_consumption_change_pct",
    "oil_exposure_pct",
    "spr_days_2026"
]])

# ================================
# BAR CHART 1: Oil Exposure
# ================================
plt.figure(figsize=(10,6))

df_exposure = df_2024.sort_values("oil_exposure_pct", ascending=False)

plt.bar(df_exposure["country"], df_exposure["oil_exposure_pct"])

plt.xticks(rotation=45)
plt.ylabel("Oil Exposure (%)")
plt.title("Oil Exposure by Country (2024)")

plt.tight_layout()
plt.savefig(visual_path / "bar_oil_exposure.png", dpi=300)
plt.close()


# ================================
# BAR CHART 2: Oil Consumption Change
# ================================
plt.figure(figsize=(10,6))

df_oil_change = df_2024.sort_values("oil_consumption_change_pct")

plt.bar(df_oil_change["country"], df_oil_change["oil_consumption_change_pct"])

plt.xticks(rotation=45)
plt.axhline(0)  # baseline
plt.ylabel("Oil Consumption Change (%)")
plt.title("Oil Consumption Change by Country (2024)")

plt.tight_layout()
plt.savefig(visual_path / "bar_oil_consumption_change.png", dpi=300)
plt.close()


# ================================
# COLOR-CODED SCATTER
# ================================
colors = []

for val in df_2024["oil_exposure_pct"]:
    if val >= 60:
        colors.append("red")
    elif val >= 30:
        colors.append("orange")
    else:
        colors.append("green")

plt.figure(figsize=(8,6))

plt.scatter(
    df_2024["oil_exposure_pct"],
    df_2024["oil_consumption_change_pct"],
    c=colors
)

# Labels
for _, row in df_2024.iterrows():
    plt.text(
        row["oil_exposure_pct"],
        row["oil_consumption_change_pct"],
        row["iso_code"],
        fontsize=8
    )

plt.xlabel("Oil Exposure (%)")
plt.ylabel("Oil Consumption Change (%)")
plt.title("Oil Exposure vs Oil Consumption Change (Color-Coded)")
plt.axhline(0)
plt.grid(True)

plt.tight_layout()
plt.savefig(visual_path / "scatter_exposure_vs_oil_change.png", dpi=300)
plt.close()


print("Charts created successfully.")