from django.shortcuts import render, redirect
from django.views.generic import View

from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

from .forms import wifiform, actionForm
from API_web.models import userWifi, request_action, Computer

def post_action(request, mac_addr, action):
    a = Computer.objects.get(mac_addr=mac_addr)
    print(a.mac_addr)
    if request.method =='POST':
        request_action.objects.create(
            macaddr = a,
            action = action
        )
        return HttpResponse('OK')
    else:
        return HttpResponse('ERROR')
        

class activView(View):
    def get(self, request):
        data = Computer.objects.filter(isAlive=True).values()
        context = {
            'data' : data
        }
        return render(request,'main/active.html' ,context=context)

    def post(self, request, mac_addr, action):
        a = Computer.objects.get(mac_addr=mac_addr)
        tambah = request_action.objects.create(
            macaddr = a,
            action = action)
        print(tambah)
        return redirect('Main_App:active')

        

class actionView(View):
    def get(self, request):
        data_view = request_action.objects.select_related('macaddr').all()
        form = actionForm()
        context = {
            'data' : data_view,
            'form': form
        }
        return render(request, 'main/action.html', context=context)        


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
                
    
    
