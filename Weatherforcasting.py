import requests



def get_weather(city):
    try:
        
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url, params=geo_params, timeout=15
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            print("City not found. Please try another city.")
            return

        place = geo_data["results"][0]
        lat = place["latitude"]
        lon = place["longitude"]

       
        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "wind_speed_10m",
                "weather_code"
            ],
            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_probability_max"
            ],
            "forecast_days": 7,
            "timezone": "auto"
        }

        response = requests.get(
            weather_url, params=params, timeout=15
        )
        response.raise_for_status()
        data = response.json()

        current = data["current"]
        daily = data["daily"]

        conditions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            80: "Rain showers",
            81: "Moderate rain showers",
            82: "Heavy rain showers",
            95: "Thunderstorm",
            96: "Thunderstorm with hail",
            99: "Thunderstorm with heavy hail"
        }

        
        print("=" * 42)
        print("       REAL-TIME WEATHER REPORT")
        print("=" * 42)
        print("City:", place["name"])
        print("Country:", place.get("country", "Unknown"))
        print("Local time:", current["time"])
        print("Temperature:", current["temperature_2m"], "°C")
        print("Feels like:", current["apparent_temperature"], "°C")
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Wind speed:", current["wind_speed_10m"], "km/h")
        print("Weather:", conditions.get(
            current["weather_code"], "Other conditions"
        ))

        
        print("\n" + "=" * 42)
        print("          7-DAY FORECAST")
        print("=" * 42)

        for i, date in enumerate(daily["time"]):
            print(f"\nDate: {date}")
            print("Maximum temperature:",
                  daily["temperature_2m_max"][i], "°C")
            print("Minimum temperature:",
                  daily["temperature_2m_min"][i], "°C")
            print("Rain probability:",
                  daily["precipitation_probability_max"][i], "%")

    except requests.exceptions.RequestException as e:
        print("Network error:", e)
    except (KeyError, IndexError, ValueError) as e:
        print("Error processing weather data:", e)



city = input("Enter city name: ").strip()

if city:
    get_weather(city)
else:
    print("Please enter a city name.")
