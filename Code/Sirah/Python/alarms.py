import csv


Path = "/home/pi/Desktop/Sirah/Auxiliars/"

   
Actuators=[]
Actuators.append([Path + "Test/PumpTime.txt", Path + "Test/PumpMaxTime.txt", "pump"])
Actuators.append([Path + "Test/FillingValveTime.txt", Path + "Test/FillingValveMaxTime.txt", "filling valve"])
Actuators.append([Path + "Test/RecirculationValveTime.txt", Path + "Test/RecirculationValveMaxTime.txt", "recirculation valve"])
Actuators.append([Path + "Test/LeachedValveTime.txt", Path + "Test/LeachedValveMaxTime.txt", "leached valve"])
Actuators.append([Path + "Test/Nutrient1Time.txt", Path + "Test/Nutrient1MaxTime.txt", "nutrient 1 peristaltic pump"])
Actuators.append([Path + "Test/Nutrient2Time.txt", Path + "Test/Nutrient2MaxTime.txt", "nutrient 1 peristaltic pump"])
#Actuators.append([Path + "Test/Nutrient3Time.txt", Path + "Test/Nutrient3MaxTime.txt"])
Actuators.append([Path + "L/L1/StateValveTime.txt",Path + "L/L1/StateValveMaxTime.txt", "line 1 valve"])
Actuators.append([Path + "L/L2/StateValveTime.txt",Path + "L/L2/StateValveMaxTime.txt", "line 2 valve"])
Actuators.append([Path + "L/L3/StateValveTime.txt", Path + "L/L3/StateValveMaxTime.txt", "line 3 valve"])
Actuators.append([Path + "L/L4/StateValveTime.txt", Path + "L/L4/StateValveMaxTime.txt", "line 4 valve"])
#Actuators.append([Path + "L/L1/StateValveTime.txt", 0, 0])
#Actuators.append([Path + "L/L2/StateValveTime.txt", 0, 0])
#Actuators.append([Path + "L/L3/StateValveTime.txt", 0, 0])
#Actuators.append([Path + "L/L4/StateValveTime.txt", 0, 0])

actions=[]

for actuator in range(10):
    print(Actuators[actuator][0])
    with open(Actuators[actuator][0], 'r') as f:
        hour, minuts, seconds = f.readline().strip().split(':')
    print(hour, minuts, seconds)
    
    print(Actuators[actuator][1])
    with open(Actuators[actuator][1], 'r') as f:
        hourmax = f.readline()
    print(hourmax)
    
    if int(hourmax)-int(hour)<0:
        actions.append(("Maintanance action required in " + Actuators[actuator][2], Actuators[actuator][2]))
        print("canvi")
    
#eliminem el contingut de l'arxiu
with open(Path + 'alarms.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerows([])  # Escribir una lista vacía para borrar el contenido
        
#escrivim el que hem guardat
with open(Path + 'alarms.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerows(actions)