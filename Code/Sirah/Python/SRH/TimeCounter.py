#Class line
import time
from datetime import datetime, timedelta, date
import csv

class TimeCounter:
    file = "/home/pi/Desktop/Sirah/Auxiliars/"
    log = "/home/pi/Desktop/Sirah/"

    def __init__(self):
        self.Actuators=[]
        #self.VectorTemporalData=[]
        #for i in range(15):
        #    self.VectorTemporalData.append(0)
        #self.InitialTime=[]
        #for i in range(15):
        #    self.InitialTime.append(0)
        # (path, status, initial time, cumulated)
        self.Actuators.append([self.file + "Test/PumpTime.txt", 0, 0])
        self.Actuators.append([self.file + "Test/FillingValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "Test/RecirculationValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "Test/LeachedValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "Test/Nutrient1Time.txt", 0, 0])
        self.Actuators.append([self.file + "Test/Nutrient2Time.txt", 0, 0])
        self.Actuators.append([self.file + "Test/Nutrient3Time.txt", 0, 0])
        self.Actuators.append([self.file + "L/L1/StateValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "L/L2/StateValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "L/L3/StateValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "L/L4/StateValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "L/L5/StateValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "L/L6/StateValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "L/L7/StateValveTime.txt", 0, 0])
        self.Actuators.append([self.file + "L/L8/StateValveTime.txt", 0, 0])
        self.DeltaTime = timedelta(seconds=10)

    def CheckTime(self, StatusActuatorsString):
        StatusActuatorsB = StatusActuatorsString.split(",")
        print(StatusActuatorsB)
        StatusActuators = [int(num) for num in StatusActuatorsB]
        print(StatusActuators)
        for actuator in range(15):
            if StatusActuators[actuator]==1:
                if self.Actuators[actuator][1]==0:
                    self.Actuators[actuator][1]=1
                    self.Actuators[actuator][2]=datetime.now()
                if self.Actuators[actuator][1]==1:
                    self.CheckSave(actuator)
            if StatusActuators[actuator] == 0:
                if self.Actuators[actuator][1] == 0:
                    pass
                if self.Actuators[actuator][1] == 1:
                    self.Actuators[actuator][1] = 0
                    self.SaveTime(actuator)

    def CheckSave(self, actuator):
        TimeDifference = datetime.now() - self.Actuators[actuator][2]
        if TimeDifference > self.DeltaTime:
            self.SaveTime(actuator)

    def SaveTime(self, actuator):
        #Reading the file
        with open(self.Actuators[actuator][0], 'r') as f:
            hour, minuts, seconds = f.readline().strip().split(':')
        print(hour)
        print(minuts)
        print(seconds)
        time = int(hour)*3600 + int(minuts) * 60 + int(seconds)
        print(time)
        delta = datetime.now() - self.Actuators[actuator][2]
        time = round(time + delta.total_seconds(),0)

        h = time // 3600
        m = (time % 3600) // 60
        sec = (time % 3600) % 60  # just for reference


        with open(self.Actuators[actuator][0], 'w') as f:
            f.write(self.TimeToStr(h) + ":" + self.TimeToStr(m) + ":" + self.TimeToStr(sec))
        self.ResetTemporalTime(actuator)

    def TimeToStr(self,time):
        if time<10:
            return str("0"+str(int(time)))
        else:
            return str(int(time))

    def ResetTemporalTime(self, actuator):
        self.Actuators[actuator][2]=datetime.now()