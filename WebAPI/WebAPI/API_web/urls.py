from django.contrib import admin
from django import views
from django.urls import path, include
from . import views

app_name = 'API_web'

urlpatterns=[
    path('', views.getData, name='index')
]