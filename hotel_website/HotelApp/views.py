from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.


def home(request):

    return render(request, "home.html")
  

def kamers(request):
    return render(request, 'kamers.html')

def restaurants(request):
    return render(request, 'restaurants.html')

def over_ons(request):
    return render(request, 'over_ons.html')

def contact(request):
    return render(request, 'contact.html')

def verwerken(request):
    if request.method == 'POST':
        naam = request.POST.get('naam')
        email = request.POST.get('email')
        bericht = request.POST.get('bericht')

        # Process the form data (e.g., send an email)
        send_mail(
            f'Contact Form Submission from {naam}',
            bericht,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        return HttpResponse('Bedankt voor je bericht!')

    return redirect('contact')