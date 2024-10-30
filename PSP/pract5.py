def fibonacci(n):
    if n<2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n=int(input("introduce que numero de fibonacci quieres calcular: "))
for i in range(n):
    print (fibonacci(i))