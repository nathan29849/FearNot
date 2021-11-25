from rest_framework import serializers
from .models import Calc, TotalData

class CalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calc
        fields = ('title', 'body', 'rate', 'count')

class TotalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalData
        exclude = ('first_death', 'first_conf', 'second_death', 'second_conf', 'third_death', 'third_conf')