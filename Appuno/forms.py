from django import forms


class ProdForm(forms.Form):
    
    nombre = forms.CharField(label="Nombre", max_length=50)
    codigo = forms.IntegerField(label="Codigo")
    categoria = forms.CharField(label="Categoria", max_length=30)

class SucuForm(forms.Form):

    nombre = forms.CharField(label="Nombre", max_length=50)
    calle = forms.CharField(label="Calle", max_length=30)
    altura = forms.IntegerField(label="Altura")
    