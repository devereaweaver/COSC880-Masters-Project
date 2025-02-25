# use yfinance API to download time series data for a given asset
import json
import yfinance as yf
import pandas as pd
import os

def fetch_time_series_data(json_file):
    """
    Reads a JSON file, extracts ticker symbols and date ranges, 
    then fetches historical price data from Yahoo Finance.
    """
    try:
        # Read JSON file
        with open(json_file, 'r') as file:
            user_data = json.load(file)

        # Store results
        results = {}

        for asset in user_data["assets"]:
            ticker = asset["ticker"]
            start_date = asset["start_date"]
            end_date = asset["end_date"]

            print(f"Fetching data for {ticker} from {start_date} to {end_date}...")

            # Download historical data (implicit conversion to dataframe)
            stock_data = yf.download(ticker, start=start_date, end=end_date)

            if stock_data.empty:
                print(f"No data found for {ticker} in the given date range.")
            else:
                results[ticker] = stock_data

        return results

    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def run():
    # Define the JSON file name
    json_filename = "./assets.json"

    # Fetch and display the results
    time_series_data = fetch_time_series_data(json_filename)

    if time_series_data:
        for ticker, df in time_series_data.items():
            print(f"\nTime Series Data for {ticker}:")
            print(df.head())  # Show first few rows