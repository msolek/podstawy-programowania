def fibonacci(n):
    if n <= 0:
        pass
    elif n == 1:
        return 0 
    elif n == 2:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)




n = int(input("Podaj ktory wyraz chesz obliczyc: "))
wynik = fibonacci(n)
print(f"{n} wyraz ciagu to : {wynik}")