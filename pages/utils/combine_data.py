import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "cleaned_accidents_data.csv")


def read_accidents_data():
    """Reads the cleaned accidents data from CSV."""

    data = pd.read_csv(DATA_PATH)
    
    renamed_df = data.rename({"SPV":"Speed Violation", "UPD":"Use of Phone While Driving",
                              "TBT":"Tyre Burst", "MDV":"Mechanically Deficient Vehicle",
                              "BFL":"Brake Failure", "OVL":"Overloading", "DOT":"Dangerous Overtaking",
                              "WOT":"Wrongful Overtaking", "DGD":"Dangerous Driving",
                              "BRD":"Bad Road", "RTV":"Route Violation", "OBS":"Road Obstruction Violation",
                              "SOS":"Sleeping on Steering", "DAD":"Driving Under Alcohol/Drug Influence",
                              "PWR" : "Poor Weather", "FTQ":"Fatigue", "SLV":"Sign Light Violation",
                              "OTH":"Others"}, axis=1)
    return renamed_df

# Load dataset
road_accidents_csv = read_accidents_data()
