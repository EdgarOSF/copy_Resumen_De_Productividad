from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from tribunal.forms import TribunalForm

from .models import Tribunal


def tribunal_detail(request, id):
    tribunal = get_object_or_404(Tribunal, id=id)
    return render(request, 'tribunal/pages/detail.html', {'tribunal': tribunal})


class TribunalListView(ListView):
    queryset = Tribunal.objects.all()
    context_object_name = 'tribunales'
    template_name = 'tribunal/pages/index.html'


class TribunalCreateView(CreateView):
    model = Tribunal
    form_class = TribunalForm
    template_name = 'tribunal/forms/agregar_tribunal_form.html'
    success_url = reverse_lazy('tribunal:index')
    success_message = "%(nombre)s was created successfully"


def delete_tribunal(request, pk):
    record = Tribunal.objects.get(id=pk)
    record.delete()
    messages.info(request, 'Eliminado Correctamente')
    return redirect('/tribunal')


class TribunalUpdateView(UpdateView):
    model = Tribunal
    form_class = TribunalForm
    template_name = 'tribunal/forms/modificar_tribunal.html'
    success_url = reverse_lazy('tribunal:index')
