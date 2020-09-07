from PricePredictionModel import model
from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .serializers import AvocadoPredictionSerializer


def predict_price(avocado_order):
    """
    Predict the average price of an avocado given the order details
    @param avocado_order: A dataframe containing the data about avocado orders to use for the prediction
    @return: A python dictionary containing {"price": avocado price prediction}
    """
    return {"price": model.get_model().predict(avocado_order)}


def get_prediction_page(request):
    """
    Returns the main page for the price prediction form
    @param request: A django request object wrapping a simple http get
    @return: An HTML page with the form for the avocado price prediction
    """
    template = loader.get_template("price_prediction/form-dumb.html")
    return HttpResponse(template.render())


@api_view(["GET", "POST"])
@parser_classes([JSONParser])
def get_price_prediction(request, format=None):
    """
    Receives data about an avocado and returns a price prediction for it
    @param request: A django request object containing the data about avocado orders to use for the prediction
    @param format: A request django format specifier
    @return: A json response containing the predicted average price of an avocado
    """
    serializer = AvocadoPredictionSerializer(data=request.data)

    if serializer.is_valid():
        return HttpResponse(JSONRenderer().render(predict_price(serializer.validated_data)))

    else:
        return HttpResponse(content="Error invalid request", status=400)
