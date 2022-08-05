from django.shortcuts import render, HttpResponse
from eventos.models import eventos
# Create your views here.
def inicio(request):
    return render(request, "ProyectoWebApp/inicio.html")

def login(request):
    return render(request,"ProyectoWebApp/login.html")

def evento(request):
    mostrar = eventos.objects.all()
    print(mostrar)
    return render(request, "ProyectoWebApp/eventos.html", {"mostrar":mostrar})

def calendario(request):
    return render(request, "ProyectoWebApp/calendario.html")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")    