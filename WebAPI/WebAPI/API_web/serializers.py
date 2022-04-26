from dataclasses import field, fields
from importlib.metadata import files
from pyexpat import model
from rest_framework import serializers
from .models import Computer, userWifi

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = '__all__'