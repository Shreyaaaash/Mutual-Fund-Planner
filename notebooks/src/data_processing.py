import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_roi(data):
    initial_prices = data.iloc[0]
    final_prices = data.iloc[-1]
    return ((final_prices - initial_prices) / initial_prices) * 100

def calculate_volatility(data):
    return data.std()
