# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.conf import settings
import os
from django.http import HttpResponse
from main.models import Edificio
import unicodedata
import facebook
from test.test_multiprocessing import latin
from django.core import serializers
from django.db import transaction

def main(request):
    return render_to_response('index.html', {"foo": "bar"})

@transaction.atomic
def process_data(request):
    import csv
    files = {"bomberos.csv", "colegios.csv"  , "gasolineras.csv" , "idiomas.csv" , "oficinaempleo.csv", "piscinas.csv" , "polideportivos.csv" }
    data = {}
    data['error'] = 200
    try :
        for file1 in files:
            with open(os.path.join(settings.FILES_ROOT, file1)) as f:
                reader = csv.DictReader(f, delimiter=';')
                line = 0
                for row in reader:
                    for r in row:
                        row[r] = unicode(strip_accents(row[r]))
                    # print row
                    if(line == 0):
                        line = 1
                        continue
                    Edificio.objects.create(nombre=row['NOMBRE'], descripcion=row['DESCRIPCION'],
                    tipo_via=row['CLASE-VIAL'], nombre_via=row['NOMBRE-VIA'],
                    localidad=row['LOCALIDAD'] , provincia=row['PROVINCIA'],
                    numero=row['NUM'], codigo_postal=row['CODIGO-POSTAL'],
                    barrio=row['BARRIO'], distrito=row['DISTRITO'],
                    latitud=float(row['LATITUD']), longitud=float(row['LONGITUD']), telefono=row['TELEFONO'])
        data['num_data'] = Edificio.objects.count()
    except Exception as e:
        data['error'] = 500
        data['error_cause'] = e
            
    return HttpResponse(json.dumps(data), content_type="application/json")
    
    
def facebook_login(request):
    data = {}
    graph = facebook.GraphAPI(settings.FACEBOOK_STATIC_ACCESS_TOKEN)
    jsondata = {}
    jsondata['q'] = 'coffee'
    jsondata['type'] = 'place'
    jsondata['center'] = '37.76,-122.427'
    jsondata['distance'] = '1000'
    # q="coffee", type="place" ,center=37.76,-122.427, distance=1000, ""
    data['data'] = graph.request("search", jsondata , None)['data']
    return HttpResponse(json.dumps(data), content_type="application/json")
    

def obtain_data(request):
    data = {}
    parameters = request.GET
    if 'x' and 'y' and 'distance' in parameters:
        sensibility = 0.015
        x = float(parameters['x'])
        y = float(parameters['y'])
        distance = parameters['distance']
        graph = facebook.GraphAPI(settings.FACEBOOK_STATIC_ACCESS_TOKEN)
        jsondata = {}
        jsondata['q'] = ''
        jsondata['type'] = 'place'
        jsondata['locale'] = 'es_ES'
        center = str(x) + "," + str(y)
        print center
        jsondata['center'] = center 
        jsondata['distance'] = '3000'
        data['facebook'] = graph.request("search", jsondata , None)['data']
        data['madrid'] = json.loads(serializers.serialize('json', Edificio.objects.filter(latitud__range=(x - sensibility, x + sensibility) , longitud__range=(y - sensibility, y + sensibility))))
    return HttpResponse(json.dumps(data), content_type="application/json")
    

def strip_accents(s):
    s = s.decode("cp1252")  # decode from cp1252 encoding instead of the implicit ascii encoding used by unicode()
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
    return s

def short_url(request):
    import osa
    parameters = request.GET
    data = {}
    if 'url' in parameters:
        print parameters['url']
        wsdlFile = 'http://bn.gy/API.asmx?WSDL'
        cl = osa.Client(wsdlFile)
        response = str(cl.service.CreateUrl(real_url=str(parameters['url'])))
        data['url'] = response[str(response).find("ShortenedUrl"):str(response).find("CreateDate")][15:][:18]                    
    return HttpResponse(json.dumps(data), content_type="application/json")
