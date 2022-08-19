from django.shortcuts import render, redirect
from django.views.generic import View
from usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class Registro(View):
    model = Usuario 
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.cleaned_data['username'])
            return redirect('calendario')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request, 'registro/registro.html', {'form': form})    
      
    



