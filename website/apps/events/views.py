from django.shortcuts import render

from .models import Event

def index(request):
    events = Event.objects.all()
    return render(request,"events/events.html",{"events":events})

def international(request):
    events = Event.objects.all().filter(event_type="international")
    return render(request,"events/events.html",{"events":events,"title":"International"})

def local(request):
    events = Event.objects.all().filter(event_type="local")
    return render(request,"events/events.html",{"events":events,"title":"Local"})
