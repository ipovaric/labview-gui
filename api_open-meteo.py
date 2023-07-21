import requests
import matplotlib.pyplot as plt
import pandas as pd

def get_weather_data_with_plot(coordinates, plot_enabled=True):
    base_url = "https://api.open-meteo.com/v1/forecast"

    # Add query parameters for the coordinates and desired weather data
    params = {
        "hourly": "temperature_2m,relativehumidity_2m",
        "latitude": f"{coordinates[0]}",
        "longitude": f"{coordinates[1]}",
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch weather data. Status code: {response.status_code}")

    weather_data = response.json()

    # Extract temperature and relative humidity
    timestamps = weather_data["hourly"]["time"]
    temperatures = weather_data["hourly"]["temperature_2m"]
    humidity = weather_data["hourly"]["relativehumidity_2m"]

    timestamps = [pd.to_datetime(ts) for ts in timestamps]

    if plot_enabled:
        plot_weather_data(timestamps, temperatures, humidity)

    return temperatures, humidity

def plot_weather_data(timestamps, temperatures, humidity):
    #hours = list(range(len(temperatures)))


    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, label="Temperature (°C)", color="red")
    plt.plot(timestamps, humidity, label="Relative Humidity (%)", color="blue")

    plt.title("Temperature and Relative Humidity")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    #plt.xticks(hours[::3])  # Show only every 3rd hour on the x-axis
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        coordinates = (39.7392, -104.9847)
        plot_weather = True  # Set to False to disable plotting

        temperatures, humidity = get_weather_data_with_plot(coordinates, plot_enabled=plot_weather)

        # If you don't want to plot but still need the data, use:
        # temperatures, humidity = get_weather_data_with_plot(coordinates, plot_enabled=False)

    except Exception as e:
        print(f"Error: {e}")
