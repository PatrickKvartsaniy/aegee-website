from django.urls import path, include
from rest_framework import routers

from .views import index, international, local, EventView

router = routers.DefaultRouter()
router.register('events', EventView)

urlpatterns = [
    path('', index),
    path('international', international),
    path('local', local),
    path('api',include(router.urls))
]