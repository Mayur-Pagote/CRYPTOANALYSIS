# Lakshya Crypto Price Graph Analysis

## Overview

This project provides a graphical representation of the price movement of Bitcoin (BTC) against the US Dollar (USD) using a candlestick chart and a 30-day moving average. The data is fetched from Yahoo Finance (`yfinance` library), and the graph is displayed using Plotly, an interactive plotting library.

### Features:
- **Candlestick Chart**: Displays the open, high, low, and close prices for Bitcoin.
- **30-Day Moving Average**: Plots a smoothed trend line representing the average closing price over the last 30 days.
- **Interactive Plot**: Users can hover over the chart to view details, zoom in/out, and inspect the candlesticks and moving average.

---

## Requirements

To run this project, you will need the following Python libraries:
- `yfinance`: To download historical cryptocurrency data.
- `plotly`: To plot interactive candlestick charts and graphs.
- `datetime`: To handle dates and time.

You can install the necessary libraries using pip:

```bash
pip install yfinance plotly
```

---

## Getting Started

### Step 1: Clone or Download the Repository

Clone the repository or download the source files to your local machine.

```bash
git clone https://github.com/yourusername/lakshya-crypto-analysis.git
cd lakshya-crypto-analysis
```

### Step 2: Run the Script

Once the repository is set up and the necessary libraries are installed, simply run the script to fetch and visualize the data.

```bash
python main.py
```

- The script will fetch Bitcoin price data from January 1, 2024, to the current date.
- It will then plot the candlestick chart and the 30-day moving average.

The chart will open in your default web browser.

---

## Code Explanation

### 1. **Import Dependencies**

```python
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime as dt
```

- `yfinance`: Used to download cryptocurrency price data from Yahoo Finance.
- `plotly.graph_objects`: Used to create and display the candlestick chart and moving average.
- `datetime`: To get the current date for fetching up-to-date data.

### 2. **Data Fetching**

```python
def get_data():
    start_date = '2024-01-01'
    end_date = dt.now().strftime("%Y-%m-%d")
    data = yf.download(CRYPTO_NAME, start=start_date, end=end_date)
    return data
```

- Data for Bitcoin (BTC-USD) is fetched from Yahoo Finance, starting from January 1, 2024, up to the current date.
- `yf.download()` function is used to get the price data.

### 3. **Plotting the Graph**

```python
def run():
    crypto_data = get_data()

    graph = go.Figure(data=[
        go.Candlestick(
            x=crypto_data.index,
            open=crypto_data['Open'],
            high=crypto_data['High'],
            low=crypto_data['Low'],
            close=crypto_data['Close'],
            name='Candlesticks',
            increasing_line_color='blue',
            decreasing_line_color='grey'
        ),
        go.Scatter(
            x=crypto_data.index,
            y=crypto_data['Close'].rolling(window=30).mean(),
            name='30 Day Moving Average',
            mode='lines'
        )
    ])
    
    graph.update_layout(title='Lakshya Crypto Price Graph Analysis', yaxis_title='Price (USD)')
    graph.show()
```

- `go.Candlestick` is used to create the candlestick chart with open, high, low, and close prices.
- A 30-day moving average is plotted using `go.Scatter` with the rolling mean of the close prices.
- The `graph.show()` function opens the chart in an interactive Plotly window.

### 4. **Running the Script**

```python
run()
```

- This function fetches the data and displays the graph.

---

## Customization

### 1. **Change Cryptocurrency**

To analyze a different cryptocurrency, replace the `CRYPTO_NAME` variable with the ticker symbol for the desired crypto. For example:
- `'ETH-USD'` for Ethereum.
- `'DOGE-USD'` for Dogecoin.

### 2. **Change Date Range**

The script is currently set to start from January 1, 2024. You can modify the `start_date` in the `get_data()` function to any other date.

### 3. **Adjust Moving Average**

You can change the rolling window for the moving average by adjusting the `window` parameter inside the `rolling()` function.

```python
crypto_data['Close'].rolling(window=50).mean()  # 50-day moving average
```

---

## Contributing

Feel free to open an issue or submit a pull request if you'd like to contribute to this project. Suggestions and improvements are welcome!

---


## Acknowledgments

- **Yahoo Finance API**: For providing free historical data on cryptocurrencies.
- **Plotly**: For their powerful, interactive plotting library.

---
