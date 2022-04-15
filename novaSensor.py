import logging

from pysds011.driver import SDS011


class NovaSensor:
    def __init__(self, path: str):

        logger = logging.getLogger(__name__)

        # noinspection PyTypeChecker
        self.sensor: SDS011 = SDS011(path, logger)
        self.sensor.cmd_set_sleep(0)
        self.sensor.cmd_set_mode(self.sensor.MODE_QUERY)


    def get_data(self):
        data = self.sensor.cmd_query_data()
        return NovaSensorData(data.get('pm25'), data.get('pm10'))

class NovaSensorData:
    def __init__(self, pm25: float, pm10: float):
        self.pm25 = pm25
        self.pm10 = pm10