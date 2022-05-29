from random import seed
from django.db import models
from django.contrib.auth.models import User

class Lector(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    telefono= models.IntegerField()
    libroEnPrestamo= models.BooleanField()

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

    def __str__(self):
        txt="{0}  {1}"
        return txt.format(self.nombre, self.apellido)


class Prestamo(models.Model):
    lector= models.CharField(max_length=30)
    libro= models.CharField(max_length=30)
    fechaDePrestamo= models.DateField()
    devuelto= models.BooleanField(blank=False)

    def __str__(self):
        txt="{0} {1} {2}"
        return txt.format(self.lector,'/', self.libro)


class Libro(models.Model):
    nombre= models.CharField(max_length=30)
    enPrestamo= models.BooleanField()

    def __str__(self):
        txt="{0}"
        return txt.format(self.nombre)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null = True, blank=True)
    
    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatares'
    

    
