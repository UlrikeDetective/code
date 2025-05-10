""" Prompt: Advertising-sales correlation

Plot a bubble chart to explore the correlation between advertising spend
and sales volume across different media channels, using 'chocolate' for TV,
'cyan' for online, and 'crimson' for print media.

Matplotlib Color Mapping: colors = {'TV': 'chocolate', 'Online': 'cyan', 
'Print': 'crimson'}Matplotlib Figure Size: figsize=(10, 6)Plotly Color 
Mapping: color_discrete_map={'TV': 'chocolate', 'Online': 'cyan', 'Print': 
'crimson'} """

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Create sample data
np.random.seed(42)
data = {
    'Channel': ['TV'] * 20 + ['Online'] * 20 + ['Print'] * 20,
    'Ad_Spend': np.random.uniform(10, 100, 60),
    'Sales': np.random.uniform(50, 200, 60),
    'Market_Size': np.random.uniform(1000, 5000, 60)
}
df = pd.DataFrame(data)

# Matplotlib visualization
plt.figure(figsize=(10, 6))
colors = {'TV': 'chocolate', 'Online': 'cyan', 'Print': 'crimson'}

for channel in colors:
    mask = df['Channel'] == channel
    plt.scatter(df[mask]['Ad_Spend'], 
               df[mask]['Sales'],
               s=df[mask]['Market_Size']/50,
               c=colors[channel],
               alpha=0.6,
               label=channel)

plt.xlabel('Advertising Spend ($K)')
plt.ylabel('Sales Volume ($K)')
plt.title('Advertising Spend vs. Sales Volume by Channel')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Plotly visualization
fig = px.scatter(df, 
                x='Ad_Spend',
                y='Sales',
                size='Market_Size',
                color='Channel',
                color_discrete_map={'TV': 'chocolate', 
                                  'Online': 'cyan', 
                                  'Print': 'crimson'},
                title='Advertising Spend vs. Sales Volume by Channel',
                labels={'Ad_Spend': 'Advertising Spend ($K)',
                       'Sales': 'Sales Volume ($K)',
                       'Market_Size': 'Market Size'},
                height=600,
                width=1000)

fig.show()