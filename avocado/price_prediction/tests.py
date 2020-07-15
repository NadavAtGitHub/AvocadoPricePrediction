import pytest
import pytest_django

from django.test import TestCase, RequestFactory

from price_prediction.models import AvocadoOrder
# Create your tests here.

@pytest.fixture
def rf():
    request_factory = RequestFactory()
    
    pass

def test_price_prediction_with_valid_data():
    pass

def test_price_prediction_with_missing_data():
    pass

def test_price_prediction_with_invalid_data():
    pass
