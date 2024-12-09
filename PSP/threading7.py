import threading
import random
import time

def show(d):
    try:
        val = d.valor
    except AttributeError:
        print(f"{threading.current_thread().name}: Not initialized yet\n", end="")
    else:
        print(f"{threading.current_thread().name}: {val}\n", end="")

def thread(data):
    show(data)
    data.valor = random.randint(1, 100)
    show(data)

    local_data = threading.local()
    show(local_data)
    local_data.valor = 999
    show(local_data)

# Create a shared data object
data = threading.local()

# Start multiple threads
for i in range(3):
    t = threading.Thread(target=thread, args=(data,))
    t.start()

# Wait for threads to complete
time.sleep(5)
