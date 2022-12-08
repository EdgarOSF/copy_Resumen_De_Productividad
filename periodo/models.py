from django.db import models

from tribunal.models import Tribunal


class Periodo (models.Model):
    fecha_inicio_periodo = models.DateField(auto_now=False, auto_now_add=False)
    fecha_termino = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    fk_tribunal = models.ForeignKey(Tribunal, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Periodo'
        verbose_name = "periodo"
        ordering = ['-fecha_inicio_periodo']
        verbose_name_plural = "periodos"

        def __str__(self):
            return self.fecha_inicio_periodo

