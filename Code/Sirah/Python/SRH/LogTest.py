#Class LogTest
from datetime import datetime

class LogTest:
    file = "/home/pi/Desktop/Sirah/"
    def __init__(self):
        self.TestOn()
        
    def TestOn(self):
        current=datetime.now()
        log=open(self.file + "LogTest.txt", "a")
        log.write("-----------------------------------")
        log.write("\n")
        log.write("Starting test at: " + str(current))
        log.write("\n")
        log.close()
        
        self.StatusTestOn()

    def TestOff(self):
        current=datetime.now()
        log=open(self.file + "LogTest.txt", "a")
        log.write("Final test at: " + str(current))
        log.write("\n")
        log.write("**********************************")
        log.write("\n")
        log.close()
        
        self.StatusTestOff()

    def ReadStatus(self):
        log=open(self.file + "StatusTest.txt")
        Status = float(log.read())
        log.close()
        return Status
        
    def StatusTestOn(self):
        log=open(self.file + "StatusTest.txt", "w")
        log.write("1")
        log.close()

    def StatusTestOff(self):
        log=open(self.file + "StatusTest.txt", "w")
        log.write("0")
        log.close()
        
    def WriteStatus(self, message):
        log=open(self.file + "LogTest.txt", "a")
        log.write(message)
        log.write("\n")
        log.close()
        
    def CheckTest(self):
        Status=self.ReadStatus()
    
        if Status==0: 
            self.TestOff()
            return True
        else:
            return False
        

#l=LogSirah()
#l.SirahOff()

#print("fin")
