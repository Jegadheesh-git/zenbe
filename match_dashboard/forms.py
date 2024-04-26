# forms.py
from django import forms
from match_api.models import Tournament, Competition, Match

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        exclude = ['createdBy']

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        exclude = ['createdBy']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        exclude = ['createdBy']
       