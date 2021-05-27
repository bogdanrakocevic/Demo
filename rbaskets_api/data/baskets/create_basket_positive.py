from data import tokens
from utils.data import Data

master_token = tokens.tokens.master_token

create_basket_positive_ids = ['basic_case1', 'basic_case2', 'basic_case3', 'basic_case4', 'basic_case5']

data_create_basket_positive = [
    # basic_case1
    Data(
        parameter="basket1",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": False,
            "capacity": 250
        },
        expected_response={
            "token": "mkGOkqxBy1ky-XvQLV418pWuRJZe9Vbhh0f90puRmZ-S"
        }
    ),
    # basic_case2
    Data(
        parameter="lalala",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": True,
            "capacity": 250
        },
        expected_response={
            "token": "mkGOkqxBy1ky-XvQLV418pWuRJZe9Vbhh0f90puRmZ-S"
        }
    ),
    # basic_case3
    Data(
        parameter="hahaha",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": True,
            "expand_path": True,
            "capacity": 250
        },
        expected_response={
            "token": "mkGOkqxBy1ky-XvQLV418pWuRJZe9Vbhh0f90puRmZ-S"
        }
    ),
    # basic_case4
    Data(
        parameter="basket2",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": True,
            "insecure_tls": True,
            "expand_path": True,
            "capacity": 250
        },
        expected_response={
            "token": "mkGOkqxBy1ky-XvQLV418pWuRJZe9Vbhh0f90puRmZ-S"
        }
    ),
    # basic_case5
    Data(
        parameter="basket3",
        request_body={
            "forward_url": "https://myservice.example.com/events-collector",
            "proxy_response": False,
            "insecure_tls": False,
            "expand_path": True,
            "capacity": 1999
        },
        expected_response={
            "token": "mkGOkqxBy1ky-XvQLV418pWuRJZe9Vbhh0f90puRmZ-S"
        }
    )
]
