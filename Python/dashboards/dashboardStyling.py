# How to Style Your Dashboard for Map-Based Apps With Python
# A Practical Guide to Designing Clean, User-Friendly Dashboards for Geospatial Data Using Python

import streamlit as st
import folium
from streamlit_folium import st_folium

# Set page config
st.set_page_config(layout="wide", page_title="Styled Geo Dashboard")

# Sidebar controls
st.sidebar.title("Controls")
selected_layer = st.sidebar.selectbox("Select Layer", ["Default", "Heatmap", "Clusters"])
show_metrics = st.sidebar.checkbox("Show Key Metrics", value=True)

# Layout
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("### Key Insights")
    if show_metrics:
        st.metric("Coverage Area", "1,250 km²")
        st.metric("Active Sites", "82")
        st.metric("Population Reached", "540,000")

with col2:
    st.markdown("### Interactive Map")

    # Create a Folium map
    m = folium.Map(location=[-1.2921, 36.8219], zoom_start=10, tiles="CartoDB positron")

    # Add sample marker
    folium.Marker(
        [-1.2921, 36.8219],
        popup="Nairobi",
        tooltip="Center",
        icon=folium.Icon(color="blue")
    ).add_to(m)

    # Render map in Streamlit
    st_data = st_folium(m, width=700, height=500)

    # Run the app using: streamlit run Python/dashboards/dashboardStyling.py
