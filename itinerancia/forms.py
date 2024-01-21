from django import forms

from itinerancia.models import Itinerancia


class ItineranciaForm(forms.ModelForm):
    class Meta:
        model = Itinerancia
        fields = ('fecha', 'municipio_sede', 'poblado_sede', 'total_asuntos', 'sentencias', 'nucleos_poblacion', 'fk_periodo')
        labels = {'fk_periodo': 'Selecciona un periodo'}
        widgets = {
            'fecha': forms.TextInput( attrs={ 'placeholder': 'dd/mm/yyyy', 'type': 'date' } ),
        }
    