from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Resumen_Año, Asuntos_En_Tramite_Anteriores, Asuntos_En_Tramite, Asuntos_Turnados_A_Sentencia

import json


class ResumenListView(ListView):

    model = Resumen_Año
    template_name = 'dashboard/base.html'

    def get_context_data(self, **kwargs):
        print(self.request)
        context = super().get_context_data(**kwargs)
        # context['resumen_porcentaje'] = Resumen_Año.asuntos_anteriores.porcentaje_asuntos_anteriores()
        context['resumenes'] = Resumen_Año.objects.filter(fk_periodo=1)
        print(context['resumenes'])
        return context


class ResumenTUADetailView(DetailView):

    model = Resumen_Año
    context_object_name = 'resumen'
    template_name = 'dashboard/resumen_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        props = Resumen_Año.asuntos.resumen_calculado(self.get_object())
        asuntos_anteriores = Asuntos_En_Tramite_Anteriores.objects.filter(fk_resumen = self.get_object())
        asuntos_tramite = Asuntos_En_Tramite.objects.filter(fk_resumen = self.get_object())
        asuntos_turnados = Asuntos_Turnados_A_Sentencia.objects.filter(fk_resumen = self.get_object())
        context.update(
            {
                'resumen': props, 
                'asuntos_anteriores': asuntos_anteriores,
                'asuntos_tramite': asuntos_tramite,
                'asuntos_turnados': asuntos_turnados
            })
        return context
