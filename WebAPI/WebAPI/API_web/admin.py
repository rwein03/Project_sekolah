from django.contrib import admin
from .models import Computer, userWifi, request_action

# Register your models here.
admin.site.register(Computer)
admin.site.register(userWifi)
admin.site.register(request_action)