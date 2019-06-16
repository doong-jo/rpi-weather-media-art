import RPi.GPIO as GPIO
import threading

from const import Const
from http_request import HttpRequest

# HttpRequest example.
# HttpRequest.request(Const.REQUEST_RESIST, value)

class DynamicResist(object):
    def __init__(self):
        pass

    def watch(self):
        while True:
            print('DynamicResist watching..')
            pass

    def run(self):
        t1 = threading.Thread(target=self.watch)
        t1.daemon = True
        t1.start()
