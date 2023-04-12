from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Itinerancia


class ItineranciaDetailView(DetailView):
    model = Itinerancia
    context_object_name = 'itinerancia'
