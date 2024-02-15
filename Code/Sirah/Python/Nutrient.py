import datetime
import time
import SRH

AS=SRH.StatusActuators()
log=SRH.LogTest()


with open("/home/pi/Desktop/Sirah/Auxiliars/Nutrients/NutMins.txt", 'r') as file:
    minutes = int(file.readline())
with open("/home/pi/Desktop/Sirah/Auxiliars/Nutrients/NutSeg.txt", 'r') as file:
    seconds = int(file.readline())
    
NutrientTime = (minutes * 60) + seconds

print("   Filling the tank with nutients...")
log.WriteStatus("   Filling the tank with nutients...")
AS.SetNutrient1(1)
print("     Waiting 10 seconds")
log.WriteStatus("     Waiting 10 seconds")
time.sleep(NutrientTime)
print("   ... stop filling the tank with nutrients process.")
log.WriteStatus("   ... stop filling the tank with nutrients process.")
AS.SetNutrient1(0)