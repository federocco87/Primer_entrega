from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Appuno.forms import *

def inicio(request):
    return render (request, "inicio.html")

# Create your views here.
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
            return render (request,"productosFormulario.html",{"mensaje": "Producto Guardado"})
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


def busquedaProductos(request):
    return render(request, "busquedaProductos.html")

def buscar(request):
    prod = request.GET["codigo"]
    print(prod)
    if prod!= "":
        productos=Productos.objects.filter(codigo=prod)
        return render(request,"resultadosBusqueda.html",{"producto":productos})
    else:
        return render(request,"busquedaProductos.html",{"mensaje": "ingrese un producto"})

def empleadosFormulario(request):
    if request.method == "POST":
        form= EmpForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre= informacion["nombre"]
            edad= informacion["edad"]
            categoria=informacion["catwgoria"]
            emp = Sucursales(nombre= nombre, edad= edad, categoria= categoria)
            emp.save()
            return render (request,"empleadosFormulario.html",{"mensaje": "Empleado Guardada"})
        else:
            return render (request,"empleadosFormulario.html",{"form": formulario, "mensaje": "informacion no valida"})

    else:
        formulario = EmpForm()
        return render (request,"empleadosFormulario.html",{"form": formulario})

    

