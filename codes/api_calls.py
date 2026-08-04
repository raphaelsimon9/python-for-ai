import requests

# We use coordinates to get weather data from a free weather API.
longitude = 2.35 # Paris Longitude
latitude = 48.85 # Paris Latitude

# Build the API URL with the coordinates
api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

print(f"Fetching weather data from: {api_url}")


# Using a function to get coordinates for weather data from a free weather API.
def weather (longitude, latitude):

    # Build the API URL with the coordinates
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    print(f"Fetching weather data from: {api_url}")

    # Making a GET request to the API and parsing the JSON response
    response = requests.get(api_url)
    data = response.json()
    print()
    print(data)
    print(data['timezone'], data['current']['time'], " - ", data['current']['temperature_2m'])

    # data.keys()

# Calling the function with the coordinates
weather(10.35, 78.85)


"""
Defining a function to get weather data from OpenWeatherMap API
using latitude and longitude.
"""
api_key = REDACTED" "
def weather (latitude, longitude):

    # Build the API URL with the coordinates
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"

    print(f"Fetching weather data from: {url}")

    # Making a GET request to the API and parsing the JSON response
    response = requests.get(url)
    data = response.json()
    
    print()
    print(
        f"The weather information for {data['sys']['country']}, {data['name']} is: "
        # f"{data['name']} - "
        f"{data['main']['temp']}°C - "
        f"{data['weather'][0]['description']} - "
        f"{data['coord']['lat']} "
        f"{data['coord']['lon']}"
    )
    # data.keys()

# Calling the function with the coordinates
weather(51.5, -0.12)  # Coordinates for London
weather()


"""
Function to get weather data from OpenWeatherMap API
using city name.
"""
api_key = REDACTED" "
# -------------------------------------------------------------------------
def get_city(city):

    # Get latitude and longitude from city name using OpenWeatherMap API
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

    print(f"Fetching Latitude and Longitude for: {city} from OpenWeatherMap")
    print()

    # GET request to the API
    geo_response = requests.get(geo_url).json()

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

# -------------------------------------------------------------------------
    print(f"Fetching weather data from: {city}")
    print()
    print(
        f"The weather information for {data['sys']['country']}, {data['name']} is: "
        # f"{data['name']} - "
        f"{data['main']['temp']}°C - "
        f"{data['weather'][0]['description']} - "
        f"{data['coord']['lat']} "
        f"{data['coord']['lon']}"
    )
    # data.keys()

# Calling the function with the coordinates
get_city("London")