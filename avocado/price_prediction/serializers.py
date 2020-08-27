from rest_framework import serializers
from .models import AvocadoOrder


class AvocadoPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvocadoOrder
        fields = ["id", "total_volume", "type", "num_plu_4046", "num_plu_4225", "num_plu_4770", "total_bags",
                  "small_bags", "large_bags", "extra_large_bags", "region", "year"]

