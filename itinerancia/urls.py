from django.urls import path

from .views import ItineranciaDetailView

app_name = 'itinerancia'

urlpatterns = [
    path('<int:pk>/', ItineranciaDetailView.as_view(), name='itinerancia_detail'),
    
]