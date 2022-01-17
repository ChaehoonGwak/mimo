from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detectme', views.detectme, name='detectme'),
]
