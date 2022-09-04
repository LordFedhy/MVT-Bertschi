from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def Bono(request):
    ON=Bonos(nombre="YPF", Ticker="YPFD", origen="Privado", cupon="0.04", cotizacion="99")
    ON.save()
    texto=f"El Bono creado es el {ON.nombre} con ticker {ON.Ticker} y a una cotización de {ON.cotizacion}, es de origen {ON.origen} y paga un cupon anual del {ON.cupon}."
    return render(request,"Bonos.html")


def inicio(request):
    return render(request,"inicio.html")