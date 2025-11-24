import streamlit as st
from utils.combine_data import road_accidents_csv
from plotly.express import scatter_mapbox

def run_map_analysis():
    """
    Streamlit UI for interactive accident severity map.
    """
    st.subheader("Accident Severity Map Visualization")

    options = ["FATAL", "SERIOUS", "MINOR", "TOTAL CASES"]
    selected_metric = st.selectbox("Select Severity Type", options, index=0)

    # Plot map
    fig = scatter_mapbox(
        road_accidents_csv,
        lat="lat",
        lon="lon",
        size=selected_metric,
        color=selected_metric,
        hover_name="STATE",
        hover_data={"lat": False, "lon": False, selected_metric: True},
        zoom=5,
        height=600,
        color_continuous_scale="Reds",
        size_max=30
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        title=f"{selected_metric} Distribution Across Locations",
        margin={"r":0, "t":40, "l":0, "b":0}
    )

    st.plotly_chart(fig, use_container_width=True)
