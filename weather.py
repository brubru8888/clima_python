from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

weather_translation = {
    "clear sky": "céu limpo",
    "few clouds": "poucas nuvens",
    "scattered clouds": "nuvens dispersas",
    "broken clouds": "nuvens quebradas",
    "shower rain": "pancadas de chuva",
    "rain": "chuva",
    "thunderstorm": "tempestade",
    "snow": "neve",
    "mist": "névoa",
    "overcast clouds": "nublado"
}

def get_current_weather(city="São Paulo"):
    api_key = os.getenv("API_KEY")

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    if weather_data.get('cod') == 200:
        weather_description = weather_data["weather"][0]["description"]
        translated_status = weather_translation.get(weather_description, weather_description)  # Default to original if not in dictionary
        weather_data["weather"][0]["description"] = translated_status

    return weather_data


if __name__ == "__main__":
    print('\n*** Obtenha a Previsão do Tempo ***')

    city = input("\nInsira o nome da cidade: ")

    if not bool(city.strip()):
        city = "São Paulo"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
