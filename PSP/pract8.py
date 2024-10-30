try:
    n=int(input("dime la edad de una persona: "))
    assert n > 0 and n < 150
    
except:
    print("El año debe ser mayor que 0 y menor que 150")

else:
    i = 0

    if n<18:
        i = 1
    if n>=18 and n<65:
        i = 2
    if n>=65 and n<120:
        i = 3
        
    match i:
        case 1:    
            print("es menor de edat")
        case 2:
            print("edat laboral")
        case 3:
            print("edat para gubilarse")
        case _:
            print("edat de record mundial")

finally:
    print("de locos")


