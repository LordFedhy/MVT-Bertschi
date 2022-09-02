from datetime import date
from django.db import models

class Familiar(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField(max_length=100)
    fecha_nac=models.CharField(max_length=100)

