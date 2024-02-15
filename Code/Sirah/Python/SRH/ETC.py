# Class etc
import pandas as pd
import datetime
from datetime import date
from datetime import timedelta
import numpy as np


class ETC:
    file = "/home/pi/Desktop/Sirah"

    def __init__(self):
        self.beta1 = 0.733367
        self.beta2 = -0.022568
        self.performance=0.90

    def Kc(self, day, CropType):
        #If crop is tomato
        if (CropType==1):
            if (day<35):
                kc=0.15
            elif (day>=35) and (day<80):
                kc=0.15+(day-35)*(1.1-0.15)/(80-35)
            elif (day >= 80) and (day < 150):
                kc=1.1
            elif (day>=150) and (day<180):
                kc=1.1-(day-150)*(1.1-0.7)/(180-150)
            elif (day>=180):
                kc=0.7
        #if crop is lettuce
        if (CropType==2):
            if (day<20):
                kc=0.15
            elif (day>=20) and (day<=50):
                kc=0.15+(day-20)*(0.9-0.15)/(50-20)
            elif (day > 50):
                kc=1
        # If crop is beans
        if (CropType == 3):
            if (day < 20):
                kc = 0.15
            elif (day >= 20) and (day < 50):
                kc = 0.15 + (day - 20) * (1 - 0.15) / (50 - 20)
            elif (day >= 50) and (day < 80):
                kc = 1
            elif (day >= 80) and (day < 90):
                kc = 1 - (day - 80) * (1 - 0.5) / (90 - 80)
            elif (day >= 90):
                kc = 0.5

        return round(kc,2)

    def Taverage(self):
        # load csv file
        df = pd.read_csv("/home/pi/Desktop/Sirah/Logs/Dades/DBEnvironmentalData.csv")
        #df = pd.read_csv("C:\\Users\\marcel\\Documents\\GitHub\\sirah\\Sirah\\Logs\\Dades\\DBEnvironmentalData.csv")

        # convert date column into date format
        df['day'] = pd.to_datetime(df['day'], format='%d/%m/%Y %H:%M')

        #Current date and yesterday
        current_date = datetime.datetime.now().date()
        yesterday = current_date - timedelta(days=1)
        current_date = datetime.datetime.now().date().strftime("%Y/%m/%d")
        yesterday=yesterday.strftime("%Y/%m/%d")

        # filter rows on the basis of date
        newdf = (df['day'] > yesterday) & (df['day'] <= current_date)

        # locate rows and access them using .loc() function
        newdf = df.loc[newdf]

        Taverage=newdf['temperature'].mean()

        if np.isnan(Taverage):
            Taverage=21
        elif Taverage==0:
            Taverage=21

        return Taverage

    def ETO(self):
        av_temp=self.Taverage()
        ET0 = 1/(self.beta1 + av_temp*self.beta2)
        return ET0

    def ETC(self, day, CropType):
        ETC=self.ETO()*self.Kc(day,CropType)/self.performance
        return round(ETC,3)