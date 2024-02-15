#Class line
from datetime import datetime
import csv
import os

class Line:
    file = "/home/pi/Desktop/Sirah/Auxiliars/L/"
    #file = "C:\\Users\\marcel\\Documents\\GitHub\\sirah\\Sirah\\Auxiliars\\L\\"
    def __init__(self, line): #1
        self.LineName= "L"+str(line) #"L"+"1"
        self.LineNumber = line
        self.Path=self.file + self.LineName + "/" #"/home/pi/Desktop/Sirah/Auxiliars/L/" + "L1" + "/"
        #self.Path=self.file + self.LineName + "\\"
        self.getConfig()

    def getLineName(self):
        print(self.LineName)

    def setLineName(self, LineName):
        self.LineName=LineName

    def getStateValve(self):
        print(self.StateValve)

    def setStateValve(self,StateValve):
        self.StateValve=StateValve
        file=open(self.Path+"StateValve.txt", "w")
        file.write(str(StateValve))
        file.close()

    def getUse(self):
        file = self.Path + "Status.txt"

        # Verificar si el archivo está vacío
        file = open(self.Path + "Status.txt", "r")
        TempStateValve= file.read()
        if TempStateValve=='':
            self.StateValve=self.StateValve
        else:
            self.StateValve = int(TempStateValve)

        #if os.stat(file).st_size == 0:
        #    self.StateValve=self.StateValve
        #else:
        #    file = open(self.Path + "Status.txt", "r")
        #    self.StateValve = int(file.read())
        file.close()
        return self.StateValve

    def setUse(self, Use):
        self.Use=Use

    def getCropType(self):
        print(self.CropType)

    def setCropType(self, CropType):
        self.CropType=CropType

    def getIrrigationTime(self):
        print(self.IrrigationTime)

    def setIrrigationTime(self, IrrigationTime):
        self.IrrigationTime=IrrigationTime

    def getDripper(self):
        print(self.Dripper)

    def setDripper(self, Dripper):
        self.Dripper=Dripper

    def getSurface(self):
        print(self.Surface)

    def setSurface(self, Surface):
        self.Surface=Surface

    def getPlants(self):
        print(self.Plants)

    def setPlants(self, Plants):
        self.Plants=Plants

    def getInitialDate(self):
        print(self.InitialDate)

    def setInitialDate(self, InitialDate):
        self.InitialDate = InitialDate

    def day(self):
        now = datetime.now()
        InitialDate=self.InitialDate
        day= now.date()- InitialDate.date()
        self.day=day.days
        file=open(self.Path + "Day.txt", 'w')
        file.write(str(day.days))
        file.close()
        return day.days

    def getInitialHour(self):
        file=open(self.Path + "IrrigationTimeP1.txt", 'r')
        self.InitialHour = datetime.strptime(file.read(), '%H:%M')
        file.close()
        return self.InitialHour

    def getFinalHour(self):
        file = open(self.Path + "IrrigationTimeP2.txt", 'r')
        self.FinalHour = datetime.strptime(file.read(), '%H:%M')
        file.close()
        return self.FinalHour

    def RemainingDays(self):
        if(self.CropType==1):
            #tomato
            self.RemainingDays=180-self.day
        elif (self.CropType==2):
            self.RemainingDays = 75- self.day
        elif (self.CropType==3):
            self.RemainingDays = 90- self.day

        file=open(self.Path + "RemainingDays.txt", 'w')
        file.write(str(self.RemainingDays))
        file.close()
    
    def getETC(self):
        print(self.ETC)

    def setETC(self, ETC):
        self.ETC=ETC
        file=open(self.Path + "ETC.txt", 'w')
        file.write(str(ETC))
        file.close()

    def getET0(self):
        print(self.ET0)

    def setET0(self, ET0):
        self.ET0=round(ET0,3)
        file=open(self.Path + "ET0.txt", 'w')
        file.write(str(ET0))
        file.close()

    def getkc(self):
        print(self.kc)

    def setkc(self, kc):
        self.kc=kc
        file=open(self.Path + "kc.txt", 'w')
        file.write(str(kc))
        file.close()
    
    def getgain(self):
        print(self.gain)
        
    def setgain(self, gain):
        self.gain=gain
        file=open(self.Path + "Gain.txt", 'w')
        file.write(str(gain))
        file.close()
    

    def Irrigation(self):
        irrigacio = self.ETC*self.Plants*self.Surface
        irrigacio_gain = irrigacio * (self.gain/100)
        self.irrigation=round(irrigacio + irrigacio_gain,2)
        file=open(self.Path + "Irrigation.txt", 'w')
        file.write(str(self.irrigation))
        file.close()
    
    def getIrrigation(self):
        print(self.irrigation)
        
    def setIrrigation(self, irrigation):
        self.irrigation=irrigation
        file=open(self.Path + "Irrigation.txt", 'w')
        file.write(str(irrigation))
        file.close()


    def DailyIrrigationTimes(self):
        self.DailyIrrigationTimes=round(self.ET0, 0)
        #print(self.DailyIrrigationTimes)
        file=open(self.Path + "DailyIrrigationTimes.txt", 'w')
        file.write(str(self.DailyIrrigationTimes))
        file.close()

    def Progress(self):
        if(self.CropType==1):
            #tomato
            TotalDays=180
        elif (self.CropType==2):
            TotalDays = 75
        elif (self.CropType==3):
            TotalDays = 90
        self.Progress=self.day/TotalDays*100
        file=open(self.Path + "Progress.txt", 'w')
        file.write(str(self.Progress))
        file.close()

    def ToCsv(self):
        # Datos a guardar en el archivo CSV
        data_to_save = [self.CropType, self.day, self.kc, self.RemainingDays, self.Progress, self.ETC, self.ET0, self.DailyIrrigationTimes, self.irrigation, self.gain]
        #print(data_to_save)
        # Abre el archivo CSV en modo de lectura y escritura
        with open(self.Path + "LineParameters.csv", 'r+', newline='') as file:
            # Crea un objeto reader para leer el archivo CSV
            reader = csv.reader(file)

            # Convierte el objeto reader a una lista
            rows = list(reader)
            #print(rows)
            # Sustituye la última fila en la lista con los nuevos datos
            rows[-1] = data_to_save

            # Vuelve al principio del archivo CSV
            file.seek(0)

            # Crea un objeto writer para escribir en el archivo CSV
            writer = csv.writer(file)

            # Escribe las filas actualizadas en el archivo CSV
            for row in rows:
                writer.writerow(row)


    def getall(self):
        print("Line name:")
        self.getLineName()
        print("Line use:")
        self.getUse()
        print("Irrigation timne:")
        self.getIrrigationTime()
        print("Dripper characteristics(l/h):")
        self.getDripper()
        print("Gain:")
        self.getgain()
        #put all parameters

    def getConfig(self):
        file=open(self.Path + "IrrigationTime.txt")
        self.IrrigationTime=float(file.read())
        file.close()

        file=open(self.Path + "Dripper.txt")
        self.Dripper=float(file.read())
        file.close()

        file=open(self.Path + "Type.txt")
        self.CropType=float(file.read())
        file.close()

        file=open(self.Path + "Status.txt")
        self.Use=float(file.read())
        file.close()

        file=open(self.Path + "NumberPlants.txt")
        self.Plants=float(file.read())
        file.close()

        file=open(self.Path + "Surface.txt")
        self.Surface=float(file.read())
        file.close()

        file=open(self.Path + "InitialDate.txt")
        self.InitialDate = datetime.strptime(file.read(), '%Y-%m-%d')
        file.close()
        
        file=open(self.Path + "Gain.txt")
        self.gain=float(file.read())
        file.close()
        
        file=open(self.Path + "kc.txt")
        self.kc=float(file.read())
        file.close()
        
        file=open(self.Path + "ET0.txt")
        self.ET0=float(file.read())
        file.close()
        
        file=open(self.Path + "Irrigation.txt")
        self.irrigation=float(file.read())
        file.close()


#L1=Line("L1")
#print(L1.getFinalHour())
#print(L1.day())
#Line1=Line("L1",2,3)
#Line1.getall()
#print("------------------------")
#print(Line1.Path)
#print(Line1.Dripper)
