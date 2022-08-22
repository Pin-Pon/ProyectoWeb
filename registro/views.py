from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import CreateView
from .forms import FormularioRegistro
from usuarios.models import Usuario
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





#   class Registro(CreateView):
#       model = Usuario
#       form_class = FormularioRegistro
#       template_name = "registro/registro.html"

#       def get_success_url(self, **kwargs):
#           return reverse("inicio") 


class Registro(View):
    model = Usuario 
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
        else:
            return render(request, 'registro/registro.html', {'form': form})    

     
     





# def cerrar_sesion(request):
#     logout(request)
#     return redirect("inicio")

         
      
    



