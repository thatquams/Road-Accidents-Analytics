
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Accident Prevention Dashboard",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 3rem;
        padding: 0.5rem 2rem;
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0;'>
        <h1>⚠️ Accident Prevention Dashboard</h1>
        <p style='color: #666; font-size: 1.1rem;'>Real-time risk analysis and prediction</p>
    </div>
""", unsafe_allow_html=True)

# Create tabs for navigation
analysis, map_analysis, predicions = st.tabs(["Analysis", "Map Analysis", "Predictions"])

with analysis:
    # Import and run Analysis page
    exec(open('analysis_page.py').read())
    
with map_analysis:
    # Import and run Map Analysis page
    exec(open('map_analysis_page.py').read())
    

with predicions:
    # Import and run Predictions page
    exec(open('predictions_page.py').read())
 