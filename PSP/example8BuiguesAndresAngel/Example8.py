import psutil
import os
import subprocess
import sys

def ProcesoActual():
    return psutil.Process(os.getpid())

def esWindows():
    return sys.platform.startswith('win')

print(ProcesoActual().name())
print(ProcesoActual().cwd())
print(ProcesoActual().nice())

if esWindows():
    try:
        subprocess.check_output(["wmic", "process", "where", f"processid={os.getpid()}", "CALL", "setpriority", "below normal"])
    except subprocess.CalledProcessError as e:
        print(f"Error setting priority: {e}")
else:
    try:
        os.nice(1)
    except OSError as e:
        print(f"Error setting priority: {e}")

print(ProcesoActual().nice())
input("Presiona Enter para salir...")
