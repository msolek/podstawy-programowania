import pandas as pd

#Utworzony jest obiekt Pandas Series, który jest jednowymiarową strukturą
#danych. Dane to lista [10, 20, 30, 40],Indeksy to ['a', 'b', 'c', 'd'].
#Indeks jest jak etykieta przypisana do każdej wartości.
data = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(data)
# Pobranie wartość z serii dla indeksu 'c'
print(data['c'])


#####

# Tworzenie słownika data, klucze ('Imię', 'Wiek', 'Ocena') reprezentują
# kolumny a wartości to listy zawierające dane, które trafią do tych kolumn.
data = {
 'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
 'Wiek': [22, 21, 24, 23],
 'Ocena': [4.5, 5.0, 3.5, 4.0]
}
# Funkcja pd.DataFrame(data) zamienia słownik na obiekt DataFrame.
df = pd.DataFrame(data)
print(df)

######

ListaSlownikow = [
 {'Imię': 'Anna', 'Wiek': 22, 'Ocena': 4.5},
 {'Imię': 'Jan', 'Wiek': 21, 'Ocena': 5.0}
]
ListaList = [
 ['Anna', 22, 4.5],
 ['Jan', 21, 5.0]
]
for osoba in ListaSlownikow: print(f"{osoba['Imię']} ma {osoba['Wiek']} lat i ocenę {osoba['Ocena']}.")
for osoba in ListaList: print(f"{osoba[0]} ma {osoba[1]} lat i ocenę {osoba[2]}.")
df1 = pd.DataFrame(ListaSlownikow)
df2 = pd.DataFrame(ListaList)
print(df1)
print(df2)
df3 = pd.DataFrame(ListaList, columns=['Imię', 'Wiek', 'Ocena'])
print(df3)

###
# df = pd.read_csv('nazwa_pliku.csv')
# Wczytywanie z określonym separatorem (np. średnik)
# df = pd.read_csv('nazwa_pliku.csv', sep=';')