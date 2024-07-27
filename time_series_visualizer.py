import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) 
     & (df['value'] <= df['value'].quantile(0.975))]
# convert index date values to pandas datetime objects
df.index = pd.to_datetime(df.index)

def draw_line_plot():
    # Draw line plot
    fig = plt.figure()
    
    plt.plot(df.index, df['value'])
    #stretched fig horizontally
    fig.set_figwidth(10)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    #return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby('date')['value'].mean().reset_index().set_index('date')
    df_bar['year'] = df_bar.index.strftime('%Y')
    df_bar['month'] = df_bar.index.strftime('%B')

    # Draw bar plot
    fig = sns.catplot(x='year', y='value', hue='month', hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], palette='colorblind', kind='bar', data=df_bar, errorbar=None)
    #Use the bbox_to_anchor parameter for more fine-grained control, including moving the legend outside of the axes
    sns.move_legend(fig, "upper left", bbox_to_anchor=(1, 1))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    pass
    # Prepare data for box plots (this part is done!)
    #df_box = df.copy()
    #df_box.reset_index(inplace=True)
    #df_box['year'] = [d.year for d in df_box.date]
    #df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
   



    # Save image and return fig (don't change this part)
    #fig.savefig('box_plot.png')
    #return fig
