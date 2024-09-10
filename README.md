# Weather Notifier

A Python application that fetches real-time weather data for a specified city and sends desktop notifications with temperature and weather conditions. The application uses the OpenWeatherMap API to retrieve the data and Plyer to display notifications.

## Features
- Fetches real-time weather data (temperature, weather conditions) for any city.
- Sends desktop notifications with the weather information.
- Updates weather information at customizable intervals (default: 30 minutes).

## Prerequisites
- Python 3.x
- OpenWeatherMap API key (You can get one by signing up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rhidhanmadai/Weather_notifier.git
   cd Weather_notifier
2.  Usage
Run the Weather_notifier.py script:

The application will fetch the weather data for the specified city (default is London) and display notifications with the weather information every 30 minutes.

To change the city or interval:

Modify the city and time.sleep() in the main() function as needed.
