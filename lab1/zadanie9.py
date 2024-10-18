import math

a = float(input("Podaj A: "))
b = float(input("Podaj B: "))


print("Jaka operacje chcesz wykonac? Wybierz jedna z powyzszych liczb:", "\n", 
      "1. Dodawanie", "\n", "2. Odejmowanie", "\n", "3. Mnozenie", "\n", "4. Dzielenie","\n", "5. Potegowanie")
operacja = int(input("Twoj wybor: "))
               
# zamiast if statement mozna uzyc instrukcji switch

match operacja:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case 5:
        print(math.pow(a,b))
    case _:
        print(f"Wybrales zla liczbe: {operacja}, sproboj jeszcze raz")
