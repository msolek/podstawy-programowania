import math
import random

start = int(input("podaj min wartość przedziału: "))
stop = int(input("podaj max wartość przedziału: "))


krotka = tuple(random.randint(start, stop) for x in range(10))
print("krotka: ", krotka)


# obliczenie sredniej geometrycznej
# metoda math prod - #Return the product of the elements - zamiast mnozyc ilocznyn przez kazdy element krotki

iloczyn = math.prod(krotka)


print ('iloczyn', iloczyn)

## zeby obliczyc srednia, to bierzemy iloczyn do potegi 1/ilosc elementow krotki - nasza krotka ma na sztywno podane 10 elementow
srednia = math.pow(iloczyn,1/10)

print('srednia', srednia)