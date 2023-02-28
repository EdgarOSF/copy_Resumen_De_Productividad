from django.db import models

from periodo.models import Periodo

class Itinerancia(models.Model):
    fecha = models.DateField('Fecha de Itinerancia')
    municipio_sede = models.CharField('Municipio Sede', max_length=200)
    poblado_sede = models.CharField('Poblado Sede', max_length=200)
    total_asuntos = models.DecimalField(max_digits=2, decimal_places=0)
    sentencias = models.DecimalField(max_digits=2, decimal_places=0)
    nucleos_poblacion = models.DecimalField(max_digits=2, decimal_places=0)
    fk_periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name='itinerancia_periodo')

    def __str__(self):
        return f'({self.fecha}) - {self.municipio_sede}'


class Municipio_Atendido(models.Model):
    nombre = models.CharField('Municipio', max_length=200)
    fk_itinerancia = models.ForeignKey(Itinerancia, on_delete=models.CASCADE, related_name='municipio_itinerancia')
