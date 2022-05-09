from attr import fields
from django import forms
from django.utils.datastructures import MultiValueDict

from API_web.models import userWifi, request_action

class actionForm(forms.ModelForm):
    
    class Meta:
        model = request_action
        fields = ['macaddr', 'action']

        labels = {
            'macaddr' : 'SELECT MAC ADDRESS'
        }
        
        widgets = {
            'macaddr' : forms.TextInput(
                attrs={
                    'class':'form-control'
                    }
            ),
            'action' : forms.TextInput(
                attrs={
                    'class':'form-control'
                    }
            ),
        }
        
class wifiform(forms.ModelForm):
    class Meta:
        model = userWifi
        fields = [
            'username', 
            'password'
            ]
        
        labels = {
            'username' : 'USERNAME',
            'password' : 'PASSWORD'
        }
        
        widgets = {
            'username' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'INPUT USERNAME'
                }
            ),
            'password' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'INPUT PASSWORD'
                }
            ),
        }
        
        