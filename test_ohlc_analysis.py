import pandas as pd
from ohlc_analysis import *

# Load ohlc data
df = pd.read_csv("sample_ohlc_data.csv")

# Test each function
day_types = identify_day_types(df)
print("Day Types:\n", day_types.head())

green_days = get_green_day_subset(df, day_types)
print("First Green Day:\n", green_days.head())

red_days = get_red_day_subset(df, day_types)
print("First Red Day:\n", red_days.head())

green_count = get_green_day_count(day_types)
print("Green Day Count:", green_count)

percentage = calculate_percentage(green_count, len(df))
print("Percentage of Green Days:", percentage , "%")

returns = calculate_daily_returns(df)
print("First 5 Daily Returns:\n", returns.head())

print("Average Reutrn:", get_avg_return(returns))
print("Median Return:", get_median_return(returns))
print("Max Return:", get_max_return(returns))
print("Min Return:", get_min_return(returns))
print("Standard Deviation of Returns:", get_return_std_dev(returns))


empty_df = pd.DataFrame(columns=['Open', 'Close'])
print("Empty Test:", identify_day_types(empty_df))  # Should return empty Series
