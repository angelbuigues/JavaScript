import multiprocessing  # Importar el módulo multiprocessing para manejar procesos en Windows
import os  # Importar el módulo os para obtener el ID del proceso actual

def padre():
    while True:  # Iniciar un bucle infinito
        new_process = multiprocessing.Process(target=hijo)  # Crear un nuevo proceso que ejecutará la función hijo
        new_process.start()  # Iniciar el nuevo proceso
        pids = (os.getpid(), new_process.pid)  # Obtener el ID del proceso padre y el nuevo ID del proceso hijo
        print("Parent: %d, Child: %d\n" % pids)  # Imprimir los IDs de los procesos padre e hijo
        reply = input("Press 's' if you want to create a new process: ")  # Pedir al usuario que presione 's' para crear un nuevo proceso
        if reply != 's':  # Si el usuario no presiona 's', romper el bucle
            break
            
def hijo():
    print('\n>>>>>>>>>>>>>>>> New child created with pid %d about to exit <<<<<<<<<<<<' % os.getpid())  # Imprimir un mensaje indicando que se ha creado un nuevo proceso hijo con su ID y que está a punto de salir
        
if __name__ == '__main__':  # Verificar si el script se está ejecutando directamente (no importado como un módulo)
    padre()  # Llamar a la función padre para iniciar el proceso