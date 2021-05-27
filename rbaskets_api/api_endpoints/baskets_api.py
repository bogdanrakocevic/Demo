from api_endpoints.api import Api
from utils.request_method import RequestMethod

base_api_url = 'api'


class BaseApi(Api):
    def __init__(self, session_uid):
        super(BaseApi, self).__init__(session_uid)
        self.base_url = '{}/{}'.format(self.base_url, base_api_url)


class BaseBasketsApi(BaseApi):
    def __init__(self, session_uid):
        super(BaseBasketsApi, self).__init__(session_uid)
        self.base_url = '{}/baskets'.format(self.base_url)

    def get_baskets(self):
        return self.request()

    def get_baskets_max_skip(self, max, skip):
        return self.request('?max={}&skip={}'.format(max, skip))

    def get_baskets_search_query(self, search_query):
        return self.request('?q={}'.format(search_query))

    def create_basket(self, basket_name, payload):
        return self.request('/{}'.format(basket_name), method=RequestMethod.POST, payload=payload)
