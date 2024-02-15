from datetime import datetime, timedelta, date
import time
import SRH
import sys
import SRH.StatusActuators
import SRH.WaterLevel

#PID=SRH.PID(sys.argv)
#PID.savePID()

#comprovar si existeix LOckfile
#comprovar que el procés està en marxa
#si està en marxa exit

# PID=SRH.PID(100)
# 
# PID.savePID()

L1 = SRH.Line(1) #1
L2 = SRH.Line(2) #1
L3 = SRH.Line(3) #1
L4 = SRH.Line(4) #1

# Cuántas acciones quiere planific28.30ar
#IrrigationProcess=SRH.IrrigationProcess(sys.argv)
ScheduledIrrigationProcess=SRH.LogScheduledIrrigation()

Actuators=SRH.StatusActuators()
Filled = 0

while ScheduledIrrigationProcess.ReadStatus()==1:
    while ScheduledIrrigationProcess.ReadStatus() == 1:
        today = date.today()
        tomorrow = today + timedelta(days=1)
        #print(IrrigationProcess.Path)
        #print(IrrigationProcess.L.Path)
        ScheduledIrrigationProcess.IrrigationActions()

        # Itera a través de cada acción y espera hasta que llegue la hora correspondiente
        for ScheduledIrrigationProcess.action, ScheduledIrrigationProcess.ScheduledIrrigationTime in ScheduledIrrigationProcess.actions:
            # Espera hasta que llegue la hora deseada
            print("Següent rec: " + str(ScheduledIrrigationProcess.action))
            while datetime.now() < ScheduledIrrigationProcess.action:
                print("Waiting")
                time.sleep(5)
                if (ScheduledIrrigationProcess.CheckTest()):
                    #IrrigationProcess.SetNextUpdate()
                    break
            if (ScheduledIrrigationProcess.CheckTest()):
                #IrrigationProcess.SetNextUpdate()
                break
            delta = datetime.now() - ScheduledIrrigationProcess.action
            print(ScheduledIrrigationProcess.ScheduledIrrigationTime*60)
            print(delta)
            # Ejecuta la acción correspondiente
            if (ScheduledIrrigationProcess.CheckDelta()):
                    ScheduledIrrigationProcess.LogStartAction()
                    if (ScheduledIrrigationProcess.Irrigate_L1()):
                        L1.setStateValve(1)
                    if (ScheduledIrrigationProcess.Irrigate_L2()):
                        L2.setStateValve(1)
                    if (ScheduledIrrigationProcess.Irrigate_L3()):
                        L3.setStateValve(1)
                    if (ScheduledIrrigationProcess.Irrigate_L4()):    
                        L4.setStateValve(1)
                    Actuators.SetPump(1)
                    print("Tiempo de riego:" + str(ScheduledIrrigationProcess.ScheduledIrrigationTime))
                    time.sleep(ScheduledIrrigationProcess.ScheduledIrrigationTime*60)
                    L1.setStateValve(0)
                    L2.setStateValve(0)
                    L3.setStateValve(0)
                    L4.setStateValve(0)
                    Actuators.SetPump(0)
                    ScheduledIrrigationProcess.LogFinishAction()
                    print("fin")
            else:
                print("Tard!")

            if (ScheduledIrrigationProcess.CheckTest()):
                #IrrigationProcess.SetNextUpdate()
                break
        print("Stop")
        now = date.today()
        print (now)
        print (tomorrow)
        #if (ScheduledIrrigationProcess.CheckUpdate()):
            #ScheduledIrrigationProcess.SetNextUpdate()
        #    print("++++++++++++++++++++++++++++++++++++++")
        #    print("Updating")
        #    print("++++++++++++++++++++++++++++++++++++++")
        #    break
        while now<tomorrow:
            print("esperant a demà")
            print(ScheduledIrrigationProcess.CheckTest())
            if (ScheduledIrrigationProcess.CheckTest()):
                break
            time.sleep(60)
            now = date.today()
        
        if (ScheduledIrrigationProcess.CheckTest()):
            #ScheduledIrrigationProcess.SetNextUpdate()
            time.sleep(6)
            print("++++++++++++++++++++++++++++++++++++++")
            print("Updating v2")
            print("++++++++++++++++++++++++++++++++++++++")
            break
        print("++++++++++++++++++++++++++++++++++++++")
        print("Nou dia de reg")
        print("++++++++++++++++++++++++++++++++++++++")
        time.sleep(6)