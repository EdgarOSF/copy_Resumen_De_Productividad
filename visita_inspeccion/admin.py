from django.contrib import admin
from .models import VisitaInspeccion


@admin.register(VisitaInspeccion)
class VisitaInspeccionAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'fecha_inicio_insp', 'fecha_corte', 'resultado', 'fk_periodo']
    list_filter = ['fecha', 'fecha_inicio_insp', 'fecha_corte', 'resultado', 'fk_periodo']
    search_fields = ['fecha', 'fecha_inicio_insp', 'fecha_corte', 'resultado', 'fk_periodo']
