from django.urls import path

from .views import index, international, local


urlpatterns = [
    path('', index),
    path('international', international),
    path('local', local)
]