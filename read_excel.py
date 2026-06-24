import pandas as pd

try:
    df = pd.read_excel('PROSPECTOS_CORPICIA.xlsx')
    print("Columns:")
    print(df.columns.tolist())
    print("\nFirst 3 rows:")
    print(df.head(3).to_dict(orient='records'))
except Exception as e:
    print(f"Error reading file: {e}")
