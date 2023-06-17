import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_scatterplot(ax, df, *, x_col, y_col, title, xlabel, ylabel, color):
    """
    This function creates a scatter plot with a linear regression line from a DataFrame.

    Parameters:
    ax (matplotlib.axes.Axes): The Axes object to plot on.
    df (pandas.DataFrame): The DataFrame containing the data.
    x_col (str): The column in the DataFrame to use for the x-axis.
    y_col (str): The column in the DataFrame to use for the y-axis.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    color (str): The color of the scatter plot points.
    """

    # Create the plot
    sns.regplot(x=df[x_col], y=df[y_col], scatter_kws={"alpha": 0.3}, color=color, ax=ax)

    # Add labels and title
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

def create_scatterplot2(df1, df2, x_col, y_col, title, xlabel, ylabel):
    # Scatter plot for yellow taxis
    plt.scatter(df1[x_col], df1[y_col], color='yellow', label='Yellow Taxis')
    
    # Scatter plot for green taxis
    plt.scatter(df2[x_col], df2[y_col], color='green', label='Green Taxis')

    # Adding labels and a legend
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    
    # Linear regression line for yellow taxis
    sns.regplot(x=df1[x_col], y=df1[y_col], scatter=False, color='yellow')

    # Linear regression line for green taxis
    sns.regplot(x=df2[x_col], y=df2[y_col], scatter=False, color='green')
    
    # Displaying the scatter plot
    plt.show()
    
    
    
def create_scatterplot1(df, x_col, y_col, title, xlabel, ylabel):
    """
    This function creates a scatter plot with a linear regression line from a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    x_col (str): The column in the DataFrame to use for the x-axis.
    y_col (str): The column in the DataFrame to use for the y-axis.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    """

    # Create the plot
    plt.figure(figsize=(7, 7))
    sns.regplot(x=df[x_col], y=df[y_col], scatter_kws={"alpha": 0.3})

    # Add labels and title
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Show the plot
    plt.show()

def get_a_random_chunk_property(data):
    """
    This function only serves an example of fetching some of the properties
    from the data.
    Indeed, all the content in "data" may be useful for your project!
    """

    chunk_index = np.random.choice(len(data))

    date_list = list(data[chunk_index]["near_earth_objects"].keys())

    date = np.random.choice(date_list)

    objects_data = data[chunk_index]["near_earth_objects"][date]

    object_index = np.random.choice(len(objects_data))

    object = objects_data[object_index]

    properties = list(object.keys())
    property = np.random.choice(properties)

    print("date:", date)
    print("NEO name:", object["name"])
    print(f"{property}:", object[property])


def load_data_from_google_drive(url):
    url_processed='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url_processed)
    return df


def print_passenger_count_distribution(df, title):
    print(title)
    passenger_counts = df['passenger_count'].value_counts().sort_index()
    for count in range(1, 10):
        count_str = "{:,}".format(passenger_counts.get(count, 0))
        print(f"{count}: {count_str}")

def print_payment_type_distribution(df, title):
    print(title)
    payment_counts = df['payment_type'].value_counts()
    for payment_type, count in payment_counts.items():
        count_str = "{:,}".format(count)
        print(f"{payment_type}: {count_str}")


def plot_histogram(df, column_name, title, xlabel, ylabel, color):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.hist(df[column_name], bins=12, color=color, edgecolor='black')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.show()