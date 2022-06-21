from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from pypro.aperitivos.views import video

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
