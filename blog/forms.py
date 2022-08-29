from django import forms

from django import forms

from blog.models import Post

class FormularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "imagen","autor","categorias"]
        labels = {
            'titulo' : 'Titulo',
            'contenido' : 'Contenido',
            'imagen' : 'Imagen',
            'autor' : 'Autor',
            'categorias' : 'Categorias',

      
        }

        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo'}),
            'contenido' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Contenido'}),
            'imagen' : forms.ClearableFileInput(attrs={'class':'form-control-file', 'placeholder':'Imagen'}),
            'autor' : forms.Select(attrs={'class':'form-control', 'placeholder':'Autor'}),
            'categorias' : forms.SelectMultiple(attrs={'class':'form-control'}),

            
        }