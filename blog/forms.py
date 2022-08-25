from django import forms
from .models import Post


class CrearPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','contenido' ,'categorias', 'imagen', 'autor' ]	
        labels = {
            'imagen': 'Imagen del Post',
            'titulo' : 'Titulo del Post',
            'categorias' : 'Categoría',
            'contenido' : 'Contenido del Post',
            'autor' : 'Autor del Post',

        }

        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'titulo' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo del Evento'}),
            'categorias' : forms.Select(attrs={'class':'form-select',  'placeholder':'Categoría'}),
            'contenido' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe una descripción'}),
            'autor' : forms.Select(attrs={'class':'form-select', 'placeholder':'Autor'}),
        }