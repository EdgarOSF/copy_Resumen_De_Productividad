from django.db import models

from periodo.models import Periodo


class Resumen (models.Model):
    anio = models.IntegerField(primary_key=True)
    sentencias = models.DecimalField(max_digits=4, decimal_places=0)
    itinerancias = models.DecimalField(max_digits=2, decimal_places=0)
    convenios = models.DecimalField(max_digits=2, decimal_places=0)
    ingresos = models.DecimalField(max_digits=4, decimal_places=0)
    asuntos_en_tramite = models.DecimalField(max_digits=4, decimal_places=0)
    asuntos_turnados_a_sentencia = models.DecimalField(max_digits=4, decimal_places=0)
    archivados = models.DecimalField(max_digits=4, decimal_places=0)
    updated = models.DateTimeField(auto_now=True)
    fk_periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name='perdiodo')

    class Meta:
        db_table = 'Resumen'
        ordering = ['-anio']
        verbose_name = "resumen"
        verbose_name_plural = "resumenes"

    def __str__(self):
        return str(self.anio)
