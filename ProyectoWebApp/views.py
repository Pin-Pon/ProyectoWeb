from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from eventos.models import Eventos
#from eventos.models import eventos llevamos la importacion a la views de la app eventos propia
# Create your views here.
def inicio(request):
    return render(request, "ProyectoWebApp/inicio.html")

# def login(request):
#      return render(request,"ProyectoWebApp/login.html")

# def evento(request):
#     mostrar = eventos.objects.all()   #cambiamos a la vista de la aplicacion
#     print(mostrar)
#     return render(request, "ProyectoWebApp/eventos.html", {"mostrar":mostrar})
# def cerrar_sesion(request):
#     return render(request, "ProyectoWebApp/inicio.html")


# def login_view(request):
#     form = AuthenticationForm
#     return render (request, "ProyectoWebApp/login.html",{"form" : form})

def calendario(request):
    agenda=Eventos.objects.all()
    return render(request, "ProyectoWebApp/calendario.html", {"agenda":agenda}) #agenda es una variable que se le pasa a la vista

# def blog(request):
#     return render(request, "ProyectoWebApp/blog.html") la movemos a la appp como todas

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")    

def Asistir(request, id_usuario, id_evento):
    eventos = get_object_or_404(Eventos, id= id_evento)
    
    if eventos.participantes.filter(id = id_usuario).exists():
        eventos.participantes.add(request.user)
    eventos.save()
    return reverse('ProyectoWebApp:Calendario')
      
    

def EliminarAsistencia(request, id_usuario, id_evento):
    eventos = get_object_or_404(Eventos, id= id_evento)
    if eventos.participantes.filter(id = id_usuario).exists():
        eventos.participantes.remove(request.user)
    eventos.save() 
      
    return reverse('ProyectoWebApp:Calendario')