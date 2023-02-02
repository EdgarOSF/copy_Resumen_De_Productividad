from django.db import models

from periodo.models import Periodo

""" Modelo Abstracto Resumen """
class Resumen (models.Model):
    sentencias = models.DecimalField(max_digits=4, decimal_places=0)
    convenios = models.DecimalField(max_digits=2, decimal_places=0)
    ingresos = models.DecimalField(max_digits=4, decimal_places=0)
    archivados = models.DecimalField(max_digits=4, decimal_places=0)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


""" Modelo Resumen_Recepcion """
class Resumen_Recepcion (Resumen):
    fk_periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, related_name='resumen_recepcion_periodo')

    class Meta:
        db_table = 'Resumen_Recepcion'
        verbose_name = "resumen_recepcion"

    def __str__(self):
        return str(self.id)


class Resumen_Año_Manager(models.Manager):
    def diferencia_asuntos_anteriores(self):
        resumen = self.get_queryset()[0]
        return Asuntos_En_Tramite_Anteriores.objects.diferencia(resumen)

    def porcentaje_asuntos_anteriores(self):
        resumen = self.get_queryset()[0]
        return Asuntos_En_Tramite_Anteriores.objects.porcentaje(resumen)

    def diferencia_asuntos_en_tramite(self):
        resumen = self.get_queryset()[0]
        return Asuntos_En_Tramite.objects.diferencia(resumen)

    def porcentaje_asuntos_en_tramite(self):
        resumen = self.get_queryset()[0]
        return Asuntos_En_Tramite.objects.porcentaje(resumen)


""" Modelo Resumen_Año """
class Resumen_Año (Resumen):
    anio = models.DecimalField(max_digits=4, decimal_places=0)
    itinerancias = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True, default=0)
    fk_periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, related_name='resumen_anio_periodo')
    objects = models.Manager()
    asuntos_anteriores = Resumen_Año_Manager()
    asuntos_en_tramite = Resumen_Año_Manager()

    class Meta:
        db_table = 'Resumen_Por_Año'
        ordering = ['-anio']
        verbose_name = "resumen_a"
        verbose_name_plural = "resumenes_por_año"

    def __str__(self):
        return str(self.anio)


""" Modelo Resumen_Entrega """
class Resumen_Entrega (Resumen):
    itinerancias = models.DecimalField(max_digits=2, decimal_places=0)
    fk_periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, related_name='resumen_entrega_periodo')

    class Meta:
        db_table = 'Resumen_Entrega'
        verbose_name = "resumen_entrega"

    def __str__(self):
        return str(self.id)


MESES = [
    ('ENE', 'Enero'),
    ('FEB', 'Febrero'),
    ('MAR', 'Marzo'),
    ('ABR', 'Abril'),
    ('MAY', 'Mayo'),
    ('JUN', 'Junio'),
    ('JUL', 'Julio'),
    ('AGO', 'Agosto'),
    ('SEP', 'Septiembre'),
    ('OCT', 'Octubre'),
    ('NOV', 'Noviembre'),
    ('DIC', 'Diciembre'),
]


class AsuntosAnterioresQuerySet(models.QuerySet):
    def primer_mes(self, resumen):
        return self.filter(fk_resumen=resumen, mes='ENE')[0].cantidad

    def ultimo_mes(self, resumen):
        return self.filter(fk_resumen=resumen, mes='DIC')[0].cantidad


class AsuntosAnterioresManager(models.Manager):
    def get_queryset(self):
        return AsuntosAnterioresQuerySet(self.model, using=self._db)

    def diferencia(self, resumen):
        primer_mes = self.get_queryset().primer_mes(resumen)
        ultimo_mes = self.get_queryset().ultimo_mes(resumen)
        return ultimo_mes - primer_mes

    def porcentaje(self, resumen):
        diferencia = self.diferencia(resumen)
        primer_mes = self.get_queryset().primer_mes(resumen)
        porcentaje = diferencia / primer_mes
        porcentaje *= 100
        return f'{porcentaje:.1f} %'


""" Modelo Asuntos_En_Tramite_Anteriores """
class Asuntos_En_Tramite_Anteriores(models.Model):
    mes = models.CharField(max_length=15, choices=MESES)
    cantidad = models.DecimalField(max_digits=4, decimal_places=0)
    objects = AsuntosAnterioresManager()
    fk_resumen = models.ForeignKey(
        Resumen_Año, on_delete=models.CASCADE, related_name='asuntosAnteriores_resumen')


class AsuntosEnTramiteQuerySet(models.QuerySet):
    def primer_mes(self, resumen):
        return self.filter(fk_resumen=resumen, mes='ENE')[0].cantidad

    def ultimo_mes(self, resumen):
        return self.filter(fk_resumen=resumen, mes='DIC')[0].cantidad


class AsuntosEnTramiteManager(models.Manager):
    def get_queryset(self):
        return AsuntosEnTramiteQuerySet(self.model, using=self._db)

    def diferencia(self, resumen):
        primer_mes = self.get_queryset().primer_mes(resumen)
        ultimo_mes = self.get_queryset().ultimo_mes(resumen)
        return ultimo_mes - primer_mes

    def porcentaje(self, resumen):
        diferencia = self.diferencia(resumen)
        primer_mes = self.get_queryset().primer_mes(resumen)
        porcentaje = diferencia / primer_mes
        return f'{porcentaje:.1%}'


""" Modelo Asuntos_En_Tramite """
class Asuntos_En_Tramite(models.Model):
    mes = models.CharField(max_length=15, choices=MESES)
    cantidad = models.DecimalField(max_digits=4, decimal_places=0)
    objects = AsuntosEnTramiteManager()
    fk_resumen = models.ForeignKey(
        Resumen_Año, on_delete=models.CASCADE, related_name='asuntosTramite_resumen')
