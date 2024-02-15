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

if (last_level > minimum_level or last_level >= maximum_level):
    while(last_level >= maximum_level and last_level != 0.0):
        WL.SetFilled(0)
        WL.SetFilling(1)
        AS.SetFillingValve(1)
        print("FILLING THE SYSTEM")
        print("CARACOLE3")
        #WL.SaveCurrentLevel()
        last_level = WL.ReadLastLevel()
        print(maximum_level)
        print(last_level)
else:
    WL.SetFilled(1)

AS.SetFillingValve(0)

    
