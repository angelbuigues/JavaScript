import threading

def Function_thread():
    if(threading.current_thread().name == "mySon7"):
        threading.current_thread().name = "changed-name"
    print(f"Hello from: {threading.current_thread().name} \
    ID {threading.current_thread().ident}\n", end="")
    # threading.current_thread().ident = 666

threads = list()
for n in range(1, 11):
    t = threading.Thread(target=Function_thread, name="myThread")
    if(n > 5):
        t.name = "myThread" + str(n)
    threads.append(t)
    t.start()

input("Press Enter to exit...")
