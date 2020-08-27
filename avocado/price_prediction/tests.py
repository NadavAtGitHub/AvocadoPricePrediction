import pytest
from django.test import RequestFactory, Client

from .views import get_price_prediction


# Create your tests here.


@pytest.fixture
def rf():
    """
    A django RequestFactory for tests
    :return: a RequestFactory
    """
    request_factory = RequestFactory(content_type='application/json')
    return request_factory


@pytest.fixture
def client():
    client = Client()
    return client


def test_price_prediction_with_valid_data(rf):
    # Taken from data-set
    order = {
        'total_volume': '64236.62', 'num_plu_4046': '1036.74',
        'num_plu_4225': '54454.85', 'num_plu_4770': '48.16',
        'total_bags': '8696.87', 'small_bags': '8603.62',
        'large_bags': '93.25', 'extra_large_bags': '0.0',
        'type': 'conventional', 'year': '2015', 'region': 'Albany'
    }
    # TODO: automatically get correct url
    request = rf.post("/price_prediction/", data=order, content_type='application/json')
    response = get_price_prediction(request)
    assert response.status_code == 200


def permutations_of_missing_params():
    # TODO: move to function?
    valid_order = {
        'Total Volume': '64236.62', '4046': '1036.74',
        '4225': '54454.85', '4770': '48.16',
        'Total Bags': '8696.87', 'Small Bags': '8603.62',
        'Large Bags': '93.25', 'XLarge Bags': '0.0',
        'type': 'conventional', 'year': '2015', 'region': 'Albany'
    }
    permutations = [valid_order.copy() for i in range(len(valid_order.keys()))]

    for order, key in zip(permutations, valid_order.keys()):
        order.pop(key)

    return permutations
    # TODO: remove appropriate key from each dict


ALL_PERMUTATIONS_OF_MISSING_PARAMS = permutations_of_missing_params()


@pytest.mark.parametrize("order", ALL_PERMUTATIONS_OF_MISSING_PARAMS)
def test_price_prediction_with_missing_data(rf, order):
    # TODO: automatically get correct url
    request = rf.get("/price_prediction/", data=order, content_type='application/json')
    response = get_price_prediction(request)
    assert response.status_code == 400


def permutations_of_invalid_params():
    # TODO: move to function?
    valid_order = {
        'Total Volume': '64236.62', '4046': '1036.74',
        '4225': '54454.85', '4770': '48.16',
        'Total Bags': '8696.87', 'Small Bags': '8603.62',
        'Large Bags': '93.25', 'XLarge Bags': '0.0',
        'type': 'conventional', 'year': '2015', 'region': 'Albany'
    }
    permutations = [valid_order.copy() for i in range(len(valid_order.keys()))]

    for order, key in zip(permutations, valid_order.keys()):
        order[key] = key

    return permutations
    # TODO: remove appropriate key from each dict


ALL_PERMUTATIONS_OF_INVALID_PARAMS = permutations_of_missing_params()


@pytest.mark.parametrize("order", ALL_PERMUTATIONS_OF_INVALID_PARAMS)
def test_price_prediction_with_invalid_data(rf, order):
    # Taken from data-set
    # TODO: test every combination that should fail
    request = rf.get("/price_prediction/", data=order, content_type='application/json')
    response = get_price_prediction(request)
    assert response.status_code == 400
