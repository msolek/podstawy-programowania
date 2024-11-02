goal = int(input("Podaj liczbe zdobytych bramek: "))
bonus = int(0)

if goal >=5:
    bonus =+ 5
    if goal > 10:
        bonus =+ (5 + 10) # za wiecej niz 10 bramek druzyna zdobywa obydwa bonusy

calkowity_wynik = goal + bonus
print(f"Wynik druzyny wynosi: {calkowity_wynik}, dlatego ze druzyna zdobyla {goal} goli oraz {bonus} punktow bonusu za strzelone bramki")

