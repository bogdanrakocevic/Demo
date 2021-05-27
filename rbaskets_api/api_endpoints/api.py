import requests

from utils.config import load_config
from utils.request_method import RequestMethod


conf = load_config()


class Api(object):
    def __init__(self, session_id=None):
        self.headers = {
            'Content-type': 'application/json'
        }
        if session_id:
            self.headers.update({'Authorization': session_id})
        self.base_url = conf.api_url

    def request(self, path=None, method=RequestMethod.GET, payload=None, headers=None):

        if headers:
            self.headers.update(headers)
        response = requests.request(method, self.base_url + path if path else self.base_url,
                                    json=payload, headers=self.headers)
        return {'status_code': response.status_code, 'content': response.content, 'headers': response.headers}
