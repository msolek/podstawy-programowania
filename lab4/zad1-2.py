imiona = ["Jan", "Karol", "Tomasz", "Ewa"]

# a
print(f"Posortuj ją alfabetycznie i wyświetl: {sorted(imiona)}")

# b

imiona.append("Zbigniew")
imiona.append("Jadwiga")
pop = imiona.pop()
print("Dodaj na końcu dwie osoby i pobierz ostatnią z nich poleceniem pop(). ", pop)

# c
imiona.insert(2, "Henryk")
print("Na pozycji 3 dodaj jeszcze jedną osobę. ", imiona)

# d
imiona.reverse()
imiona = imiona * 2
print("Odwróć kolejność na liście i zdubluj ją. ", imiona)