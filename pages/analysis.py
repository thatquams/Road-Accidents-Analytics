import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from utils.combine_data import road_accidents_csv


def plot_chart_based_on_inputs(category, aggregate_column, agg_method, chart_type=""):
    data = road_accidents_csv

    try:
        # Determine aggregation function
        if agg_method == "Count":
            result_data = data.groupby(category)[aggregate_column].count().reset_index()

        elif agg_method == "Sum":
            result_data = data.groupby(category)[aggregate_column].sum().reset_index()

        elif agg_method == "Average":
            result_data = data.groupby(category)[aggregate_column].mean().reset_index()

        else:
            st.error("Invalid aggregation method.")
            return None

        #  PLOTTING SECTION 

        # Bar Chart 
        if chart_type == "Bar":
            fig = px.bar(
                result_data,
                x=category,
                y=aggregate_column,
                title=f"{agg_method} of {aggregate_column} by {category}",
                text=aggregate_column
            )
            fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')
            st.plotly_chart(fig, use_container_width=True)

        # Line Chart 
        elif chart_type == "Line":
            fig = px.line(
                result_data,
                x=category,
                y=aggregate_column,
                title=f"{agg_method} of {aggregate_column} by {category}",
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)

        # Area Chart
        elif chart_type == "Area":
            fig = px.area(
                result_data,
                x=category,
                y=aggregate_column,
                title=f"{agg_method} of {aggregate_column} by {category}"
            )
            st.plotly_chart(fig, use_container_width=True)

        # Pie Chart
        elif chart_type == "Pie":
            fig = px.pie(
                result_data,
                names=category,
                values=aggregate_column,
                title=f"{agg_method} of {aggregate_column} by {category}"
            )
            st.plotly_chart(fig, use_container_width=True)

        # Scatter Plot
        elif chart_type == "Scatter":
            fig = px.scatter(
                result_data,
                x=category,
                y=aggregate_column,
                title=f"{agg_method} of {aggregate_column} by {category}",
                trendline="ols"
            )
            st.plotly_chart(fig, use_container_width=True)

        # Histogram 
        elif chart_type == "Histogram":
            fig = px.histogram(
                result_data,
                x=aggregate_column,
                nbins=20,
                title=f"Distribution of {aggregate_column}"
            )
            fig.update_traces(hovertemplate='Value: %{x:.2f}<br>Count: %{y}')
            st.plotly_chart(fig, use_container_width=True)

        # # --- Heatmap (Correlation Matrix) ---
        # elif chart_type == "Heatmap":
        #     corr = result_data.corr(numeric_only=True).round(2)

        #     fig = px.imshow(
        #         corr,
        #         text_auto=True,
        #         color_continuous_scale="Blues",
        #         title=f"Correlation Heatmap"
        #     )
        #     st.plotly_chart(fig, use_container_width=True)

        # else:
        #     st.warning("Select a valid chart type")
        #     return None

        return result_data

    except Exception as e:
        st.error(f"Error processing data: {e}")
        return None
