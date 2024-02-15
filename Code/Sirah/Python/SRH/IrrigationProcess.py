#Class line
from datetime import datetime, timedelta, date
import csv
from SRH.ETC import ETC
from SRH.Line import Line

class IrrigationProcess:
    file = "/home/pi/Desktop/Sirah/Auxiliars/L/"
    #file = "C:\\Users\\marcel\\Documents\\GitHub\\sirah\\Sirah\\Auxiliars\\L\\"
    log = "/home/pi/Desktop/Sirah/"
    #log = "C:\\Users\\marcel\\Documents\\GitHub\\sirah\\Sirah\\"

    def __init__(self, line): #1
        self.LineName= "L" + str(line) #L1
        self.Path=self.file + self.LineName + "/" # "/home/pi/Desktop/Sirah/Auxiliars/L/" + "L1" + "/"
        #self.Path=self.file + self.LineName + "\\"
        self.L = Line(line) #1
        # Crear un objeto timedelta que represente 30 minutos
        self.DeltaTime = timedelta(minutes=20)
        self.ETCCalculation = ETC()  # Element that calculate the ETC

    def Update(self):
        self.L = Line(self.L.LineNumber) #"L1"
        self.getCongifuration()
        self.CalculateDailyWater()

    def getCongifuration(self):
        #update L element to get all information to determine the
        self.L.day()
        self.day = self.L.day
        self.L.setETC(self.ETCCalculation.ETC(self.day, self.L.CropType))
        self.L.setET0(self.ETCCalculation.ETO())
        self.L.setkc(self.ETCCalculation.Kc(self.L.day, self.L.CropType))
        self.L.Irrigation()
        self.L.DailyIrrigationTimes()
        self.CalculateNumberDailyIrrigationTimes()
        self.DailyIrrigationProcesses = int(self.DailyIrrigationTimes)
        self.InitialHour = self.L.getInitialHour()
        self.FinalHour = self.L.getFinalHour()
        self.gain = self.L.getgain()

        self.TotalDuration = self.FinalHour - self.InitialHour
        self.Period = self.TotalDuration / self.DailyIrrigationProcesses
        self.HalfPeriod = self.Period / 2

    def CalculateNumberDailyIrrigationTimes(self):
        # Corrección primeros dias
        if self.day < 15:
            self.DailyIrrigationTimes=6
        else:
            self.DailyIrrigationTimes = self.L.DailyIrrigationTimes

    def CalculateDailyWater(self):
        # Calcular agua por vez
        self.Water = self.L.irrigation / self.DailyIrrigationTimes
        self.Minutes = self.Water / (self.L.Dripper * self.L.Plants) * 60
        if self.Minutes < 2:
            self.Minutes = 2

    def IrrigationActions(self):
        # Crea una lista vacía para almacenar las acciones
        self.actions = []

        # Obtener la fecha actual
        self.fecha_actual = date.today()

        # Crear un objeto datetime con la hora y fecha actual
        self.IrrigationTime = datetime.combine(self.fecha_actual, self.InitialHour.time())
        self.IrrigationTime = self.IrrigationTime + self.HalfPeriod

        # Itera a través de cada acción y solicita la acción y la hora correspondiente
        for i in range(self.DailyIrrigationProcesses):
            self.action = self.IrrigationTime
            self.IrrigationTime = self.IrrigationTime + self.Period
            self.actions.append((self.action, round(self.Minutes,2)))

        # Ordena las acciones por hora
        self.SortedActions = sorted(self.actions, key=lambda x: x[1])
        
        with open(self.Path + 'report.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerows([])  # Escribir una lista vacía para borrar el contenido
        
        with open(self.Path + 'report.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerows(self.actions)

    def IrrigationControl(self):
        self.L.setStateValve(1)
        time.sleep(self.Minutes)
        self.L.setStateValve(0)

    def CheckDelta(self):
        delta = datetime.now() - self.action
        return delta < self.DeltaTime

    def CheckUpdate(self):
        file=open(self.Path + "NextUpdate.txt", "r")
        CheckUpdate=file.read()
        print(CheckUpdate)
        if CheckUpdate=="1":
            return True
        else:
            return False

    def SetNextUpdate(self):
        file = open(self.Path + "NextUpdate.txt", "w")
        file.write("0")
        file.close()

    def LogStartAction(self):
        current = datetime.now()
        file = open(self.log + "LogSirah.txt", "a")
        file.write("Irrigation process on at " + self.L.LineName + ": " + str(current))
        file.write("\n")
        file.close()

    def LogFinishAction(self):
        current = datetime.now()
        file = open(self.log + "LogSirah.txt", "a")
        file.write("Irrigation process off at " + self.L.LineName + ": " + str(current))
        file.write("\n")
        file.close()