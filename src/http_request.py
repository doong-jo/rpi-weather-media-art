import requests
from const import Const

class HttpRequest(object):

    def __init__(self):
        pass

    @staticmethod
    def request(identity, value):

        prefix = ""
        if identity == Const.REQUEST_WIND:
            prefix = Const.REQUEST_WIND_PREFIX
        elif identity == Const.REQUEST_RESIST:
            prefix = Const.REQUEST_RESIST_PREFIX

        endPoint = Const.REQUEST_URL + prefix + value

        requests.post(endPoint, data={})
