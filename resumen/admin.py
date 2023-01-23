from django.contrib import admin
from .models import Resumen_Año, Resumen_Entrega, Resumen_Recepcion


admin.site.register(Resumen_Año)
admin.site.register(Resumen_Recepcion)
admin.site.register(Resumen_Entrega)
