from data import tokens
from utils.data import Data

master_token = tokens.tokens.master_token

get_baskets_positive_ids = ['basic_case']

data_get_baskets_positive = [
    # basic_case
    Data(
        session_uid=master_token,
        expected_response={
            "names": [
                "basket1",
                "lalala",
                "hahaha",
                "basket2",
                "basket3"
            ],
            "count": 5,
            "has_more": False
        }
    )
]

get_baskets_max_skip_positive_ids = ['max_2_skip_2']

data_get_baskets_max_skip_positive = [
    # max_2_skip_2
    Data(
        session_uid=master_token,
        expected_response={
            "names": [
                "hahaha",
                "basket2"
            ],
            "count": 5,
            "has_more": True
        },
        additional_data={
            "max": 2,
            "skip": 2
        }
    )
]

get_baskets_search_query_positive_ids = ['basic_case']

data_get_baskets_search_query_positive = [
    # basic_case
    Data(
        session_uid=master_token,
        expected_response={
            "names": [
                "hahaha"
            ],
            "has_more": False
        },
        additional_data={
            "search_query": "h"
        }
    )
]
