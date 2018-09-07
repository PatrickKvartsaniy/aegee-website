from django.urls import path

from .views import index, message


urlpatterns = [
    path('', index),
    path('message', message)
]