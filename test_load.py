from data_loader import load_data
import os

print("Testing data_loader.py...")
try:
    df = load_data()
    print(f"Success! Loaded {len(df)} rows.")
    print(f"Columns: {df.columns.tolist()}")
except Exception as e:
    print(f"Error loading data: {e}")
