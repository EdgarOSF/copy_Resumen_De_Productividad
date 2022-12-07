from django.db import models

from tribunal.models import Tribunal


class Periodo (models.Model):
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_termino = models.DateField(auto_now=False, auto_now_add=False)
    fk_tribunal = models.ForeignKey(Tribunal, on_delete=models.CASCADE)
