# Real-Time Stock Price Plotter (Console Version)
# Hacktoberfest 2025 Contribution
# Author: Sonika KC
# Works without installing any external libraries

import random
import time
import datetime
import os

# Function: Generate dummy stock price
def get_stock_price(dummy_price):
    """Simulates stock price fluctuations."""
    fluctuation = random.uniform(-1.0, 1.0)  # +/- $1
    return round(dummy_price + fluctuation, 2)

# Function: Draw simple text-based graph
def draw_graph(prices):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    max_price = max(prices)
    min_price = min(prices)
    scale = 50 / (max_price - min_price + 0.01)  # Scale to 50 characters

    print("Real-Time Stock Price (AAPL)\n")
    for price in prices:
        num_chars = int((price - min_price) * scale)
        print(f"${price:6} | " + "*" * num_chars)
    print("\nPress Ctrl+C to stop.\n")

# Main function
def main():
    stock_ticker = 'AAPL'
    max_points = 20  # number of points to display
    current_price = 150.0
    prices = []

    try:
        while True:
            current_price = get_stock_price(current_price)
            prices.append(current_price)
            if len(prices) > max_points:
                prices.pop(0)

            draw_graph(prices)
            print(f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped real-time plotting.")

# Run the program
if __name__ == "__main__":
    main()
