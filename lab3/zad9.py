# 1  Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
imie = input("Podaj swoje imię: ")
print("Witaj", imie)

# 2 Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to: ” oraz wczytany wiek.
wiek = input("Podaj swój wiek: ")
print("Twój wiek to:", wiek)

# 3 Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
print("Twoje inicjały:", imie[0].upper() + nazwisko[0].upper())

# 4 Wczyta łańcuch i wyświetli go pięć razy
lancuch = input("Podaj łańcuch znaków: ")
print(lancuch * 5) # albo mozna uzyc petli

# 5 Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy.
lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
polaczony = lancuch1 + lancuch2
print("Polaczony lancuch:", polaczony)

# 6 • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę
lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
polaczony = lancuch1[:len(lancuch1)//2] + lancuch2[:len(lancuch2)//2]
print("Łańcuch z połączonych pierwszych połówek:", polaczony)
