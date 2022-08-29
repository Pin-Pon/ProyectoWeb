from django.shortcuts import render
from django.views.generic import ListView
from .forms import FormularioPost
from blog.models import Post , Categoria
from core.mixins import SuperUsuarioMixin
from django.views.generic import CreateView
from django.urls import reverse
# Create your views here.
'''
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})
'''    
class blog( ListView):
    template_name="blog/blog.html"
    model= Post      
    context_object_name = "posts"
    paginate_by=1

    def get_queryset(self):
        return Post.objects.all().order_by('categorias')    



def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)

    return render(request,"blog/categoria.html",{"categoria": categoria,"posts": posts})
class CrearPost(SuperUsuarioMixin,CreateView):
        model = Post
        form_class = FormularioPost
        template_name = 'blog/crear_post.html'

        def get_success_url(self): # Redirecciona a otra pagina despues de crear un evento
              return reverse('Blog')