from django.shortcuts import render , redirect
import email
from django.shortcuts import render
from .forms import FormularioRegistro

# Create your views here.
def login(request):
    formulario_registro = FormularioRegistro
    if request.method=="post":
        formulario_registro = FormularioRegistro(data=request.post)
        if formulario_registro.is_valid():
            nombre=request.post.get("nombre")
            email=request.post.get("email")
            return redirect("/registro/?valido")
    return render(request,"registro/login.html",{'miFormulario':formulario_registro})