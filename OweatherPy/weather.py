
import requests
import os
import pandas as pd
from datetime import datetime

BASE_URL = "https://api.openweathermap.org/data/2.5/"
PRO_BASE_URL = "https://pro.openweathermap.org/data/2.5/"

def set_weather_key(api_key):
    """Set the API key for OpenWeather in the environment variables."""
    os.environ["WEATHER_API_KEY"] = api_key

def get_weather_data(lat, lon, lang="en", units="standard", tibble_format=False):
    """Get current weather data by latitude and longitude."""
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"{BASE_URL}weather?lat={lat}&lon={lon}&appid={api_key}&lang={lang}&units={units}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame([data]) if tibble_format else data
    else:
        raise Exception("Error fetching weather data. Is your API key active?")

def get_weather_by_name(name, lang="en", units="standard", tibble_format=False):
    """Get current weather data by city name."""
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"{BASE_URL}weather?q={name}&appid={api_key}&lang={lang}&units={units}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame([data]) if tibble_format else data
    else:
        raise Exception("Error fetching weather data. Is your API key active?")
    

def weather_forecast_req(lat, lon, api_key=os.getenv("weather_key"), lang="en", units="standard", tibble_format=True):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&lang={lang}&units={units}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["list"] if tibble_format else response.json()
        
        for item in data:
            item['dt'] = datetime.utcfromtimestamp(item['dt'])
        
        return pd.DataFrame(data) if tibble_format else data
    except requests.exceptions.RequestException:
        raise Exception("Error to collect the data. Is your API Key active?")

def weather_state_forecast(api_key=os.getenv("weather_key"), lang="en", units="standard", name=None, tibble_format=True):
    url = f"https://api.openweathermap.org/data/2.5/forecast?appid={api_key}&lang={lang}&units={units}&q={name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["list"] if tibble_format else response.json()
        
        for item in data:
            item['dt'] = datetime.utcfromtimestamp(item['dt'])
        
        return pd.DataFrame(data) if tibble_format else data
    except requests.exceptions.RequestException:
        raise Exception("Error to collect the data. Is your API Key active?")

