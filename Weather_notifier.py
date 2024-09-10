import time
from plyer import notification
import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Weather App',
        timeout=10
    )

def main():
    api_key = '69e1a59e03cc1ba53a29ed731bbc23ea'
    city = 'Gulu'

    while True:
        weather_data = get_weather(api_key, city)
        if weather_data.get('cod') == 200:
            main_weather = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']

            title = f"Weather Update: {city}"
            message = f"{main_weather} - {description}\nTemperature: {temp}°C"

            show_notification(title, message)
        else:
            print("Error fetching weather data.")

        # Wait for 30 minutes before checking again
        time.sleep(1800)

if __name__ == "__main__":
    main()