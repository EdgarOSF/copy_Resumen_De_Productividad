from django.urls import path

from .views import VisitaInspeccionDetailView

app_name = 'visita'

urlpatterns = [
    path('<int:pk>/', VisitaInspeccionDetailView.as_view(), name='visita_detail'),
    
]