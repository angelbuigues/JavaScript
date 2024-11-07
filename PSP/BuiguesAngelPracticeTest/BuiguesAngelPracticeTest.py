import psutil
import subprocess
import os
import sys
import multiprocessing

def googleXD():
    url = "https://www.google.com/search?q=" + "Python"
    try:
        #aqui estava intentando bajar la prioridad al proceso, pero no he podido XD
        
        #subprocess.check_output(["wmic", "process", "where", f"processid={new_process.pid}", "CALL", "setpriority", "below normal"])
        #print(psutil.Process(new_process.pid).nice())
        
        #aqui creo el subproceso de abrir google con la url, y junto con todos los try: except:
        subprocess.run(["C:\\Users\\angbuiand\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe", url])
    except subprocess.CalledProcessError as e:  # Catch any CalledProcessError exceptions
        print(e.output)  # Print the error output
        try:
            subprocess.run(["C:\\Users\\angbuiand\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe", "https://www.bing.com/search?q=Python"])
        except subprocess.CalledProcessError as e:  
            print(e.output)
            try:                
                subprocess.run(["C:\\Users\\angbuiand\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe", "https://www.google.es/search?q=Python"])
            except subprocess.CalledProcessError as e:  
                print(e.output)
    
       
def padre():
    try:
        ActualPracess = psutil.Process(os.getpid())  
        print("---> name of the process: ", ActualPracess.name(), ' ---> name of the ID: ', ActualPracess.pid ,' ---> name of the priority: ', ActualPracess.nice())
    except:
        print("error")
    input("Presiona Enter para buscar Python en google...")
    #new_process = multiprocessing.Process(target=googleXD)
    #new_process.start()
    googleXD()


#esto es un intento para hacer arrancar el subproceso, pero no lo consegui XD
    
#if __name__ == '__main__':
    #padre()
padre()