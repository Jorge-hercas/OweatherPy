

def get_coordinates(country, state, only_coordinates=False):
    """Get coordinates of a country and state."""
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={state},{country}&appid={api_key}&limit=1&lang=en"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            if only_coordinates:
                return {"lat": data[0]["lat"], "lon": data[0]["lon"]}
            return {
                "country": data[0]["country"],
                "state": data[0]["name"],
                "lat": data[0]["lat"],
                "lon": data[0]["lon"],
            }
    raise Exception("Error fetching coordinates.")

def get_historic_weather(lat, lon, date, lang="en", units="standard", tibble_format=False):
    """Get historic weather data."""
    api_key = os.getenv("WEATHER_API_KEY")
    timestamp = int(datetime.strptime(date, "%Y-%m-%d").timestamp())
    url = f"http://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={api_key}&lang={lang}&units={units}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data["hourly"]) if tibble_format else data
    else:
        raise Exception("Error fetching historical weather data.")
