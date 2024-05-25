""" Data Profiling
Data profiling is the process of examining and summarizing the characteristics of a dataset. It helps in understanding 
the structure, content, and quality of the data. You can automate data profiling using Python libraries like Pandas Profiling or Dora.

Example: Generating Data Profile using Pandas Profiling
Suppose you have a dataset and want to generate a comprehensive data profile report. Here’s how you can automate this task using 
Pandas Profiling: This code snippet loads the dataset using Pandas and creates a ProfileReport object from the Pandas Profiling library, 
specifying the dataset and a title for the report.The to_file() method is used to save the generated data profile report as an HTML file.
    The generated report includes various statistics and visualizations, such as data types, missing values, value distributions, 
correlations, and more. It provides a comprehensive overview of the dataset's characteristics. 

Code isn't working yet."""

import pandas as pd
from pandas_profiling import ProfileReport

# Load the dataset
data = pd.read_csv('GPS_location_cleaned.csv')

# Generate data profile report
profile = ProfileReport(data, title='Data Profile Report')

# Save the report as an HTML file
profile.to_file('data_profile_report.html')
