from django.urls import path
from . import views

app_name = 'tribunal'

urlpatterns = [
    path('', views.TribunalListView.as_view(), name='tribunal_list'),
    path('<int:id>/', views.tribunal_detail, name='tribunal_detail'),
]
