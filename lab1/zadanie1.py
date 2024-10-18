# zadanie 1

# operator dodawania
x1 = 1+2 
print(type(x1))
# <class 'int'>

### operator dodawania - liczba zmiennoprzecinkowa
x2 = 1 + 4.5
print(type(x2))
# <class 'float'>

### operator dzielenia
x3 = 3 / 2
print(type(x3))
# <class 'float'>

### operator dzielienia
x4 = 4 / 2
print(type(x4))
# <class 'float'>

### operator dzielenia calkowitego
x5 = 3 // 2
print(type(x5))
# <class 'int'>

### operator dzielenia calkowitego
x6 = -3 // 2
print(type(x6))
# <class 'int'>

### operator dzielenie modulo - zwraca reszte z dzielenia
x7 = 11 % 2
print(type(x7))
# <class 'int'>

### operator potegowania
x8 = 2 ** 10 
print(type(x8))
# <class 'int'>
 
### operator potegowania
x9 = 8 ** (1/3)
print(type(x9))
# <class 'float'>

######################
# zadanie 1.b
print("\n","zadanie 1b", "\n")
print(type(int(3.0)))
# zmienia liczbe zmiennoprzecinkowa (float) na liczbe calkowita (int)

print(type(float(3)))
# zmienia liczbe calkowita (int) na zmimennoprzecinkowa (float)

print(type(float("3.0")))
# konwertuje string (tekst) na liczbe float

print(type(str(12.4)))
# konwertuje liczbe float na string (tekst)

print(type(bool(0)))
# normalnie boolean opisuje sie jako True/False, ale mozliwe jest uzywanie 0 jako false i 1 jako true, tutaj konwertuje liczbe na wartosc boolean

