import streamlit as st
import plotly.express as px
from utils.combine_data import road_accidents_csv

def plot_chart_based_on_inputs(category, aggregate_column, agg_method, chart_type="", display=True):
    """
    Generates a Plotly chart based on user-selected category, aggregation, and chart type.

    Parameters:
    - category (str): Column to group by.
    - aggregate_column (str): Column to aggregate.
    - agg_method (str): Aggregation method ('Count', 'Sum', 'Average').
    - chart_type (str): Type of chart ('Bar', 'Line', 'Area', 'Pie', 'Scatter', 'Histogram').
    - display (bool): If True, renders the chart in Streamlit.

    Returns:
    - result_data (pd.DataFrame): Aggregated DataFrame
    - fig (plotly.graph_objs._figure.Figure): Plotly figure object (or None if invalid)
    """
    data = road_accidents_csv

    try:
        # Aggregation
        if agg_method == "Count":
            result_data = data.groupby(category)[aggregate_column].count().reset_index()
        elif agg_method == "Sum":
            result_data = data.groupby(category)[aggregate_column].sum().reset_index()
        elif agg_method == "Average":
            result_data = data.groupby(category)[aggregate_column].mean().reset_index()
        else:
            st.error("Invalid aggregation method.")
            return None, None

        if result_data.empty:
            st.warning("No data available for the selected options.")
            return result_data, None

        # Plotting
        fig = None
        if chart_type == "Bar":
            fig = px.bar(
                result_data, x=category, y=aggregate_column,
                title=f"{agg_method} of {aggregate_column} by {category}",
                text=aggregate_column
            )
            fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')

        elif chart_type == "Line":
            fig = px.line(result_data, x=category, y=aggregate_column,
                          title=f"{agg_method} of {aggregate_column} by {category}",
                          markers=True)

        elif chart_type == "Area":
            fig = px.area(result_data, x=category, y=aggregate_column,
                          title=f"{agg_method} of {aggregate_column} by {category}")

        elif chart_type == "Pie":
            fig = px.pie(result_data, names=category, values=aggregate_column,
                         title=f"{agg_method} of {aggregate_column} by {category}")

        elif chart_type == "Scatter":
            fig = px.scatter(result_data, x=category, y=aggregate_column,
                             title=f"{agg_method} of {aggregate_column} by {category}",
                             trendline="ols")

        elif chart_type == "Histogram":
            fig = px.histogram(result_data, x=aggregate_column, nbins=20,
                               title=f"Distribution of {aggregate_column}")
            fig.update_traces(hovertemplate='Value: %{x:.2f}<br>Count: %{y}')

        else:
            st.warning("Select a valid chart type.")
            return result_data, None

        # Display chart in Streamlit
        if display and fig:
            st.plotly_chart(fig, use_container_width=True)

        return result_data, fig

    except Exception as e:
        st.error(f"Error processing data: {e}")
        return None, None
