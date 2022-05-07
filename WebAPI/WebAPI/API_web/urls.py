from msilib.schema import ListView
from django.contrib import admin
from django import views
from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'API_web'

urlpatterns=[
    path('', views.getData, name='index'),
    path('<int:id_data>/', views.data_detail, name='detail'),
    path('class', views.listData.as_view(), name='class_based'),
    path('action', views.actionData.as_view(), name='action_list'),
    path('userfilter/', views.userComputer.as_view(), name='user_filter'),
    path('actionfilter/', views.getAction.as_view(), name='action_filter'),
    path('class/<str:mac>', views.listDataDetail.as_view(), name='class_detail'),
    path('action/<int:pk>', views.detailAction.as_view(), name='action_detail')
]

# urlpatterns = format_suffix_patterns(urlpatterns)