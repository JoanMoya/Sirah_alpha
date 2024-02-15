
class 24hReport:
    file = "/home/pi/Desktop/Sirah/24hReport.csv"
    def __init__(self):
        
        self.LastReading=datetime.now()
        self.LineName=line
        self.Use=use
        self.CropType=Croptype
        self.Path=self.file + "/" + self.LineName
        self.getConfig()
        
    def getLineName(self):
        print(self.LineName)