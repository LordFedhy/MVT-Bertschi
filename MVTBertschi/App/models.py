from datetime import date
from django.db import models

class Bonos(models.Model):
    nombre=models.CharField(max_length=50)
    Ticker=models.CharField(max_length=50)
    origen=models.CharField(max_length=50)
    cotizacion=models.IntegerField(max_length=50)
    cupon=models.FloatField(max_length=5)

