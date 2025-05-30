import pandas as pd
import numpy as np

def identify_day_types(ohlc_df):
    """
    identifies whether each trading day is 'green', 'red', or 'neutral' based on the Open and Close prices.

    Parameters:
        ohlc_df (pd.DataFrame): DataFrame containing Open and Close prices with columns 'Open' and 'Close'.

    Returns:
        pd.Series: A Series containing 'green' or 'red' for each day

    Example usage:
        day_types = identify_day_types(ohlc_df)
    """

    df = ohlc_df.copy() 

    df['DayType'] = df.apply( 
        
        lambda row: 'green' if row['Close'] > row['Open'] else ( 
            'red' if row['Close'] < row['Open'] else 'Neutral' 
        ),
        axis=1
    )

    return df

def get_green_day_subset(ohlc_df, day_types):
    """
    Filters and returns rows for green days (close > open).

    Parameters:
        ohlc_df (pd.DataFrame) : the full OHLC DataFrame
        day_types (pd.Series) : Series containing day types ('green', 'red', 'neutral')

    Returns:
        pd.DataFrame: DataFrame containing only the rows for green days.

    Example usage:
        green_days = get_green_day_subset(ohlc_df, day_types)
    """
    green_days = ohlc_df[day_types == 'green']
    return green_days


def get_red_day_subset(ohlc_df, day_types):
    """
    Filters and returns rows for red days (close < open).

    Parameters:
        ohlc_df (pd.DataFrame) : the full OHLC DataFrame
        day_types (pd.Series) : Series containing day types ('green', 'red', 'neutral')
    
    Returns:
        pd.DataFrame: DataFrame containing only the rows for red days.

    Example usage:
        red_days = get_red_day_subset(ohlc_df, day_types)
    """
    red_days = ohlc_df[day_types == 'red']
    return red_days

# Counting and Percentage Functions
def get_green_day_count(day_types):
    """
    Counts the number of 'green' days in the day_types Series.

    Parameters:
        day_types (pd.Series): Series containing day types ('green', 'red', 'neutral').

    Returns:
        int: The count of 'green' days.

    Example usage:
        green_count = get_green_day_count(day_types)
    """
    return (day_types == 'green').sum()

def get_red_day_count(day_types):
    """
    Calculates the number of 'red' days in the day_types Series.

    Parameters:
        day_types (pd.Series): Series containing day types ('green', 'red', 'neutral').

    Returns:
        int: The count of 'red' days.

    Example usage:
        red_count = get_red_day_count(day_types)
    """
    return (day_types == 'red').sum()

def calculate_percentage(specific_count, total_count):
    """
    Calculates the percentage of a specific count relative to a total count.

    Parameters:
        specific_count (int): The count of the specific category (e.g., green or red days).
        total_count (int): The total count of all categories.

    Returns:
        float: The percentage of the specific count relative to the total count, rounded to 2 decimal places.

    Example usage:
        percentage = calculate_percentage(green_count, total_count)
    """
    if total_count == 0:
        return 0
    return round((specific_count / total_count) * 100, 2)

# Return calculation functions
def calculate_daily_returns(ohlc_df):
    """
    Calculates daily returns based on Open and Close prices.

    Parameters:
        ohlc_df (pd.DataFrame): DataFrame containing Open and Close prices with columns 'Open' and 'Close'

    Returns:
        pd.Series: A Series containing daily returns as a percentage.

    Example usage:      
        daily_returns = calculate_daily_returns(ohlc_df)
    """
    return (ohlc_df['Close'] - ohlc_df['Open']) / ohlc_df['Open']

# Statistical Analysis Functions
def get_avg_return(return_series):
    """
    Calculates the average return from a Series of daily returns.
    Parameters:
        return_series (pd.Series): Series containing daily returns.
    Returns:
        float: The average return, rounded to 4 decimal places.
    Example usage:
        avg_return = get_avg_return(daily_returns)
    """
    return round(return_series.mean(), 4)

def get_median_return(return_series):
    """
    Calculates the median return from a Series of daily returns.

    Parameters:
        return_series (pd.Series): Series containing daily returns.
    
    Returns:
        float: The median return, rounded to 4 decimal places.
    
    Example usage:
        median_return = get_median_return(daily_returns)
    """
    return round(return_series.median(), 4)

def get_max_return(return_series):
    """
    Calculates the maximum return from a Series of daily returns.

    Parameters:
        return_series (pd.Series): Series containing daily returns. 

    Returns:
        float: The maximum return, rounded to 4 decimal places.

    Example usage:
        max_return = get_max_return(daily_returns)
    """
    return round(return_series.max(), 4)

def get_min_return(return_series):
    """
    Calculates the minimum return from a Series of daily returns.

    Parameters:
        return_series (pd.Series): Series containing daily returns.

    Returns:
        float: The minimum return, rounded to 4 decimal places.

    Example usage:
        min_return = get_min_return(daily_returns)
    """
    return round(return_series.min(), 4)

def get_return_std_dev(return_series):
    """
    Calculates the standard deviation of returns from a Series of daily returns.    

    Parameters:
        return_series (pd.Series): Series containing daily returns.

    Returns:
        float: The standard deviation of returns, rounded to 4 decimal places.

    Example usage:
        std_dev = get_return_std_dev(daily_returns)
    """
    return round(return_series.std(), 4)

