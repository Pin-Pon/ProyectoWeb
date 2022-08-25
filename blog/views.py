from django.shortcuts import render
from django.urls import reverse
from core.mixins import SuperUsuarioMixin
from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .forms import CrearPostForm

from blog.models import Post , Categoria

# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)

    return render(request,"blog/categoria.html",{"categoria": categoria,"posts": posts})


class CrearPost(SuperUsuarioMixin,LoginRequiredMixin,CreateView):
        model = Post
        form_class = CrearPostForm
        template_name = 'blog/crearpost.html'

        def get_success_url(self): # Redirecciona a otra pagina despues de crear un evento
              return reverse('Blog')