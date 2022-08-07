from django.shortcuts import render
from eventos.models import eventos
# Create your views here.
def evento(request):
    mostrar = eventos.objects.all()
    print(mostrar)
    return render(request, "eventos/eventos.html", {"mostrar":mostrar})