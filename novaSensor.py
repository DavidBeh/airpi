import logging
import os
import serial
from pysds011.driver import SDS011


class NovaSensor:

    @staticmethod
    def get_path():
        paths = os.listdir("/dev/")
        # filter for entries beginning with ttyUSB
        paths = [p for p in paths if p.startswith("ttyUSB")]
        if len(paths) == 0:
            return None
        return "/dev/" + paths[0]

    def __init__(self, path: str):

        logger = logging.getLogger(__name__)

        ser = serial.Serial(path, 9600)
        if not ser.isOpen():
            ser.open()

        # noinspection PyTypeChecker
        self.sensor: SDS011 = SDS011(ser, logger)
        self.sensor.cmd_set_sleep(0)
        self.sensor.cmd_set_mode(self.sensor.MODE_QUERY)
        self.sensor.cmd_set_working_period(0)

        # self.sensor.cmd_set_mode(self.sensor.MODE_QUERY)

    def get_data(self):
        data = self.sensor.cmd_query_data()
        if data is None:
            return None
        return NovaSensorData(data.get('pm25'), data.get('pm10'))


class NovaSensorData:
    def __init__(self, pm25: float, pm10: float):
        self.pm25 = pm25
        self.pm10 = pm10

    # String representation of the data
    def __str__(self):
        return "PM2.5: {0:.2f} | PM10: {1:.2f}".format(self.pm25, self.pm10)