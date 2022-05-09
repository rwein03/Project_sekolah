import json
from telnetlib import STATUS
from django.shortcuts import render, redirect
from django.views.generic import View

from django.http import JsonResponse
from django.forms.models import model_to_dict

from .forms import wifiform, actionForm
from API_web.models import userWifi, request_action

class actionView(View):
    def get(self, request):
        form = actionForm()
        data_view = request_action.objects.all()
        context = {
            'data' : data_view,
            'form': form
        }
        return render(request, 'main/action.html', context=context)
    
    def post(self, request):
        form = actionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Main_App:action')


class userWifiView(View):
    def get(self, request):
        form =  wifiform(request.POST or None)
        data  = userWifi.objects.all()
        context = {
            'form' : form,
            'data' : data
        }
        return render(request, 'main/index.html', context=context)
    
    def post(self, request):
        form = wifiform(request.POST)
        if form.is_valid():
            new_wifi = form.save()
            context = {
                'dataList' : model_to_dict(new_wifi)
            }
            return JsonResponse(context, status=200)
        else :
            return redirect('MainWeb:index')
        
class deleteWifi(View):
    def post(self, request, id):
        data_delete = userWifi.objects.get(id=id)
        data_delete.delete()
        return JsonResponse({'result':'ok'})
                
    
    
