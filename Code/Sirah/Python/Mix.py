from datetime import datetime, timedelta, date
import time
import SRH
import sys

AS=SRH.StatusActuators()
log=SRH.LogTest()


with open("/home/pi/Desktop/Sirah/Auxiliars/Mixing/MixMins.txt", 'r+') as file:
    minutes = float(file.read())
with open("/home/pi/Desktop/Sirah/Auxiliars/Mixing/MixSeg.txt", 'r+') as file:
    seconds = float(file.read())
    
MixingTime = (minutes * 60) + seconds

print("  Mixing...")
log.WriteStatus("  Mixing...")
AS.SetRecirculationValve(1)
AS.SetPump(1)
print("     Waiting 1 minute")
log.WriteStatus("     Waiting 1 minute")
time.sleep(MixingTime)
print("   ... stop mixing process.")
log.WriteStatus("   ... stop mixing process.")
AS.SetRecirculationValve(0)
AS.SetPump(0)