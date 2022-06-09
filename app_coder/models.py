
from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField (max_length=40)
    camada = models.IntegerField()

class Alumno(models.Model):

    nombre = models.CharField (max_length=30)
    apellido = models.CharField (max_length=30)
    email = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField (max_length=30)
    legajo = models.IntegerField()
