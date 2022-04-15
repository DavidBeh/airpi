import serial
from pysds011.driver import SDS011

from novaSensor import NovaSensor

ns = NovaSensor("/dev/ttyUSB1")

while True:
    dust_data = ns.get_data()
    print("10: " + dust_data.pm10 + " |25: " + dust_data.pm25)

ser = serial.Serial('/dev/ttyUSB1', 9600)
if ser.isOpen() == False:
    ser.open()

import logging

l = NovaSensor("/dev/ttyUSB1", 9600)
log = logging.getLogger(__name__)

# Create a new SDS011-Driver instance
sd = SDS011(ser, log)
sd.cmd_set_sleep(0)

sd.cmd_set_mode(sd.MODE_QUERY)
# fw_ver = sd.cmd_firmware_version()
# loop infinitely