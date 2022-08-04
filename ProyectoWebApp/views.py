from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "ProyectoWebApp/inicio.html")

def login(request):
    return render(request,"ProyectowebApp/login.html")

def eventos(request):
    return render(request, "ProyectoWebApp/eventos.html")

def calendario(request):
    return render(request, "ProyectoWebApp/calendario.html")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")    