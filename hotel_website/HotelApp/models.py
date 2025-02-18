from django.db import models

class Room(models.Model):  
    ROOM_TYPES = [ 
        ('comfort kamer', 'Comfortkamer'),
        ('deluxe kamer', 'Deluxekamer'),
        ('junior suite', 'Junior Suite'),
        ('familie suite', 'Familie Suite'),
        ('bruidssuite', 'Bruidssuite'),
    ]

    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)  
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2) 
    availability = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.get_room_type_display()} - €{self.price_per_night:.2f}"


class Reservations(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE) 
    date = models.DateField()