import pandas as pd
import datetime
import serial
import math
from csv import writer
from datetime import date
from datetime import datetime
import time
import SRH
from SRH.WaterLevel import WaterLevel
import subprocess

command = 'dmesg | grep -v disconnect | grep -Eo "ttyUSB." | tail -1'
output = subprocess.check_output(command, shell=True, executable='/bin/bash')
result = output.decode().strip()
print(result)
path_antena = '/dev/'+ result

WL = WaterLevel()

PID=SRH.PID(0)

PID.savePID()

# dmesg | grep -v disconnect| grep -Eo "tty(ACM|USB)." | tail -1
ser = serial.Serial('/dev/ttyACM0',9600, timeout=0.5)

ser.flush()
time.sleep(1)
#ser.flushInput()
Ard_RX = serial.Serial(path_antena, 9600, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
Ard_RX.flushInput()
Ard_RX.flushOutput()
time.sleep(1)


fitxer_log= "/home/pi/Desktop/Sirah/Logdic4.txt"

# Inicialization of log element
log=SRH.LogSirah()

# Inicialization of Actuators element
AS=SRH.StatusActuators()
file=open(fitxer_log, "a")
file.write("Inicialitzats els actuadors \n")
file.close()
LS=SRH.LocalStor()

#Inicialization of KcUpdate element
ETCLastUpdate=SRH.UpdateETC() #Element that manages last ETC update
ETCCalculation=SRH.ETC() #Element that calculate the ETC

file=open(fitxer_log, "a")
file.write("Inicialitzat l'element Kc_Update \n")
file.close()

#Initialize lines

L1=SRH.Line(1)


file=open(fitxer_log, "a")
file.write("L1 Inicialitzada \n")
file.close()

L2=SRH.Line(2)

file=open(fitxer_log, "a")
file.write("L2 Inicialitzada \n")
file.close()

L3=SRH.Line(3)

file=open(fitxer_log, "a")
file.write("L3 Inicialitzada \n")
file.close()

L4=SRH.Line(4)

file=open(fitxer_log, "a")
file.write("L4 Inicialitzada \n")
file.close()
#Initialize counter
TimeCounter=SRH.TimeCounter()
y=0
lp=1

#Inicialization of the loop
while(True):
    print("inici loop")
    print(lp)
    lp=lp+1
    #Update Lines
    L1.getConfig()
    
    file=open(fitxer_log, "a")
    file.write("Get config L1 ok \n")
    file.close()
    
    L2.getConfig()
        
    file=open(fitxer_log, "a")
    file.write("Get config L2 ok \n")
    file.close()
    
    L3.getConfig()
        
    file=open(fitxer_log, "a")
    file.write("Get config L3 ok \n")
    file.close()
    
    L4.getConfig()
        
    file=open(fitxer_log, "a")
    file.write("Get config L4 ok \n")
    file.close()
    
    
    #Recieve data
    #t="D"+"\n"
    #msg=t.encode('latin-1')
    #ser.write(msg)
    #send_string=("D")
    AS.UpdateAll()
        
    file=open(fitxer_log, "a")
    file.write("Update ok \n")
    file.close()
    TimeCounter.CheckTime(AS.Actions())
    t=str(AS.Actions())+",D"
    print(t)
    msg=t.encode('latin-1')
  
    ser.flushInput()
    ser.flushOutput()
    ser.write(msg)

    print(msg)

    time.sleep(0.2)
    #ser.write(send_string.encode('latin-1'))
    #print(send_string)
    #time.sleep(1)
    #lineBytes = ser.readline()
    #line = lineBytes.decode('latin-1').strip()
    #print(line)
    
#     no_valor = True
#     while no_valor:
#        with serial.Serial('/dev/ttyACM0',9600, timeout=0.5) as s:
#            s.flush()
#            cm=s.readline().decode('latin-1').rstrip()
#            print(cm)
#            if cm != "":
#                no_valor = False
    
#     line=ser.readline().decode('latin-1').rstrip()
#     print("xxxxxxxxxxxxxxxxx")
#     print(type(line))
#     print("xxxxxxxxxxxxxxxxx")
#     line_array = line.split(',')
#     print(line_array)
    cm = WL.SaveCurrentLevel()
    
    
    
    
    
    with serial.Serial(path_antena, 9600, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) as s:
        try:
            linea_llegida = s.readline().decode('latin-1').rstrip()
            llista = linea_llegida.split(",")
            llista.append(cm)
        except:
            pass 
        print(llista)
        


    if (len(llista)>3):

        LS.CheckTime(llista)
    else:
           
        y=y+1
        current=datetime.now()
        file=open("/home/pi/Desktop/Sirah/Logs/Dades" + "LogVectors.txt", "a")
        file.write("Vector incomplet rebut: " + str(current) )
        file.write("\n")
        file.write("Vector incomplet rebut: " + str(len(llista)) + " - " + str(y))
        file.write("\n")
        file.close()

    CurrentTime=datetime.now()
    CurrentSec = int(CurrentTime.strftime('%S'))
    
    if (CurrentSec%1==0):
        print(CurrentTime)
        print("Store:")
        print(LS.average())
        print(LS.FlagTemperature)
        print("Local:")
        print(LS.TempStor.average())
        print(LS.TempStor.FlagTemperature)
        print(LS.TempStor.Height)
        print(AS.Actions())
        print("")

#    WL.Fill_Tank(AS)

    #Tasks to be done at the begining of the day
    if ETCLastUpdate.CheckLastUpdate():
        
        #seria convenient generar un check lastupdate per cadalinea?
        if L1.Use==1:
            L1.setETC(ETCCalculation.ETC(L1.day(), L1.CropType))
            ETCLastUpdate.WriteKcLog("L1", L1.ETC)
            L1.getConfig()
                
            file=open(fitxer_log, "a")
            file.write("Get dins L1.USE == 1config L1 ok \n")
            file.close()
    
            L1.ToCsv()
            
            file=open(fitxer_log, "a")
            file.write("ToCSV l1 ok")
            file.close()
    
        if L2.Use== 1:
            L2.setETC(ETCCalculation.ETC(L2.day(), L2.CropType))
            ETCLastUpdate.WriteKcLog("L2", L2.ETC)
            L2.getConfig()
                
            file=open(fitxer_log, "a")
            file.write("Get dins L2.USE == 1config L2 ok \n")
            file.close()
    
            L2.ToCsv()
            
            file=open(fitxer_log, "a")
            file.write("ToCSV l2 ok")
            file.close()
    
        if L3.Use == 1:
            L3.setETC(ETCCalculation.ETC(L3.day(), L3.CropType))
            ETCLastUpdate.WriteKcLog("L3", L3.ETC)
            L3.getConfig()
            
                
            file=open(fitxer_log, "a")
            file.write("Get dins L3.USE == 1config L3 ok \n")
            file.close()
    
            L3.ToCsv()
            
            file=open(fitxer_log, "a")
            file.write("ToCSV l3 ok")
            file.close()
    
        if L4.Use == 1:
            L4.setETC(ETCCalculation.ETC(L4.day(), L4.CropType))
            ETCLastUpdate.WriteKcLog("L4", L4.ETC)
            L4.getConfig()
                
            file=open(fitxer_log, "a")
            file.write("Get dins L4.USE == 1config L4 ok \n")
            file.close()
    
            L4.ToCsv()
                
            file=open(fitxer_log, "a")
            file.write("ToCSV l4 ok")
            file.close()
    
        ETCLastUpdate.WriteLastUpdate()

    #Check if we have to turnoff Sirah
    Status=log.ReadStatus()
    
    if Status==0: 
        log.SirahOff()
        break
    
print("fin")
