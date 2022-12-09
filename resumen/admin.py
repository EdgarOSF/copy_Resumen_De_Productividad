from django.contrib import admin
from .models import Resumen


@admin.register(Resumen)
class ResumenAdmin(admin.ModelAdmin):
    list_display = ['anio', 'sentencias', 'itinerancias', 'convenios', 'ingresos',
                    'asuntos_en_tramite', 'asuntos_turnados_a_sentencia', 'archivados', 'updated', 'fk_periodo']
    list_filter = ['anio', 'sentencias', 'itinerancias', 'convenios', 'ingresos',
                   'asuntos_en_tramite', 'asuntos_turnados_a_sentencia', 'archivados', 'updated', 'fk_periodo']
    search_fields = ['anio', 'sentencias', 'itinerancias', 'convenios', 'ingresos',
                     'asuntos_en_tramite', 'asuntos_turnados_a_sentencia', 'archivados', 'updated', 'fk_periodo']
