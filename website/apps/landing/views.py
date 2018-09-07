from django.shortcuts import render

from website.apps.events.models import Event
from website.apps.blog.models import Post

def index(request):
    events = Event.objects.all().order_by('-id')[:4]
    blog = Post.objects.all().order_by('-id')[:3]
    return render(request,'landing/index.html', {"events":events,"blog":blog})