import pandas as pd

def load_market_data(file_path):
    """Load market data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def calculate_moving_average(data, window=10):
    """Calculate moving average for the given data."""
    data['MA'] = data['Close'].rolling(window=window).mean()
    return data