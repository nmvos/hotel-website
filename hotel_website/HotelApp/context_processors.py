import requests

def weather_data(request):
    api_key = '969c22d28f33d607faa1dce4ef079679'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Alkmaar",
        "appid": api_key,
        "units": "metric",
        "lang": "nl"
    }

    try:
        r = requests.get(url=url, params=params)
        res = r.json()

        weather = {
            "description": res["weather"][0]["description"],
            "icon": res["weather"][0]["icon"],
            "temp": res["main"]["temp"],
            "city": res["name"]
        }
    except Exception as e:
        weather = {
            "description": "Niet beschikbaar",
            "icon": "01d",  
            "temp": "--",
            "city": "Onbekend"
        }

    return {"weather": weather}
