from django.db import models

from periodo.models import Periodo

class VisitaInspeccion (models.Model):
    fecha_inicio_insp = models.DateField(auto_now=False, auto_now_add=False)
    fecha_corte = models.DateField(auto_now=False, auto_now_add=False)
    resultado = models.CharField(max_length=200)
    fk_periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name='periodo')
