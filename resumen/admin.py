from django.contrib import admin
from .models import Resumen_Año, Resumen_Entrega, Resumen_Recepcion, Asuntos_En_Tramite_Anteriores, Asuntos_En_Tramite, Asuntos_Turnados_A_Sentencia


admin.site.register(Resumen_Recepcion)
admin.site.register(Resumen_Entrega)


@admin.register(Asuntos_En_Tramite_Anteriores)
class AsuntosEnTramiteAnterioresAdmin(admin.ModelAdmin):
    list_display = ['mes', 'cantidad', 'fk_resumen']
    list_filter = ['fk_resumen']
    search_fields = ['mes', 'fk_resumen']


@admin.register(Asuntos_En_Tramite)
class AsuntosEnTramiteAdmin(admin.ModelAdmin):
    list_display = ['mes', 'cantidad', 'fk_resumen']
    list_filter = ['fk_resumen']
    search_fields = ['mes', 'fk_resumen']

@admin.register(Asuntos_Turnados_A_Sentencia)
class AsuntosTurnadosASentenciaAdmin(admin.ModelAdmin):
    list_display = ['mes', 'cantidad', 'fk_resumen']
    list_filter = ['fk_resumen']
    search_fields = ['mes', 'fk_resumen']


@admin.register(Resumen_Año)
class ResumenAñoAdmin(admin.ModelAdmin):
    list_display = ['fk_periodo','anio', 'sentencias', 'asuntos_turnados_sentencia', 'convenios', 'ingresos', 'archivados', 'itinerancias']
