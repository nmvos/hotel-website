# Generated by Django 5.1.6 on 2025-02-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('standaard', 'Standaard'), ('deluxe', 'Deluxe'), ('suite', 'Suite'), ('familiekamer', 'Familiekamer')], max_length=25),
        ),
    ]
