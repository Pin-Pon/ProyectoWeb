from django import forms

class FormularioRegistro(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.CharField(label="Email",required=True)


    #  fields = ["first_name", "last_name", "username", "password1", "password2", "email", "telefono", "domicilio"]