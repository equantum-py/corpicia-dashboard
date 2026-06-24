import pandas as pd
import os

try:
        file_path = os.path.join(os.path.dirname(__file__), 'PROSPECTOS_CORPICIA.xlsx')
        df = pd.read_excel(file_path)
        print("Columns:")
        print(df.columns.tolist())
        print("\nFirst 3 rows:")
        print(df.head(3).to_dict(orient='records'))
except Exception as e:
        print(f"Error reading file: {e}")
