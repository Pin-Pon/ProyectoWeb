from django import forms
from .models import eventos


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'



class CrearEventoForm(forms.ModelForm):
    class Meta:
        model = eventos
        fields = ['titulo', 'categoria', 'imagen', 'fecha', 'hora', 'modalidad', 'lugar', 'descripcion']	
        labels = {
            'imagen': 'Imagen del evento',
            'titulo' : 'Titulo del evento',
            'fecha' : '',
            'hora' : '',
            'lugar' : 'Lugar del evento',
            'categoria' : 'Categoría',
            'modalidad' : 'Modalidad',
            'descripcion' : 'Descripción',

        }

        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'titulo' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo del Evento'}),
            'fecha' : DateInput(),
            'hora' : TimeInput(),
            'lugar' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Lugar'}),
            'categoria' : forms.Select(attrs={'class':'form-select',  'placeholder':'Categoría'}),
            'modalidad' : forms.Select(attrs={'class':'form-select', 'placeholder':'Modalidad'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe una descripción'}),
        }




    