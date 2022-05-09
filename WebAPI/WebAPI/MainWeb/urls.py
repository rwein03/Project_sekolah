from django.contrib import admin
from django.urls import path, include

from .views import userWifiView, deleteWifi, actionView, activView, post_action

app_name = 'Main_App'

urlpatterns = [
    path('',userWifiView.as_view(), name='index'),
    path('action',actionView.as_view(), name='action'),
    path('active',activView.as_view(), name='active'),
    path('active/<str:mac_addr>/<str:action>/add/',activView.as_view(), name='add_action'),
    # path('active/<str:mac_addr>/<str:action>/shutdown/',activView.as_view(), name='shutdown'),
    # path('active/<str:mac_addr>/<str:action>/restart/',activView.as_view(), name='restart'),
    path('<str:id>/delete/', deleteWifi.as_view())
]