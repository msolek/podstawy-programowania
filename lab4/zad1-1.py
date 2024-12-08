moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
lista = moja_lista

### dodawanie elementow
lista.append(99)
print(f"append, {lista}")

lista.insert(0,0)
print(f"insert, {lista}")

lista2 = [101,102]
lista.extend(lista2)
print(f"extend, {lista}")

### usuwnanie elementow

lista.remove(0)
print(f"remove, {lista}")

lista.pop(0)
print(f"pop, {lista}")

lista.clear()
print(f"clear, {lista}")

### indeksowanie i wycinanie
lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(f"index 0, {lista[0]}")

print(f"start,stop,step {lista[0:-1:1]}")

### inne
print(f"length, {len(lista)}")

print(f"min, {min(lista)}")

print(f"max, {max(lista)}")

print(f"sum, {sum(lista)}")

lista_rev = lista.reverse()
print(f"reverse, {lista_rev}")




