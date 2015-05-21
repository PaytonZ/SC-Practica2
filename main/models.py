
from django.db import models

class Edificio(models.Model):
    TIPO_EDIFICIO = (
        (1, 'Colegio'),

    )
    nombre = models.CharField(max_length=800)
    descripcion = models.CharField(max_length=800)
    tipo_via = models.CharField(max_length=800)
    nombre_via = models.CharField(max_length=800)
    numero = models.CharField(max_length=800)
    localidad = models.CharField(max_length=800)
    provincia = models.CharField(max_length=800)
    codigo_postal = models.CharField(max_length=800)
    barrio = models.CharField(max_length=800)
    distrito = models.CharField(max_length=800)
    telefono = models.CharField(max_length=800)
    latitud = models.FloatField()
    longitud = models.FloatField()
    tipo = models.IntegerField(default=1 , choices=TIPO_EDIFICIO)
