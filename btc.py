import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime as dt

CRYPTO_NAME = 'BTC-USD'

def get_data():
    try:
        start_date = '2024-01-01'
        end_date = dt.now().strftime("%Y-%m-%d")

        # Download the data
        data = yf.download(CRYPTO_NAME, start=start_date, end=end_date)

        # Check if the data is empty
        if data.empty:
            raise ValueError("No data found for the given cryptocurrency.")

        return data
    
    except Exception as e:
        print(f"Error occurred while fetching data: {e}")
        return None

def run():
    # Fetch the cryptocurrency data
    crypto_data = get_data()

    if crypto_data is None:
        print("Exiting because there was an error fetching data.")
        return

    try:
        # Create the candlestick chart and moving average
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

        # Update layout and show the graph
        graph.update_layout(title='Lakshya Crypto Price Graph Analysis', yaxis_title='Price (USD)')
        graph.show()

    except Exception as e:
        print(f"Error occurred while generating the graph: {e}")

run()
