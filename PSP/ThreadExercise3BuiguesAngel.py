import threading
import random
import time

def thread_function(name, **kwargs):
    # Acceder y mostrar el nombre y el identificador del hilo
    current_thread = threading.current_thread()
    print(f"Hilo inicial: {current_thread.name} (ID: {current_thread.ident})")

    # Cambiar el nombre del hilo si cumple con una condición
    if name.startswith("HiloEspecial"):
        current_thread.name = f"{name}_Modificado"
    
    print(f"Hilo modificado: {current_thread.name} (ID: {current_thread.ident})")

    # Asignar un valor aleatorio a un atributo del hilo
    random_value = random.randint(1, 100)
    print(f"{current_thread.name}: Valor aleatorio asignado -> {random_value}")

    # Manejo de datos locales por hilo
    local_data = threading.local()
    local_data.valor = random_value
    print(f"{current_thread.name}: Dato local -> {local_data.valor}")

    # Simular trabajo
    time.sleep(random.uniform(0.5, 1.5))

# Crear una lista de nombres para los hilos
thread_names = [f"HiloEspecial{i}" if i % 2 == 0 else f"Hilo{i}" for i in range(1, 11)]

# Crear y gestionar hilos
threads = []
for name in thread_names:
    t = threading.Thread(target=thread_function, args=(name,), kwargs={"param": "valor"})
    threads.append(t)
    t.start()

# Esperar a que todos los hilos terminen
for t in threads:
    t.join()

print("Todos los hilos han completado su ejecución.")
