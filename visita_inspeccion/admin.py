from django.contrib import admin
from .models import VisitaInspeccion


@admin.register(VisitaInspeccion)
class VisitaInspeccionAdmin(admin.ModelAdmin):
    list_display = ['fecha_realizacion', 'fecha_inicio_periodo_insp', 'fecha_corte_periodo_insp','realizo', 'resultado', 'fk_periodo']
    list_filter = ['fecha_realizacion', 'fecha_inicio_periodo_insp', 'fecha_corte_periodo_insp', 'resultado', 'fk_periodo']
    search_fields = ['fecha_realizacion', 'fecha_inicio_periodo_insp', 'fecha_corte_periodo_insp', 'resultado', 'fk_periodo']
