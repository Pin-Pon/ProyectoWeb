from audioop import reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from eventos.models import eventos
from django.views.generic.edit import CreateView
from .forms import CrearEventoForm

# Create your views here.
def evento(request):
    mostrar = eventos.objects.all()
    print(mostrar)
    return render(request, "eventos/eventos.html", {"mostrar":mostrar})

class CrearEvento(CreateView):
        model = eventos
        form_class = CrearEventoForm
        template_name = 'eventos/crear_eventos.html'

        def get_success_url(self, **kwargs): # Redirecciona a otra pagina despues de crear un evento
              return reverse('eventos')


      
