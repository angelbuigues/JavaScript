import threading
import time
import random

def firstTask():
    global Done
    # time.sleep(random.random())
    if not Done:
        print("work done")
        Done = True
    return

Done = False
t = threading.Thread(target=firstTask)
t.start()
time.sleep(0.1)
firstTask()