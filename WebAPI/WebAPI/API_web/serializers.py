from dataclasses import field, fields
from importlib.metadata import files
from rest_framework import serializers
from .models import Computer, userWifi, request_action

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = '__all__'
        
class actionSerializer(serializers.ModelSerializer):
    class Meta:
        model = request_action
        fields = '__all__'

        