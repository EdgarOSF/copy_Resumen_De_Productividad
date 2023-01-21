from django.db import models

from periodo.models import Periodo


class VisitaInspeccion (models.Model):
    fecha_realizacion = models.DateField(auto_now=False, auto_now_add=False)
    fecha_inicio_periodo_insp = models.DateField(auto_now=False, auto_now_add=False)
    fecha_corte_periodo_insp = models.DateField(auto_now=False, auto_now_add=False)
    resultado = models.CharField(max_length=200, blank=True, null=True)
    realizo = models.CharField(max_length=200, blank=True, null=True)
    duracion = models.DecimalField(decimal_places=1, max_digits=3, blank=True, null=True)
    observaciones = models.CharField(max_length=300, blank=True, null=True)
    fk_periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name='periodo')

    class Meta:
        db_table = 'VisitaInspeccion'
        verbose_name = "visita"
        verbose_name_plural = "visitas"

    def __str__(self):
        return f'{str(self.fecha_inicio_periodo_insp)} - {str(self.fecha_corte_periodo_insp)}'
