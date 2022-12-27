from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("productosFormulario/", productosFormulario, name="productosFormulario"),
    path("sucursalesFormulario/", sucursalesFormulario, name="sucursalesFormulario"),
    path("busquedaProductos/", busquedaProductos, name="busquedaProductos"),
    path("buscar/", buscar, name="buscar"),
    path("empleadosFormulario/", empleadosFormulario, name="empleadosFormulario"),

]