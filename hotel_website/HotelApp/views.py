from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import RoomForm, ReservationForm
from .models import Room, Reservations
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
    rooms = Room.objects.all()  # haalt alle kamers op
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



@login_required() # je moet ingelogd zijn anders kan je niet naar de pagina
def edit_room(request, room_id): # def edit_room een je geeft de room_id mee (primary key) zodat je deze in de code kunt gebruiken
    room = get_object_or_404(Room, id=room_id) # room is de model room en omdat daar niet de room_id (primary_key) in zit geef je die appart mee

    if request.method == 'POST': # als de request methode post is dan:
        form = RoomForm(request.POST, instance=room) # het formulier is mijn custom form die ik heb aangemaakt en die vraag je met post, met instance=room vraag je alle data ervan uit
        if form.is_valid(): # als de form voldoet aan de form standaarden dan:
            form.save()  # slaat de form op
            return redirect("kamers")  # verwijst je naar de kamer pagina
    else:
        form = RoomForm(instance=room)  # zorgt ervoor dat je altijd de kamer gegevens kan zien in de kamer

    return render(request, "edit_room.html", {"form": form}) # redirect je naar edit_room.html en de rest snap ik niet



# reserve functie
def reserve_room(request):
  if request.method == 'GET': 
    form = ReservationForm()

  elif request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid(): # validatie
            reservation = form.save(commit=False)
            reservation.save() 
            return redirect("kamers") 
        
  return render(request, "reserve_room.html", {"form": form})
    
  


def restaurants(request):
    return render(request, 'restaurants.html')

def over_ons(request):
    return render(request, 'over_ons.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')
