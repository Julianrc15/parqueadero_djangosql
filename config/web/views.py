from django.shortcuts import render

from web.models import Tarifas



# Create your views here.
def home(request):
    return render(request,'index.html')
    
def tarifas(request):
    #usar modelo
    tarifas=Tarifas.objects.all()
    #crear dic para datos
    diccionario={
        'tarifas': tarifas,
    }


    return render(request,'tarifas.html',diccionario)

