from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre =models.CharField(max_length=50)
    edad = models.IntegerField()
    fnac = models.DateField()

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    categoria = models.CharField(max_length=30)
        
class Sucursales(models.Model):
    nombre = models.CharField(max_length=50)
    calle = models.CharField(max_length=30)
    altura = models.IntegerField()
  