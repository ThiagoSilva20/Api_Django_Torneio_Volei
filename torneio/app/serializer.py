from .models import Teams, Athletes, Coach
from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['id', 'name_team', 'coaches']

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athletes
        fields = ['id', 'full_name', 'email', 'birth_date', 'federado', 'teams', 'cpf', 'rg']

class CoachSerializer(serializers.ModelField):
    class Meta:
        model = Coach
        fields = ['full_name', 'email', 'birth_date', 'team', 'cpf', 'rg']
