from django.urls import path

from .views import index, feedback


urlpatterns = [
    path('', index),
    path('feedback', feedback)
]