from django import forms
from AppAscenzi.models import Minorista

class MinForm(forms.ModelForm):
    class Meta:
        model = Minorista
        fields = '__all__'
