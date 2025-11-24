import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "cleaned_accidents_data.csv")

def combine_data(on: str = "STATE", how: str = "left"):
    """Combines weather and state coordinates datasets."""
    df1 = pd.read_csv(os.path.join(os.path.dirname(__file__), "..", "data", "weather_accidents.csv"))
    df2 = pd.read_csv(os.path.join(os.path.dirname(__file__), "..", "data", "state_coordinates.csv"))
    
    combined_df = pd.merge(df1, df2, on=on, how=how)
    combined_df.to_csv(DATA_PATH, index=False)
    return combined_df

def read_accidents_data():
    """Reads the cleaned accidents data from CSV."""
    # If file doesn't exist, create it
    if not os.path.exists(DATA_PATH):
        combine_data()
    return pd.read_csv(DATA_PATH)

# Load dataset
road_accidents_csv = read_accidents_data()
