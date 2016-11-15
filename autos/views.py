# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.template import RequestContext

from autos.models import *
import json

# Create your views here.

def index(request):
    
    diccionario = {'saludo': "Hola Mundo"}
    return render(request, 'index.html', diccionario, 
        context_instance=RequestContext(request))

def listado_vehiculos(request):
    
    # obtengo las provincias
    vehiculos = Vehiculos.objects.all()
    diccionario = {'vehiculos': vehiculos, 'mensaje': 'Mensaje de la pantalla'}
    return render(request, 'listado_vehiculos.html', diccionario, 
        context_instance=RequestContext(request))

def listado_provincias(request):
    
    # obtengo las provincias
    provincias = Provincias.objects.all()
    diccionario = {'provincias': provincias, 'mensaje': 'Mensaje de la pantalla'}
    return render(request, 'listado_provincias.html', diccionario, 
        context_instance=RequestContext(request))


def buscador_placas(request):
    abecedario = [
            ('-', '-'),
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E'),
            ('F', 'F'),
            ('G', 'G'),
            ('H', 'H'),
            ('I', 'I'),
            ('J', 'J'),
            ('K', 'K'),
            ('M', 'M'),
            ('N', 'N'),
            ('O', 'O'),
            ('P', 'P'),
            ('Q', 'Q'),
            ('R', 'R'),
            ('S', 'S'),
            ('T', 'T'),
            ('W', 'W'),
            ('X', 'X'),
            ('Y', 'Y'),
            ('Z', 'Z'),
            ]
    context = {'abecedario': abecedario}
    
    return render(request, 'buscador_placas.html', context)


@csrf_exempt
def funcion_ajax(request):
    """
    """
    # print request
    # print request.POST.getlist('valor')
    if request.is_ajax() == True:
        req = {}
        letra = request.POST.getlist('valor')[0]
        vehiculos = serializers.serialize('json', Vehiculos.objects.filter(placa__startswith = letra ))
        req['mensaje'] = 'Correcto .... cargando datos '
        req['vehiculos'] = vehiculos 
        return JsonResponse(req, safe=False)


def buscador_placas_dos(request):
    abecedario = [
            ('-', '-'),
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E'),
            ('F', 'F'),
            ('G', 'G'),
            ('H', 'H'),
            ('I', 'I'),
            ('J', 'J'),
            ('K', 'K'),
            ('M', 'M'),
            ('N', 'N'),
            ('O', 'O'),
            ('P', 'P'),
            ('Q', 'Q'),
            ('R', 'R'),
            ('S', 'S'),
            ('T', 'T'),
            ('W', 'W'),
            ('X', 'X'),
            ('Y', 'Y'),
            ('Z', 'Z'),
            ]
    context = {'abecedario': abecedario}
    
    return render(request, 'buscador_placas_dos.html', context)


@csrf_exempt
def funcion_ajax_dos(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        letra = request.POST.getlist('valor')[0]
        vehiculos = Vehiculos.objects.filter(placa__startswith='A').all()
        vehiculos2 = json.dumps( [{'placa': o.placa, 'provincia': o.idprov.nombreprov} for o in vehiculos] )
        req['mensaje'] = 'Correcto .... cargando datos '
        req['vehiculos'] = vehiculos2 
        return JsonResponse(req, safe=False)




