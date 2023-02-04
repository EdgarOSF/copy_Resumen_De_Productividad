from django.db import models
from django.db.models import Value

from periodo.models import Periodo

""" Modelo Abstracto Resumen """
class Resumen (models.Model):
    sentencias = models.DecimalField(max_digits=4, decimal_places=0)
    convenios = models.DecimalField(max_digits=2, decimal_places=0)
    ingresos = models.DecimalField(max_digits=4, decimal_places=0)
    archivados = models.DecimalField(max_digits=4, decimal_places=0)
    asuntos_turnados_sentencia = models.DecimalField(max_digits=4, decimal_places=0)
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

    """ Asuntos Anteriores"""
    def get_primer_mes_asuntos_anteriores(self, resumen):
        mes = Asuntos_En_Tramite_Anteriores.asuntos_manager.get_primer_mes(resumen)
        return mes

    def get_ultimo_mes_asuntos_anteriores(self, resumen):
        mes = Asuntos_En_Tramite_Anteriores.asuntos_manager.get_ultimo_mes(resumen)
        return mes

    def diferencia_asuntos_anteriores(self, resumen):
        diferencia = Asuntos_En_Tramite_Anteriores.asuntos_manager.diferencia(resumen)
        return diferencia

    def porcentaje_asuntos_anteriores(self, resumen):
        porcentaje = Asuntos_En_Tramite_Anteriores.asuntos_manager.porcentaje(resumen)
        return porcentaje

    """ Asuntos En Tramite """
    def get_primer_mes_asuntos_en_tramite(self, resumen):
        mes = Asuntos_En_Tramite.asuntos_manager.get_primer_mes(resumen)
        return mes

    def get_ultimo_mes_asuntos_en_tramite(self, resumen):
        mes = Asuntos_En_Tramite.asuntos_manager.get_ultimo_mes(resumen)
        return mes

    def diferencia_asuntos_en_tramite(self, resumen):
        diferencia = Asuntos_En_Tramite.asuntos_manager.diferencia(resumen)
        return diferencia
    

    def porcentaje_asuntos_en_tramite(self, resumen):
        porcentaje = Asuntos_En_Tramite.asuntos_manager.porcentaje(resumen)
        return porcentaje


    """ Asuntos Turnados A Sentencia """
    def get_primer_mes_asuntos_turnados_a_sentencia(self, resumen):
        mes = Asuntos_En_Tramite.asuntos_manager.get_primer_mes(resumen)
        return mes

    def get_ultimo_mes_asuntos_turnados_a_sentencia(self, resumen):
        mes = Asuntos_En_Tramite.asuntos_manager.get_ultimo_mes(resumen)
        return mes

    def diferencia_asuntos_turnados_a_sentencia(self, resumen):
        diferencia = Asuntos_En_Tramite.asuntos_manager.diferencia(resumen)
        return diferencia
    

    def porcentaje_asuntos_turnados_a_sentencia(self, resumen):
        porcentaje = Asuntos_En_Tramite.asuntos_manager.porcentaje(resumen)
        return porcentaje

    def resumen_calculado(self, resumen):
        resumen_c = self.get_queryset()
        resumen_c = resumen_c.annotate(p_mes_asuntos_anteriores = Value(self.get_primer_mes_asuntos_anteriores(resumen)))
        resumen_c = resumen_c.annotate(u_mes_asuntos_anteriores = Value(self.get_ultimo_mes_asuntos_anteriores(resumen)))
        resumen_c = resumen_c.annotate(diferencia_asuntos_anteriores = Value(self.diferencia_asuntos_anteriores(resumen)))
        resumen_c = resumen_c.annotate(porcentaje_asuntos_anteriores = Value(self.porcentaje_asuntos_anteriores(resumen)))
        resumen_c = resumen_c.annotate(p_mes_asuntos_tramite = Value(self.get_primer_mes_asuntos_en_tramite(resumen)))
        resumen_c = resumen_c.annotate(u_mes_asuntos_tramite = Value(self.get_ultimo_mes_asuntos_en_tramite(resumen)))
        resumen_c = resumen_c.annotate(diferencia_asuntos_tramite = Value(self.diferencia_asuntos_en_tramite(resumen)))
        resumen_c = resumen_c.annotate(porcentaje_asuntos_tramite = Value(self.porcentaje_asuntos_en_tramite(resumen)))
        resumen_c = resumen_c.annotate(p_mes_asuntos_turnados = Value(self.get_primer_mes_asuntos_turnados_a_sentencia(resumen)))
        resumen_c = resumen_c.annotate(u_mes_asuntos_turnados = Value(self.get_ultimo_mes_asuntos_turnados_a_sentencia(resumen)))
        resumen_c = resumen_c.annotate(diferencia_asuntos_turnados = Value(self.diferencia_asuntos_turnados_a_sentencia(resumen)))
        resumen_c = resumen_c.annotate(porcentaje_asuntos_turnados = Value(self.porcentaje_asuntos_turnados_a_sentencia(resumen)))
        resumen_c = resumen_c.get(id=resumen.id)
        return resumen_c

