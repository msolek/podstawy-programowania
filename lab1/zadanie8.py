import math

a = float(input("Podaj wspolczynnik a: "))
b = float(input("Podaj wspolczynnik b: "))
c = float(input("Podaj wspolczynnik c: "))

# sprawdzenie czy wspolczynnik a nie jest rowny 0, wtedy rownanie nie jest kwadratowe

if a==0:
     print("Rownanie nie jest kwadratowe!")

else:
    # obliczenie delty
    delta = b**2 - 4 * a * c
    print(f"Delta wynosi: {delta:.2f}")
    if delta > 0:
        # mamy dwa rozne rozwiazania
        x1 = (-b + math.sqrt(delta) / (2 * a))
        x2 = (-b - math.sqrt(delta) / (2 * a))
        print(f"Rownanie ma dwa rozwiazania, x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        # mamy jedno rozwiazanie
        x = -b / (2 * a)
        print(f"Rownanie ma jedno rozwiazanie, x = {x:.2f}")
    else:
        # nie mamy rozwiazan rzeczywistych
        print("Brak rozwiazan")
