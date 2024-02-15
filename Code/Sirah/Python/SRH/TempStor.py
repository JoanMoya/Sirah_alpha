#Class LogSirah
from datetime import datetime,timedelta

class TempStor:
    def __init__(self):
        self.LastReading=""
        self.TimeStep = 1
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
        
        
    def SaveReading(self,line_array):
        #If data is float, then save
        ##Temperature
        try:
            valor_float = float(line_array[0])
            if valor_float>=-24 and valor_float <= 50:
                self.CumTemperature = float(line_array[0]) + self.CumTemperature
                self.FlagTemperature = self.FlagTemperature + 1
            else:
                self.CumTemperature = self.CumTemperature
                self.FlagTemperature = self.FlagTemperature
        except:
            self.CumTemperature = self.CumTemperature
            self.FlagTemperature = self.FlagTemperature
        ##Humidity
        try:
            valor_float=float(line_array[1])
            if valor_float>=0 and valor_float <= 100:
                self.CumHumidity = float(line_array[1])+self.CumHumidity
                self.FlagHumidity =self.FlagHumidity + 1
            else:
                self.CumHumidity = self.CumHumidity
                self.FlagHumidity =self.FlagHumidity
        except:
            self.CumHumidity = self.CumHumidity
            self.FlagHumidity = self.FlagHumidity

        ##CO2
        try:
            valor_float=float(line_array[2])
            if valor_float >= 300 and valor_float <= 3000:
                self.CumCo2 = float(line_array[2])+self.CumCo2
                self.FlagCo2 = self.FlagCo2 + 1
            else:
                self.CumCo2 = self.CumCo2
                self.FlagCo2 = self.FlagCo2
        except:
            self.CumCo2 = self.CumCo2
            self.FlagCo2 = self.FlagCo2
        ##UV
        try:
            valor_float=float(line_array[3])
            if valor_float >= 0 and valor_float <= 20000:
                self.CumUV = float(line_array[3]) + self.CumUV
                self.FlagUV = self.FlagUV + 1
            else:
                self.CumUV = self.CumUV
                self.FlagUV = self.FlagUV
        except:
            self.CumUV = self.CumUV
            self.FlagUV = self.FlagUV
        try:
            valor_float=float(line_array[4])
            if valor_float >= 0 and valor_float <= 5000:
                self.Height = float(line_array[4]) + self.Height
                self.FlagHeight = self.FlagHeight + 1
            else:
                self.Height = self.Height
                self.FlagHeight = self.FlagHeight
        except:
            self.CumUV = self.CumUV
            self.FlagUV = self.FlagUV

        self.LastReading=datetime.now()
        #self.CumTemperature = float(line_array[0]) + self.CumTemperature
        #self.FlagTemperature = self.FlagTemperature + 1
        #self.CumHumidity = float(line_array[1])+self.CumHumidity
        #self.FlagHumidity =self.FlagHumidity + 1
        #self.CumCo2 = float(line_array[2])+self.CumCo2
        #self.FlagCo2 = self.FlagCo2 + 1
        #self.CumUV = float(line_array[3]) + self.CumUV
        #self.FlagUV = self.FlagUV+1
        #self.LastReading=datetime.now()

    def Reset(self):
        self.CumTemperature = 0
        self.FlagTemperature = 0
        self.CumHumidity = 0
        self.FlagHumidity = 0
        self.CumCo2 = 0
        self.FlagCo2 = 0
        self.CumUV = 0
        self.FlagUV = 0
        self.Height = 0
        self.FlagHeight = 0

    def CheckTime(self, line_array):
        CurrentTime=datetime.now()
        if not self.LastReading:
            self.SaveReading(line_array)
        if CurrentTime - self.LastReading > timedelta(minutes=self.TimeStep):
            self.SaveReading(line_array)
    
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

