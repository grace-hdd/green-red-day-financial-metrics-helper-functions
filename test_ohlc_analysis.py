import pandas as pd
from ohlc_analysis import *

def test_identify_day_types():
    # Load ohlc data
    df = pd.read_csv("sample_ohlc_data.csv")
    
    # Test identify_day_types
    df_with_types, percentages = identify_day_types(df)
    print("Day Types and Percentages:")
    print("DataFrame:")
    print(df_with_types.head())
    print("\nPercentages:")
    print(percentages)
    
    # Test get_green_day_subset
    green_days = get_green_day_subset(df)
    print("\nFirst Green Day:")
    print(green_days.head())
    
    # Test get_red_day_subset
    red_days = get_red_day_subset(df)
    print("\nFirst Red Day:")
    print(red_days.head())
    
    # Test get_green_day_count
    green_count = get_green_day_count(df)
    print("\nGreen Day Count:", green_count)
    
    # Test get_red_day_count
    red_count = get_red_day_count(df)
    print("Red Day Count:", red_count)
    
    # Test calculate_percentage
    percentage = calculate_percentage(green_count, len(df))
    print("Percentage of Green Days:", percentage, "%")
    
    # Test calculate_daily_returns
    returns = calculate_daily_returns(df)
    print("\nFirst 5 Daily Returns:")
    print(returns.head())
    
    # Test statistical functions
    print("\nAverage Return:", get_avg_return(returns))
    print("Median Return:", get_median_return(returns))
    print("Max Return:", get_max_return(returns))
    print("Min Return:", get_min_return(returns))
    print("Standard Deviation of Returns:", get_return_std_dev(returns))
    
    # Test empty DataFrame
    empty_df = pd.DataFrame(columns=['Open', 'Close'])
    empty_result, empty_percentages = identify_day_types(empty_df)
    print("\nEmpty Test:")
    print(empty_result)
    print("Percentages:", empty_percentages)

if __name__ == "__main__":
    test_identify_day_types()
