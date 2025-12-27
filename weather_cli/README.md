# Weather CLI

A command-line weather application that fetches real-time weather data using the OpenWeatherMap API.

## Features

- Real-time weather data for any city
- Temperature in Celsius or Fahrenheit
- Detailed weather information:
  - Current temperature and feels like
  - Min/Max temperatures
  - Weather conditions
  - Humidity and pressure
  - Wind speed
- Clean, formatted output with emojis

## Setup

1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
2. Set the environment variable:
   ```bash
   export OPENWEATHER_API_KEY='your_api_key_here'
   ```

## Usage

```bash
python weather.py
```

## Example

```
Weather CLI Application
============================================================

Menu:
1. Get Weather by City
2. Change Temperature Units
3. Exit

Select option (1-3): 1
Enter city name: London
Units (metric/imperial) [metric]: metric

============================================================
         Weather in London, GB
============================================================

🌡️  Temperature: 15.5°C
   Feels like: 14.2°C
   Min: 13.0°C | Max: 17.0°C

☁️  Conditions: Partly Cloudy

💧 Humidity: 72%
🌀 Pressure: 1013 hPa
💨 Wind Speed: 3.5 m/s

============================================================
```

## Note

This application requires an active internet connection and a valid OpenWeatherMap API key to function.
