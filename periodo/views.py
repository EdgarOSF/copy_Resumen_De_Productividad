from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from periodo.forms import PeriodoForm

from periodo.models import Periodo


class Index(ListView):
    model = Periodo
    template_name = 'periodo/index.html'


class PeriodoCreate(CreateView):
    model = Periodo
    form_class = PeriodoForm
    success_url = reverse_lazy('periodo:index')


class PeriodoUpdate(UpdateView):
    model = Periodo
    form_class = PeriodoForm
    success_url = reverse_lazy('periodo:index')
    template_name = 'periodo/periodo_update_form.html'


class PeriodoDetail(DetailView):
    model = Periodo
    context_object_name = 'periodo'


class PeriodoDelete(DeleteView):
    model = Periodo
    success_url = reverse_lazy('periodo:index')


