import random

# a Wylosuje „Twoją szczęśliwą liczbę”

print(random.randint(0, 10))

# b 
roczniki = [1999,2000,2001,2002,2003]
szczesliwy_rocznik = random.randint(0,len(roczniki)-1)
print(roczniki[szczesliwy_rocznik])
