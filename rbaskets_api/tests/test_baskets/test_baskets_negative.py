import pytest

from api_endpoints.baskets_api import BaseBasketsApi
from data.baskets.get_baskets_negative import *
from data.baskets.create_basket_negative import *
from utils.helper import *


@pytest.fixture(name='create_basket_negative', params=data_create_basket_negative, ids=create_basket_negative_ids)
def data_create_basket_negative(request):
    yield request.param


@pytest.mark.run(order=5)
def test_create_basket_negative(create_basket_negative):
    bba = BaseBasketsApi(create_basket_negative.session_uid)
    response = bba.create_basket(create_basket_negative.parameter, create_basket_negative.request_body)
    assert_response_code(response, create_basket_negative.expected_http_code)
    assert response['content'].startswith(create_basket_negative.expected_response)


@pytest.fixture(name='get_baskets_negative', params=data_get_baskets_negative, ids=get_baskets_negative_ids)
def data_get_baskets_negative(request):
    yield request.param


@pytest.mark.run(order=6)
def test_get_baskets_negative(get_baskets_negative):
    bba = BaseBasketsApi(get_baskets_negative.session_uid)
    response = bba.get_baskets()
    assert_response_code(response, get_baskets_negative.expected_http_code)
