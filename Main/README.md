# Cryptocurrency Price Analysis Tool - README

## Overview

This program is a simple cryptocurrency price analysis tool that allows users to:
1. Fetch historical price data for a selected cryptocurrency from Yahoo Finance.
2. Generate a candlestick chart with a 30-day moving average.
3. Display the generated graph in a web browser.

The tool provides a graphical interface to change the cryptocurrency symbol, view the graph, and interact with various options using `easygui` for pop-up windows.

The tool uses:
- `yfinance` to download the historical price data from Yahoo Finance.
- `plotly.graph_objects` to generate an interactive candlestick chart.
- `easygui` for user interface interactions.
- `webbrowser` to display the chart in a web browser.

---

## Requirements

To run this program, you need the following Python libraries:

- `yfinance`: For fetching cryptocurrency price data from Yahoo Finance.
- `plotly`: For creating the interactive candlestick chart.
- `easygui`: For displaying the graphical user interface.
- `webbrowser`: For opening the HTML file of the graph in the default browser.
- `datetime`: For date manipulation.

### Installation

Before running the script, make sure you have the required libraries installed. You can install them using pip:

```bash
pip install yfinance plotly easygui
```

---

## Script Breakdown

### 1. **Imports**

```python
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime as dt
import easygui
import webbrowser
```

These are the libraries required for:
- Fetching data (`yfinance`).
- Plotting the chart (`plotly.graph_objects`).
- Working with dates (`datetime`).
- User interactions (`easygui`).
- Opening the chart in a browser (`webbrowser`).

### 2. **Global Variables**

```python
CRYPTO_NAME = 'BTC-USD'
```

This variable holds the default cryptocurrency symbol, which is set to Bitcoin (`BTC-USD`). It can be changed later by the user.

### 3. **get_data(symbol)**
This function fetches historical price data for the given cryptocurrency symbol.

#### Parameters:
- `symbol` (str): The cryptocurrency symbol (e.g., `BTC-USD`).

#### Returns:
- A Pandas DataFrame containing the historical price data for the given symbol.
- If an error occurs (e.g., no data is found), it displays an error message using `easygui`.

```python
def get_data(symbol):
    try:
        start_date = '2024-01-01'
        end_date = dt.now().strftime("%Y-%m-%d")
        data = yf.download(symbol, start=start_date, end=end_date)

        if data.empty:
            raise ValueError(f"No data found for the given cryptocurrency symbol: {symbol}")
        return data

    except Exception as e:
        easygui.msgbox(f"Error occurred while fetching data: {e}", title="Error")
        return None
```

### 4. **create_graph(data)**

This function generates a candlestick chart along with a 30-day moving average for the given cryptocurrency price data.

#### Parameters:
- `data` (DataFrame): The historical price data (including Open, High, Low, Close) for the cryptocurrency.

#### Returns:
- The file path (`crypto_graph.html`) of the generated HTML graph.
- If an error occurs, an error message is shown via `easygui`.

```python
def create_graph(data):
    try:
        graph = go.Figure(data=[ 
            go.Candlestick(
                x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],
                name='Candlesticks',
                increasing_line_color='blue',  # Color for upward movements
                decreasing_line_color='grey'    # Color for downward movements
            ),
            go.Scatter(
                x=data.index,
                y=data['Close'].rolling(window=30).mean(),
                name='30 Day Moving Average',
                mode='lines'
            )
        ])
        
        graph.update_layout(title=f'{CRYPTO_NAME} Price Graph Analysis', yaxis_title='Price (USD)')
        graph.write_html("crypto_graph.html")
        return "crypto_graph.html"
    except Exception as e:
        easygui.msgbox(f"Error occurred while generating the graph: {e}", title="Error")
        return None
```

### 5. **get_symbol_from_user()**

This function prompts the user to enter a new cryptocurrency symbol using an input box. If the user provides a valid symbol, it updates the global `CRYPTO_NAME` variable with the new symbol.

#### Functionality:
- The symbol is updated globally for subsequent data fetching and graph generation.
- If the input is empty or invalid, it keeps the default symbol (`BTC-USD`).

```python
def get_symbol_from_user():
    global CRYPTO_NAME
    new_symbol = easygui.enterbox("Enter the cryptocurrency symbol (e.g., BTC-USD, ETH-USD):", 
                                  title="Cryptocurrency Symbol", default=CRYPTO_NAME)

    if new_symbol:
        CRYPTO_NAME = new_symbol.strip().upper()
        easygui.msgbox(f"Cryptocurrency symbol set to: {CRYPTO_NAME}", title="Symbol Changed")
    else:
        easygui.msgbox("Invalid input. Keeping the default symbol: BTC-USD.", title="Invalid Symbol")
```

### 6. **display_graph()**

This function asks the user if they want to display the generated cryptocurrency graph. If the user chooses "Yes", it fetches the data, generates the graph, and opens it in the default web browser.

#### Functionality:
- Fetches data using `get_data()`.
- Creates the graph using `create_graph()`.
- Opens the graph in the browser via `webbrowser.open()`.

```python
def display_graph():
    choice = easygui.buttonbox("Would you like to display the cryptocurrency graph?", choices=["Yes", "No"])
    if choice == "Yes":
        crypto_data = get_data(CRYPTO_NAME)

        if crypto_data is None:
            return

        html_file = create_graph(crypto_data)
        if html_file is None:
            return

        easygui.msgbox(f"The graph for {CRYPTO_NAME} has been generated! Opening it in your default browser.", title="Graph Generated")
        webbrowser.open(html_file)
```

### 7. **run()**

This is the main function that drives the program. It displays an introductory message and calls other functions to interact with the user.

#### Functionality:
- Displays a welcome message.
- Prompts the user to enter a cryptocurrency symbol.
- Displays the generated cryptocurrency graph.

```python
def run():
    easygui.msgbox("Welcome to the Cryptocurrency Price Analysis Tool!", title="Welcome")
    get_symbol_from_user()
    display_graph()
```

### 8. **Main Execution Block**

The script starts running by calling the `run()` function when the file is executed.

```python
if __name__ == "__main__":
    run()
```

---

## User Interaction Flow

1. The program starts with a welcome message.
2. The user is prompted to enter a cryptocurrency symbol (e.g., `BTC-USD` or `ETH-USD`). If no symbol is entered, it keeps the default symbol (`BTC-USD`).
3. The user is asked if they want to display the graph.
4. If the user chooses "Yes":
   - Data is fetched for the selected cryptocurrency.
   - A candlestick chart with a 30-day moving average is generated.
   - The chart is saved as an HTML file and automatically opened in the default web browser.

---

## Notes

- Ensure you have an active internet connection to fetch the data from Yahoo Finance.
- The 30-day moving average is displayed as a line on top of the candlestick chart.
- The tool is designed to be simple and intuitive with a graphical interface for ease of use.



