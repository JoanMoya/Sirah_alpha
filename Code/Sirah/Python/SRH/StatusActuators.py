
   #Class StatusActuators

class StatusActuators:
    file = "/home/pi/Desktop/Sirah"
    def __init__(self):
        self.PathPump=self.file + "/Auxiliars/Test/Pump.txt"
        self.PathFillingValve=self.file + "/Auxiliars/Test/FillingValve.txt"
        self.PathRecirculationValve=self.file + "/Auxiliars/Test/RecirculationValve.txt"
        self.PathLeachedValve=self.file + "/Auxiliars/Test/LeachedValve.txt" #Be sure this file exists
        self.PathNutrient1=self.file + "/Auxiliars/Test/Nutrient1.txt"
        self.PathNutrient2=self.file + "/Auxiliars/Test/Nutrient2.txt"
        self.PathNutrient3=self.file + "/Auxiliars/Test/Nutrient3.txt" #Be sure this file exists
        self.PathL1=self.file + "/Auxiliars/L/L1/StateValve.txt"
        self.PathL2=self.file + "/Auxiliars/L/L2/StateValve.txt"
        self.PathL3=self.file + "/Auxiliars/L/L3/StateValve.txt"
        self.PathL4=self.file + "/Auxiliars/L/L4/StateValve.txt"
        self.PathL5=self.file + "/Auxiliars/L/L1/StateValve.txt"
        self.PathL6=self.file + "/Auxiliars/L/L2/StateValve.txt"
        self.PathL7=self.file + "/Auxiliars/L/L3/StateValve.txt"
        self.PathL8=self.file + "/Auxiliars/L/L4/StateValve.txt" #Be sure this file exists
        #self.ResetAll() #I'm not sure if this actions should be done. What happens when we restart the system?
        
    def ResetPump(self):
        file=open(self.PathPump, "w")
        state=0
        file.write(f"{state}")
        file.close()

    def ResetFillingValve(self):
        file=open(self.PathFillingValve, "w")
        file.write("0")
        file.close()

    def ResetRecirculationValve(self):
        file=open(self.PathRecirculationValve, "w")
        file.write("0")
        file.close()
        
    def ResetLeachedValve(self):
        file=open(self.PathLeachedValve, "w")
        file.write("0")
        file.close()

    def ResetPathNutrient1(self):
        file=open(self.PathNutrient1, "w")
        file.write("0")
        file.close()
        
    def ResetPathNutrient2(self):
        file=open(self.PathNutrient2, "w")
        file.write("0")
        file.close()
        
    def ResetPathNutrient3(self):
        file=open(self.PathNutrient3, "w")
        file.write("0")
        file.close()
        
    def ResetPathL1(self):
        file=open(self.PathL1, "w")
        file.write("0")
        file.close()
        
    def ResetPathL2(self):
        file=open(self.PathL2, "w")
        file.write("0")
        file.close()
        
    def ResetPathL3(self):
        file=open(self.PathL3, "w")
        file.write("0")
        file.close()
        
    def ResetPathL4(self):
        file=open(self.PathL4, "w")
        file.write("0")
        file.close()
        
    def ResetPathL5(self):
        file=open(self.PathL5, "w")
        file.write("0")
        file.close()
        
    def ResetPathL6(self):
        file=open(self.PathL6, "w")
        file.write("0")
        file.close()
        
    def ResetPathL7(self):
        file=open(self.PathL7, "w")
        file.write("0")
        file.close()
        
    def ResetPathL8(self):
        file=open(self.PathL8, "w")
        file.write("0")
        file.close()
        
    def ResetAll(self):
        self.ResetPump()
        self.ResetFillingValve()
        self.ResetRecirculationValve()
        self.ResetLeachedValve()
        self.ResetPathNutrient1()
        self.ResetPathNutrient2()
        self.ResetPathNutrient3()
        self.ResetPathL1()
        self.ResetPathL2()
        self.ResetPathL3()
        self.ResetPathL4()
        self.ResetPathL5()
        self.ResetPathL6()
        self.ResetPathL7()
        self.ResetPathL8()        
        
    def SetPump(self, PumpStatus):
        self.PumpStatus=PumpStatus
        file=open(self.PathPump, "w")
        file.write(str(PumpStatus))
        file.close()

    def SetFillingValve(self, FillingValveStatus):
        self.FillingValveStatus=FillingValveStatus
        file=open(self.PathFillingValve, "w")
        file.write(str(FillingValveStatus))
        file.close()

    def SetRecirculationValve(self, RecirculationValveStatus):
        self.RecirculationValveStatus=RecirculationValveStatus
        file=open(self.PathRecirculationValve, "w")
        file.write(str(RecirculationValveStatus))
        file.close()
    
    def SetLeachedValve(self, LeachedValveStatus):
        self.LeachedValveStatus=LeachedValveStatus
        file=open(self.PathLeachedValve, "w")
        file.write(str(LeachedValveStatus))
        file.close()  

    def SetNutrient1(self, Nutrient1Status):
        self.Nutrient1Status=Nutrient1Status
        file=open(self.PathNutrient1, "w")
        file.write(str(Nutrient1Status))
        file.close()

    def SetNutrient2(self, Nutrient2Status):
        self.Nutrient2Status=Nutrient2Status
        file=open(self.PathNutrient2, "w")
        file.write(str(Nutrient2Status))
        file.close()
        
    def SetNutrient3(self, Nutrient3Status):
        self.Nutrient3Status=Nutrient3Status
        file=open(self.PathNutrient3, "w")
        file.write(str(Nutrient3Status))
        file.close()

    def SetL1Status(self, L1Status):
        self.L1Status=L1Status
        file=open(self.PathL1, "w")
        file.write(str(L1Status))
        file.close()
        
    def SetL2Status(self, L2Status):
        self.L2Status=L2Status
        file=open(self.PathL2, "w")
        file.write(str(L2Status))
        file.close()
        
    def SetL3Status(self, L3Status):
        self.L3Status=L3Status
        file=open(self.PathL3, "w")
        file.write(str(L3Status))
        file.close()
        
    def SetL4Status(self, L4Status):
        self.L4Status=L4Status
        file=open(self.PathL4, "w")
        file.write(str(L4Status))
        file.close()
        
    def SetL5Status(self, L5Status):
        self.L5Status=L5Status
        file=open(self.PathL5, "w")
        file.write(str(L5Status))
        file.close()
        
    def SetL6Status(self, L6Status):
        self.L6Status=L6Status
        file=open(self.PathL6, "w")
        file.write(str(L6Status))
        file.close()
            
    def SetL7Status(self, L7Status):
        self.L7Status=L7Status
        file=open(self.PathL7, "w")
        file.write(str(L7Status))
        file.close()
        
    def SetL8Status(self, L8Status):
        self.L8Status=L8Status
        file=open(self.PathL8, "w")
        file.write(str(L8Status))
        file.close()

    def UpdatePump(self):
        try:
            file=open(self.PathPump)
            self.PumpStatus=float(file.read())
            file.close()
        except:
            pass
    def UpdateRecirculationValve(self):
        try:
            file=open(self.PathRecirculationValve)
            self.RecirculationValveStatus=float(file.read())
            file.close()
        except:
            pass
    def UpdateFillingValve(self):
        try:
            file=open(self.PathFillingValve)
            self.FillingValveStatus=float(file.read())
            file.close()
        except:
            pass
    def UpdateLeachedValve(self):
        try:
            file=open(self.PathLeachedValve)
            self.LeachedValveStatus=float(file.read())
            file.close()
        except:
            pass
    def UpdateNutrient1(self):
        try:
            file=open(self.PathNutrient1)
            self.Nutrient1Status=float(file.read())
            file.close()
        except:
            pass
    def UpdateNutrient2(self):
        try:
            file=open(self.PathNutrient2)
            self.Nutrient2Status=float(file.read())
            file.close()
        except:
           pass
    def UpdateNutrient3(self):
        try:
            file=open(self.PathNutrient3)
            self.Nutrient3Status=float(file.read())
            file.close()
        except:
            pass
    def UpdateL1Status(self):
        try:
            file=open(self.PathL1)
            self.L1Status = float(file.read())
            file.close()
        except:
            pass
    def UpdateL2Status(self):
        try:
            file=open(self.PathL2)
            self.L2Status = float(file.read())
            file.close()
        except:
            pass
    def UpdateL3Status(self):
        try:
            file=open(self.PathL3)
            self.L3Status = float(file.read())
            file.close()
        except:
            pass
    def UpdateL4Status(self):
        try:
            file=open(self.PathL4)
            self.L4Status = float(file.read())
            file.close()
        except:
            pass
        
    def UpdateL5Status(self):
        try:
            file=open(self.PathL5, "r")
            self.L5Status = float(file.read())
            file.close()
        except:
            pass
    def UpdateL6Status(self):
        try:
            file=open(self.PathL6)
            self.L6Status = float(file.read())
            file.close()
        except:
            pass
    def UpdateL7Status(self):
        try:
            file=open(self.PathL7)
            self.L7Status = float(file.read())
            file.close()
        except:
            pass
    def UpdateL8Status(self):
        try:
            file=open(self.PathL8)
            self.L8Status = float(file.read())
            file.close()
        except:
            pass
    def UpdateAll(self):
        self.UpdatePump()
        self.UpdateRecirculationValve()
        self.UpdateFillingValve()
        self.UpdateLeachedValve()
        self.UpdateNutrient1()
        self.UpdateNutrient2()
        self.UpdateNutrient3()
        self.UpdateL1Status()
        self.UpdateL2Status()
        self.UpdateL3Status()
        self.UpdateL4Status()
        self.UpdateL5Status()
        self.UpdateL6Status()
        self.UpdateL7Status()
        self.UpdateL8Status()
        
        
    def Actions(self):
        self.message= str(int(self.PumpStatus)) + "," + str(int(self.FillingValveStatus)) + "," + str(int(self.RecirculationValveStatus)) + "," + str(int(self.LeachedValveStatus)) + "," +str(int(self.Nutrient1Status))+ "," + str(int(self.Nutrient2Status)) + "," + str(int(self.Nutrient3Status)) + "," +str(int(self.L1Status))+","+str(int(self.L2Status))+","+str(int(self.L3Status))+","+str(int(self.L4Status))+ "," +str(int(self.L5Status))+","+str(int(self.L6Status))+","+str(int(self.L7Status))+","+str(int(self.L8Status))
        return self.message