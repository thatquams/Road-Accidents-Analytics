# predictions_page.py
import streamlit as st
import pandas as pd
import joblib
from utils.combine_data import road_accidents_csv
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "utils/data/gradient_boosting.pkl")
STATE_ENCODER_PATH = os.path.join(os.path.dirname(__file__), "utils/data/state_encoder.pkl")
SCALER_PATH = os.path.join(os.path.dirname(__file__), "utils/data/scaler.pkl")

# Load pre-trained model and encoders/scalers
load_model = joblib.load(MODEL_PATH)
state_encoder = joblib.load(STATE_ENCODER_PATH)
scaler = joblib.load(SCALER_PATH)


def run_predictions_page():
    """
    Launches the Predictions tab for predicting road accident severity.

    Users can input:
    1. Causative factors: Driver, Mechanical, Environment, Road, Vehicle (0-1 scale)
    2. Temporal features: Year and Quarter
    3. Weather conditions: Cloud Amount, Soil Wetness, Precipitation, Pressure, Humidity, Dew Point,
       Earth Skin Temperature, Wind Direction, Wind Speed
    4. Location: STATE (Nigerian state)

    The function:
    - Collects all inputs via Streamlit UI components
    - Encodes categorical 'STATE' using a pre-trained encoder
    - Scales numerical features using a pre-trained StandardScaler
    - Predicts accident severity using the pre-trained SVC model
    - Displays input summary and predicted severity interactively
    """

    st.title("Road Accident Severity Prediction")
    
    #  Field Instructions
    with st.expander("Instructions for Each Field  (kindly read before making selections)"):
        st.markdown("""
        ### Causative Factors (0 - 1)
        **Choose a value between 0 and 1 for each factor, reflecting its contribution to the accident.**  
        - **Driver:** Human Factors (Speed Violation, Overloading, Dangerous Overtaking, Wrongful Overtaking, Dangerous Driving, Sleeping on Steering, Driving Under Alcohol/Drug Influence).  
        _Select a higher value (closer to 1) if these factors significantly contributed to the accident._  
        - **Mechanical:** Vehicle mechanical issues (Brake Failure, Mechanically Deficient Vehicle, Tyre Burst, Bad Road).  
        _Use a higher value if mechanical problems were a major cause._  
        - **Environment:** Environmental or weather conditions (Road Obstruction Violation, Poor Weather, Fatigue).  
        _Assign a higher value if environmental factors played a strong role._  
        - **Road:** Road condition or infrastructure issues (Route Violation, Sign Light Violation).  
        _Higher value indicates poor road conditions contributed to the accident._  
        - **Vehicle:** Vehicle type or condition contribution (Tyre Burst).  
        _Select a value based on how much vehicle condition influenced the accident._  

        **Year & Quarter:**  
        - **Year:** Year of the accident (2025 or above).  
        - **Quarter:** Quarter of the year (1-4).  

        **Weather Conditions:**  
        - **Cloud Amount (%):** Cloud coverage percentage.  
        - **Surface Soil Wetness (1):** Soil wetness index (0-1).  
        - **Precipitation (mm/day):** Daily precipitation in mm.  
        - **Surface Pressure (kPa):** Atmospheric surface pressure.  
        - **Specific Humidity (g/kg):** Humidity at 2 meters.  
        - **Dew/Frost Point (°C):** Dew or frost point temperature.  
        - **Earth Skin Temperature (°C):** Temperature of the earth surface.  
        - **Wind Direction (°):** Wind direction in degrees.  
        - **Wind Speed (m/s):** Wind speed at 2 meters.  

        **State:**  
        - Select the Nigerian state where the accident occurred.
            """)

    # Causative factors
    DRIVER = st.slider("Driver Factor (0-1)", 0.0, 1.0, 0.5)
    MECHANICAL = st.slider("Mechanical Factor (0-1)", 0.0, 1.0, 0.5)
    ENVIRONMENT = st.slider("Environment Factor (0-1)", 0.0, 1.0, 0.5)
    ROAD = st.slider("Road Factor (0-1)", 0.0, 1.0, 0.5)
    VEHICLE = st.slider("Vehicle Factor (0-1)", 0.0, 1.0, 0.5)

    # Year & Quarter
    YEAR = st.number_input("Year", min_value=2025, max_value=2100, value=2025)
    QUARTER = st.selectbox("Quarter", options=[1, 2, 3, 4])

    # Weather conditions
    with st.expander("Weather Conditions"):
        col1, col2 = st.columns(2)
        with col1:
            cloud_amt = st.number_input("Cloud Amount (%)", value=50.0)
            soil_wet = st.number_input("Surface Soil Wetness (1)", value=0.5)
            precip = st.number_input("Precipitation (mm/day)", value=1.0)
            pressure = st.number_input("Surface Pressure (kPa)", value=101.0)
            humidity = st.number_input("Specific Humidity (g/kg)", value=10.0)
        with col2:
            dew_point = st.number_input("Dew/Frost Point (°C)", value=15.0)
            earth_temp = st.number_input("Earth Skin Temp (°C)", value=25.0)
            wind_dir = st.number_input("Wind Direction (°)", min_value=0.0, max_value=360.0, value=180.0)
            wind_speed = st.number_input("Wind Speed (m/s)", value=2.0)

    # State selection
    STATE = st.selectbox("STATE", options=road_accidents_csv['STATE'].unique().tolist())

    # Predict button
    if st.button("Predict Accident Severity"):
        input_df = pd.DataFrame([{
            "DRIVER": DRIVER,
            "MECHANICAL": MECHANICAL,
            "ENVIRONMENT": ENVIRONMENT,
            "ROAD": ROAD,
            "VEHICLE": VEHICLE,
            "deg Cloud Amount (%)": cloud_amt,
            "Surface Soil Wetness (1)": soil_wet,
            "Precipitation Corrected (mm/day)": precip,
            "Surface Pressure (kPa)": pressure,
            "Specific Humidity at 2 Meters (g/kg)": humidity,
            "Dew/Frost Point at 2 Meters (C)": dew_point,
            "Earth Skin Temperature (C)": earth_temp,
            "Wind Direction at 2 Meters (Degrees)": wind_dir,
            "Wind Speed at 2 Meters (m/s)": wind_speed,
            "YEAR": YEAR,
            "QUARTER": QUARTER,
            "STATE": STATE
        }])

        # Display inputs
        st.json(input_df.to_dict(orient="records")[0])

        # Encode STATE
        input_df["STATE_TE"] = state_encoder.transform(input_df[["STATE"]])
        input_df = input_df.drop("STATE", axis=1)

        # Scale features
        input_df[input_df.columns] = scaler.transform(input_df[input_df.columns])

        # Predict
        prediction = load_model.predict(input_df)
        risk_map = {0: "LOW RISK", 1: "HIGH RISK"}
        st.success(f"Predicted Accident Severity: {risk_map.get(prediction[0], 'UNKNOWN')}")


