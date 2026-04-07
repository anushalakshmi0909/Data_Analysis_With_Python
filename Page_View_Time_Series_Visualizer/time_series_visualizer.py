import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# Load and clean data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.lineplot(data=df, x=df.index, y='value', ax=ax)
    ax.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
           xlabel="Date",
           ylabel="Page Views")
    fig.savefig("line_plot.png")
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month_num'] = df_bar.index.month
    df_bar['month'] = df_bar.index.month_name()  # Full month names

    # Pivot: average page views per month per year
    df_pivot = df_bar.groupby(['year', 'month_num', 'month'])['value'].mean().reset_index()
    df_pivot = df_pivot.pivot(index='year', columns='month', values='value')

    # Ensure month order Jan-Dec
    month_order = list(calendar.month_name[1:])
    df_pivot = df_pivot[month_order]

    # Plot
    fig = df_pivot.plot(kind='bar', figsize=(20, 10)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    df_box = df.copy().reset_index()
    df_box['year'] = df_box['date'].dt.year
    df_box['month_num'] = df_box['date'].dt.month
    df_box['month'] = df_box['date'].dt.strftime('%b')  # Abbreviated month names: Jan, Feb, ...

    # Sort months for boxplot
    df_box = df_box.sort_values('month_num')

    fig, axes = plt.subplots(1, 2, figsize=(24, 10))

    # Year-wise Box Plot
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], orient='v')
    axes[0].set(title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views")

    # Month-wise Box Plot (secondary)
    month_order = list(calendar.month_abbr[1:])  # Jan, Feb, ..., Dec
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=axes[1], orient='v')
    axes[1].set(title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views")

    fig.savefig("box_plot.png")
    return fig