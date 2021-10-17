from django.shortcuts import render, HttpResponse
from datetime import datetime
from application.models import Contact
from application.models import Home
from django.contrib import messages

def home(request):
    if request.method == "POST":
        email = request.POST['email']
        home = Home(email=email, date=datetime.today())
        home.save()
        messages.success(request, 'New E-Mail registered.')
        return render(request, 'home.html')
    
    else:
        return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'New Profile details updated.')
        return render(request, 'contact.html')
    
    else:
        return render(request, 'contact.html')

def others(request):
    return render(request, 'others.html')


