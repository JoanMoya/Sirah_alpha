#Class Red_Zone
from datetime import datetime, date, timedelta
import csv

class RedZone:
    file = "/home/pi/Desktop/Sirah/Auxiliars/ConfigurationFiles/"
    def __init__(self):
        # Define la hora de inicio permitida (14:00) y la hora de finalización permitida (12:00)
        self.BeginningRedHour = datetime.strptime('12:00', '%H:%M')
        self.EndRedHour = datetime.strptime('14:00', '%H:%M')
        self.RedPeriod = 0
        self.Update()

    def Update(self):
        log=open(self.file + "BeginningRedHour.txt")
        self.BeginningRedHour = datetime.strptime(log.read(), '%H:%M')
        log.close()

        log=open(self.file + "EndRedHour.txt")
        self.EndRedHour = datetime.strptime(log.read(), '%H:%M')
        log.close()

        log=open(self.file + "StatusRedPeriod.txt")
        self.RedPeriod = int(log.read())
        log.close()

    def UpdateDate(self, CurrentDate):
        self.BeginningRedHour = datetime.combine(CurrentDate, self.BeginningRedHour.time())
        self.EndRedHour = datetime.combine(CurrentDate, self.EndRedHour.time())
