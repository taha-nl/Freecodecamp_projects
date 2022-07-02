import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x,y)


    # Create first line of best fit
    res=linregress(x,y)
    x1 = list(range(1880, 2051))
    y1 = []
    for year in x1:
      y1.append(res.intercept + res.slope * year)
    
    plt.plot(x1, y1, 'r', label = 'Best Fit Line 1', color='red')
    plt.legend()
  


    # Create second line of best fit
    xx = df[ df['Year'] >= 2000 ]['Year']
    yy = df[ df['Year'] >= 2000 ]['CSIRO Adjusted Sea Level']
    result=linregress(xx,yy)
    new_slope = result.slope
    new_intercept = result.intercept
    x2=list(range(2000, 2051))
    y2=[]
    for year in x2:
      y2.append(new_intercept + new_slope * year)
    
    plt.plot(x2, y2, 'r', label = 'Best Fit Line 2', color='red')
    plt.legend()


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()