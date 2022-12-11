from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

def inicio(request):
    return HttpResponse()
    
# Create your views here.
def familiar(request):
    familiar1 = Familiar(nombre= "Federico", edad= 35, fnac = "1987-09-10")
    familiar1.save()
    familiar2 = Familiar(nombre= "Matias", edad= 32, fnac="1990-12-11")
    familiar2.save()
    familiar3 = Familiar(nombre= "Martin", edad= 30, fnac = "1992-02-23")
    familiar3.save()


    return render(request, "familiares.html", {"familiares" : [familiar1, familiar2, familiar3]})

