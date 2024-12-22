import pandas as pd

df = pd.read_csv('lab5-2/demografia.csv', sep=',', decimal=".", na_values=['NA', 'n/a', 'NaN'])

najwiekszy_przyrost_22 = df["2022"].idxmax(skipna=True)
print(najwiekszy_przyrost_22)


kraj_z_najwiekszym_przyrostem = df.loc[najwiekszy_przyrost_22, 'KRAJE']
print(kraj_z_najwiekszym_przyrostem)

