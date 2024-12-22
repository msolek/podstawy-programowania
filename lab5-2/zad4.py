import pandas as pd
import os 
# df
data = {
    "Numer identyfikacyjny": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "Wiek": [35, 28, 40, 30, 45],
    "Pensja (w PLN)": [8000, 4500, 6000, 5500, 7000],
}

df = pd.DataFrame(data)

# a Wybierz pracowników, którzy mają pensję większą niż 5000 PLN

df_pensja_5000 = df[df["Pensja (w PLN)"] > 5000]
print("pensja wyzsza niz 5k")
print(df_pensja_5000)

# b Posortuj pracowników według wieku (od najmłodszych do najstarszych).
df_po_wieku = df.sort_values(by="Wiek")
print("sortowanie po wieku")
print(df_po_wieku)

# c Zgrupuj pracowników według stanowiska i oblicz średnią pensję w każdej grupie
df_po_stanowisku_srednia_pensja = df.groupby("Stanowisko")["Pensja (w PLN)"].mean().reset_index()
print("grupowanie po stanowisku i srednia pensja")
print(df_po_stanowisku_srednia_pensja)

# d Utwórz ramkę danych zawierającą informacje o pracownikach, którzy zmienili stanowisko (np. po
#    awansie) i połącz ją z ramką pierwszego terminu na podstawie wspólnego klucza (np. numer
#    identyfikacyjny).

awans = {
    "Numer identyfikacyjny": [2, 3],
    "Nowe Stanowisko": ["Senior Programista", "Starszy Konsultant"],
}
df_awans = pd.DataFrame(awans)

df_scalenie = pd.merge(df, df_awans, on="Numer identyfikacyjny", how="left")

#e Zapisz przygotowany DataFrame do pliku CSV.

import os
cwd = os.getcwd()
print (cwd)
plik = "/Users/msolek/WSIIZ/podstawy-programowania/lab5-2/pracownicy.csv"
df_scalenie.to_csv(plik, index=False)

# f Wczytanie z pliku CSV
df_wczytane = pd.read_csv('lab5-2/pracownicy.csv', sep=',', decimal=".", na_values=['NA', 'n/a', 'NaN'])
print(df_wczytane)