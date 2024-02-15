import pandas as pd
import datetime
import serial
import math
from csv import writer
from datetime import date
from datetime import datetime
import time
import SRH

# dmesg | grep -v disconnect| grep -Eo "tty(ACM|USB)." | tail -1
arduino = serial.Serial('/dev/ttyACM0',9600)

#ser.flushInput()

def fill_conditions(line_array):
    if len(line_array) == 4:
        temperature = float(line_array[0])
        humidity = float(line_array[1])
        co2 = float(line_array[2])
        uv = float(line_array[3])
        today = date.today()
        day = today.strftime('%d/%m/%Y')

        filename = "/home/pi/Desktop/log.csv"
            
        now = datetime.now()
        current_h = now.strftime('%H')
        current_min = now.strftime('%M')
        current_s = now.strftime('%S')

        if int(current_min) == 00 and int(current_s) == 00:
            if int(current_h) >= 6 and int(current_h) < 18:
                DN = 1
            else:
                DN = 0
            with open(filename, 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow([day, temperature, humidity, co2, uv, DN])
                f_object.close()
                
    return None

def sirah(current_kc, df):
    beta1 = 0.733367
    beta2 = -0.022568
    
    df0 = pd.read_csv('/home/pi/Desktop/date.csv', header = None)
    
    today = df0[0].loc[len(df0[0])-1]
    prev_today = df0[0].loc[len(df0[0])-2]

    temp = 0
    flag = 0
    av_temp = None

    if prev_today != today:
        for i in range(0,len(df['day'])-1):
            if df['day'].loc[i] == prev_today:
                temp = temp + df['temperature'].loc[i]
                flag = flag + 1
        if temp != 0:
            av_temp = round(temp/(flag),2)
        else:
            temp=20
        
        ET0 = 1/(beta1 + av_temp*beta2)
        ETc = round(ET0*current_kc,3)
        
        return ETc

def date_format(df):
    df[0] = pd.to_datetime(df[0], format = "%d/%m/%Y")
    date = df.loc[len(df)- 1, 0]
    return date

def select(crop_type):
    h = open(crop_type, 'r')
    content = h.readline()
    for line in content:
        for i in line:
            if i.isdigit() == True:
                option = int(i)
    return option

def via(option, date):
    if option == 1:
        df_crop = pd.read_csv('/home/pi/Desktop/Tomato.csv')
    elif option == 2:
        df_crop = pd.read_csv('/home/pi/Desktop/Lettuce.csv')
    elif option == 3:
        df_crop = pd.read_csv('/home/pi/Desktop/Jew.csv')
    
    current_day = date0 - date
    current_day = current_day.days + 1

    kc = df_crop['Kc']
    current_kc = kc.loc[current_day - 1]

    days = df_crop['Día']
    total_days = days.loc[len(days) - 1]

    remaining = total_days - current_day
    progress = round(current_day/total_days*100,2)
    
    return current_day, current_kc, remaining, progress
    
def via_fill(filename, option, current_day, current_kc, remaining, progress):
    df_via = pd.read_csv(filename)
    pre_option = df_via['option'].loc[len(df_via['option']) - 1]
    pre_current_day = df_via['day'].loc[len(df_via['day']) - 1]
    
    if pre_current_day != current_day or pre_option != option:
        with open(filename, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([option, current_day, current_kc, remaining, progress])
            f_object.close()
        
    return None

def evapo_fill(filename, ETc):
    df_via = pd.read_csv(filename)
    pre_ETc = df_via['ETc'].loc[len(df_via['ETc']) - 1]
    
    if ETc != None:
        if pre_ETc != ETc:
            with open(filename, 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow([ETc])
    
    return None

def geo_mean(min, max):
    mean = math.sqrt(min*max)
    return mean

def LIV(x, ref):
    if x > 0:
        liv = math.log(x/ref)
    else:
        liv = 0
    return liv

def DN(R):
    if R != 0:
        dn = 1
    elif R == 0:
        dn = 0
    return dn

def GEQI(wT, wH, wC, wR, alivT, alivH, alivC, alivR):
    wNaliv = math.sqrt(wT*alivT*alivT + wH*alivH*alivH + wC*alivC*alivC + wR*alivR*alivR)
    
    if wNaliv <= 0.5:
        geqi = 100 - 200*wNaliv
    elif wNaliv > 0.5:
        geqi = 0
    geqi = round(geqi,3)
    return geqi

def compute_geqi(df_geqi):
        
    wT = 0.45
    wH = 0.1
    wC = 0.05
    wR = 0.4

    #T = df_geqi['temperature']
    T = df_geqi['temperature'] + 273.15
    Tmin = 286
    Tmax = 299
    Tref = geo_mean(Tmin, Tmax)

    H = df_geqi['humidity']
    Hmin = 60
    Hmax = 75
    Href = geo_mean(Hmin, Hmax)

    C = df_geqi['co2']
    Cmin = 340
    Cmax = 1000
    Cref = geo_mean(Cmin, Cmax)

    R = df_geqi['uv']*df_geqi['DN']
    Rmin = 70
    Rmax = 150
    Rref = geo_mean(Rmin, Rmax)

    df_geqi['livT'] = T.apply(LIV, ref = Tref)
    df_geqi['livH'] = H.apply(LIV, ref = Href)
    df_geqi['livC'] = C.apply(LIV, ref = Cref)
    df_geqi['livR'] = R.apply(LIV, ref = Rref)

    alivT = df_geqi['livT'].mean()
    alivH = df_geqi['livH'].mean()
    alivC = df_geqi['livC'].mean()
    alivR = df_geqi['livR'].sum()/df_geqi['DN'].sum()

    geqi = GEQI(wT, wH, wC, wR, alivT, alivH, alivC, alivR)
    
    df_prevgeqi = pd.read_csv('/home/pi/Desktop/geqi.csv')['geqi']
    prev_geqi = df_prevgeqi.loc[len(df_prevgeqi) - 2]
    
    now = datetime.now()
    current_min = now.strftime('%M')
    current_s = now.strftime('%S')
    
    if int(current_min) == 33 and int(current_s) == 00 and prev_geqi != geqi :
        with open('/home/pi/Desktop/geqi.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([geqi])
            f_object.close()
                
    #print(geqi)
    
    return None

# Inicialization of log element
log=SRH.LogSirah()

# Inicialization of Actuators element
AS=SRH.StatusActuators()

LS=SRH.LocalStor()

#Inicialization of the loop
while(True):
    #Recieve data
    t="1"
    print("1")
    if arduino.isOpen():
        print("{} connected!".format(arduino.port))
        try:
            arduino.write(t.encode())
            while arduino.inWaiting()==0: pass
            if arduino.inWaiting()>0:
                answer=arduino.readline()
                print(answer.decode())
                arduino.flushInput()
            print("1")                        
        except KeyboardInterrupt:
            print("KeyboardInterrupt has been caught.")
    
#    if ser.isOpen():        
#        t="data"
#        msg=t.encode('latin-1')
#        ser.write(msg)
        #time.sleep(0.5)
        #print(msg)
#        print(ser.inWaiting())
#        lineBytes = ser.readline()
#        line = lineBytes.decode('latin-1').strip()
#        line_array = line.split(',')
#        print(line)
#        fill_conditions(line_array)
#        ser.flushInput()
#        LS.CheckTime(line_array)

    df0 = pd.read_csv('/home/pi/Desktop/date.csv', header = None)
    date0 = date_format(df0)

    df = pd.read_csv('/home/pi/Desktop/log.csv')

    df1 = pd.read_csv('/home/pi/Desktop/day1.csv', header = None)
    date1 = date_format(df1)

    df2 = pd.read_csv('/home/pi/Desktop/day2.csv', header = None)
    date2 = date_format(df2)

    df3 = pd.read_csv('/home/pi/Desktop/day3.csv', header = None)
    date3 = date_format(df3)

    df4 = pd.read_csv('/home/pi/Desktop/day4.csv', header = None)
    date4 = date_format(df4)

    type1 = "/home/pi/Desktop/type1.txt"
    type2 = "/home/pi/Desktop/type2.txt"
    type3 = "/home/pi/Desktop/type3.txt"
    type4 = "/home/pi/Desktop/type4.txt"

    option1 = select(type1)
    current_day1, current_kc1, remaining1, progress1 = via(option1, date1)

    option2 = select(type2)
    current_day2, current_kc2, remaining2, progress2 = via(option2, date2)

    option3 = select(type3)
    current_day3, current_kc3, remaining3, progress3 = via(option3, date3)

    option4 = select(type4)
    current_day4, current_kc4, remaining4, progress4 = via(option4, date4)

    ETc1 = sirah(current_kc1, df)
    ETc2 = sirah(current_kc2, df)
    ETc3 = sirah(current_kc3, df)
    ETc4 = sirah(current_kc4, df)

    filename1 = "/home/pi/Desktop/via1.csv"
    via_fill(filename1, option1, current_day1, current_kc1, remaining1, progress1)
    filename1ETc = "/home/pi/Desktop/ETc1.csv"
    evapo_fill(filename1ETc, ETc1)

    filename2 = "/home/pi/Desktop/via2.csv"
    via_fill(filename2, option2, current_day2, current_kc2, remaining2, progress2)
    filename2ETc = "/home/pi/Desktop/ETc2.csv"
    evapo_fill(filename2ETc, ETc2)

    filename3 = "/home/pi/Desktop/via3.csv"
    via_fill(filename3, option3, current_day3, current_kc3, remaining3, progress3)
    filename3ETc = "/home/pi/Desktop/ETc3.csv"
    evapo_fill(filename3ETc, ETc3)

    filename4 = "/home/pi/Desktop/via4.csv"
    via_fill(filename4, option4, current_day4, current_kc4, remaining4, progress4)
    filename4ETc = "/home/pi/Desktop/ETc4.csv"
    evapo_fill(filename4ETc, ETc4)

    #df_geqi = pd.read_csv('/home/pi/Descargas/geqi - Full 1.csv')
    df_geqi = pd.read_csv('/home/pi/Desktop/log.csv')
    compute_geqi(df_geqi)
    
#    info = current_kc1(line).encode('latin-1')
#    ser.write(info)
    CurrentTime=datetime.now()
    CurrentSec = int(CurrentTime.strftime('%S'))
    
    AS.UpdateAll()
    
    if ser.isOpen():        
        t=str(AS.PumpStatus)
        msg=t.encode('latin-1')
        ser.write(msg)
        time.sleep(0.5)
        if ser.inWaiting()>0:
            lineBytes = ser.readline()
            line = lineBytes.decode('latin-1').strip()
            print(line)
    
    
    #t="dia"
    #ser.write(t.encode('latin-1'))
    #ser.write(AS.Actions().encode('latin-1'))
    
    CurrentTime=datetime.now()
    CurrentSec = int(CurrentTime.strftime('%S'))
    
    if (CurrentSec%10==0):
        print(CurrentTime)
        print("Store:")
        print(LS.average())
        print(LS.FlagTemperature)
        print("Local:")
        print(LS.TempStor.average())
        print(LS.TempStor.FlagTemperature)
        print(AS.Actions())
    
    Status=log.ReadStatus()
    
    if Status==0: 
        log.SirahOff()
        break
    
