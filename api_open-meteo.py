import requests
import matplotlib.pyplot as plt
import pandas as pd
import win32com.client as win32
import time

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

    idx = 13 # index of about now
    print(f"{timestamps[19]}:::Temp={temperatures[19]}C:::humidity={humidity[19]}%")
    if plot_enabled:
        plot_weather_data(timestamps, temperatures, humidity)

    shared_data = [timestamps,temperatures,humidity]
    # push_data_to_shared_variable(shared_data)
    
    return timestamps, temperatures, humidity

def plot_weather_data(timestamps, temperatures, humidity):
    #hours = list(range(len(temperatures)))

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, label="Temperature (°C)", color="red")
    plt.plot(timestamps, humidity, label="Relative Humidity (%)", color="blue")

    ts = time.time()
    plt.title("Temperature and Relative Humidity")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    #plt.xticks(hours[::3])  # Show only every 3rd hour on the x-axis
    plt.tight_layout()
    plt.show()

def main(coordinates,plot_enabled):
     
     print(f"Starting for coordinates={coordinates}")
     for i in range(1000):
        get_weather_data_with_plot(coordinates, plot_enabled)
        time.sleep(5)


# def push_data_to_shared_variable():
#     # Connect to the LabVIEW application instance
#     labview = win32.Dispatch("LabVIEW.Application")
    
#     # Get the shared variable reference
#     shared_variable = labview.GetSharedVariable("Weather")
    
#     # Write data to the shared variable
#     shared_variable.Value = "Sunny"


if __name__ == "__main__":
    try:
        coordinates = (39.7392, -104.9847)
        plot_weather = False  # Set to False to disable plotting

        main(coordinates, plot_enabled=False)

        # If you don't want to plot but still need the data, use:
        # temperatures, humidity = get_weather_data_with_plot(coordinates, plot_enabled=False)

    except Exception as e:
        print(f"Error: {e}")
