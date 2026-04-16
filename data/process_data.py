import pandas as pd
from pathlib import Path

# Get the folder this script is in
base_path = Path(__file__).parent

# Load all three CSV files
df1 = pd.read_csv(base_path / "daily_sales_data_0.csv")
df2 = pd.read_csv(base_path / "daily_sales_data_1.csv")
df3 = pd.read_csv(base_path / "daily_sales_data_2.csv")

# Combine them into one DataFrame
df = pd.concat([df1, df2, df3], ignore_index=True)

# Keep only pink morsel
df = df[df["product"] == "pink morsel"]

# Remove dollar sign and convert price to float
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

# Calculate sales
df["sales"] = df["price"] * df["quantity"]

# Keep only required columns
df = df[["sales", "date", "region"]]

# Save output in the same folder as this script
df.to_csv(base_path / "output.csv", index=False)

print("Processing complete. Output saved to data/output.csv")