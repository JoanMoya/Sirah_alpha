#Class LogSirah
from datetime import datetime,timedelta
from csv import writer
from SRH.TempStor import TempStor

class LocalStor:
    def __init__(self):
        self.LastReading=datetime.now()
        self.TimeStep = 15
        self.TimeStep2 = 1
        self.CumTemperature = 0
        self.FlagTemperature = 0
        self.CumHumidity = 0
        self.FlagHumidity = 0
        self.CumCo2 = 0
        self.FlagCo2 = 0
        self.CumUV = 0
        self.FlagUV = 0
        self.TempStor = TempStor()
        self.FlagHeight = 0
        self.Height = 0
        
    def SaveReading(self,line_array):

        self.CumTemperature = float(line_array[0]) + self.CumTemperature
        self.FlagTemperature = self.FlagTemperature + 1
        self.CumHumidity = float(line_array[1])+self.CumHumidity
        self.FlagHumidity =self.FlagHumidity + 1
        self.CumCo2 = float(line_array[2])+self.CumCo2
        self.FlagCo2 = self.FlagCo2 + 1
        self.CumUV = float(line_array[3]) + self.CumUV
        self.FlagUV = self.FlagUV+1
        self.FlagHeight = self.FlagHeight+1
        self.Height = float(line_array[4]) + self.Height
        self.LastReading=datetime.now()

    def Reset(self):
        self.CumTemperature = 0
        self.FlagTemperature = 0
        self.CumHumidity = 0
        self.FlagHumidity = 0
        self.CumCo2 = 0
        self.FlagCo2 = 0
        self.CumUV = 0
        self.FlagUV = 0
        self.FlagHeight = 0
        self.Height = 0

    def CheckTime(self, line_array):
        CurrentTime=datetime.now()
        CurrentMin = int(CurrentTime.strftime('%M'))
        delta = CurrentTime - self.LastReading
        if (CurrentMin%self.TimeStep==0) and (delta > timedelta(minutes=self.TimeStep2)):
            #self.Report(line_array)
            #self.SaveReading(self.TempStor.average())
            print("que tal!")
            self.Report(self.TempStor.average())
            print("que tal2!")
            self.TempStor.Reset()
            self.LastReading=datetime.now()
        else:
            self.TempStor.CheckTime(line_array)
        
    
    def average(self):  
        #Calculate average temperature of the period
        if self.FlagTemperature==0:
            Taverage=0
        else:
            Taverage=self.CumTemperature/self.FlagTemperature
        
        #Calculate average humidity of the period
        if self.FlagHumidity==0:
            Haverage=0
        else:
            Haverage=self.CumHumidity/self.FlagHumidity
            
        #Calculate average CO2 of the period
        if self.FlagCo2==0:
            Co2average=0
        else:
            Co2average=self.CumCo2/self.FlagCo2
        
        #Calculate average UV of the period
        if self.FlagUV==0:
            UVaverage=0
        else:
            UVaverage=self.CumUV/self.FlagUV
            
        if self.FlagHeight==0:
            Heightaverage=0
        else:
            Heightaverage=self.Height/self.FlagHeight
        
        average=(Taverage, Haverage, Co2average, UVaverage, Heightaverage)
        
        
        return average

    def Report(self,line_array):
        filename = "/home/pi/Desktop/Sirah/Logs/Dades/DBEnvironmentalData.csv"
        temperature = float(line_array[0])
        humidity = float(line_array[1])
        co2 = float(line_array[2])
        uv = float(line_array[3])
        height = float(line_array[4])
        today = datetime.now()
        day = today.strftime('%d/%m/%Y %H:%M')
            
        with open(filename, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([day, temperature, humidity, co2, uv, height])
            f_object.close()