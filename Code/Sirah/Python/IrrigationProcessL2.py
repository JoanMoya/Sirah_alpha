from datetime import datetime, timedelta, date
import time
import SRH
import sys

#PID=SRH.PID(sys.argv)
#PID.savePID()

PID=SRH.PID(2)

#if PID.Exists() and PID.IsActive():
#    exit()

PID.savePID()

# Cuántas acciones quiere planificar
#IrrigationProcess=SRH.IrrigationProcess(sys.argv)
IrrigationProcess=SRH.IrrigationProcess(2)
Actuators=SRH.StatusActuators()


while IrrigationProcess.L.getUse()==1:
    while IrrigationProcess.L.getUse() == 1:
        today = date.today()
        tomorrow = today + timedelta(days=1)
        #print(IrrigationProcess.Path)
        #print(IrrigationProcess.L.Path)
        IrrigationProcess.Update()
        IrrigationProcess.IrrigationActions()

        # Itera a través de cada acción y espera hasta que llegue la hora correspondiente
        for IrrigationProcess.action, IrrigationProcess.Minutes in IrrigationProcess.actions:
            # Espera hasta que llegue la hora deseada
            print("Següent rec: " + str(IrrigationProcess.action))
            while datetime.now() < IrrigationProcess.action:
                print("Waiting")
                time.sleep(60)
            delta = datetime.now() - IrrigationProcess.action
            print(IrrigationProcess.Minutes*60)
            print(delta)
            # Ejecuta la acción correspondiente
            if (IrrigationProcess.CheckDelta()):
                print(f"¡Es hora de {IrrigationProcess.action}!")
                IrrigationProcess.LogStartAction()
                IrrigationProcess.L.setStateValve(1)
                Actuators.SetPump(1)
                print("Tiempo de riego:" + str(IrrigationProcess.Minutes))
                time.sleep(IrrigationProcess.Minutes*60)
                IrrigationProcess.L.setStateValve(0)
                Actuators.SetPump(0)
                IrrigationProcess.LogFinishAction()
                print("fin")
            else:
                print("Tard!")

            if (IrrigationProcess.CheckUpdate()):
                #IrrigationProcess.SetNextUpdate()
                break
        print("Stop")
        now = date.today()
        print (now)
        print (tomorrow)
        if (IrrigationProcess.CheckUpdate()):
            IrrigationProcess.SetNextUpdate()
            print("++++++++++++++++++++++++++++++++++++++")
            print("Updating")
            print("++++++++++++++++++++++++++++++++++++++")
            break
        while now<tomorrow:
            print("esperant a demà")
            print(IrrigationProcess.CheckUpdate())
            if (IrrigationProcess.CheckUpdate()):
                break
            time.sleep(60*60)
            now = date.today()
        
        if (IrrigationProcess.CheckUpdate()):
            IrrigationProcess.SetNextUpdate()
            time.sleep(6)
            print("++++++++++++++++++++++++++++++++++++++")
            print("Updating v2")
            print("++++++++++++++++++++++++++++++++++++++")
            break
        print("++++++++++++++++++++++++++++++++++++++")
        print("Nou dia de reg")
        print("++++++++++++++++++++++++++++++++++++++")
        time.sleep(6)
