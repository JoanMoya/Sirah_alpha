import SRH
import time

SA=SRH.StatusActuators()
WL= SRH.WaterLevel()


if WL.GetCurrentLevel() > WL.GetMinimumLevel():
    WL.SetFilled(0)
    WL.SetFilling(1)
    while WL.GetFilling():
        SA.SetPump(1)
        SA.SetFillingValve(1)
        print(WL.GetCurrentLevel())
        print(WL.GetMaximumLevel())
        if(WL.GetCurrentLevel() < WL.GetMaximumLevel()):
            SA.SetPump(0)
            SA.SetFillingValve(0)
            SA.SetNutrient1(1)
            time.sleep(30)
            SA.Nutrient1(0)
            WL.SetFilled(1)
            WL.SetFilling(0)
        else:
            print(WL.GetCurrentLevel())
else:
    print(WL.GetCurrentLevel())