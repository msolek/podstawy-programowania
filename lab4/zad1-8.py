stopnie = (
 "Szeregowy",
 "Kapral",
 "Sierżancie",
 "Porucznik",
 "Kapitan",
 "Major",
 "Pułkownik",
)

#a - liczba stopni 
ilość_stopni = len(stopnie)
print(ilość_stopni)

#b - znajdź indeks krotki dla elementu "Major" i przypisz do zmiennej Major_index,
Major_index = stopnie.index('Major')
print(Major_index)

#c - sprawdź, czy wartość "Pułkownik" znajduje się w krotce stopnie i przypisz do zmiennej Pułkownik_wstepowanie.
Pułkownik_wstepowanie = "Pułkownik" in stopnie # zwroci true albo false - true to istnieje
print(Pułkownik_wstepowanie)
