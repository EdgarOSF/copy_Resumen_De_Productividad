from django.urls import path

from .views import ResumenListView, ResumenTUADetailView

app_name = 'resumen'

urlpatterns = [
    path('a/', ResumenListView.as_view(), name='list'),
    path('<int:anio>/', ResumenTUADetailView.as_view(), name='resumen-detail'),
]
