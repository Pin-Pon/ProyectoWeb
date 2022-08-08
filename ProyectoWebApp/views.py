from django.shortcuts import render, HttpResponse
#from eventos.models import eventos llevamos la importacion a la views de la app eventos propia
# Create your views here.
def inicio(request):
    return render(request, "ProyectoWebApp/inicio.html")

def login(request):
    return render(request,"ProyectoWebApp/login.html")

# def evento(request):
#     mostrar = eventos.objects.all()   #cambiamos a la vista de la aplicacion
#     print(mostrar)
#     return render(request, "ProyectoWebApp/eventos.html", {"mostrar":mostrar})

def calendario(request):
    return render(request, "ProyectoWebApp/calendario.html")

# def blog(request):
#     return render(request, "ProyectoWebApp/blog.html") la movemos a la appp como todas

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")    