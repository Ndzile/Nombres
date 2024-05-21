from django import forms
from .models import MembreBureauRegional, Region, CoordinationLocale, Jeune


class MembreBureauRegionalForm(forms.ModelForm):
    nom = forms.CharField(label="Nom", max_length=255, required=True)
    prenom = forms.CharField(label="Prénom", max_length=255, required=True)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label="Région")

    class Meta:
        model = MembreBureauRegional
        fields = ['nom', 'prenom', 'region']


class MembreCoordinationLocaleForm(forms.ModelForm):
    nom = forms.CharField(label="Nom", max_length=255, required=True)
    prenom = forms.CharField(label="Prénom", max_length=255, required=True)
    coordination_locale = forms.ModelChoiceField(queryset=CoordinationLocale.objects.all(), label="Coordination Locale")

    class Meta:
        model = Jeune
        fields = ['nom', 'prenom', 'coordination_locale']

    def __init__(self, *args, user=None, **kwargs):
        super(MembreCoordinationLocaleForm, self).__init__(*args, **kwargs)
        if user:
            # Filter coordination locales based on the user's region
            self.fields['coordination_locale'].queryset = CoordinationLocale.objects.filter(region=user.coordination_locale.region)

