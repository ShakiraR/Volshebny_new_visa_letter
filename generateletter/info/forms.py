from django import forms
from .models import Visaletters

class visaForm(forms.ModelForm):
    class Meta():
        model = Visaletters
        fields ='__all__'
        


