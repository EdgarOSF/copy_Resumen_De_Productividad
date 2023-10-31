from django import forms

from tribunal.models import Tribunal


class TribunalForm(forms.ModelForm):
    nombre = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}), label='')
    estado = forms.ChoiceField(choices = Tribunal.ESTADO_CHOICES, label='', ) 
    municipio = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Municipio', 'class': 'form-control'}), label='')

    class Meta:
        model = Tribunal
        fields = ("id", "nombre", "estado", "municipio")
