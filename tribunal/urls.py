from django.urls import path
from . import views

app_name = 'tribunal'

urlpatterns = [
    path('', views.TribunalListView.as_view(), name='list'),
    path('<int:id>/', views.tribunal_detail, name='detail'),
    path('new/', views.TribunalCreateView.as_view(), name='post'),
]
