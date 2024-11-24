paliwo = 100
paliwo_zuzyte_na_s = 10 
czas = 0

while paliwo > 0:
    print(f"Pozostałe paliwo: {paliwo}.")
    paliwo -= paliwo_zuzyte_na_s
    czas +=1
print(f"Koniec paliwa, czas lotu: {czas}")
