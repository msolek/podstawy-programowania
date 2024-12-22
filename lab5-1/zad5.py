import random

liczby = list(range(1,50))

# losowanie bez powtórzen - metoda sample

wylosowane_liczby = random.sample(liczby,6)

print("wylosowane liczny: ", wylosowane_liczby)