from attr import fields
from django import forms

from API_web.models import userWifi, request_action

class actionForm(forms.ModelForm):
    class Meta:
        model = request_action
        fields = '__all__'

        labels = {
            'isStatus' : 'Execute(?)',
            'macaddr' : 'SELECT MAC ADDRESS'
        }
        
        widgets = {
            'macaddr' : forms.Select(
                attrs={
                    'class':'form-control'
                    }
            ),
            'action' : forms.Select(
                attrs={
                    'class':'form-control'
                    }
            ),
            'isStatus' : forms.CheckboxInput(
            )
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
        
        