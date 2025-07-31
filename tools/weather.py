# tools/weather.py
import requests

def get_weather(city, speak):
    """Fetches and speaks the weather for a given city."""
    try:
        url = f"https://wttr.in/{city.replace(' ', '+')}?format=j1"
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes
        weather_data = response.json()

        current = weather_data['current_condition'][0]
        desc = current['weatherDesc'][0]['value']
        temp_c = current['temp_C']
        feels_like_c = current['FeelsLikeC']

        report = (f"The current weather in {city} is {desc}. "
                  f"The temperature is {temp_c} degrees Celsius, but it feels like {feels_like_c}.")
        speak(report)

    except requests.exceptions.RequestException as e:
        print(f"Weather API request failed: {e}")
        speak(f"I'm sorry, sir, I couldn't retrieve the weather for {city}.")
