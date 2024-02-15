#Class LogSirah
from datetime import datetime

class LogSirah:
    file = "/home/pi/Desktop/Sirah/"
    def __init__(self):
        self.SirahOn()
        
    def SirahOn(self):
        current=datetime.now()
        log=open(self.file + "LogSirah.txt", "a")
        log.write("On: " + str(current))
        log.write("\n")
        log.close()
        
        self.StatusSirahOn()

    def SirahOff(self):
        current=datetime.now()
        log=open(self.file + "LogSirah.txt", "a")
        log.write("Off:" + str(current))
        log.write("\n")
        log.close()
        
        self.StatusSirahOff()

    def ReadStatus(self):
        log=open(self.file + "StatusSirah.txt")
        Status = float(log.read())
        log.close()
        return Status
        
    def StatusSirahOn(self):
        log=open(self.file + "StatusSirah.txt", "w")
        log.write("1")
        log.close()

    def StatusSirahOff(self):
        log=open(self.file + "StatusSirah.txt", "w")
        log.write("0")
        log.close()

        

#l=LogSirah()
#l.SirahOff()

#print("fin")
