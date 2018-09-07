from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('AllEvents', views.AllEventsAPI, 'all_events')
router.register('FutureEvents', views.FutureEventsAPI, 'future_events')
router.register('AllPosts', views.AllPostsAPI, 'all_posts')
router.register('LastPosts', views.LastPostsAPI, 'last_posts')

urlpatterns = [
    path('',include(router.urls))
]