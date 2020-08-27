from django.http import HttpRequest, HttpResponse
from django.template import loader
import io

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import AvocadoPredictionSerializer
from PricePredictionModel import model

import pandas as pd
from datetime import datetime
import io

from PricePredictionModel import model
from django.http import HttpRequest, HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .serializers import AvocadoPredictionSerializer


# Create your views here.


@api_view(["GET", "POST"])
def get_price_prediction(request: HttpRequest):
    """ Gets data about an avocado and returns a price prediction for it """
    # TODO:
    # 1. Data validation on request
    # 2. send to predict method
    # 3. return
    request_body = io.BytesIO(request.body)
    data = JSONParser().parse(request_body)
    serializer = AvocadoPredictionSerializer(data=data)

    if serializer.is_valid():
        return HttpResponse(JSONRenderer().render(predict_price(serializer.validated_data)))

    else:
        return HttpResponse(content="Error invalid request", status=400)


def predict_price(avocado_order):
    """" Stub method for price prediction """
    # TODO: implement
    data = order_as_np_array(avocado_order)

    return {"price": model.get_model().predict(data)}


# TODO: move to serializer, add format specifier to model to maintain match
def order_as_np_array(avocado_order):
    avocado_data = pd.json_normalize(avocado_order)

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


def get_prediction_page(request):
    template = loader.get_template("price_prediction/form-dumb.html")
    return HttpResponse(template.render())
