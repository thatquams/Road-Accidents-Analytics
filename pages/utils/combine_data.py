import pandas as pd
def combine_data(on: str, how: str):
    """
    Combines two DataFrames on a specified column using the given method.

    Parameters:
    - df1: First DataFrame.
    - df2: Second DataFrame.
    - on: Column name to join on.
    - how: Type of join to perform (default is 'inner').

    Returns:
    - Combined DataFrame.
    """
    df1 = pd.read_csv('../data/weather_accidents.csv')
    df2 = pd.read_csv('../data/state_coordinates.csv')
    
    combined_df = pd.merge(df1, df2, on=on, how=how)
    combined_df.to_csv("../data/cleaned_accidents_data.csv",index=False)
    return combined_df


# print(combine_data(on="STATE", how="left"))


def read_accidents_data():
    """
    Reads the cleaned accidents data from CSV.

    Returns:
    - DataFrame containing cleaned accidents data.
    """
    return pd.read_csv("../data/cleaned_accidents_data.csv")


road_accidents_csv = read_accidents_data()