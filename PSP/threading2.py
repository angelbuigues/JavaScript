import threading

def activity():
    print("i'm writing from the thread")
    return

print("Beginning")
threads = list()
for i in range(50):
    t = threading.Thread(target=activity)
    threads.append(t)
    t.start()
print("i'm writing from the principal")