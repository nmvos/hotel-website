from django import forms
from .models import Room, Reservations

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'price_per_night', 'availability']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ['name', 'email', 'date', 'room']