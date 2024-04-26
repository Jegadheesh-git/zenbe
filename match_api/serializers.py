from rest_framework import serializers
from .models import *

class TournamentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class CompetitionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

class MatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

    def validate(self, data):
        squadA = data.get('squadA', None)
        if squadA is not None and len(squadA) < 11:
            raise serializers.ValidationError("SquadA must have at least 11 players.")

        return data

class StadiumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        