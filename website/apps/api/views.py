import datetime

from django.shortcuts import render
from rest_framework import viewsets

from website.apps.events.models import Event
from website.apps.blog.models import Post


from .serializers import EventSerializer, BlogSerializer

# Events views

class AllEventsAPI(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class FutureEventsAPI(viewsets.ModelViewSet):
    queryset = Event.objects.all().filter(date__gt=datetime.date.today())
    serializer_class = EventSerializer


# Blog posts views

class AllPostsAPI(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

class LastPostsAPI(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date')[:3]
    serializer_class = BlogSerializer
