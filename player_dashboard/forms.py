# forms.py
from django import forms
from player_api.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ['createdBy']
       