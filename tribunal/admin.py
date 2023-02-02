from django.contrib import admin
from .models import Tribunal


@admin.register(Tribunal)
class PostAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'municipio', 'estado']
    list_filter = ['nombre', 'municipio', 'estado']
    search_fields = ['nombre', 'municipio', 'estado']
