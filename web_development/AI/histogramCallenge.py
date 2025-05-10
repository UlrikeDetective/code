# run env + pip install

""" Create a histogram to analyze the distribution of customer spending per 
visit at a shopping mall, using 'mintcream' for low spenders, 'salmon' for 
medium spenders, and 'darkcyan' for high spenders.

Matplotlib Color Mapping: colors = {'Low Spenders': 'mintcream', 
'Medium Spenders': 'salmon', 'High Spenders': 'darkcyan'}Matplotlib 
Figure Size: figsize=(12, 6)Plotly Color Mapping: color_discrete_map = 
{'Low Spenders': 'mintcream', 'Medium Spenders': 'salmon', 'High Spenders': 
 'darkcyan'} """

import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# Generate sample spending data
np.random.seed(42)
spending_data = np.concatenate([
    np.random.normal(50, 15, 300),  # Low spenders
    np.random.normal(150, 25, 400),  # Medium spenders
    np.random.normal(300, 50, 300)   # High spenders
])

# Matplotlib implementation
plt.figure(figsize=(12, 6))
bins = np.linspace(0, 500, 50)

# Create histogram with custom colors
plt.hist(spending_data[spending_data < 100], bins=bins, alpha=0.7, color='mintcream', label='Low Spenders', edgecolor='black')
plt.hist(spending_data[(spending_data >= 100) & (spending_data < 200)], bins=bins, alpha=0.7, color='salmon', label='Medium Spenders', edgecolor='black')
plt.hist(spending_data[spending_data >= 200], bins=bins, alpha=0.7, color='darkcyan', label='High Spenders', edgecolor='black')

plt.title('Distribution of Customer Spending per Visit', fontsize=14)
plt.xlabel('Spending Amount ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Plotly implementation
df = pd.DataFrame({
    'Spending': spending_data,
    'Category': pd.cut(spending_data, 
                      bins=[0, 100, 200, np.inf], 
                      labels=['Low Spenders', 'Medium Spenders', 'High Spenders'])
})

fig = px.histogram(df, x='Spending', 
                   color='Category',
                   color_discrete_map={
                       'Low Spenders': 'mintcream',
                       'Medium Spenders': 'salmon',
                       'High Spenders': 'darkcyan'
                   },
                   title='Distribution of Customer Spending per Visit',
                   labels={'Spending': 'Spending Amount ($)', 'count': 'Frequency'},
                   nbins=50)

fig.update_layout(
    width=800,
    height=400,
    showlegend=True
)
fig.show()
