#1. Square 2. Rectangle 3. Triangle 4. Circle
#Ask an option, if the option is 1, you must calculate the area of the square, and so on.
#For example: 

import math

def cuadrado(lado):
    area=lado*lado
    return(area)

def ractangel(lado1,lado2):
    area=lado1*lado2
    return(area)

def triangle(lado1,lado2):
    area=(lado1*lado2)/2
    return(area)

def circle(lado):
    area=(lado*lado)*math.pi
    return(area)

print("Introduce number 1 if you want to calculatede area of a Square,")
opcion=int(input("2 for a Rectangla, 3 for a Triangle, 4 a for Circle: "))


match opcion:
    case 1:    
        lado=int(input("Introduce el lado: "))
        print("El área del cuadrado es: ",cuadrado(lado))
    case 2:
        lado=int(input("Introduce el base: "))
        altura=int(input("Introduce la altura:  "))
        print("El área del rectangulo es: ",rectanguel(lado,altura))
    case 3:
        lado=int(input("Introduce la longitud: "))
        altura=int(input("Introduce el ancho: "))
        print("El área del triangulo es: ",triangle(lado,altura))
    case 4:
        lado=int(input("Introduce el radio: "))
        print("El área del triangulo es: ",circle(lado))
    case _:
        print("no me has dado un numero del 1 al 4.")