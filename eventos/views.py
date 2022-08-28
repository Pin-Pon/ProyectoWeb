from django.urls import reverse
from django.shortcuts import render, HttpResponse
from ProyectoWeb.ProyectoWeb.settings import BASE_DIR
from ProyectoWeb.eventos.models import CsvFile
from core.mixins import SuperUsuarioMixin
import os

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from eventos.models import eventos
from django.views.generic import CreateView ,UpdateView , DeleteView
from .forms import CrearEventoForm

# Create your views here.
def evento(request):
    mostrar = eventos.objects.all()
    print(mostrar)
    return render(request, "eventos/eventos.html", {"mostrar":mostrar})

class CrearEvento(SuperUsuarioMixin,LoginRequiredMixin,CreateView):
        model = eventos
        form_class = CrearEventoForm
        template_name = 'eventos/crear_eventos.html'

        def get_success_url(self): # Redirecciona a otra pagina despues de crear un evento
              return reverse('EventosNuevos')

class Editar(SuperUsuarioMixin,LoginRequiredMixin, UpdateView):
    template_name="eventos/editar.html"
    model=eventos
    form_class = CrearEventoForm

    def get_success_url(self, **kwargs):
        return reverse('EventosNuevos')   


class Eliminar(SuperUsuarioMixin,LoginRequiredMixin, DeleteView):
    template_name="eventos/eliminar.html"
    model=eventos
  
    
    
    def get_success_url(self, **kwargs):
        return reverse('EventosNuevos')
'''
class CsvUploadView(generic.CreateView):
    model=CsvFile
    fields=['csv_file']
    template_name='eventos/cargar.html'

    def get_queryset(self):
        return CsvFile.objects.all().order_by('-id')

    def get_success_url(self):
        return reverse('EventosNuevos')

class CsvDownloadView(generic.ListView):
    model=CsvFile
    fields=['csv_file']
    template_name='eventos/descargar.html'

    def get_queryset(self):
        return CsvFile.objects.all().order_by('-id')

    def get_success_url(self):
        return reverse('EventosNuevos')
'''
'''
def desascargarArchivo(request,pk):
    csv_file = CsvFile.objects.get(pk=pk)
    filename = csv_file.csv_file.name
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '/media/' + filename
    path = open(filepath, 'rb')
    mime_tipe = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_tipe)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
'''  


      
