from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from itinerancia.forms import ItineranciaForm

from .models import Itinerancia


class Index(ListView):
    queryset = Itinerancia.objects.all().order_by('id')
    context_object_name = 'itinerancias'
    template_name = 'itinerancia/index.html'


class ItineranciaDetailView(DetailView):
    model = Itinerancia
    context_object_name = 'itinerancia'
    # template_name = 'itinerancia/itinerancia_detail.html'


class ItineranciaCreateForm(CreateView):
    model = Itinerancia
    form_class = ItineranciaForm
    template_name = 'itinerancia/agregar_itinerancia_form.html'
    success_url = reverse_lazy('itinerancia:index')


class ItineranciaUpdateForm(UpdateView):
    model = Itinerancia
    form_class = ItineranciaForm
    template_name = 'itinerancia/editar_itinerancia_form.html'
    success_url = reverse_lazy('itinerancia:index')


class ItineranciaDeleteView(DeleteView):
    model = Itinerancia
    success_url = reverse_lazy('itinerancia:index')


