grades = [85, 90, 78, 92, 88]

def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def add_note(note):
    try:
        note = float(note)
        if 0 <= note <= 100:
            grades.append(note)
            print("Añadida correctamente la nota: ", grade[len(grades) - 1])
        else:
            print("No está entre 0 y 100.")
    except:
        print("Número inválido.")

while True:
    print("----- Gestión de Notas -----")
    
    average = calculate_average(grades)
    print("Promedio: ", "{:.2f}".format(average))
    
    if average >= 70:
        print("Aprobado")
    else:
        print("Suspendido")
    
    new_note = input("Escribe una nueva nota, o escribe 'salir' para terminar): ")
    
    if new_note == 'salir':
        print("Adiós")
        break
    else:
        add_note(new_note)
