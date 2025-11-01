"""
Handles the data loading phase.

- Saves the final processed DataFrame to a specified CSV output path.
- Ensures consistent file formatting and no index column.
"""

import pandas as pd

def load_data(df: pd.DataFrame, output_path: str):
    df.to_csv(output_path, index = False)
    print(f"Data saved tp {output_path}")