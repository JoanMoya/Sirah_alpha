import datetime
import time
import SRH

AS=SRH.StatusActuators()
log=SRH.LogTest()

TimeStep=60

while (True):
    AS.ResetAll()
    AS.UpdateAll()
    InitialDate=datetime.datetime.now()
    print("Starting the cycle at " + str(InitialDate))
    log.WriteStatus("Starting the cycle at " + str(InitialDate))
    print("   Filling the tank with water...")
    log.WriteStatus("   Filling the tank with water...")
    AS.SetFillingValve(1)
    print("     Waiting 1 minutes")
    log.WriteStatus("     Waiting 1 minuts")
    time.sleep(1*TimeStep)
    print("   ... stop filling the tank with water process.")
    log.WriteStatus("   ... stop filling the tank with water process.")
    AS.SetFillingValve(0)
    
    if log.CheckTest()==True:
        break
    print("   Filling the tank with nutients...")
    log.WriteStatus("   Filling the tank with nutients...")
    AS.SetNutrient1(1)
    print("     Waiting 10 seconds")
    log.WriteStatus("     Waiting 10 seconds")
    time.sleep(10)
    print("   ... stop filling the tank with nutrients process.")
    log.WriteStatus("   ... stop filling the tank with nutrients process.")
    AS.SetNutrient1(0)
    
    if log.CheckTest()==True:
        break
    print("  Mixing...")
    log.WriteStatus("  Mixing...")
    AS.SetRecirculationValve(1)
    AS.SetPump(1)
    print("     Waiting 1 minute")
    log.WriteStatus("     Waiting 1 minute")
    time.sleep(1*TimeStep)
    print("   ... stop mixing process.")
    log.WriteStatus("   ... stop mixing process.")
    AS.SetRecirculationValve(0)
    AS.SetPump(0)
    
    if log.CheckTest()==True:
        break
    print("  Irrigating sectror 1...")
    log.WriteStatus("  Irrigating sectror 1...")
    AS.SetL1Status(1)
    AS.SetPump(1)
    AS.UpdateL1Status()
    print("     Waiting 5 minute")
    log.WriteStatus("     Waiting 5 minute")
    time.sleep(1*TimeStep)
    print("   ... stop irrigation sectore 1 process.")
    log.WriteStatus("   ... stop irrigation sectore 1 process.")
    AS.SetL1Status(0)
    AS.UpdateL1Status()
    AS.SetPump(0)
    
    if log.CheckTest()==True:
        break
    
    FinalDate=datetime.datetime.now()
    print("Final of the cycle at " + str(FinalDate))
    log.WriteStatus("Final of the cycle at " + str(FinalDate))
    print("Time taken by the cycle: " + str(FinalDate-InitialDate))
    log.WriteStatus("Time taken by the cycle: " + str(FinalDate-InitialDate))
    print("--------------------------------------------")
    print("--------------------------------------------")
    log.WriteStatus("            -----")
    log.WriteStatus("            -----")
    time.sleep(1*TimeStep)
    
    if log.CheckTest()==True:
        break