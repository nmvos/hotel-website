# Generated by Django 5.1.6 on 2025-02-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0003_alter_room_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('comfort kamer', 'Comfortkamer'), ('deluxe kamer', 'Deluxekamer'), ('junior suite', 'Junior Suite'), ('familie suite', 'Familie Suite'), ('bruidssuite', 'Bruidssuite')], max_length=20),
        ),
    ]
