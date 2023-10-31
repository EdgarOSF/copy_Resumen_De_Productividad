from django.urls import path
from . import views

app_name = 'tribunal'

urlpatterns = [
    path('', views.TribunalListView.as_view(), name='index'),
    path('<int:id>/', views.tribunal_detail, name='detail'),
    path('new/', views.TribunalCreateView.as_view(), name='new'),
    path('update/<int:pk>', views.TribunalUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.delete_tribunal, name='delete'),
]
