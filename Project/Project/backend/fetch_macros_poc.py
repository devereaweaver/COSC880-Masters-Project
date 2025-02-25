import json
from fredapi import Fred
import pandas as pd
from ..config import fred_api_key

# Replace with your FRED API Key
#FRED_API_KEY = "your_fred_api_key"

def fetch_fred_data(json_file):
    """
    Reads macroeconomic indicators and date range from a JSON file,
    fetches data from FRED's API, and returns a DataFrame.
    """
    try:
        # Load JSON data
        with open(json_file, "r") as f:
            macro_data = json.load(f)

        # Extract start/end dates & indicators
        start_date = macro_data["start_date"]
        end_date = macro_data["end_date"]
        indicators = macro_data["indicators"]

        print(f"Using Date Range: {start_date} to {end_date}")

        # Initialize FRED client
        fred = Fred(api_key=fred_api_key)
        macro_results = {}

        # Fetch data for each indicator
        for code, name in indicators.items():
            print(f"Fetching {name} ({code}) from {start_date} to {end_date}...")
            try:
                series = fred.get_series(code, start_date, end_date)
                macro_results[code] = series
            except Exception as e:
                print(f"Error fetching {name}: {e}")

        # Convert to DataFrame
        df_macro = pd.DataFrame(macro_results)

        return df_macro

    except Exception as e:
        print(f"Error: {e}")
        return None

def run():
    """
    Main function to execute the script.
    Fetches macroeconomic data and saves it to a CSV file.
    """
    json_file = "macro_indicators.json"
    
    # Fetch data
    df_macro = fetch_fred_data(json_file)

    if df_macro is not None:
        # Save to CSV (for debugging)
        df_macro.to_csv("fred_macro_data.csv")
        print("\nDownloaded Macroeconomic Data:")
        print(df_macro.head())
    else:
        print("No data was retrieved.")
