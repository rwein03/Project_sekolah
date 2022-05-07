from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import wifiform
from API_web.models import userWifi

class MainIndex(View):
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
            form.save()
        return redirect('Main_App:index')
    
class deleteWifi(View):
    get
                
    
    