""" Modelo Resumen_Año """
class Resumen_Año (Resumen):
    anio = models.DecimalField(max_digits=4, decimal_places=0)
    itinerancias = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True, default=0)
    fk_periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, related_name='resumen_anio_periodo')
    objects = models.Manager()
    asuntos = Resumen_Año_Manager()

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
        return self.get(fk_resumen=resumen, mes='ENE').cantidad

    def ultimo_mes(self, resumen):
        return self.get(fk_resumen=resumen, mes='DIC').cantidad


class AsuntosAnterioresManager(models.Manager):
    def get_queryset(self):
        return AsuntosAnterioresQuerySet(self.model, using=self._db)

    def get_primer_mes(self, resumen):
        return self.get_queryset().primer_mes(resumen)

    def get_ultimo_mes(self, resumen):
        return self.get_queryset().ultimo_mes(resumen)

    def diferencia(self, resumen):
        primer_mes = self.get_primer_mes(resumen)
        ultimo_mes = self.get_ultimo_mes(resumen)
        return ultimo_mes - primer_mes

    def porcentaje(self, resumen):
        diferencia = self.diferencia(resumen)
        primer_mes = self.get_primer_mes(resumen)
        porcentaje = diferencia / primer_mes
        return f'{porcentaje:.1%}'


""" Modelo Asuntos_En_Tramite_Anteriores """
class Asuntos_En_Tramite_Anteriores(models.Model):
    mes = models.CharField(max_length=15, choices=MESES)
    cantidad = models.DecimalField(max_digits=4, decimal_places=0)
    objects = models.Manager()
    asuntos_manager = AsuntosAnterioresManager()
    fk_resumen = models.ForeignKey(
        Resumen_Año, on_delete=models.CASCADE, related_name='asuntosAnteriores_resumen')


class AsuntosEnTramiteQuerySet(models.QuerySet):
    def primer_mes(self, resumen):
        return self.get(fk_resumen=resumen, mes='ENE').cantidad

    def ultimo_mes(self, resumen):
        return self.get(fk_resumen=resumen, mes='DIC').cantidad


class AsuntosEnTramiteManager(models.Manager):
    def get_queryset(self):
        return AsuntosEnTramiteQuerySet(self.model, using=self._db)

    def get_primer_mes(self, resumen):
        return self.get_queryset().primer_mes(resumen)

    def get_ultimo_mes(self, resumen):
        return self.get_queryset().ultimo_mes(resumen)

    def diferencia(self, resumen):
        primer_mes = self.get_primer_mes(resumen)
        ultimo_mes = self.get_ultimo_mes(resumen)
        return ultimo_mes - primer_mes

    def porcentaje(self, resumen):
        diferencia = self.diferencia(resumen)
        primer_mes = self.get_primer_mes(resumen)
        porcentaje = diferencia / primer_mes
        return f'{porcentaje:.1%}'


""" Modelo Asuntos_En_Tramite """
class Asuntos_En_Tramite(models.Model):
    mes = models.CharField(max_length=15, choices=MESES)
    cantidad = models.DecimalField(max_digits=4, decimal_places=0)
    objects = models.Manager()
    asuntos_manager = AsuntosEnTramiteManager()
    fk_resumen = models.ForeignKey(
        Resumen_Año, on_delete=models.CASCADE, related_name='asuntosTramite_resumen')


""" Modelo Asuntos_En_Tramite_Anteriores """
class Asuntos_En_Tramite_Anteriores(models.Model):
    mes = models.CharField(max_length=15, choices=MESES)
    cantidad = models.DecimalField(max_digits=4, decimal_places=0)
    objects = models.Manager()
    asuntos_manager = AsuntosAnterioresManager()
    fk_resumen = models.ForeignKey(
        Resumen_Año, on_delete=models.CASCADE, related_name='asuntosAnteriores_resumen')


class AsuntosTurnadosASentenciaQuerySet(models.QuerySet):
    def primer_mes(self, resumen):
        return self.get(fk_resumen=resumen, mes='ENE').cantidad

    def ultimo_mes(self, resumen):
        return self.get(fk_resumen=resumen, mes='DIC').cantidad


class AsuntosTurnadosASentenciaManager(models.Manager):
    def get_queryset(self):
        return AsuntosEnTramiteQuerySet(self.model, using=self._db)

    def get_primer_mes(self, resumen):
        return self.get_queryset().primer_mes(resumen)

    def get_ultimo_mes(self, resumen):
        return self.get_queryset().ultimo_mes(resumen)

    def diferencia(self, resumen):
        primer_mes = self.get_primer_mes(resumen)
        ultimo_mes = self.get_ultimo_mes(resumen)
        return ultimo_mes - primer_mes

    def porcentaje(self, resumen):
        diferencia = self.diferencia(resumen)
        primer_mes = self.get_primer_mes(resumen)
        porcentaje = diferencia / primer_mes
        return f'{porcentaje:.1%}'



""" Modelo Asuntos_Turnados_A_Sentencia """
class Asuntos_Turnados_A_Sentencia(models.Model):
    mes = models.CharField(max_length=15, choices=MESES)
    cantidad = models.DecimalField(max_digits=4, decimal_places=0)
    objects = models.Manager()
    asuntos_manager = AsuntosTurnadosASentenciaManager()
    fk_resumen = models.ForeignKey(
        Resumen_Año, on_delete=models.CASCADE, related_name='asuntosTurnados_resumen')
