import threading

#method which is going to be associated to the thread
def Greeting():
    print('Hello World')
    
t = threading.Thread(target=Greeting)
t.start()
print('Hola')