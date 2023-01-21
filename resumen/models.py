from django.db import models

from periodo.models import Periodo


class Resumen (models.Model):
    sentencias = models.DecimalField(max_digits=4, decimal_places=0)
    convenios = models.DecimalField(max_digits=2, decimal_places=0)
    ingresos = models.DecimalField(max_digits=4, decimal_places=0)
    asuntos_en_tramite = models.DecimalField(max_digits=4, decimal_places=0)
    asuntos_turnados_a_sentencia = models.DecimalField(
        max_digits=4, decimal_places=0)
    archivados = models.DecimalField(max_digits=4, decimal_places=0)
    updated = models.DateTimeField(auto_now=True)
    fk_periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, related_name='periodo')

    class Meta:
        abstract = True


class Resumen_Recepcion (Resumen):

    class Meta:
        db_table = 'Resumen_Recepcion'
        ordering = ['-anio']
        verbose_name = "resumen_recepcion"

    def __str__(self):
        return str(self.anio)


class Resumen_Año (Resumen):
    anio = models.IntegerField(primary_key=True)
    itinerancias = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        db_table = 'Resumen_Por_Año'
        ordering = ['-anio']
        verbose_name = "resumen_a"
        verbose_name_plural = "resumenes"

    def __str__(self):
        return str(self.anio)


class Resumen_Entrega (Resumen):
    itinerancias = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        db_table = 'Resumen_Recepcion'
        ordering = ['-anio']
        verbose_name = "resumen_recepcion"

    def __str__(self):
        return str(self.anio)
