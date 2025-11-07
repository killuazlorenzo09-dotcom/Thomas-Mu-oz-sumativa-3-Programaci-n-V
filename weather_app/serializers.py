from rest_framework import serializers
from .models import CityTemperature

class CityTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityTemperature
        fields = '__all__'
        # 'last_updated' no debe ser editable, se actualiza solo
        read_only_fields = ('last_updated',)