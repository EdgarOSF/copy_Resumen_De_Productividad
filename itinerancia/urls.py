from django.urls import path

from .views import Index, ItineranciaCreateForm, ItineranciaDeleteView, ItineranciaDetailView, ItineranciaUpdateForm

app_name = 'itinerancia'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:pk>', ItineranciaDetailView.as_view(), name='detail'),
    path('create', ItineranciaCreateForm.as_view(), name='create'),
    path('edit/<int:pk>', ItineranciaUpdateForm.as_view(), name='edit'),
    path('delete/<int:pk>', ItineranciaDeleteView.as_view(), name='delete'),    
]