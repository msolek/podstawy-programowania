wynik=float(input("Podaj uzyskany wynik: "))

if wynik > 80:
    print(f"Gratulacje, zaliczyles egzamin w pierwszym terminie! Uzyskany wynik: {wynik}.")
elif 50 <= wynik <= 80:
    print(f"Mozesz poprawic egzamin. Uzyskany wynik: {wynik}.")
else:
    print(f"Musisz poprawic swoj egzamin by zaliczyc. Uzyskany wynik: {wynik}.")
