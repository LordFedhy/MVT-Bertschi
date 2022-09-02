from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def Esposa(request):
    familiar=Familiar(nombre="Noelia", apellido="Peralta", edad="38", fecha_nac="18/07/1984")
    familiar.save()
    texto=f"El familiar creado se llama {familiar.nombre} {familiar.apellido}, tiene {familiar.edad} y nació el {familiar.fecha_nac}."
    return HttpResponse (texto)

def Hermano_menor(request):
    familiar=Familiar(nombre="Diego", apellido="Bertschi", edad="33", fecha_nac="30/09/1988")
    familiar.save()
    texto=f"El familiar creado se llama {familiar.nombre} {familiar.apellido}, tiene {familiar.edad} y nació el {familiar.fecha_nac}."
    return HttpResponse (texto)

def Hermano_mayor(request):
    familiar=Familiar(nombre="Pablo", apellido="Bertschi", edad="41", fecha_nac="02/12/1980")
    familiar.save()
    texto=f"El familiar creado se llama {familiar.nombre} {familiar.apellido}, tiene {familiar.edad} y nació el {familiar.fecha_nac}."
    return HttpResponse (texto)