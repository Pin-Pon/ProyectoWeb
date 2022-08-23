from django.urls import reverse
from core.mixins import SuperUserRequiredMixin
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from eventos.models import eventos
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .forms import CrearEventoForm

# Create your views here.
def evento(request):
    mostrar = eventos.objects.all()
    print(mostrar)
    return render(request, "eventos/eventos.html", {"mostrar":mostrar})

class CrearEvento(SuperUserRequiredMixin,CreateView):
        model = eventos
        form_class = CrearEventoForm
        template_name = 'eventos/crear_eventos.html'

        def get_success_url(self): # Redirecciona a otra pagina despues de crear un evento
              return reverse('EventosNuevos')

class Editar(LoginRequiredMixin, UpdateView):
    template_name="eventos/editar.html"
    model=eventos
    form_class = CrearEventoForm

    def get_success_url(self, **kwargs):
        return reverse('eventos')             


      
