from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import RoomForm
from .models import Room
import requests, json
from django.contrib.auth.decorators import login_required



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
    rooms = Room.objects.all()  # Haal alle kamers op
    return render(request, "kamers.html", {"rooms": rooms})  


@login_required()
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



@login_required()
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()  # Direct opslaan
            return redirect("kamers")  # Stuur door naar de juiste pagina
    else:
        form = RoomForm(instance=room)  

    return render(request, "edit_room.html", {"form": form})  # Altijd een response geven




def restaurants(request):
    return render(request, 'restaurants.html')

def over_ons(request):
    return render(request, 'over_ons.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')
