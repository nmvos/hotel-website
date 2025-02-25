from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import RoomForm, ReservationForm
from django.core.mail import send_mail
from .models import Room, Reservations
import requests, json
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
   
   return render(request, "home.html")

  
def kamers(request):
    rooms = Room.objects.all()  # haalt alle kamers op
    return render(request, "kamers.html", {"rooms": rooms})  


@login_required()
def add_room(request):
  if request.method == 'GET': 
    form = RoomForm()

  elif request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid(): # validatie
            new_room = form.save(commit=False)
            new_room.save() 
            messages.info(request, "Kamer is toegevoegd!")
            return redirect("kamers") 
        
  return render(request, "add_room.html", {"form": form})


@login_required() # je moet ingelogd zijn anders kan je niet naar de pagina
def edit_room(request, room_id): # def edit_room een je geeft de room_id mee (primary key) zodat je deze in de code kunt gebruiken
    room = get_object_or_404(Room, id=room_id) # room is de model room en omdat daar niet de room_id (primary_key) in zit geef je die appart mee

    if request.method == 'POST': # als de request methode post is dan:
        form = RoomForm(request.POST, request.FILES, instance=room) # het formulier is mijn custom form die ik heb aangemaakt en die vraag je met post, met instance=room vraag je alle data ervan uit
        if form.is_valid(): # als de form voldoet aan de form standaarden dan:
            if 'image' in request.FILES:
              print("Nieuwe afbeelding ontvangen:", request.FILES['image'].name)
            else:
              print("Geen nieuwe afbeelding ontvangen")

            form.save()  # slaat de form op
            messages.info(request, "Kamer is gewijzigd!")
            return redirect("kamers")  # verwijst je naar de kamer pagina
    else:
        form = RoomForm(instance=room)  

    return render(request, "edit_room.html", {"form": form}) # redirect je naar edit_room.html 


@login_required()
def remove_room(request, room_id):
    if request.method == 'POST':
      room = get_object_or_404(Room, id=room_id)
      room.delete()
      messages.info(request, "Kamer is verwijderd")

      return redirect("kamers")
        

# reserve functie
def reserve_room(request):
  if request.method == 'GET': 
    form = ReservationForm()

  elif request.method == 'POST':
        form = ReservationForm(request.POST)
        naam = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        room_id = request.POST.get('room')


        if form.is_valid(): # validatie
            reservation = form.save(commit=False)
            reservation.save()

            room = Room.objects.get(id=room_id)  # room objects
            room_name = room.get_room_type_display() 

            # voegt naam en e-mail toe aan het bericht
            email_tekst = f"Naam: {naam}\nE-mail: {email}\n\nDatum:{date}\nKamer:{room_name}"

           # processeed de form data
            send_mail(
            subject=f'Nieuwe reservering van {naam}',
            message=email_tekst,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
            )
        messages.info(request, "Kamer gereserveerd!")
        return redirect("kamers") 
        
  return render(request, "reserve_room.html", {"form": form})

def verwerken(request):
    if request.method == 'POST':
        naam = request.POST.get('naam')
        email = request.POST.get('email')
        bericht = request.POST.get('bericht')

         # voegt naam en e-mail toe aan het bericht
        email_tekst = f"Naam: {naam}\nE-mail: {email}\n\nBericht:\n{bericht}"

        # processeed de form data
        send_mail(
            subject=f'Contactformulier van {naam}',
            message=email_tekst,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.info(request, "Bedankt voor je bericht!")
        return redirect('contact')
        

    return redirect('contact')
    
  
def restaurants(request):
    return render(request, 'restaurants.html')

def over_ons(request):
    return render(request, 'over_ons.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')


