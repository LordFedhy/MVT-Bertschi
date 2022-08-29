from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

def punto2 (request):
    dia=datetime.datetime.today()
    cadena="hoy es "+str(dia)

    return HttpResponse(cadena)

def familiar1(request):
    nombre="Federico"
    apellido="Bertschi"
    edad=37
    diccionario={"nombre":nombre,"apellido":apellido,"edad":edad}
    archivo=open("C:/Users/RM/Desktop/phyton/MVT+Bertschi/Plantillas/familiar1.html")
    contenido=archivo.read()
    archivo.close()
    plantilla=Template(contenido)
    Contexto=Context(diccionario)
    documento=plantilla.render(Contexto)
    return HttpResponse(documento)

def familiar2(request):
    nombre="Noelia"
    apellido="Peralta"
    edad=38
    diccionario={"nombre":nombre,"apellido":apellido,"edad":edad}
    archivo=open("C:/Users/RM/Desktop/phyton/MVT+Bertschi/Plantillas/familiar2.html")
    contenido=archivo.read()
    archivo.close()
    plantilla=Template(contenido)
    Contexto=Context(diccionario)
    documento=plantilla.render(Contexto)
    return HttpResponse(documento)

def familiar3(request):
    nombre="Franco"
    apellido="Bertschi"
    edad=21
    diccionario={"nombre":nombre,"apellido":apellido,"edad":edad}
    archivo=open("C:/Users/RM/Desktop/phyton/MVT+Bertschi/Plantillas/familiar3.html")
    contenido=archivo.read()
    archivo.close()
    plantilla=Template(contenido)
    Contexto=Context(diccionario)
    documento=plantilla.render(Contexto)
    return HttpResponse(documento)

