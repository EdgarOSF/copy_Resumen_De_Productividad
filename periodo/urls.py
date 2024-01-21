from django.urls import path

from periodo.views import Index, PeriodoCreate, PeriodoDelete, PeriodoDetail, PeriodoUpdate

app_name = 'periodo'


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<int:pk>', PeriodoDetail.as_view(), name='detail'),
    path('create', PeriodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', PeriodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', PeriodoUpdate.as_view(), name='update'),
]
