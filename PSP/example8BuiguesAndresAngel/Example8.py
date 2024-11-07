# Importamos las bibliotecas necesarias para nuestro script
import psutil  # Para gestionar y obtener información sobre procesos del sistema
import os      # Para interactuar con el sistema operativo
import subprocess  # Para ejecutar comandos del sistema
import sys     # Para acceder a características específicas del intérprete de Python

def ProcesoActual():
    # Esta función devuelve el objeto del proceso actual utilizando el ID de proceso del script en ejecución
    return psutil.Process(os.getpid())

def esWindows():
    # Esta función comprueba si el sistema operativo es Windows
    return sys.platform.startswith('win')

# Imprimimos el nombre del proceso actual
print(ProcesoActual().name())

# Imprimimos el directorio de trabajo actual del proceso
print(ProcesoActual().cwd())

# Imprimimos la prioridad actual del proceso
print(ProcesoActual().nice())

if esWindows():
    # Si el sistema operativo es Windows, intentamos cambiar la prioridad del proceso
    try:
        # Usamos la herramienta 'wmic' para cambiar la prioridad a "below normal"
        subprocess.check_output(["wmic", "process", "where", f"processid={os.getpid()}", "CALL", "setpriority", "below normal"])
    except subprocess.CalledProcessError as e:
        # Capturamos errores si no se puede cambiar la prioridad
        print(f"Error setting priority: {e}")
else:
    # Si no es Windows (por ejemplo, si es Linux), intentamos cambiar la prioridad usando os.nice()
    try:
        os.nice(1)  # Aumenta la prioridad del proceso (hace que el proceso sea menos preferido)
    except OSError as e:
        # Capturamos errores si no se puede cambiar la prioridad
        print(f"Error setting priority: {e}")

# Imprimimos la nueva prioridad del proceso después del cambio
print(ProcesoActual().nice())

# Esperamos a que el usuario presione Enter para salir del programa
input("Presiona Enter para salir...")
