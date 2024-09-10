import os
from dotenv import load_dotenv
import requests
from plyer import notification
import time

# Load environment variables from .env
load_dotenv()

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    # Check if the response has an error code
    if weather_data.get("cod") != 200:
        print(f"Error fetching weather data: {weather_data.get('message')}")
        return None
    return weather_data

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Weather App',
        timeout=10
    )

def main():
    api_key = os.getenv("API_KEY")
    city = 'London'

    while True:
        weather_data = get_weather(api_key, city)
        if weather_data:
            main_weather = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']

            title = f"Weather Update: {city}"
            message = f"{main_weather} - {description}\nTemperature: {temp}°C"

            show_notification(title, message)
        else:
            print("Error fetching weather data. Check the API key or city name.")

        time.sleep(1800)

if __name__ == "__main__":
    main()
