from django.urls import path
from .views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("familiar/", familiar, name="familiares"),
    path("productosFormulario/", productosFormulario, name="productosFormulario"),
    path("sucursalesFormulario/", sucursalesFormulario, name="sucursalesFormulario"),


]