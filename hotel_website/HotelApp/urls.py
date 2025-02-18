from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('kamers/', views.kamers, name='kamers'),
    path('add_room/', views.add_room, name='add_room'),
    path('edit_room/<int:room_id>/', views.edit_room, name='edit_room'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('reserve_room/', views.reserve_room, name='reserve_room'),
    path('over_ons/', views.over_ons, name='over_ons'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('verwerken/', views.verwerken, name='verwerken'),

]