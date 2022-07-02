import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df =df=pd.read_csv('fcc-forum-pageviews.csv',index_col=0,parse_dates=[0]) 

# Clean data
df=df[(df['value']>=df['value'].quantile(0.025))&(df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    fig=plt.figure(figsize=(12,6))
    plt.plot(df.index,df['value'].values,color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar =df.copy().reset_index()
    df_bar['year']=df_bar['date'].dt.year
    df_bar['month']=df_bar['date'].dt.month_name()
    df_bar=df_bar.groupby(['year','month']).mean().reset_index()

    # Draw bar plot
    list_month=['January','February','March','April','May','June','July','August','September','October','November','December']
    g = sns.catplot(x="year", kind="bar", hue="month", y="value", data=df_bar, hue_order=list_month, ci=None, legend=False, palette="hls")
    fig = g.fig
    ax = g.ax    
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    plt.xticks(rotation=90)
    plt.legend(loc='upper left', title="Month")
    plt.setp(ax.get_legend().get_texts(), fontsize='8')
    plt.setp(ax.get_legend().get_title(), fontsize='8')
    plt.tight_layout()
  





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    list_month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    sns.boxplot(x="year", y="value", data=df_box,ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('Page Views')
    ax.set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(x="month", y="value", data=df_box,ax=ax2,order=list_month)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
