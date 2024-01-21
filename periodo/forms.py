from django import forms

from . models import Periodo


class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ('fecha_inicio', 'fecha_termino', 'fk_tribunal')
        labels = {
            'fecha_inicio': 'Fecha de Inicio', 
            'fecha_termino': 'Fecha de Termino', 
            'fk_tribunal': 'Selecciona un tribunal'
        }
        widgets = {
            'fecha_inicio': forms.TextInput( attrs={ 'placeholder': 'dd/mm/yyyy', 'type': 'date' } ),
            'fecha_termino': forms.TextInput( attrs={ 'placeholder': 'dd/mm/yyyy', 'type': 'date' } ),
        }

