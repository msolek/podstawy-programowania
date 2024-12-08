def potega(a, n):
    if n == 0:  # 0 do potegi to 1 
        return 1
    elif n < 0:  # ujemne potegi
        return 1 / potega(a, -n)
    else:  # rekurencja
        return a * potega(a, n - 1)

a = float(input("liczba a : "))
n = int(input("potega n: "))

wynik = potega(a, n)

print(f"{a} do potegi {n} wynosi: {wynik}")