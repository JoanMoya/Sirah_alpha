import sys

def escribir_archivo(nombre_archivo):
    ruta="/home/pi/Desktop/Sirah/Auxiliars/" + nombre_archivo + ".txt"
    with open(ruta, 'w') as archivo:
        archivo.write("00:00:00")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        nombre_archivo = sys.argv[1]
        escribir_archivo(nombre_archivo)
    else:
        print("Uso: python script.py <nombre_archivo>")