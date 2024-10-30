print("3 + 5 = 8")
print(3,"+",5,"=",8)
print("3 + 5 =",3+5)
print("20 - 25 =",20-25)
print("20 - 25 =",20-25)
num = int(input("Dame un bisiesto: "))
if (num%4 == 0 and num%100 != 0) or (num%400 == 0):
    print(num,"si es bisiesto")
else:
    print(num,"no es bisiesto")