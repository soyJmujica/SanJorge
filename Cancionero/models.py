from django.db import models

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    
# Create your models here.
