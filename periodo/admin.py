from django.contrib import admin
from .models import Periodo


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['fecha_inicio_periodo', 'fecha_termino', 'fk_tribunal']
    list_filter = ['fecha_inicio_periodo', 'fecha_termino', 'fk_tribunal']
    search_fields = ['fecha_inicio_periodo', 'fecha_termino', 'fk_tribunal']
