# Generated by Django 5.1.6 on 2025-02-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0006_alter_reservations_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='room_images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Comfortkamer', 'Comfortkamer'), ('Deluxekamer', 'Deluxekamer'), ('Junior Suite', 'Junior Suite'), ('Familie Suite', 'Familie Suite'), ('Bruidssuite', 'Bruidssuite')], max_length=20),
        ),
    ]
