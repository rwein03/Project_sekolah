from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('api/',include('API_web.urls', namespace='API_web')),
    path('main/',include('MainWeb.urls', namespace='Main_App')),
]
