import pandas as pd

df = pd.read_csv('lab5-2/demografia.csv', sep=',', decimal=".", na_values=['NA', 'n/a', 'NaN'])
print(df)