from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Tribunal


def tribunales_list(request):
    tribunales = Tribunal.objects.all()
    return render(request, 'tribunal/pages/list.html', {'tribunales': tribunales})


def tribunal_detail(request, id):
    tribunal = get_object_or_404(Tribunal, id=id)
    return render(request, 'tribunal/pages/detail.html', {'tribunal': tribunal})


class TribunalListView(ListView):
    queryset = Tribunal.objects.all()
    context_object_name = 'tribunales'
    template_name = 'tribunal/pages/list.html'


class TribunalCreateView(CreateView):
    model = Tribunal
    fields = ['nombre', 'ubicacion', 'estado']
    template_name = 'tribunal/forms/tribunal_form.html'
    success_url = reverse_lazy('tribunal:tribunal_list')
