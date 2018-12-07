from django.shortcuts import render

from website.apps.events.models import Event
from website.apps.blog.models import Post
from website.apps.projects.models import Project


def index(request):
    events = Event.objects.all().order_by('-id')[:4]
    projects = Project.objects.all().order_by('-id')[:4]
    blog = Post.objects.all().order_by('-id')[:3]
    return render(request,'landing/index.html', {"events":events,"blog":blog, "projects":projects})