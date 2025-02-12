from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kamers/', views.kamers, name='kamers'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('over_ons/', views.over_ons, name='over_ons'),
    path('contact/', views.contact, name='contact'),

]