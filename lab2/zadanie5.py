# podpunk A zadania:
with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia)

# podpunk B zadania:
# otwieranie pliku w trybie dopisywania (append)
with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("ALR,114\n")

# otwieranie trybu by przeczytac wszystkie rekordy
with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia)
