import SRH
import time

AS=SRH.StatusActuators()
log=SRH.LogTest()
WL=SRH.WaterLevel()

#WL.SaveCurrentLevel()
last_level = WL.ReadLastLevel()
print(last_level)
minimum_level = WL.GetMinimumLevel()
maximum_level = WL.GetMaximumLevel()

print("SISTEM FILLED, NOW PROCEDING WITH NUTRIENTS")
AS.SetNutrient1(1)
time.sleep(30)
AS.SetNutrient1(0)
print("DONE WITH NUTRIENTS, NOW RECIRCULATING")
AS.SetPump(1)
AS.SetRecirculationValve(1)
time.sleep(10)
AS.SetPump(0)
AS.SetRecirculationValve(0)
WL.SetFilled(1)
WL.SetFilling(0)

    

