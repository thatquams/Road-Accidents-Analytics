import streamlit as st 
from analysis import plot_chart_based_on_inputs
from utils.combine_data import road_accidents_csv

aggregation_methods = ['Sum', 'Average', 'Count']
chart_types = ['Bar', 'Line', 'Area', 'Pie', 'Scatter', 'Histogram']

columns = road_accidents_csv.columns.tolist()

category, aggregate_column, agg_method, chart_type = st.columns(4)

with category:
    cat = st.selectbox('Category', options=columns, index=None, placeholder="Select a Category")

with aggregate_column:
    agg_col = st.selectbox('Aggregate', options=columns, index=None, placeholder="Select Aggregate Column")

with agg_method:
    agg = st.selectbox('Aggregation Method', options=aggregation_methods, 
                               index=None, placeholder="Select Aggregation method")

with chart_type:
    chart_type = st.selectbox('Chart Type', options=chart_types, 
                              index=None, placeholder="Select chart")
 
if cat and agg_col and agg and chart_type:
    fig = plot_chart_based_on_inputs(cat, agg_col, agg, chart_type)
    # st.write(fig)
    # st.pyplot(fig)
else:
    st.info("Choose all options to generate a chart.")