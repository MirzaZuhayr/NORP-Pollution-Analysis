import pandas as pd
import sys
import os

def clean_aqi_data(year):
    """Clean annual AQI by county data for the given year."""
    input_file = f"annual_aqi_by_county_{year}.csv"
    output_file = f"cleaned_aqi_{year}.csv"

    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return

    # Load raw dataset
    aqi = pd.read_csv(input_file)

    # Keep only relevant columns
    aqi_clean = aqi[[
        "State",
        "County",
        "Year",
        "Days with AQI",
        "Good Days",
        "Moderate Days",
        "Unhealthy for Sensitive Groups Days",
        "Unhealthy Days",
        "Max AQI",
        "Median AQI"
    ]].copy()

    # Derived metrics
    aqi_clean["Pct_Good"] = aqi_clean["Good Days"] / aqi_clean["Days with AQI"]
    aqi_clean["Pct_Unhealthy"] = (
        (aqi_clean["Unhealthy for Sensitive Groups Days"] + aqi_clean["Unhealthy Days"])
        / aqi_clean["Days with AQI"]
    )

    # Clean up names
    aqi_clean["County"] = aqi_clean["County"].str.replace(" County", "", regex=False).str.strip()
    aqi_clean["State"] = aqi_clean["State"].str.title()
    aqi_clean["County"] = aqi_clean["County"].str.title()

    # Save cleaned dataset
    aqi_clean.to_csv(output_file, index=False)

    print(f"Cleaned AQI dataset saved as {output_file}")
    print(aqi_clean.head())

if __name__ == "__main__":
    # Allow year to be passed as argument: python clean_aqi_data.py 2018
    if len(sys.argv) < 2:
        print("Usage: python clean_aqi_data.py <year>")
    else:
        year = sys.argv[1]
        clean_aqi_data(year)
