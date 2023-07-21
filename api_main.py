import requests

def get_weather_data():
    base_url = "https://api.weather.gov"
    #location = "Denver,CO"
    # Denver
    #location = "39.7438465,-105.0206761"
    location = "BOU/62,62"
    station = "KBJC"
    # Get the current observation data
    #current_observation_url = f"{base_url}/gridpoints/{location}/forecast"
    current_observation_url = f"{base_url}/stations/{station}/observations"

    response = requests.get(current_observation_url)
    if response.status_code != 200:
        error_message = response.json()['title'] if response.status_code == 404 else response.reason
        raise Exception(f"Failed to fetch current weather data. Status code: {response.status_code}, Error: {error_message}")

    current_weather_data = response.json()

    # Get the current temperature and weather conditions
    current_temperature = current_weather_data['properties']['periods'][0]['temperature']
    current_conditions = current_weather_data['properties']['periods'][0]['shortForecast']

    # Get the 5-day forecast data
    forecast_url = current_weather_data['properties']['forecast']
    forecast_response = requests.get(forecast_url)
    if forecast_response.status_code != 200:
        error_message = forecast_response.json()['title'] if forecast_response.status_code == 404 else forecast_response.reason
        raise Exception(f"Failed to fetch 5-day forecast data. Status code: {forecast_response.status_code}, Error: {error_message}")

    forecast_data = forecast_response.json()

    # Extract the 5-day forecast
    five_day_forecast = []
    for period in forecast_data['properties']['periods'][:5]:
        day_forecast = {
            'date': period['startTime'],
            'temperature': period['temperature'],
            'conditions': period['shortForecast']
        }
        five_day_forecast.append(day_forecast)

    return current_temperature, current_conditions, five_day_forecast

if __name__ == "__main__":
    try:
        current_temp, current_conditions, forecast = get_weather_data()
        print(f"Current Temperature in Denver, CO: {current_temp}°F")
        print(f"Current Conditions in Denver, CO: {current_conditions}")
        print("\n5-Day Forecast:")
        for day in forecast:
            print(f"{day['date']}: {day['temperature']}°F, {day['conditions']}")
    except Exception as e:
        print(f"Error: {e}")

get_weather_data()