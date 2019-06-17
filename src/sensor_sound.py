import threading
import spidev
import time

from const import Const
from http_request import HttpRequest

# HttpRequest example.
# HttpRequest.request(Const.REQUEST_WIND, value)

# value range : 0 ~ 100

class SensorSound(object):
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1000000
        self.mcp3008_channel = 1
        self.delay = 0.2

    def read_channel(self, channel):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def watch(self):
        while True:
            adc_value = self.read_channel(self.mcp3008_channel)
            if adc_value > 100:
                calc_wind = int(100 * (adc_value-100) / 100)
                wind_value = calc_wind > 100 and 100 or calc_wind
                HttpRequest.request(Const.REQUEST_WIND, wind_value)
            time.sleep(self.delay)

    def run(self):
        t1 = threading.Thread(target=self.watch)
        t1.daemon = True
        t1.start()
