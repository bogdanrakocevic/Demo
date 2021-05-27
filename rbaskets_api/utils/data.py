class Data(object):
    def __init__(self, session_uid=None, request_body=None, parameter=None, expected_http_code=None,
                 expected_response=None, additional_data=None):

        self.session_uid = session_uid
        self.request_body = request_body
        self.parameter = parameter
        self.expected_http_code = expected_http_code
        self.expected_response = expected_response
        self.additional_data = additional_data
