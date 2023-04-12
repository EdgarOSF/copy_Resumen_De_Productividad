from django.contrib import admin
from .models import Itinerancia, Municipio_Atendido

admin.site.register(Itinerancia)

@admin.register(Municipio_Atendido)
class MunicipioAtendidoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fk_itinerancia']
    search_fields = ['nombre', 'fk_itinerancia__municipio_sede']