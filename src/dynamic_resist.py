import threading
import spidev
import time

from const import Const
from http_request import HttpRequest

# HttpRequest example.
# HttpRequest.request(Const.REQUEST_RESIST, value

# value range : 0 ~ 4
class DynamicResist(object):
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1000000
        self.mcp3008_channel = 0
        self.delay = 0.5
        self.city = -1

    def read_channel(self, channel):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def watch(self):
        try:
            while True:
                adc_value = self.read_channel(self.mcp3008_channel)
                city_value = int(5 * adc_value /1024)
                if self.city == city_value:
                    pass
                else:
                    self.city = city_value
                    HttpRequest.request(Const.REQUEST_RESIST, self.city)

                time.sleep(self.delay)
        except KeyboardInterrupt:
            self.spi.close()



    def run(self):
        t1 = threading.Thread(target=self.watch)
        t1.daemon = True
        t1.start()
