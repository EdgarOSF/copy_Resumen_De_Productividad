from django.contrib import admin
from .models import Tribunal


@admin.register(Tribunal)
class PostAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion', 'estado']
    list_filter = ['nombre', 'ubicacion', 'estado']
    search_fields = ['nombre', 'ubicacion', 'estado']
