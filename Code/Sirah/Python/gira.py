
#file=open("/home/pi/Desktop/status.txt", "w")
#file.write("0")
#file.close()



file=open("/home/pi/Desktop/status.txt")

Status = float(file.read())

file.close()

print(Status)

if Status == 1:
    print(Status)
    
#file=open("/home/pi/Desktop/logsirah.txt", "a")
#file.write("0")
#file.write("\n")
#file.close()

import datetime

current=datetime.datetime.now()

print ("On: " + str(current))


file=open("/home/pi/Desktop/status.txt")
status=int(file.read())
file.close()
print(status)
if status=="0":
    print("adeu")
    
    
if status==0:
    print("adeu")
    current=datetime.datetime.now()
    file=open("/home/pi/Desktop/logsirah.txt", "a")
    file.write("Off:" + str(current))
    file.write("\n")
    file.close()
