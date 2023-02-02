from django.contrib import admin
from .models import Resumen_Año, Resumen_Entrega, Resumen_Recepcion, Asuntos_En_Tramite_Anteriores, Asuntos_En_Tramite


admin.site.register(Resumen_Año)
admin.site.register(Resumen_Recepcion)
admin.site.register(Resumen_Entrega)
admin.site.register(Asuntos_En_Tramite_Anteriores)
admin.site.register(Asuntos_En_Tramite)
