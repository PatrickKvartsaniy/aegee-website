from django.shortcuts import render

from events.models import Event
from blog.models import Post

def index(request):
    events = Event.objects.all().order_by('-id')[:4]
    blog = Post.objects.all().order_by('-id')[:3]
    return render(request,'landing/index.html', {"events":events,"blog":blog})