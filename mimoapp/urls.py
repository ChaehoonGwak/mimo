from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mimo', views.mimo_video, name='mimo'),
]
