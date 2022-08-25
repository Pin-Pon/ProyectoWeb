from django.urls import reverse
from core.mixins import SuperUsuarioMixin
from django.shortcuts import render
import mimetypes
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import generic
from eventos.models import Eventos, CsvFile
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .forms import CrearEventoForm

# Create your views here.
def evento(request):
    mostrar = Eventos.objects.all()
    print(mostrar)
    return render(request, "eventos/eventos.html", {"mostrar":mostrar})

class CrearEvento(SuperUsuarioMixin,LoginRequiredMixin,CreateView):
        model = Eventos
        form_class = CrearEventoForm
        template_name = 'eventos/crear_eventos.html'

        def get_success_url(self): # Redirecciona a otra pagina despues de crear un evento
              return reverse('EventosNuevos')

class Editar(SuperUsuarioMixin,LoginRequiredMixin, UpdateView):
    template_name="eventos/editar.html"
    model=Eventos
    form_class = CrearEventoForm

    def get_success_url(self, **kwargs):
        return reverse('EventosNuevos')   


class Eliminar(SuperUsuarioMixin,LoginRequiredMixin, DeleteView):
    template_name="eventos/eliminar.html"
    model=Eventos
  
    
    
    def get_success_url(self, **kwargs):
        return reverse('EventosNuevos')

class CsvUploadView(generic.CreateView):  #para subir un archivo csv
   model = CsvFile
   fields = ['csv_file']
   template_name = 'eventos/cargar.html'


   def get_queryset(self):
    return CsvFile.objects.all().order_by('-id')

   def get_success_url(self): # Redirecciona a otra pagina despues de crear un evento
    return reverse('EventosNuevos')


class CsvDownloadView(generic.ListView):  #para descargar un archivo csv  csv_file

    model = CsvFile
    fields = ['csv_file']
    template_name = 'eventos/descargR2.html'


    def get_success_url(self):
        return reverse('EventosNuevos')

def descargarArchivo(request,pk):
    csv_file = CsvFile.objects.get(pk=pk)
    filename=csv_file.csv_file.name
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '/media/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def Asistir(request, pk):
    eventos = get_object_or_404(Eventos, id= request.POST.get("evento_id"))
    asiste = False
    if eventos.participantes.filter(id = request.user.id).exists():
        eventos.participantes.remove(request.user)
        asiste = False
    else:
        eventos.participantes.add(request.user)
        asiste = True
      
    return HttpResponseRedirect(reverse('EventosNuevos', args=[str(pk)]))



        
