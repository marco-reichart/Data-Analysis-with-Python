import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', delimiter=',')
    
    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    #include every year in the dataset till 2050
    year_range = np.arange(1880, 2051, 1)
    plt.plot(year_range, res.intercept + res.slope * year_range, 'r', label='fitted line')

    # Create second line of best fit
    #include only the years between 2000 and 2050
    year_range_recent = np.arange(2000, 2051, 1)
    #filter out years that predate the year 2000
    recent_df = df[df['Year'] >= 2000]
    res_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    plt.plot(year_range_recent, res_recent.intercept + res_recent.slope * year_range_recent, 'g', label='fitted line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()