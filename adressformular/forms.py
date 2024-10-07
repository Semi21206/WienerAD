from django import forms
from .models import Adresse

class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['strasse', 'hausnummer', 'plz', 'ort', 'bundesland']
        widgets = {
            'strasse': forms.TextInput(attrs={'placeholder': 'Straße eingeben'}),
            'hausnummer': forms.TextInput(attrs={'placeholder': 'Hausnummer'}),
            'plz': forms.TextInput(attrs={'placeholder': 'PLZ'}),
            'ort': forms.TextInput(attrs={'placeholder': 'Ort'}),
            'bundesland': forms.TextInput(attrs={'placeholder': 'Bundesland'}),
        }
