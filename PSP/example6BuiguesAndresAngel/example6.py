import psutil

try:
    for proc in psutil.process_iter(['name', 'pid']):
        processName = proc.info['name']
        processID = proc.info['pid']
        print(processName, ' ::: ', processID)

except:
    print("error")

input("Presiona Enter para salir...")
