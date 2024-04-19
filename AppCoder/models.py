from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    legajo = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    legajo = models.IntegerField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"User: {self.user} - Imagen: {self.imagen}"