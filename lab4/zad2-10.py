def wspolne(l1, l2):
    return list(set(l1) & set(l2))  

l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]

wynik = wspolne(l1, l2)

print(wynik)