import random

#dystans = float(input("Podaj droge pokonana przez samochod w kilometrach: "))
spalanie = float(input("Podaj srednie spalanie paliwa w litrach na 100km: "))

# dystanas zaimplementowany w wersji zadania A:
dystans = random.randint(1,100000)


# Stala cena paliwa 
cena_paliwa = 6.5

# Oblieczenia zuzycia paliwa
zuzycie_paliwa = (spalanie/100) * dystans

# Oblczenie kosztu podrozy 
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print(f"Przewidywane zuzycie paliwa w litrach: {zuzycie_paliwa:.2f}.")
print(f"Szacowany koszt podrozy: {koszt_podrozy:.2f} PLN.")
print(f"Do pokonania bedzie dystans: {dystans} km.")
      
