from django.db import models

from periodo.models import Periodo

class VisitaInspeccion (models.Model):
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    fecha_inicio_insp = models.DateField(auto_now=False, auto_now_add=False)
    fecha_corte = models.DateField(auto_now=False, auto_now_add=False)
    resultado = models.CharField(max_length=200)
    fk_periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name='periodo')

    class Meta:
        db_table = 'VisitaInspeccion'
        verbose_name = "visita"
        verbose_name_plural = "visitas"

    def __str__(self):
        return self.fecha
