from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Appuno.forms import *


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

def productosFormulario(request):
    if request.method == "POST":
        form= ProdForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre= informacion["nombre"]
            codigo= informacion["codigo"]
            categoria=informacion["categoria"]
            prod = Productos(nombre= nombre, codigo= codigo, categoria= categoria)
            prod.save()
            return render (request,"inicio.html",{"mensaje": "Producto Guardado"})
        else:
            return render (request,"productosFormulario.html",{"form": formulario, "mensaje": "informacion no valida"})

    else:
        formulario = ProdForm()
        return render (request,"productosFormulario.html",{"form": formulario})

def sucursalesFormulario(request):
    if request.method == "POST":
        form= SucuForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre= informacion["nombre"]
            calle= informacion["calle"]
            altura=informacion["altura"]
            suc = Sucursales(nombre= nombre, calle= calle, altura= altura)
            suc.save()
            return render (request,"inicio.html",{"mensaje": "Sucursal Guardada"})
        else:
            return render (request,"sucursalesFormulario.html",{"form": formulario, "mensaje": "informacion no valida"})

    else:
        formulario = SucuForm()
        return render (request,"sucursalesFormulario.html",{"form": formulario})




    

