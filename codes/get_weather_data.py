# Install and Import required libraries and modules
import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv


load_dotenv("api_keys.env") # Load environment variables from .env file

api_key = os.getenv("OPENWEATHER_API_KEY") # Get the API key from environment variable

# -------------------------------------------------------------------------

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=10)
num_of_days = (today - week_ago).days


# Format dates for the API
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

start_date
end_date

# -------------------------------------------------------------------------

# Function to get longitude and latitude for the provided city
def get_weather(city):

    # Get latitude and longitude from city name using OpenWeatherMap API
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    
    statement = f"Fetching Latitude and Longitude for: {city.title()} from OpenWeatherMap"
    print(statement)
    print("-" * len(statement))
    print()

    # GET request to the API
    geo_response = requests.get(geo_url).json()
    geo_url = geo_url.replace(api_key, "******")  # Mask the API key in the URL for security

    if not geo_response:
        print(f"{city} not found.")

        return

    lat = geo_response[0]['lat']
    lon = geo_response[0]['lon']
    country = geo_response[0]['country']
# -------------------------------------------------------------------------
    # Get API data from open-meteo using the long and lat from openweathermap API
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
    
    print(f"Fetching Last {num_of_days} days weather data from: {country} - {city.title()} (Lat: {lat} Lon: {lon})")
    
    # Making a GET request to the API and parsing the JSON response
    response = requests.get(api_url)
    data = response.json()

# -------------------------------------------------------------------------
    # Load Data Into Pandas

    daily_data = data['daily'] # Extract the daily data

    # Create a dataframe
    df = pd.DataFrame({
        'date': daily_data['time'],
        'max_temp': daily_data['temperature_2m_max'],
        'min_temp': daily_data['temperature_2m_min']
    })

    df['date'] = pd.to_datetime(df['date'])

    print(df)


city = input("Enter City Name: ")
get_weather(city)