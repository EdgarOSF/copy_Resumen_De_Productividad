from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import VisitaInspeccion


class VisitaInspeccionDetailView(DetailView):
    model = VisitaInspeccion
    template_name = 'visita_inspeccion/visitainspeccion_detail.html'
    context_object_name = 'visita'
