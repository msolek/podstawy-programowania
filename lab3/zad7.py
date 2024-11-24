n = int(input("Podaj liczbę studentów w grupie: "))

suma_punktow = 0
liczba_studentow = 0


#print("\nPodaj liczbę punktów dla każdego studenta (od 0 do 100).")

#i = 0
#while i < n:
#    punkty = int(input(f"Punkty dla studenta {i + 1}: "))
#    if punkty < 0 or punkty > 100:
#        print("Niepoprawna liczba punktów!!! Pomijamy.")
#        continue  # pomijamy jako że niepoprawna liczba pkt
#    suma_punktow += punkty
#    liczba_studentow += 1
#    i += 1
##########

#### pkt B
while True:
    punkty = int(input("Podaj liczbę punktów: "))
    if punkty < 0:
        print("Koniec wprowadzania punktów.")
        break  
    if punkty > 100:
        print("Niepoprawna liczba punktów!!!! Pomijamy.")
        continue  # nastepny student
    suma_punktow += punkty
    liczba_studentow += 1



srednia = suma_punktow / liczba_studentow if liczba_studentow > 0 else 0

print(f"Średnia liczba punktów w grupie: {srednia:.2f}")


