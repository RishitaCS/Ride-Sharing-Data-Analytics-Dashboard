import pandas as pd
import sqlite3
from pathlib import Path

DATA_PATH = Path("data/raw/uber-rides-dataset.csv")
DB_PATH = Path("data/rides.db")
CLEANED_PATH = Path("data/cleaned_trips.parquet")

# Create data folder if not exists
Path("data").mkdir(exist_ok=True)

# Load CSV
df = pd.read_csv(DATA_PATH)

# Convert datetime columns
for col in ['trip_start_time', 'trip_end_time', 'trip_completed_at']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Fill missing numerical values with 0
for col in ['distance_kms', 'price_usd', 'wait_time']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Save cleaned parquet
df.to_parquet(CLEANED_PATH, index=False)

# Save to SQLite
with sqlite3.connect(DB_PATH) as conn:
    df.to_sql("trips", conn, if_exists="replace", index=False)

print("Data cleaned and saved to SQLite and Parquet")
