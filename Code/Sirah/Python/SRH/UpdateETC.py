#Class LogTest
from datetime import datetime

class UpdateETC:
    file = "/home/pi/Desktop/Sirah/"
    def __init__(self):
        pass

    def ReadLastUpdate(self):
        log=open(self.file + "LastKcUpdate.txt", 'r')
        LastKcUpdate = datetime.strptime(log.read(), '%Y-%m-%d')
        log.close()
        return LastKcUpdate

    def WriteLastUpdate(self):
        #Obtenim data i hora actual
        now = datetime.now()
        log=open(self.file + "LastKcUpdate.txt", "w")
        NewDate=now.strftime('%Y-%m-%d')
        log.write(str(NewDate))
        log.close()


    def CheckLastUpdate(self):
        #Obtenim data de la darrera actualització
        LastKcUpdate=self.ReadLastUpdate()

        #Obtenim data i hora actual
        now = datetime.now()

        if LastKcUpdate.date()!=now.date():
            return True
        else:
            return False

    def WriteKcLog(self, Line, Kc):
        current=datetime.now()
        log=open(self.file + "LogSirah.txt", "a")
        log.write("Calculating Kc for Line " + Line + ": " + str(current) )
        log.write("\n")
        log.write("New Kc for Line " + Line + ": " + str(Kc))
        log.write("\n")
        log.close()