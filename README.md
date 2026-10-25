# Python Weather Forecast App 🌦️

A simple Python application that fetches current weather conditions and a 7-day weather forecast for any supported city using the Open-Meteo API.

## Features

- 🌍 Search for a city by name
- 🌡️ View current temperature and feels-like temperature
- 💧 Check relative humidity
- 💨 View wind speed
- ☁️ Get current weather conditions
- 📅 View a 7-day temperature forecast
- 🌧️ Check daily maximum rain probability
- ⚠️ Handle network errors and invalid city names
- 🆓 Uses the free Open-Meteo weather API without requiring an API key

## Technologies Used

- Python 3
- Requests library
- Open-Meteo Geocoding API
- Open-Meteo Forecast API

## Requirements

- Python 3.10 or newer
- Internet connection

## Installation

**1. Clone this repository**

```bash
git clone https://github.com/YOUR-USERNAME/python-weather-forecast.git
```

Replace `YOUR-USERNAME` with your GitHub username.

**2. Open the project directory**

```bash
cd python-weather-forecast
```

**3. Install the required package**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python weather.py
```

Enter a city name when prompted to view its current weather and 7-day forecast.

## Example

```text
Enter city name: Patna

==========================================
       REAL-TIME WEATHER REPORT
==========================================
City: Patna
Country: India
Local time: [local date and time]
Temperature: [current temperature] °C
Feels like: [feels-like temperature] °C
Humidity: [relative humidity] %
Wind speed: [wind speed] km/h
Weather: [current conditions]

==========================================
          7-DAY FORECAST
==========================================
```

*The values above are placeholders. Actual weather information depends on the city and the API response.*

## APIs Used

- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) — finds the coordinates of a city.
- [Open-Meteo Forecast API](https://open-meteo.com/en/docs) — provides current weather data and daily forecasts.

## Future Improvements

- Build a graphical user interface (GUI).
- Display weather icons and charts.
- Add support for Celsius and Fahrenheit.
- Save recent searches.
- Add a web interface using Flask.

## Author

**Adan Shoaib**

B.Tech Computer Science and Engineering student | Python Developer

## License

This project is available under the MIT License if an MIT `LICENSE` file is included in the repository.
