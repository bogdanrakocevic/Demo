import json
import re

TOKEN_RE = re.compile('[_a-zA-Z0-9-]{44}')


def load_response_content(response):
    return json.loads(response['content'])


def assert_response_code(response, expected_code):
    assert response['status_code'] == expected_code,\
        'Actual http response code: {} is not as expected: {}.Response content: {}'.\
        format(response['status_code'], expected_code, response['content'])


def assert_response_content(d1, d2, check_format):
    check_response_structure(d1, d2)
    check_response_values(d1, d2, check_format)


def check_response_structure(d1, d2):
    if isinstance(d1, dict):
        assert isinstance(d2, dict), 'Actual response(part): \n{}\n is a dictionary, but expected response(part):' \
                                     ' \n{}\n is not'.format(d1, d2)
        check_dict_keys(d1, d2)
        for key, value in d1.iteritems():
            check_response_structure(value, d2[key])
    elif isinstance(d1, unicode):
        assert isinstance(d2, str), 'Actual response(part): \n{}\n is string, ' \
                                         'but expected response(part): \n{}\n is not'.format(d1, d2)
    elif isinstance(d1, int):
        assert isinstance(d2, int), 'Actual response(part): \n{}\n is integer, ' \
                                         'but expected response(part): \n{}\n is not'.format(d1, d2)
    elif isinstance(d1, list):
        assert isinstance(d2, list), 'Actual response(part): \n{}\n is a list, ' \
                                     'but expected response(part): \n{}\n is not'.format(d1, d2)
        assert len(d1) == len(d2), "Actual response list: \n{}\n and expected response list : \n{}\n does not have " \
                                   "same size - actual response list size: {}, expected response list size: {}"\
            .format(d1, d2, len(d1), len(d2))
        for i in range(len(d1)):
            check_response_structure(d1[i], d2[i])
            continue


def check_dict_keys(d1, d2):
    actual_response_keys = d1.keys()
    expected_response_keys = d2.keys()

    for key in expected_response_keys:
        assert key in actual_response_keys, 'Property "{}" not found in actual API response(part):' \
                                            ' \n{}\n although it is present in expected response(part):' \
                                            ' \n{}'.format(key, d1, d2)
    for key1 in actual_response_keys:
        assert key1 in expected_response_keys, 'Property "{}" not found in expected API response(part):' \
                                               ' \n{}\n although it is present in actual response(part):' \
                                               ' \n{}'.format(key1, d2, d1)


def check_response_values(d1, d2, check_format):

    if isinstance(d1, dict):
        for key, value in d1.iteritems():
            if isinstance(value, list):
                if len(value) == 0:
                    assert len(d2[key]) == 0
                    continue
                value = sorted(value)
                d2[key] = sorted(d2[key])
                for i in range(len(value)):
                    assert value[i] == d2[key][i], 'Actual "{}" value {} is not as expected'.\
                        format(key, value[i], d2[value][i])
                    continue
                continue

            if 'token' in key and check_format:
                check_formats(key, value)
                continue
            else:
                assert d1[key] == d2[key], 'Actual "{}" value: {} is not as expected: {}'.format(key, d1[key], d2[key])


def check_formats(key, value):
    if 'token' in key and value is not None and isinstance(value, unicode):
        assert TOKEN_RE.match(value), get_format_error_message(key, value, 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


def get_format_error_message(key, value, property_format=None):
    return 'Actual "{}" value: {} does not have expected format: {}'.format(key, value, property_format)
