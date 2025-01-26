
# OweatherPy

OweatherPy is a Python package that simplifies interactions with the OpenWeather API. The package encodes API requests automatically, returning data in JSON format or as a Pandas DataFrame.

## Installation
You can install the package using the following command:

```bash
pip install OweatherPy
```

OpenWeather is a weather information system that allows you to obtain data through its API. To use the package, you must register on their website (https://openweathermap.org) and activate an API key. Once registered, you can make queries with this library, for example:

```python
from oweatherpy.weather import get_weather_data

# Set your API key
set_weather_key("YOUR API KEY")

# Get current weather data
weather_data = get_weather_data(lat=19, lon=-19, tibble_format=True)
print(weather_data)
```

The result will be:

```
   coord.lon  coord.lat  weather.id weather.main weather.description weather.icon base main.temp
0        -19         19         800       Clear         clear sky          01d stations     293.0
# … with more variables: main.feels_like, main.temp_min, main.temp_max, etc.
```

You can also retrieve historical data using the following function:

```python
from oweatherpy.utils import get_historic_weather

historic_data = get_historic_weather(lat=19, lon=-19, date="2022-01-01", tibble_format=True)
print(historic_data)
```

Using the equivalent function `get_weather_by_name()`, you can retrieve weather data by country or state name (only for the USA):

```python
from oweatherpy.weather import get_weather_by_name

data = get_weather_by_name(name="New York", tibble_format=True)
print(data)
```

You can also obtain forecasts, massive historical data, and air pollution data.

The package includes a function to obtain coordinates for available cities using their names. You can use the `get_coordinates()` function to get this information, for example:

```python
from oweatherpy.utils import get_coordinates

coordinates = get_coordinates("Mexico", "CDMX")
print(coordinates)
```

And you will get the following result:

```
{'country': 'MX', 'state': 'Mexico City', 'lat': 19.4, 'lon': -99.1}
```

