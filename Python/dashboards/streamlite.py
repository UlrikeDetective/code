# This is a simple Streamlit dashboard example that includes various UI elements
# such as text input, checkboxes, and a line chart. It also demonstrates how to use
# columns for layout and an expander for additional information.

# pip install streamlit
# To run this script, save it as streamlite.py and execute the following command in your terminal:
# streamlit --version

# Import necessary libraries

import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="My Dashboard", layout="wide")

# Sidebar configuration
st.sidebar.title("User Experience")
theme = st.sidebar.selectbox("Choose a theme", ["Light", "Dark"])
show_chart = st.sidebar.checkbox("Show Chart", value=True)

# Main content
st.title("Interactive Dashboard with Streamlit")

# Text input for dynamic interactivity
name = st.text_input("Enter your name", value="Guest")
st.write(f"Hello, {name}!")

# Generating and displaying a line chart
if show_chart:
    data = pd.DataFrame(np.random.randn(20, 3), columns=["Category A", "Category B", "Category C"])
    st.line_chart(data)
else:
    st.write("Chart hidden. Enable it from the sidebar.")

# Displaying key metrics
col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "10k", "+5%")
col2.metric("Users", "1.2k", "+10%")
col3.metric("Performance", "98%", "+2%")

# Expandable section for additional information
with st.expander("About this app"):
    st.write("This app demonstrates the power of Streamlit for creating dynamic dashboards. "
             "You can interact with various elements such as text inputs, checkboxes, and charts.")

# Footer note (optional)
st.write("---")
st.write("Built with Streamlit. Visit [streamlit.io](https://streamlit.io) for more information.")

# Run the app using: streamlit run Python/dashboards/streamlite.py