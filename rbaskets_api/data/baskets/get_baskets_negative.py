from data import tokens
from utils.data import Data

master_token = tokens.tokens.master_token

get_baskets_negative_ids = ['basic_case']

data_get_baskets_negative = [
    # basic_case
    Data(
        expected_http_code=401
    )
]
