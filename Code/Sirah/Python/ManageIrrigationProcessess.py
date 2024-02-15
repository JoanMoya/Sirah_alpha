import SRH
import os

# List to append lines
Irrigation_lines = []

for i in range(4):
    Irrigation_lines.append((SRH.Line(i+1), SRH.PID(i+1)))

ScheduledIrrigation=SRH.LogScheduledIrrigation()
ManualScheduledIrrigation=((ScheduledIrrigation, SRH.PID(100)))

#Loop process. We check if Line is in use and we open or kill the process.
while True:
    for Line in Irrigation_lines:
        if Line[0].getUse()==1:
            if (Line[1].processRunning()):
                #print("obert")
                pass
            else:
                #LokFile1.savePID()
                #print("l'he obert")
                pass
        elif Line[0].getUse()==0:
            #print(Line[1].processRunning())
            if (Line[1].processRunning()):
                try:
                    Line[1].kill()
                except:
                    pass
                Line[0].setStateValve(0)
                #print("tancat")
                #os.remove()
                #print("l'he tancat")
            else:
                pass
    
    if ManualScheduledIrrigation[0].ReadStatus() == 1:
        if (ManualScheduledIrrigation[1].processRunning()):
            pass
        else:
            pass
    elif ManualScheduledIrrigation[0].ReadStatus() == 0:
        # print(Line[1].processRunning())
        if (ManualScheduledIrrigation[1].processRunning()):
            try: 
                ManualScheduledIrrigation[1].kill()
            except:
                pass
            ManualScheduledIrrigation[0].StatusTestOff()
        else:
            pass