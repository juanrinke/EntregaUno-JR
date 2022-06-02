from django.shortcuts import render
from usuarios.models import Familiares
from django.http import HttpResponse
import datetime
# Create your views here.


def inicio (request):
    return render (request, "index.html")


def lista_familiares (request):
    familiares = Familiares.objects.all()
    datos = {"datos" : familiares}

    return render (request, "lista_familiares.html", datos)

def alta_familiares (request):
    familiar = Familiares(nombre="Juan" , edad=28 , nacimiento = "1994-05-10")
    familiar.save()
    familiar = Familiares(nombre="Cande" , edad=26 , nacimiento = "1995-10-28")
    familiar.save()
    familiar = Familiares(nombre="Carlos" , edad=66 , nacimiento = "1956-04-17")
    familiar.save()

    return HttpResponse ("se cargo correctamente")



