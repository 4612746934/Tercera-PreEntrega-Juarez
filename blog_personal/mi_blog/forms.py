from django import forms
from .models import Familiares, Amigos, Viajes

class FamiliaresForm(forms.ModelForm):
    class Meta:
        model = Familiares
        fields = '__all__'

class AmigosForm(forms.ModelForm):
    class Meta:
        model = Amigos
        fields = '__all__'

class ViajesForm(forms.ModelForm):
    class Meta:
        model = Viajes
        fields = '__all__'
