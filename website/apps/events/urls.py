from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('international', views.international),
    path('local', views.local),
]