from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
     return render(request, 'home.html')

def kamers(request):
    return render(request, 'kamers.html')

def restaurants(request):
    return render(request, 'restaurants.html')

def over_ons(request):
    return render(request, 'over_ons.html')

def contact(request):
    return render(request, 'contact.html')

def footer(request):
    return render(request, 'footer.html')
