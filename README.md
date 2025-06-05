# OHLC Analysis Package

A Python package for analyzing OHLC (Open, High, Low, Close) financial market data. This package provides tools for identifying market trends, calculating returns, and performing statistical analysis on financial time series data.

## Features

- Day Type Classification (Green/Red/Neutral days)
- Return Calculations
- Statistical Analysis
- Data Visualization
- Trend Analysis
- Volatility Metrics

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ohlc_analysis.git
cd ohlc_analysis
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

## Usage

### Basic Usage

```python
import pandas as pd
from ohlc_analysis import *

# Load your OHLC data
df = pd.read_csv("your_data.csv")

# Identify day types
df_with_types, percentages = identify_day_types(df)
print("Day Types and Percentages:", percentages)

# Calculate daily returns
returns = calculate_daily_returns(df)
print("Average Return:", get_avg_return(returns))
```

### Example Analysis

```python
# Get green and red day subsets
green_days = get_green_day_subset(df)
red_days = get_red_day_subset(df)

# Calculate statistics
avg_return = get_avg_return(returns)
median_return = get_median_return(returns)
std_dev = get_return_std_dev(returns)

print(f"Average Return: {avg_return:.4f}")
print(f"Median Return: {median_return:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")
```

## Data Format

The package expects OHLC data in a pandas DataFrame with the following columns:
- Open: Opening price
- High: Highest price
- Low: Lowest price
- Close: Closing price
- Volume (optional): Trading volume

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the pandas and numpy communities for their excellent documentation and tools
- Inspired by various financial analysis techniques and trading strategies
