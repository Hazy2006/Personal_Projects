"""
Weather CLI Application
A command-line weather application using OpenWeatherMap API.
Note: Requires an API key from https://openweathermap.org/api
"""

import json
import os
from urllib import request, parse, error


class WeatherApp:
    """A simple weather application using OpenWeatherMap API."""
    
    def __init__(self, api_key=None):
        """
        Initialize the weather app.
        
        Args:
            api_key: OpenWeatherMap API key. If None, will try to read from environment.
        """
        self.api_key = api_key or os.getenv('OPENWEATHER_API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city, units='metric'):
        """
        Get weather information for a city.
        
        Args:
            city: City name
            units: Temperature units ('metric', 'imperial', 'standard')
        
        Returns:
            Dictionary with weather information
        """
        if not self.api_key:
            return {
                'error': 'API key not found. Set OPENWEATHER_API_KEY environment variable or provide key.'
            }
        
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': units
            }
            
            url = f"{self.base_url}?{parse.urlencode(params)}"
            
            with request.urlopen(url) as response:
                data = json.loads(response.read().decode())
                return self.parse_weather_data(data, units)
        
        except error.HTTPError as e:
            if e.code == 404:
                return {'error': f'City "{city}" not found!'}
            elif e.code == 401:
                return {'error': 'Invalid API key!'}
            else:
                return {'error': f'HTTP Error: {e.code}'}
        
        except error.URLError:
            return {'error': 'Network error. Please check your internet connection.'}
        
        except Exception as e:
            return {'error': f'An error occurred: {str(e)}'}
    
    def parse_weather_data(self, data, units):
        """Parse the API response into a readable format."""
        unit_symbol = '°C' if units == 'metric' else ('°F' if units == 'imperial' else 'K')
        
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'].title(),
            'wind_speed': data['wind']['speed'],
            'unit_symbol': unit_symbol
        }
    
    def display_weather(self, weather_data):
        """Display weather information in a formatted way."""
        if 'error' in weather_data:
            print(f"\n❌ {weather_data['error']}\n")
            return
        
        print("\n" + "=" * 60)
        print(f"Weather in {weather_data['city']}, {weather_data['country']}".center(60))
        print("=" * 60)
        print(f"\n🌡️  Temperature: {weather_data['temperature']}{weather_data['unit_symbol']}")
        print(f"   Feels like: {weather_data['feels_like']}{weather_data['unit_symbol']}")
        print(f"   Min: {weather_data['temp_min']}{weather_data['unit_symbol']} | Max: {weather_data['temp_max']}{weather_data['unit_symbol']}")
        print(f"\n☁️  Conditions: {weather_data['description']}")
        print(f"\n💧 Humidity: {weather_data['humidity']}%")
        print(f"🌀 Pressure: {weather_data['pressure']} hPa")
        print(f"💨 Wind Speed: {weather_data['wind_speed']} m/s")
        print("\n" + "=" * 60 + "\n")


def main():
    """Main function to run the weather application."""
    print("=" * 60)
    print("Weather CLI Application".center(60))
    print("=" * 60)
    
    # Check for API key
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    if not api_key:
        print("\n⚠️  WARNING: No API key found!")
        print("To use this app, you need an OpenWeatherMap API key.")
        print("\nSteps to get started:")
        print("1. Sign up at https://openweathermap.org/api")
        print("2. Get your free API key")
        print("3. Set environment variable: export OPENWEATHER_API_KEY='your_key'")
        print("\nFor demo purposes, you can enter a key now (or press Enter to skip):")
        
        user_key = input("API Key: ").strip()
        if user_key:
            api_key = user_key
        else:
            print("\n🔍 Running in demo mode (will show error when querying weather)")
    
    weather_app = WeatherApp(api_key)
    
    while True:
        print("\nMenu:")
        print("1. Get Weather by City")
        print("2. Change Temperature Units")
        print("3. Exit")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == '3':
            print("Thank you for using Weather CLI!")
            break
        
        elif choice == '1':
            city = input("Enter city name: ").strip()
            if city:
                units = input("Units (metric/imperial) [metric]: ").strip().lower() or 'metric'
                if units not in ['metric', 'imperial']:
                    units = 'metric'
                
                weather_data = weather_app.get_weather(city, units)
                weather_app.display_weather(weather_data)
            else:
                print("City name cannot be empty!")
        
        elif choice == '2':
            print("\nTemperature Units:")
            print("- metric: Celsius (°C)")
            print("- imperial: Fahrenheit (°F)")
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
