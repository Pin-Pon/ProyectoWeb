
from distutils.command.upload import upload
from django.db import models
from usuarios.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

        
class Modalidad(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class eventos(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null= True, blank= True)
    imagen = models.ImageField(upload_to='eventos')
    fecha = models.DateField(null=True)
    hora = models.TimeField(null= True)
    modalidad= models.ForeignKey(Modalidad, on_delete=models.SET_NULL, null= True, blank= True)
    lugar = models.CharField(max_length=255, null= True)
    descripcion = models.TextField(null=True, blank=True)
    participantes = models.ManyToManyField(Usuario, related_name = "participantes")
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mis_eventos", null=True) # ,null=True,blank=True????  creo una carpeta donde le decimos q guarde'__>eventos' dentro de la carpeta media para los archivos media
    created  = models.DateTimeField(auto_now_add=True) #cuando se creo fecha el evento
    updated  =models.DateTimeField(auto_now_add=True)  #cuando se elimino fecha    
  
#HACER LA MIGRACION MALDITAAA....

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'


    def __str__(self):
        return self.titulo 

    def cant_participantes(self):
        return self.participantes.count() 


class CsvFile(models.Model):
    csv_file = models.FileField(upload_to='documents')           

