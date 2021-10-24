from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    genero = models.CharField(max_length=100, blank=False, null=False)
