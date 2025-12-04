import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5, label='Original Data')

    # 3. Create first line of best fit (Using all data: 1880 - 2050)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create list of years from 1880 to 2050
    years_extended = range(1880, 2051)
    
    # Calculate line values: y = mx + c (slope * x + intercept)
    line_fit = res.slope * years_extended + res.intercept
    
    # Plot the first line
    ax.plot(years_extended, line_fit, color='red', label='Best Fit (1880-2050)')

    # 4. Create second line of best fit (Using data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create list of years from 2000 to 2050
    years_recent = range(2000, 2051)
    
    # Calculate line values
    line_fit_recent = res_recent.slope * years_recent + res_recent.intercept
    
    # Plot the second line
    ax.plot(years_recent, line_fit_recent, color='green', label='Best Fit (2000-2050)')

    # 5. Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
