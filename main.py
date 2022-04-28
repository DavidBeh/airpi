import logging
import os
from time import sleep

import serial
from pysds011.driver import SDS011

from novaSensor import NovaSensor
from scheduler import Scheduler

# print working directory
print(os.getcwd())
sched = Scheduler()
sched.create_job()
exit()

paths = os.listdir("/dev/")
# filter for entries beginning with ttyUSB
paths = [p for p in paths if p.startswith("ttyUSB")]


if len(paths) != 1:
    print("Error: No or to many USB device found, number of devices: " + str(len(paths)))
    exit()


ns = NovaSensor("/dev/"+paths[0])

while True:

    d = ns.get_data()
    # Wait 1 second
    sleep(1)
    print(d)
