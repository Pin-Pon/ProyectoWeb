from django.urls import reverse
from core.mixins import SuperUsuarioMixin
from django.shortcuts import render
import mimetypes
import os
from ProyectoWebApp  import urls


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
              return reverse('eventos:EventosNuevos')

class Editar(SuperUsuarioMixin,LoginRequiredMixin, UpdateView):
    template_name="eventos/editar.html"
    model=Eventos
    form_class = CrearEventoForm

    def get_success_url(self, **kwargs):
        return reverse('eventos:EventosNuevos')   


class Eliminar(SuperUsuarioMixin,LoginRequiredMixin, DeleteView):
    template_name="eventos/eliminar.html"
    model=Eventos
  
    
    
    def get_success_url(self, **kwargs):
        return reverse('eventos:EventosNuevos')

class CsvUploadView(generic.CreateView):  #para subir un archivo csv
   model = CsvFile
   fields = ['csv_file']
   template_name = 'eventos/cargar.html'


   def get_queryset(self):
    return CsvFile.objects.all().order_by('-id')

   def get_success_url(self): # Redirecciona a otra pagina despues de crear un evento
    return reverse('eventos:EventosNuevos')


class CsvDownloadView(generic.ListView):  #para descargar un archivo csv  csv_file

    model = CsvFile
    fields = ['csv_file']
    template_name = 'eventos/descargR2.html'


    def get_success_url(self):
        return reverse('eventos:EventosNuevos')

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

'''
def Asistir(request, id_usuario, id_evento):
    eventos = get_object_or_404(Eventos, id= id_evento)
    
    if eventos.participantes.filter(id = id_usuario).exists():
        eventos.participantes.add(request.user)
    eventos.save()
      
    return HttpResponseRedirect(reverse('ProyectoWebApp:Calendario', args=[id_usuario, id_evento]))

def EliminarAsistencia(request, id_usuario, id_evento):
    eventos = get_object_or_404(Eventos, id= id_evento)
    if eventos.participantes.filter(id = id_usuario).exists():
        eventos.participantes.remove(request.user)
    eventos.save() 
      
    return HttpResponseRedirect(reverse('ProyectoWebApp:Calendario', args=[id_usuario,id_evento]))
'''






    # def get_context_data(self,*args, **kwargs):
    #     context = super(DetalleEvento, self).get_context_data(**kwargs)
    #     asiste = False
    #     evento = get_object_or_404(Evento, id= self.kwargs["pk"]) 
    #     cant_participantes = evento.cant_participantes()
    #     if evento.participantes.filter(id= self.request.user.id).exists():
    #         asiste = True
    #     context["asiste"] = asiste
    #     context["cant_participantes"] = cant_participantes
    #     return context
        
