from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario

class FormularioRegistro(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "username", "password1", "password2", "email", "telefono"]
        labels = {
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'username' : 'Nombre de usuario',
            'password1' : 'Contraseña',
            'password2' : 'Confirmar contraseña',
            'email' : 'Correo electronico',
            'telefono' : 'Telefono',
        }

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}),
            'username' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Nombre de Usuario'}),
            'password1' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Contraseña'}),
            'password2' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Ingrese su contraseña nuevamente'}),
            'email' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Correo electrónico'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Telefono'}),
            
            
        }



# class FormularioRegistro(forms.Form):
#     nombre=forms.CharField(label="Nombre", required=True)
#     email=forms.CharField(label="Email",required=True)


    #  fields = ["first_name", "last_name", "username", "password1", "password2", "email", "telefono", "domicilio"]