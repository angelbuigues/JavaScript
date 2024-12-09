import threading
#import time
from time import sleep

def writeY():
    for i in range(1000):
        print("y", end="")
        sleep(0.01)
    return

print("Beginning")
t=threading.Thread(target=writeY)
t.start()

for i in range(1000):
    print("X", end="")
    sleep(0.01)

t.join