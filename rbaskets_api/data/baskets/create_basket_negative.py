from data import tokens
from utils.data import Data

master_token = tokens.tokens.master_token

create_basket_negative_ids = ['basket_name_already_exists', 'reserved_name_as_basket_name', 'negative_capacity',
                              'too_large_capacity', 'invalid_forward_url', 'invalid_proxy_response',
                              'invalid_insecure_tls', 'invalid_expand_path', 'invalid_capacity']

data_create_basket_negative = [
    # basket_name_already_exists
    Data(
        parameter="basket1",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": True,
            "capacity": 250
        },
        expected_response="Basket with name 'basket1' already exists",
        expected_http_code=409
    ),
    # reserved_name_as_basket_name
    Data(
        parameter="baskets",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": True,
            "capacity": 250
        },
        expected_response="This basket name conflicts with reserved system path: baskets",
        expected_http_code=403
    ),
    # negative_capacity
    Data(
        parameter="basket2024",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": False,
            "capacity": -250
        },
        expected_response="Capacity should be a positive number, but was -250",
        expected_http_code=422
    ),
    # too_large_capacity
    Data(
        parameter="basket2021",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": False,
            "capacity": 1000000000
        },
        expected_response="Capacity may not be greater than 2000",
        expected_http_code=422
    ),
    # invalid_forward_url
    Data(
        parameter="basket2021",
        request_body={
            "forward_url": 1,
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": False,
            "capacity": 200
        },
        expected_response="json: cannot unmarshal number into Go struct field BasketConfig.forward_url of type string",
        expected_http_code=400
    ),
    # invalid_proxy_response
    Data(
        parameter="basket2021",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": 1,
            "insecure_tls": False,
            "expand_path": False,
            "capacity": 200
        },
        expected_response="json: cannot unmarshal number into Go struct field BasketConfig.proxy_response of type bool",
        expected_http_code=400
    ),
    # invalid_insecure_tls
    Data(
        parameter="basket2021",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": 1,
            "expand_path": False,
            "capacity": 200
        },
        expected_response="json: cannot unmarshal number into Go struct field BasketConfig.insecure_tls of type bool",
        expected_http_code=400
    ),
    # invalid_expand_path
    Data(
        parameter="basket2021",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": 1,
            "capacity": 200
        },
        expected_response="json: cannot unmarshal number into Go struct field BasketConfig.expand_path of type bool",
        expected_http_code=400
    ),
    # invalid_capacity
    Data(
        parameter="basket2021",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": False,
            "capacity": "aaa"
        },
        expected_response="json: cannot unmarshal string into Go struct field BasketConfig.capacity of type int",
        expected_http_code=400
    )
]
