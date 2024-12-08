#a
imie = input("Podaj imie: ")
print("Witaj, ", imie)

#b
wiek = int(input("Podaj wiek: "))
print("Twoj wiek to: ", wiek)

#c
nazwisko = input("Podaj nazwisko: ")
print(f"Inicjaly:  {imie[0].upper()}.{nazwisko[0].upper()}" )

#d
lancuch = input("Podaj lancuch znakow: ")
print("Lancuch 5 razy: ", lancuch * 5)

#e
lancuch1 = input("Podaj pierwszy lancuch znakow: ")
lancuch2 = input("Podaj drugi lancuch znakow: ")
lancuch3 = lancuch1 + lancuch2
print("Trzeci lancuch: ", lancuch3)

#f
lancuch4 = input("Podaj pierwszy lancuch znakow: ")
lancuch5 = input("Podaj drugi lancuch znakow: ")
lancuch6 = lancuch4[:len(lancuch4)//2] + lancuch5[:len(lancuch5)//2:]
print("Trzeci lancuch: ", lancuch6)