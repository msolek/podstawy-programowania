liczba_gosci = int(input("Podaj liczbę gości: "))
liczba_potraw = int(input("Podaj liczbę zamówionych potraw: "))

calkowity_koszt = 0
licznik = 0

while licznik < liczba_potraw:
    cena = float(input(f"Podaj cenę potrawy {licznik + 1}: "))
    calkowity_koszt += cena
    licznik += 1

srednia_cena = calkowity_koszt / liczba_potraw

koszt_na_osobe = calkowity_koszt / liczba_gosci

print(f"Całkowity koszt zamówienia: {calkowity_koszt:.2f} zł")
print(f"Średnia cena potrawy: {srednia_cena:.2f} zł")
print(f"Kwota do zapłaty na osobę: {koszt_na_osobe:.2f} zł")
