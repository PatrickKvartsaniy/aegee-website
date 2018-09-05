from django.shortcuts import render

from .models import Board_member

def index(request):
    board = Board_member.objects.all()
    return render(request,'contact/contact.html',{"board":board})

def message(request):
    if request == "POST":
        pass