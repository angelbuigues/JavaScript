import threading
import time

def task():
    time.sleep(1)
    return

for _ in range(10):
    threading.Thread(target=task).start()

print("Active threads:", threading.active_count())
for thread in threading.enumerate():
    print(thread.name)
