import os.path
import sys

from crontab import CronTab

class Scheduler:

    def __init__(self):
        print(os.path.realpath(__file__))

    def create_job(self, identifier: str = "airpi"):
        self.delete_job(identifier)
        tab = CronTab(user='pi')
        job = tab.new(command=f"{os.getcwd()}/{sys.argv[0]}")
        job.every_reboot()
        job.comment(identifier)
        tab.write()

    def delete_job(self, identifier: str = "airpi"):
        tab = CronTab(user='pi')
        for job in tab:
            if job.comment == identifier:
                tab.remove(job)
        tab.write()