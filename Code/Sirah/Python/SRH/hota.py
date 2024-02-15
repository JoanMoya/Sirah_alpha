#Això diria que es pot borrar
file = "C:\\Users\\marcel\\Documents\\GitHub\\sirah\\Sirah\\Auxiliars\\L\\"
Path=file + "L1\\"

file = open(Path + "StateValve.txt", "r")
StateValve = file.read()
file.close()
print(StateValve)