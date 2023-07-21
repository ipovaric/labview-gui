import requests

def get_current_weather():
    base_url = "https://api.open-meteo.com/v1/forecast"
    location = "Denver,CO"  # Replace this with the desired location, e.g., "Denver,CO" or coordinates "lat,lon"

    # Add query parameters for the location and current forecast
    params = {
        "hourly": "temperature_2m,weathercode",
        "current_weather": "true",
        "latitude": "",
        "longitude": "",
    }

    # Make sure to set the latitude and longitude for the desired location
    # You can also use a geocoding API to convert the location name to coordinates
    # Example: "Denver,CO" -> Latitude: 39.7392, Longitude: -104.9903

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch current weather data. Status code: {response.status_code}")

    current_weather_data = response.json()

    # Extract the current weather conditions
    current_temperature = current_weather_data["hourly"]["temperature_2m"]["values"][0]
    weather_code = current_weather_data["hourly"]["weathercode"]["values"][0]
    current_conditions = get_weather_description(weather_code)

    return current_temperature, current_conditions

def get_weather_description(weather_code):
    # Map the weather codes to human-readable descriptions
    weather_codes = {
        0: "Unknown",
        1: "Clear sky",
        2: "Few clouds",
        3: "Scattered clouds",
        4: "Broken clouds",
        5: "Overcast",
        10: "Fog",
        21: "Mist",
        22: "Haze",
        23: "Smoke",
        24: "Dust or sand",
        30: "Drizzle",
        31: "Rain showers",
        32: "Rain",
        33: "Rain and snow",
        40: "Snow showers",
        41: "Snow",
        42: "Snow and rain",
        51: "Thunderstorms",
    }

    return weather_codes.get(weather_code, "Unknown")

if __name__ == "__main__":
    try:
        current_temp, current_conditions = get_current_weather()
        print(f"Current Temperature: {current_temp}°C")
        print(f"Current Conditions: {current_conditions}")
    except Exception as e:
        print(f"Error: {e}")
