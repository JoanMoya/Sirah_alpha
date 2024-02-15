from datetime import datetime, timedelta, date
import time
import SRH

# Cuántas acciones quiere planificar
ETCCalculation=SRH.ETC() #Element that calculate the ETC
L=SRH.Line("L1")

while L.getUse()==1:
    L = SRH.Line("L1")
    L.day()
    day=L.day
    L.setETC(ETCCalculation.ETC(day, L.CropType))
    L.setET0(ETCCalculation.ETO())
    L.setkc(ETCCalculation.Kc(L.day, L.CropType))
    L.Irrigation()
    L.DailyIrrigationTimes()
    num_acciones=int(L.DailyIrrigationTimes)
    InitialHour=L.getInitialHour()
    FinalHour=L.getFinalHour()

    TotalDuration=FinalHour-InitialHour
    Period=TotalDuration/num_acciones
    HalfPeriod=Period/2

    #Corrección primeros dias
    if day<15:
        DailyIrrigationTimes=6
    else:
        DailyIrrigationTimes = L.DailyIrrigationTimes

    #Calcular agua por vez
    Water=L.irrigation/DailyIrrigationTimes

    Minutes=Water/(L.Dripper*L.Plants)*60

    if Minutes<2:
        Minutes=2


    # Crea una lista vacía para almacenar las acciones
    acciones = []

    # Obtener la fecha actual
    fecha_actual = date.today()

    # Crear un objeto datetime con la hora y fecha actual
    IrrigationTime = datetime.combine(fecha_actual, InitialHour.time())
    IrrigationTime = IrrigationTime+HalfPeriod

    # Itera a través de cada acción y solicita la acción y la hora correspondiente
    for i in range(num_acciones):
        accion = IrrigationTime
        IrrigationTime=IrrigationTime+Period
        acciones.append((accion, Minutes))

    print(acciones)
    # Ordena las acciones por hora
    acciones_ordenadas = sorted(acciones, key=lambda x: x[1])

    # Crear un objeto timedelta que represente 30 minutos
    treinta_minutos = timedelta(minutes=40)

    # Itera a través de cada acción y espera hasta que llegue la hora correspondiente
    for accion, Minutes in acciones_ordenadas:
        hora_deseada = accion
        print(accion)
        # Espera hasta que llegue la hora deseada
        while datetime.now() < hora_deseada:
            print("Waiting")
            time.sleep(60)

        delta = datetime.now() - hora_deseada
        print(delta)
        # Ejecuta la acción correspondiente
        if (delta < treinta_minutos):
            print(f"¡Es hora de {accion}!")
            current = datetime.now()
            #file = open("/home/pi/Desktop/Sirah/" + "LogSirah.txt", "a")
            file = open("C:\\Users\\marcel\\Documents\\GitHub\\sirah\\Sirah\\" + "LogSirah.txt", "a")
            file.write("Irrigation process on at " + L.LineName + ": " + str(current))
            file.write("\n")
            file.close()
            L.setStateValve(1)
            time.sleep(Minutes)
            L.setStateValve(0)
            current = datetime.now()
            file = open("C:\\Users\\marcel\\Documents\\GitHub\\sirah\\Sirah\\" + "LogSirah.txt", "a")
            file.write("Irrigation process off at " + L.LineName + ": " + str(current))
            file.write("\n")
            file.close()
            print("fin")
        else:
            print("Tard!")

    print("Stop")
    time.sleep(60)