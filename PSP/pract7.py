try:
    num = int(input("Dame un bisiesto: "))
    assert num > 0
    
except:
    print("El año debe ser mayor que 0")

else:
    if (num%4 == 0 and num%100 != 0) or (num%400 == 0):
        print(num,"si es bisiesto")
    else:
        print(num,"no es bisiesto")

finally:
    print("de locos")

