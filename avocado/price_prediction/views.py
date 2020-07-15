from django.shortcuts import render
from django.http import HttpRequest

from price_prediction.models import AvocadoOrder

# Create your views here.


def get_price_prediction(request: HttpRequest):
    """ Gets data about an avocado and returns a price prediction for it """
    # TODO:
    # 1. Data validation on request
    # 2. send to predict method
    # 3. return
    
    pass


def predict_price(avocado_order: AvocadoOrder):
    """" Stub method for price prediction """
    # TODO: implement
    return 1.0
