from django.shortcuts import render
from eventos.models import eventos
from django.views.generic.edit import CreateView
from .forms import CrearEventoForm
# Create your views here.
def evento(request):
    mostrar = eventos.objects.all()
    print(mostrar)
    return render(request, "eventos/eventos.html", {"mostrar":mostrar})

class CrearEvento(CreateView):
    class Meta:
        model = eventos
        form_class = CrearEventoForm
        template_name = 'eventos/crear_evento.html'
