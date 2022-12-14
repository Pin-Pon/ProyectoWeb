from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    created  = models.DateTimeField(auto_now_add=True) 
    updated  =models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


    def __str__(self):
        return self.nombre 

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(max_length=400)
    imagen = models.ImageField(upload_to='blog',null=True,blank=True) #pones o no la imagen entendes!!!
    autor = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE,related_name="categoria_post")
    categorias = models.ManyToManyField(Categoria)    #relacion de n-n 
    created  = models.DateTimeField(auto_now_add=True) 
    updated  =models.DateTimeField(auto_now_add=True)


    class Meta: 
        verbose_name = 'post'
        verbose_name_plural = 'posts'


    def __str__(self):
        return self.titulo

