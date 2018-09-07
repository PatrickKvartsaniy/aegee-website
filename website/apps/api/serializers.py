from rest_framework import serializers

from website.apps.events.models import Event
from website.apps.blog.models import Post


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date', 'link', 'image')


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'date', 'link', 'image')