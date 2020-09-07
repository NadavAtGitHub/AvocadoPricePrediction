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
    return {"price": model.get_model().predict(avocado_order)}


def get_prediction_page(request):
    template = loader.get_template("price_prediction/form-dumb.html")
    return HttpResponse(template.render())
