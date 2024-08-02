import requests
def get_weather(api_key, location):
    """Fetch weather data from OpenWeatherMap API"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
def display_weather(weather_data):
    if weather_data:
        city = weather_data.get('name')
        temperature = weather_data['main'].get('temp')
        humidity = weather_data['main'].get('humidity')
        description = weather_data['weather'][0].get('description')
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description.capitalize()}")
    else:
        print("Could not retrieve weather data. Please check the location or try again later.")
def main():
    print("Welcome to the Basic Weather App!")
    location = input("Enter the city or ZIP code: ").strip()
    api_key = "YOUR_API_KEY"  
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)
if __name__ == "__main__":
    main()