import requests

def weather_data(request, city="Alkmaar"):
    api_key = '969c22d28f33d607faa1dce4ef079679'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # zorgt ervoor dat je de temperatuur in celsius krijgt.
        "lang": "nl"
    }

    try:
        r = requests.get(url=url, params=params)
        r.raise_for_status() 
        res = r.json()

        if r.status_code == 200 and 'weather' in res:
            weather = {
                "description": res["weather"][0]["description"],
                "icon": res["weather"][0]["icon"],
                "temp": res["main"]["temp"],  # haalt de temperatuur in Celsius op
                "city": res["name"]
            }
        else:
            weather = {
                "description": "Niet beschikbaar",
                "icon": "01d",  
                "temp": "--", 
                "city": city
            }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        weather = {
            "description": "Niet beschikbaar",
            "icon": "01d",  
            "temp": "--",  
            "city": city
        }

    return {"weather": weather}
