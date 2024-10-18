a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))


# sprawdzenie czy a nie jest rowne 0, przez 0 sie nie dzieli
if a != 0:
    # jesli nie jest rowne 0 to kontynuujemy
    x = -b / a
    print(f"Rozwiazaniem rownania {a}x + {b} = 0 jest: x = {x:.2f}")
else:
    # sprawdzenie czy rownanie ma rozwiazania, jesli gdy a jest rowne 0
    if b == 0:
        print("Rownanie ma nieskonczenie wiele rozwiazan - rownanie tozsamosciowe")
    else:
        print("Rownanie nie ma rozwiazan - rownanie jest sprzeczne!")

