from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import RoomForm
from .models import Room
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
    rooms = Room.objects.all() # haalt de gegevens op
    context = {'rooms': rooms}
    return render(request, 'kamers.html', context)


def add_room(request):
  if request.method == 'GET':
    form = RoomForm()

  elif request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid(): # validatie
            new_room = form.save(commit=False)
            new_room.save() 
            return redirect("kamers") 
        
  return render(request, "add_room.html", {"form": form})




def restaurants(request):
    return render(request, 'restaurants.html')

def over_ons(request):
    return render(request, 'over_ons.html')

def contact(request):
    return render(request, 'contact.html')
