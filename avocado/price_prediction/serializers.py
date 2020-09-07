from rest_framework import serializers
import pandas as pd
from datetime import datetime
from .models import AvocadoOrder


class AvocadoPredictionSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        """
        Validate the data and return the data formatted as pandas dataframe
        @param attrs: A python dict of the attributes of the price prediction params object
        @return: A pandas dataframe containing  the price prediction params
        """
        avocado_data = pd.json_normalize(attrs)

        # Day of year, as int
        avocado_data["day_of_year"] = datetime.now().strftime("%-j")
        avocado_data["small_bags_of_total"] = avocado_data["small_bags"] / avocado_data["total_bags"]
        avocado_data["large_bags_of_total"] = avocado_data["large_bags"] / avocado_data["total_bags"]
        avocado_data["extra_large_bags_of_total"] = avocado_data["extra_large_bags"] / avocado_data["total_bags"]

        avocado_data["location_volumes"] = avocado_data["num_plu_4046"] + avocado_data["num_plu_4225"] + \
                                           avocado_data["num_plu_4770"]
        avocado_data["num_plu_4046_of_location_volume"] = avocado_data["num_plu_4046"] / avocado_data["location_volumes"]
        avocado_data["num_plu_4225_of_location_volume"] = avocado_data["num_plu_4225"] / avocado_data["location_volumes"]
        avocado_data["num_plu_4770_of_location_volume"] = avocado_data["num_plu_4770"] / avocado_data["location_volumes"]
        avocado_data["location_of_total_volume"] = avocado_data["location_volumes"] / avocado_data["total_volume"]

        return avocado_data

    class Meta:
        model = AvocadoOrder
        fields = ["id", "total_volume", "type", "num_plu_4046", "num_plu_4225", "num_plu_4770", "total_bags",
                  "small_bags", "large_bags", "extra_large_bags", "region", "year"]
        validators = []
