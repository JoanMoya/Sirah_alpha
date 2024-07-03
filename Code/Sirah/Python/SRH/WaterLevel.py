from datetime import datetime, timedelta, date
import time
from SRH import StatusActuators
import sys
import serial



class WaterLevel: 
    
    def __init__(self):

        self.CurrentLevel = 0
        self.MaximumWaterLevel = 20 #This value has to be substituted with the correct one
        self.MinimumWaterLevel = 40#This value has to be subsitituted with the correct one
        self.Filled = 0
        self.Filling = 0
#         self.FillingTime = 0.0
        self.NutrientTime = 30
        self.File = "/home/pi/Desktop/Sirah/Logs/Dades/Height_water.txt"
        self.CurrentValue = 0
        
    def SetMaximumLevel(self,MaxLvl):
        ##LLegirem de file quin es el lvl a posar
        self.MaximumWaterLevel = MaxLvl
    
    def SetMinimumLevel(self, MinLvl):
        ##LLegirem de file quin es el lvl a posar
        self.MinimumWaterLevel = MinLvl
        
    def GetMaximumLevel(self):
        ##LLegirem de file quin es el lvl a posar
        return(self.MaximumWaterLevel)
    
    def GetMinimumLevel(self):
        ##LLegirem de file quin es el lvl a posar
        return(self.MinimumWaterLevel)
    def GetFile(self):
        return(self.File)
    
    def GetCurrentLevel(self):
        file_path = "/home/pi/Desktop/Sirah/Logs/Dades/Height_water.txt"
        with open(file_path) as file:
            for line in reversed(list(file)):
                height = float(line.rstrip())
                self.CurrentLevel = height
                return height
                break
            
    def SaveCurrentLevel(self):
        no_valor = True
        while no_valor:
            with serial.Serial('/dev/ttyACM0',9600, timeout=0.5) as s:
               s.flush()
               cm=s.readline().decode('latin-1').rstrip()
               if cm != "":
                   no_valor = False
                   self.CurrentValue = cm
               
        with open("/home/pi/Desktop/Sirah/Logs/Dades/Height_water.txt","a") as file_height:
            file_height.write(cm+"\n")
        return cm 
    
    def ReadLastLevel(self):
        try:
            with open(self.GetFile(), 'r') as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    last_number = float(last_line)
                    return last_number
                else:
                    print("The file is empty.")
                    return None
        except FileNotFoundError:
            print(f"File /home/pi/Desktop/Sirah/Logs/Dades/Height_water.txt not found.")
            return None
        except ValueError:
            print(f"The last line in /home/pi/Desktop/Sirah/Logs/Dades/Height_water.txt does not contain a valid number.")
            return None


    def SaveLevel(self, level):
        with open("/home/pi/Desktop/Sirah/Logs/Dades/Height_water.txt","a") as file_height:
                file_height.write(level+"\n")
                
    def IsFilled(self):
        if self.Filled == 0:
            return False
        else:
            return True
    
    def SetFilled(self, value):
        self.Filled = value
        
    def SetFilling(self, value):
        self.Filling = value
    
    def IsFilling(self):
        if self.Filling == 0:
            return False
        else:
            return True
    
    def GetFilling(self):
        if self.Filling == 0:
            return False
        else:
            return True
#         
#     def SetFillingTime(self, init_time, end_time)
#         self.FillingTime = round(end_time - init_time,2)
#     
#     def GetFillingTime(self):
#         return(self.FillingTime)
    
#     def SetNutrientTime(self,value):
#         self.NutrientTime = (value*1)/100
    
    def GetNutrientTime(self):
        return(self.NutrientTime)
    
    def Fill_Tank(self, Actuadors):
        print(self.ReadLastLevel())
        self.SaveCurrentLevel()
        current_level = self.ReadLastLevel()
        if current_level > self.GetMinimumLevel():
            self.SetFilled(0)
            self.SetFilling(1)
            while self.GetFilling() == 1:
                Actuadors.SetFillingValve(1)
                self.SaveCurrentLevel()
                current_level = self.ReadLastLevel()
                if(current_level < self.GetMaximumLevel()):
                    Actuadors.SetPump(0)
                    Actuadors.SetFillingValve(0)
                    Actuadors.SetNutrient1(1)
                    time.sleep(30)
                    Actuadors.SetNutrient1(0)
                    self.SetFilled(1)
                    self.SetFilling(0)
                else:
                    print(self.ReadLastLevel())
        else:
            print(self.ReadLastLevel())
                    
                
            
        return(None)