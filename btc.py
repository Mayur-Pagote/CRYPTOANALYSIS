import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime as dt
import easygui

# Define the cryptocurrency name
CRYPTO_NAME = 'BTC-USD'

# Function to fetch data from Yahoo Finance
def get_data():
    try:
        start_date = '2024-01-01'
        end_date = dt.now().strftime("%Y-%m-%d")

        # Download the data
        data = yf.download(CRYPTO_NAME, start=start_date, end=end_date)

        if data.empty:
            raise ValueError("No data found for the given cryptocurrency.")
        return data

    except Exception as e:
        easygui.msgbox(f"Error occurred while fetching data: {e}", title="Error")
        return None

# Function to create the graph
def create_graph(data):
    try:
        # Create the candlestick chart with moving average
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

        # Update the layout of the graph
        graph.update_layout(title='Lakshya Crypto Price Graph Analysis', yaxis_title='Price (USD)')

        # Save the graph as an HTML file to view in a browser
        graph.write_html("crypto_graph.html")

        return "crypto_graph.html"

    except Exception as e:
        easygui.msgbox(f"Error occurred while generating the graph: {e}", title="Error")
        return None

# Function to ask the user whether they want to view the graph
def display_graph():
    # Ask user if they want to display the graph
    choice = easygui.buttonbox("Would you like to display the BTC-USD graph?", choices=["Yes", "No"])
    if choice == "Yes":
        # Fetch the cryptocurrency data
        crypto_data = get_data()

        if crypto_data is None:
            return

        # Create the plot and get the HTML file path
        html_file = create_graph(crypto_data)
        if html_file is None:
            return

        # Let the user know the graph has been generated
        easygui.msgbox("The graph has been generated! Opening it in your default browser.", title="Graph Generated")

        # Open the HTML file in the default web browser
        import webbrowser
        webbrowser.open(html_file)

# Main function to run the program
def run():
    # Display an introductory message
    easygui.msgbox("Welcome to the Cryptocurrency Price Analysis Tool!", title="Welcome")

    # Call the display_graph function to start the process
    display_graph()

# Run the program
if __name__ == "__main__":
    run()
