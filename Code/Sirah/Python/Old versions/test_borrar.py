import SRH
import signal

# Crea una lista vacía para almacenar las acciones
Irrigation_lines = []

for i in range(4):
    Irrigation_lines.append((SRH.Line(i+1), SRH.PID(i+1)))

while True:
    for Line in Irrigation_lines:
        if Line[0].getUse()==1:
            if (Line[1].processRunning()):
                pass
            else:
                #LokFile1.savePID()
                print("l'he obert")
        elif Line[0].getUse()==0:
            print(Line[1].processRunning())
            if (Line[1].processRunning()):
                Line[1].kill()
                print("l'he tancat")
            else:
                pass