import plotly.express as px
import streamlit as st
from utils.combine_data import road_accidents_csv

def plot_fatalities_map(df, metric):
    """
    Creates an interactive map showing accident severity distribution 
    using latitude and longitude.

    metric: selected severity column (FATAL, SERIOUS, MINOR, TOTAL CASES)
    """

    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        size=metric,                 # bubble size = selected metric
        color=metric,                # color intensity = selected metric
        hover_name="STATE",
        hover_data={"lat": False, "lon": False, metric: True},
        zoom=5,
        height=600,
        color_continuous_scale="Reds"
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        title=f"{metric} Distribution Across Locations",
        margin={"r":0, "t":40, "l":0, "b":0}
    )

    return fig


# STREAMLIT UI COMPONENT
st.subheader("Accident Severity Map Visualization")

options = ["FATAL", "SERIOUS", "MINOR", "TOTAL CASES"]
selected_metric = st.selectbox("Select Severity Type", options, index=0)

fig = plot_fatalities_map(road_accidents_csv, selected_metric)
st.plotly_chart(fig, use_container_width=True)
