#Això és pot borrar diria
import threading

# Crear un semáforo con un valor inicial de 1
sem = threading.Semaphore(0)

def funcion_protegida():
    # Solicitar acceso al semáforo
    sem.acquire()
    try:
        # Acceder al recurso compartido protegido por el semáforo
        print("Ejecutando función protegida...")
    finally:
        # Liberar el semáforo
        sem.release()

# Crear varios hilos que intentarán acceder a la función protegida al mismo tiempo
for i in range(5):
    threading.Thread(target=funcion_protegida).start()
