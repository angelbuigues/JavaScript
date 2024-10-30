listaX = ["pedro", "ivan", "paco"]

def menu():
    print("=============================")
    print("======Jugadores on-line======")
    print("=============================")
    print("= 1: Llega un jugador nuevo =")
    print("= 2: Se va un jugador       =")
    print("= 3: Fin                    =")
    print("=============================")
    
    #try catch     
    try:
        opcion = int(input("Dame la opción: "))
        assert 1 <= opcion <= 3  
        return opcion
    except:
        print("Tienes que ser un número del 1 al 3.")
        return None 

# imprimir la lista
def imprimirLista(a):
    if a: 
        for i in range(len(a)):
            print(a[i])
    else:
        print("No hay jugadores en la lista.")

# agregar jugador
def opcion1():
    nuevo = input("¿Quién eres?: ")
    listaX.append(nuevo)
    print("Bienvenido ",nuevo)
    imprimirLista(listaX)

# eliminar jugador
def opcion2():
    if listaX:
        print("Adiós al jugador ", listaX[0])
        del listaX[0]
    else:
        print("No hay jugadores para eliminar.")
    imprimirLista(listaX)

# Función de adios
def opcion3():
    print("Adiós")
    exit()

# Bucle del menú
while True:
    opcion = menu()
    
    if opcion is not None:
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()
