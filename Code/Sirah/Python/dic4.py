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

TimeCounter=SRH.TimeCounter()
y=0
lp=1

#Inicialization of the loop
while(True):

    
    #Recieve data
    t="D"+"\n"
    msg=t.encode('latin-1')
    ser.write(msg)
    send_string=("D")

    file.close()
    TimeCounter.CheckTime(AS.Actions())
    t=str(AS.Actions())+",D"
    print(t)
    msg=t.encode('latin-1')
  
    ser.flushInput()
    ser.flushOutput()
    ser.write(msg)


    time.sleep(0.2)
    ser.write(send_string.encode('latin-1'))
    print(send_string)
    time.sleep(1)
    lineBytes = ser.readline()
    line = lineBytes.decode('latin-1').strip()
    print(line)
    
    no_valor = True
    while no_valor:
        with serial.Serial('/dev/ttyACM0',9600, timeout=0.5) as s:
            s.flush()
            cm=s.readline().decode('latin-1').rstrip()
            print(cm)
            if cm != "":
                no_valor = False
    
    line=ser.readline().decode('latin-1').rstrip()
    print("xxxxxxxxxxxxxxxxx")
    print(type(line))
    print("xxxxxxxxxxxxxxxxx")
    line_array = line.split(',')
    print(line_array)
    cm = WL.SaveCurrentLevel()


    WL.Fill_Tank(AS)
    #Check if we have to turnoff Sirah
    Status=log.ReadStatus()
    
    if Status==0: 
        log.SirahOff()
        break
    
print("fin")
