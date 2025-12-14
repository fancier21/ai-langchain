import os

import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()


WTTR_API_KEY = os.getenv("WTTR_API_KEY")
url = "https://wttr.in"


@tool("get_weather_for_location", description="Get weather for a given city.")
def get_weather_for_location(city: str) -> str:
    response = requests.get(f"{url}/{city}?format=j1")
    if response.status_code == 200:
        data = response.json()
        print(data)
        return f"The weather in {city} is {data['current_condition'][0]['weatherDesc'][0]['value']}."
    else:
        return f"Failed to fetch weather data for {city}. Please check your API key."
