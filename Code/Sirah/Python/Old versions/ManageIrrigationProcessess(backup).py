import SRH
import signal

# Crea una lista vacía para almacenar las acciones
Irrigation_lines = []

for i in range(4):
    Irrigation_lines.append((SRH.Line(i+1), SRH.PID(i+1)))

#Line definition
#L1=SRH.Line(1)
#L2=SRH.Line("L2")
#L3=SRH.Line("L3")
#L4=SRH.Line("L4")

#Lockfiles controllers
#LokFile1=SRH.PID("L1")
#LookFile2=SRH.PID("L2")
#LookFile3=SRH.PID("L3")
#LookFile4=SRH.PID("L4")
while True:
    for Line in Irrigation_lines:
        if Line[0].getUse()==1:
            if (Line[1].processRunning()):
                pass
            else:
                #LokFile1.savePID()
                print("l'he obert")
        elif Line[0].getUse()==0:
            if (Line[1].processRunning()):
                Line[1].kill()
                print("l'he tancat")
            else:
                pass




while True:
    for Line in Irrigation_lines
        if L1.getUse()==1:
            if (LokFile1.processRunning()):
                pass
            else:
                #LokFile1.savePID()
                print("l'he obert")
        elif L1.getUse()==0:
            if (LokFile1.processRunning()):
                LokFile1.kill()
                print("l'he tancat")
            else:
                pass



    # Obtener la fecha actual
    self.fecha_actual = date.today()

    # Crear un objeto datetime con la hora y fecha actual
    self.IrrigationTime = datetime.combine(self.fecha_actual, self.InitialHour.time())
    self.IrrigationTime = self.IrrigationTime + self.HalfPeriod

    # Itera a través de cada acción y solicita la acción y la hora correspondiente
    for i in range(self.DailyIrrigationProcesses):
        self.action = self.IrrigationTime
        self.IrrigationTime = self.IrrigationTime + self.Period
        self.actions.append((self.action, self.Minutes))
