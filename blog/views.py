from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post , Categoria

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
