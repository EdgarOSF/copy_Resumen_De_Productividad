from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Tribunal


def tribunales_list(request):
    tribunales = Tribunal.objects.all()

    return render(request, 'tribunal/pages/list.html', {'tribunales': tribunales})


def tribunal_detail(request, id):
    tribunal = get_object_or_404(Tribunal, id=id)
    return render(request, 'tribunal/pages/detail.html', {'tribunal': tribunal})


class TribunalListView(ListView):
    """
    Alternative post list view
    """
    queryset = Tribunal.objects.all()
    context_object_name = 'tribunales'
    # paginate_by = 3
    template_name = 'tribunal/pages/list.html'
