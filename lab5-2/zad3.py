import pandas as pd

df = pd.read_csv('lab5-2/demografia.csv', sep=',', decimal=".", na_values=['NA', 'n/a', 'NaN'])



# Użyj metody max() do całej DataFrame, z wyłączeniem kolumny „KRAJ”.
df_numeryczne = df.drop(columns=["KRAJE"]).apply(pd.to_numeric, errors="coerce")  # konwersja wartości na liczby
max_wartosc = df_numeryczne.max().max()  # największa wartość

# Użyj metody idxmax() aby określić, w którym roku był największy przyrost.
max_rok = df_numeryczne.max().idxmax()  # rok największego przyrostu
#Ponownie skorzystaj z metody idxmax() w celu znalezienia „indeksu wiersza” w ramach tej kolumny, 
max_kraj_idx = df_numeryczne[max_rok].idxmax()  # indeks kraju o największym przyroście


max_kraj = df.loc[max_kraj_idx, "KRAJE"]  # nazwa kraju

print(f"Kraj {max_kraj}, rok: {max_rok}, wartosc: {max_wartosc}")
