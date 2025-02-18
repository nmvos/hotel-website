from django.db import models

class Room(models.Model):  
    ROOM_TYPES = [ 
        ('standaard', 'Standaard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
        ('familiekamer', 'Familiekamer'),
    ]

    room_type = models.CharField(max_length=25, choices=ROOM_TYPES)  
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2) 
    availability = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.get_room_type_display()} - €{self.price_per_night}"
