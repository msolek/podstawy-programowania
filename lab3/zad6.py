while True: 
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba < 0:
        print("Liczba ujemna, koniec.")
        break  
    else:
        print(f"Podano liczbę: {liczba}.")
