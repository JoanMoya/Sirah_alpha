import datetime
import time
import SRH

AS=SRH.StatusActuators()
log=SRH.LogTest()

TimeStep=60

while True:
    
    print("   Filling the tank with water...")
    log.WriteStatus("   Filling the tank with water...")
    AS.SetFillingValve(1)
    print("     Waiting 1 minutes")
    log.WriteStatus("     Waiting 1 minuts")
    time.sleep(1*TimeStep)
    print("   ... stop filling the tank with water process.")
    log.WriteStatus("   ... stop filling the tank with water process.")
    AS.SetFillingValve(0)
    

    
    

