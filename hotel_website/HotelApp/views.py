from django.shortcuts import render, HttpResponse
import requests, json

# Create your views here.


def home(request):
   api_key = '969c22d28f33d607faa1dce4ef079679'
   url = "https://api.openweathermap.org/data/2.5/weather"
   params = {
       "q": "Alkmaar",
       "appid": api_key,
       "units": "metric",
       "lang": "nl"
   }
   
   r = requests.get(url=url, params=params)
   res = r.json() # converteert de data naar json

# weather dictionary
   weather = {
    "description": res["weather"][0]["description"],
    "icon": res["weather"][0]["icon"],
    "temp": res["main"]["temp"],
    "city": res["name"]
   }
   
   return render(request, "home.html", {"weather": weather})
  

def kamers(request):
    return render(request, 'kamers.html')

def restaurants(request):
    return render(request, 'restaurants.html')

def over_ons(request):
    return render(request, 'over_ons.html')

def contact(request):
    return render(request, 'contact.html')