from django import forms
from .models import Annonce


class CreationAnnonce(forms.ModelForm):

    class Meta:
        model = Annonce
        fields = ('titre', 'prix', 'photo', 'categorie', 'description',)
