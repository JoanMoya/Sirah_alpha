
from SRH.Line import Line

from SRH.ETC import ETC

class UpdateLineParameters:
    def __init__(self, L):
        #Inicialization of KcUpdate element
        ETCCalculation=ETC() #Element that calculate the ETC
        Valor_linea = L
        #Initialize lines
        L=Line(Valor_linea)
        L.day()
        L.RemainingDays()
        day=L.day
        
        L.setETC(ETCCalculation.ETC(day, L.CropType))

        L.setET0(ETCCalculation.ETO())
        L.setkc(ETCCalculation.Kc(L.day, L.CropType))
        L.Irrigation()
        L.Progress()
        L.DailyIrrigationTimes()
        L.ToCsv()
          