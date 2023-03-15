from django import forms
from AppAscenzi.models import *

class MinForm(forms.ModelForm):
    class Meta:
        model = Minorista
        fields = '__all__'

class MayForm(forms.ModelForm):
    class Meta:
        model = Mayorista
        fields = '__all__'

class PedForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'