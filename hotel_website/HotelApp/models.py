from django.db import models

class Room(models.Model):  
    ROOM_TYPES = [ 
        ('Comfortkamer', 'Comfortkamer'),
        ('Deluxekamer', 'Deluxekamer'),
        ('Junior Suite', 'Junior Suite'),
        ('Familie Suite', 'Familie Suite'),
        ('Bruidssuite', 'Bruidssuite'),
    ]

    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)  
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2) 
    availability = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.get_room_type_display()} - €{self.price_per_night:.2f}"


class Reservations(models.Model):
    name = models.CharField(max_length=101
    )
    email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE) 
    date = models.DateField()