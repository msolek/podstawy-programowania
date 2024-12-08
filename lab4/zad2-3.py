def powitanie(imie, jezyk):
    if jezyk == "polski":
        print(f"Czesc, {imie}.")
    elif jezyk == "angielski":
        print(f"Hello, {imie}.")
    elif jezyk == "niemiecki":
        print(f"Guten Morgen, {imie}.")
    else:
        print("Jezyk nieobslugiwany.")


powitanie("Anna", "polski")
powitanie("Paul", "angielski")
powitanie("Jonatan", "niemiecki")
powitanie("Oui", "francuski")