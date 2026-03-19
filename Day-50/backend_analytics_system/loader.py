import pandas as pd

def load_data(filepath: str):
    return pd.read_csv(filepath)
