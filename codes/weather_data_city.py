import requests
import os
from dotenv import load_dotenv

load_dotenv("api_keys.env")  # Load environment variables from .env file

api_key = os.getenv("OPENWEATHER_API_KEY")  # Get the API key from environment variable

# -------------------------------------------------------------------------
"""
Function to get weather data from OpenWeatherMap API
using city name.
"""

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

# -------------------------------------------------------------------------
    # Use the extracted lon and lat in the next weather api link
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    # GET request to the API
    data = requests.get(weather_url).json()

    weather_url = weather_url.replace(api_key, "******")  # Mask the API key in the URL for security

# -------------------------------------------------------------------------
    note = f"Fetching weather data from: {city.title()}"
    print(note)
    print("-" * len(note))
    print()
    print(
        f"The weather information for {data['sys']['country']}, {data['name']} is: "
        # f"{data['name']} - "
        f"{data['main']['temp']}°C - "
        f"{data['weather'][0]['description']} - "
        f"{data['coord']['lat']} "
        f"{data['coord']['lon']}"
    )

# -------------------------------------------------------------------------
# Calling the function with the coordinates
city = input("Enter the city name: ")
get_weather(city)