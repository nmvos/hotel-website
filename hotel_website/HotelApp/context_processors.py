import requests

def weather_data(request, city="Alkmaar"):
    api_key = '969c22d28f33d607faa1dce4ef079679'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Dit zorgt ervoor dat je de temperatuur in Celsius krijgt.
        "lang": "nl"
    }

    try:
        r = requests.get(url=url, params=params)
        r.raise_for_status()  # Controleer of de status van het verzoek succesvol is
        res = r.json()

        if r.status_code == 200 and 'weather' in res:
            weather = {
                "description": res["weather"][0]["description"],
                "icon": res["weather"][0]["icon"],
                "temp": res["main"]["temp"],  # Haal de temperatuur in Celsius op
                "city": res["name"]
            }
        else:
            weather = {
                "description": "Niet beschikbaar",
                "icon": "01d",  # Placeholder icoon
                "temp": "--",  # Geen temperatuur beschikbaar
                "city": city
            }

    except requests.exceptions.RequestException as e:
        # Log de foutmelding voor het geval de API-aanroep mislukt
        print(f"Error fetching weather data: {e}")
        weather = {
            "description": "Niet beschikbaar",
            "icon": "01d",  # Placeholder icoon
            "temp": "--",  # Geen temperatuur beschikbaar
            "city": city
        }

    return {"weather": weather}
