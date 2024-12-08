def bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)  

    if bmi < 18.5:
        zakres = "niedowaga"
    elif 18.5 <= bmi <= 24.9:
        zakres = "pozadana masa ciala"
    elif 25 <= bmi <= 29.9:
        zakres = "nadwaga"
    elif 30 <= bmi <= 34.9:
        zakres = "otylosc I stopnia"
    elif 35 <= bmi <= 39.9:
        zakres = "otylosc II stopnia"
    else:
        zakres = "otylosc III stopnia"

    return f"BMI: {bmi:.2f}, Zakres: {zakres}"



waga = float(input("podaj wage: "))
wzrost = float(input("podaj wzrost (w metrach): "))
wynik = bmi(waga, wzrost)

print(wynik)