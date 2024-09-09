import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# Load the data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['value'])
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.savefig('line_plot.png')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy().resample('M').mean()
    df_bar = df_bar[(df_bar.index.year >= 2016) & (df_bar.index.year <= 2019)]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig, ax = plt.subplots(figsize=(10, 6))
    for month in range(1, 13):
        month_df = df_bar[df_bar.index.month == month]
        ax.bar([year for year in range(2016, 2020)], [month_df['value'][month_df.index.year == year].mean() for year in range(2016, 2020)], label=months[month-1])
    ax.set_title('Average Page Views by Month and Year')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', loc='upper right')
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(['2016', '2017', '2018', '2019'])
    plt.savefig('bar_plot.png')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box_year = df.copy().resample('Y').mean()
    df_box_month = df.copy().resample('M').mean()
    years = [2016, 2017, 2018, 2019]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))
    ax1.boxplot([df['value'][df.index.year == year] for year in years], labels=[str(year) for year in years])
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax2.boxplot([df_box_month['value'][df_box_month.index.month == i] for i in range(1, 13)], labels=months)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax1.set_yticks([0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000])
    ax1.set_yticklabels(['0', '20000', '40000', '60000', '80000', '100000', '120000', '140000', '160000', '180000', '200000'])
    plt.savefig('box_plot.png')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

# Call functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()