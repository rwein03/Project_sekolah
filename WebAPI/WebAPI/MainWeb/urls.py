from django.contrib import admin
from django.urls import path, include

from .views import userWifiView, deleteWifi, actionView

app_name = 'Main_App'

urlpatterns = [
    path('',userWifiView.as_view(), name='index'),
    path('action',actionView.as_view(), name='action'),
    path('<str:id>/delete/', deleteWifi.as_view())
]