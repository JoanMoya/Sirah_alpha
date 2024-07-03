#Class LogTest
from datetime import datetime, date, timedelta
import csv
from SRH.RedZone import RedZone

class LogScheduledIrrigation:
    file = "/home/pi/Desktop/Sirah/"
    def __init__(self):
        #self.TestOn()
        # Define la hora de inicio permitida (14:00) y la hora de finalización permitida (12:00)
        self.RedZone=RedZone()
        self.DeltaTime = timedelta(minutes=20)
        self.Status=1

    def TestOn(self):
        current=datetime.now()
        log=open(self.file + "LogScheduledIrrigation.txt", "a")
        log.write("-----------------------------------")
        log.write("\n")
        log.write("Starting scheduled irrigation at: " + str(current))
        log.write("\n")
        log.close()
        
        #self.StatusTestOn()

    def TestOff(self):
        current=datetime.now()
        log=open(self.file + "LogScheduledIrrigation.txt", "a")
        log.write("Final scheduled irrigation at: " + str(current))
        log.write("\n")
        log.write("**********************************")
        log.write("\n")
        log.close()
        
        self.StatusTestOff()

    def ReadStatus(self):
        log=open(self.file + "StatusScheduledIrrigation.txt")
        Status = log.read()
        if Status=='':
            self.Status=self.Status
        else:
            self.Status = int(Status)
        #print(Status)
        log.close()
        return self.Status
        
    def StatusTestOn(self):
        log=open(self.file + "StatusScheduledIrrigation.txt", "w")
        log.write("1")
        log.close()
        self.Status=1

    def StatusTestOff(self):
        log=open(self.file + "StatusScheduledIrrigation.txt", "w")
        log.write("0")
        log.close()
        
    def WriteStatus(self, message):
        log=open(self.file + "LogScheduledIrrigation.txt", "a")
        log.write(message)
        log.write("\n")
        log.close()
        
    def CheckTest(self):
        Status=self.ReadStatus()
    
        if Status==0: 
            self.TestOff()
            return True
        else:
            return False

    def IrrigationActions(self):
        self.Update()
        # Crea una lista vacía para almacenar las acciones
        self.actions = []

        # Obtener la fecha actual
        self.fecha_actual = date.today()

        self.RedZone.UpdateDate(self.fecha_actual)

        # Crear un objeto datetime con la hora y fecha actual
        self.IrrigationTime = datetime.combine(self.fecha_actual, self.ScheduledIrrigationInitialHour.time())
        self.IrrigationTime = self.IrrigationTime

        # Verifica si el tiempo de riego está dentro de la franja permitida
        if self.RedZone.BeginningRedHour < self.IrrigationTime < self.RedZone.EndRedHour and self.RedZone.StatusRedZone==1:
            # Si está dentro de la franja prohibida, lo planifica para después de la franja
            self.IrrigationTime = self.RedZone.EndRedHour

        # Itera a través de cada acción y solicita la acción y la hora correspondiente
        for i in range(self.ScheduledIrrigationPeriods):
            self.action = self.IrrigationTime
            self.IrrigationTime = self.IrrigationTime + timedelta(minutes=self.ScheduledIrrigationInterval)
            # Verifica si el tiempo de riego está dentro de la franja permitida
            if (self.RedZone.BeginningRedHour < self.IrrigationTime < self.RedZone.EndRedHour  and self.RedZone.RedPeriod==1):
                # Si está dentro de la franja prohibida, lo planifica para después de la franja
                self.IrrigationTime = self.RedZone.EndRedHour
            self.actions.append((self.action, round(self.ScheduledIrrigationTime, 2)))


        with open(self.file + 'ScheduledIrrigationPlanification.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerows([])  # Escribir una lista vacía para borrar el contenido

        with open(self.file + 'ScheduledIrrigationPlanification.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerows(self.actions)

    def Update(self):
        log=open(self.file + "ScheduledIrrigationTime.txt")
        self.ScheduledIrrigationTime = float(log.read())
        log.close()

        log=open(self.file + "ScheduledIrrigationPeriods.txt")
        self.ScheduledIrrigationPeriods = int(log.read())
        log.close()

        log=open(self.file + "ScheduledIrrigationInterval.txt")
        self.ScheduledIrrigationInterval = float(log.read())
        log.close()

        log=open(self.file + "ScheduledIrrigationHour.txt")
        self.ScheduledIrrigationInitialHour = datetime.strptime(log.read(), '%H:%M')
        log.close()

    def CheckDelta(self):
        delta = datetime.now() - self.action
        return delta < self.DeltaTime
    
    def Irrigate_L1(self):
        file = open("/home/pi/Desktop/Sirah/Auxiliars/ConfigurationFiles/IrrigateL1.txt")
        state = int(file.read())
        file.close()
        return state
    
    def Irrigate_L2(self):
        file = open("/home/pi/Desktop/Sirah/Auxiliars/ConfigurationFiles/IrrigateL2.txt")
        state = int(file.read())
        file.close()
        return state
    
    def Irrigate_L3(self):
        file = open("/home/pi/Desktop/Sirah/Auxiliars/ConfigurationFiles/IrrigateL3.txt")
        state = int(file.read())
        file.close()
        return state
    
    def Irrigate_L4(self):
        file = open("/home/pi/Desktop/Sirah/Auxiliars/ConfigurationFiles/IrrigateL4.txt")
        state = int(file.read())
        file.close()
        return state