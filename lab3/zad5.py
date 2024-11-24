lista = []

liczba = 80
# while bo musi byc spelniony warunek, że kończymy na 0
while liczba >= 0:
    lista.append(liczba)
    liczba -= 4 # zmiejszamy o 4

print("Lista liczb zmniejszających się o 4 od 80 do 0:")
print(lista)
