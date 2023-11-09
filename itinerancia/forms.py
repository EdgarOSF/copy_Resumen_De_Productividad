from django import forms

from itinerancia.models import Itinerancia


class ItineranciaForm(forms.ModelForm):
    # fecha = forms.DateField(
    #     label="Date of Birth",
    #     required=True,
    #     widget=forms.DateInput(format='%d/%m/%Y', attrs={"type": "date"}),
    #     input_formats=["%Y-%m-%d"]
    # )
    class Meta:
        model = Itinerancia
        fields = ('fecha', 'municipio_sede', 'poblado_sede', 'total_asuntos', 'sentencias', 'nucleos_poblacion', 'fk_periodo')
        labels = {'fk_periodo': 'Selecciona un periodo'}
        widgets = {
            'fecha': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'placeholder': 'dd-mm-yyyy', "type": "date"}
            )
        }
    