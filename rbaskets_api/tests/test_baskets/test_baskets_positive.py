import pytest

from api_endpoints.baskets_api import BaseBasketsApi
from data.baskets.get_baskets_positive import *
from data.baskets.create_basket_positive import *
from utils.helper import *


@pytest.fixture(name='create_basket_positive', params=data_create_basket_positive, ids=create_basket_positive_ids)
def data_create_basket_positive(request):
    yield request.param


@pytest.mark.run(order=1)
def test_create_basket_positive(create_basket_positive):
    bba = BaseBasketsApi(create_basket_positive.session_uid)
    response = bba.create_basket(create_basket_positive.parameter, create_basket_positive.request_body)
    assert_response_code(response, 201)
    assert_response_content(load_response_content(response), create_basket_positive.expected_response,
                            check_format=True)


@pytest.fixture(name='get_baskets_positive', params=data_get_baskets_positive, ids=get_baskets_positive_ids)
def data_get_baskets_positive(request):
    yield request.param


@pytest.mark.run(order=2)
def test_get_baskets_positive(get_baskets_positive):
    bba = BaseBasketsApi(get_baskets_positive.session_uid)
    response = bba.get_baskets()
    assert_response_code(response, 200)
    assert_response_content(load_response_content(response), get_baskets_positive.expected_response,
                            check_format=False)


@pytest.fixture(name='get_baskets_max_skip_positive', params=data_get_baskets_max_skip_positive,
                ids=get_baskets_max_skip_positive_ids)
def data_get_baskets_max_skip_positive(request):
    yield request.param


@pytest.mark.run(order=3)
def test_get_baskets_max_skip_positive(get_baskets_max_skip_positive):
    bba = BaseBasketsApi(get_baskets_max_skip_positive.session_uid)
    response = bba.get_baskets_max_skip(get_baskets_max_skip_positive.additional_data['max'],
                                        get_baskets_max_skip_positive.additional_data['skip'])
    assert_response_code(response, 200)
    assert_response_content(load_response_content(response), get_baskets_max_skip_positive.expected_response,
                            check_format=False)


@pytest.fixture(name='get_baskets_search_query_positive', params=data_get_baskets_search_query_positive,
                ids=get_baskets_search_query_positive_ids)
def data_get_baskets_search_query_positive(request):
    yield request.param


@pytest.mark.run(order=4)
def test_get_baskets_search_query_positive(get_baskets_search_query_positive):
    bba = BaseBasketsApi(get_baskets_search_query_positive.session_uid)
    response = bba.get_baskets_search_query(get_baskets_search_query_positive.additional_data['search_query'])
    assert_response_code(response, 200)
    assert_response_content(load_response_content(response), get_baskets_search_query_positive.expected_response,
                            check_format=False)
