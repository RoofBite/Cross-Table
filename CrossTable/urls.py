from django.contrib import admin
from django.urls import path
from . import views
import CrossTable

app_name='CrossTable'

urlpatterns = [
    path('', views.index, name='index')
]
