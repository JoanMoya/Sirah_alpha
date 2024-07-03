from os import getpid, path, remove, kill
import os
import time
import signal
import psutil

class PID:
    file = "/home/pi/Desktop/Sirah/Python/Lockfiles/"
    #file = "C:\\Users\\marcel\\Documents\\GitHub\\sirah\\Sirah\\Python\\Lockfiles\\"
    def __init__(self, name):
        self.name="L" + str(name)
        self.pathFile=self.file + self.name + ".txt"
        
    def Exists(self):
        if os.path.exists(self.pathFile):
            return True
        else:
            return False
        
    def IsActive(self):
        pid=self.getPID()
        if psutil.pid_exists(pid):
            return True
        else:
            return False

    def getPID(self):
        # get the pid
        pid = getpid()
        # report the pid
        #print(pid)
        return pid
    
    def getPIDFile(self):
        file=open(self.pathFile, "r")
        self.pid=file.read()

    def savePID(self):
        file=open(self.pathFile, "w+")
        file.write(str(self.getPID()))

    def processRunning(self):
        if path.exists(self.pathFile):
            return True
        else:
            return False

    def kill(self):
        if path.exists(self.pathFile):
            self.getPIDFile()
            print(self.pid)
            os.kill(int(self.pid), signal.SIGTERM)
            remove(self.pathFile)
        else:
            pass
